# job-search：覆盖整个求职流程的 Claude Code skill

[English](README.md) | 中文

一个 [Claude Code](https://claude.com/claude-code) skill，带学生走完求职全程：从找到一则广告，到记录最终结果。面向瑞典和欧盟的硕士论文（thesis）岗位和毕业生岗位，另有一个国内秋招阶段。作者是 Chalmers 的硕士生，边投递边写成，规则都来自真实的投递。

**主动权在你手里：Claude 负责起草、检查和审稿；每一份申请由你自己提交，每一封邮件由你自己发送。**

## 它做什么

| 阶段 | 内容 |
|---|---|
| 1. 找岗位 | 搜 Chalmers thesis 门户、LinkedIn 和 Platsbanken（`scripts/find_jobs.py`），去掉看过或投过的广告，按匹配度打分排序 |
| 2. 投递 | 资格和语言门槛 → 把广告和**你自己的证据文件**逐条对应 → 定制一页简历和求职信 → ATS 关键词表、PDF 和版面检查 → 由一个全新的 Claude 子 agent 扮演招聘经理审稿 |
| 3. 跟踪 | 投递记录配 git tag（每个 tag 就是当时发出去的版本）、读收件箱、14 天跟进、感谢信、结果复盘 |
| 4. 面试 | 每一轮的面试包、和所投简历对齐口径、模拟面试、笔试准备 |
| 5. 国内秋招 | 国内校招网申的默认做法 |
| 6. 写作规则 | 自然、诚实、“技术 + 结果”的经历条目；Profile 读起来像一个真人 |

核心是 `evidence.md`：简历或求职信里的每一条事实都必须先记在这里，模型因此不会编出你面试时答不上来的内容。

## 安装

```
git clone https://github.com/44sunsetsf/job-search-skill
ln -s "$PWD/job-search-skill/skills/job-search" ~/.claude/skills/job-search
```

然后在 Claude Code 里说“帮我初始化求职工作流”（或 “set up the job-search workflow”）。它会把 `templates/materials/` 复制到你选的文件夹（请建成**私有**仓库），写好 `skills/job-search/config.json`（参考 `config.example.json`），再通过问答帮你填 `evidence.md`。

需要 `python3`；生成简历还需要 LaTeX 引擎（如 `tectonic`）和 `pdftotext`（poppler）。

## 目录

```
skills/job-search/   SKILL.md + 01…06 各阶段文件、references/、scripts/
templates/materials/ 你自己材料的起始文件夹（证据、投递记录等）
```

## 致谢

部分阶段和检查改编自 [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)（MIT）；它的 `verify_pdf.py` 和 `verify_layout.py` 连同许可证放在 `scripts/vendor/`。简历和求职信的原则参考了高校就业服务的指南（Chalmers Career Services）。

招聘网站抓取（`find_jobs.py`）只供个人、少量使用，请遵守各网站的条款。

MIT 许可证。
