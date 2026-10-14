"""Check an English CV PDF. Fails if:
  - any bullet or sub-bullet runs longer than two lines;
  - the sections are not in the required order:
    Profile, Experience, Education, Projects, Skills and Languages .
Usage: python3 check_bullets.py <cv.pdf>"""
import sys,re,subprocess
txt=subprocess.run(['pdftotext','-layout',sys.argv[1],'-'],capture_output=True,text=True).stdout
cur=None;n=0;bad=0
def flush():
    global bad
    if cur and n>2: print(f'TOO LONG ({n} lines):',cur[:80]); bad=1
for l in txt.split('\n'):
    t=l.strip()
    if re.match(r'^[•–]',t): flush(); cur=t; n=1
    elif cur and t and l.startswith(' '): n+=1
    else: flush(); cur=None; n=0
flush()
print('max-2-lines check:', 'FAIL' if bad else 'OK')
ORDER = ['Profile', 'Experience', 'Education', 'Projects', 'Skills and Languages']
found = [l.strip() for l in txt.split('\n') if l.strip() in ORDER]
if found != ORDER:
    print('SECTION ORDER FAIL: got', found, 'expected', ORDER); bad = 1
else:
    print('section order check: OK')
sys.exit(bad)
