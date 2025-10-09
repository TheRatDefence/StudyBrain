# StudyBrain - AI-Powered HSC Study Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Claude SDK](https://img.shields.io/badge/Claude%20SDK-latest-purple.svg)](https://github.com/anthropics/claude-agent-sdk-python)

An intelligent AI study system for NSW HSC students featuring personalized diagnostics, adaptive learning, and spaced repetition across 6 subjects.

---

## 🎯 Features

- **Diagnostic Testing** - Identify knowledge gaps across entire HSC syllabus
- **AI Tutors** - Specialized agents for each subject with deep curriculum knowledge
- **Progress Tracking** - Quantitative metrics for Conceptual & Functional understanding
- **Spaced Repetition** - FSRS algorithm prevents forgetting
- **Study Optimization** - Intelligent recommendations on what to study next
- **Resource Management** - Organize and search all study materials

## 📚 Subjects

Physics | Maths Ext 1 | Maths Adv | Software Engineering | English | Music

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Claude Pro subscription
- Claude Code CLI authenticated

### Installation (Phase 1 complete)

```bash
git clone https://github.com/yourusername/studybrain.git
cd studybrain/studybrain_web
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

### For Development

**Start Here:**
1. Read [ROADMAP.md](ROADMAP.md) - 10-phase development plan
2. Check [DESIGN.md](DESIGN.md) - Technical architecture
3. Navigate to Phase-01-Core-Infrastructure/ to begin building

## 🏗️ Architecture

### Multi-Agent System

**Coordinator Agent** → Routes to subject agents, manages cross-subject integration

**6 Subject Agents** → Physics, Maths, Software Eng, English, Music
- Each has 4 specialized sub-agents:
  - Curriculum Expert
  - Question Generator
  - Answer Evaluator
  - Progress Tracker

### Tech Stack

- **Backend:** Flask 3.0.0
- **AI:** Claude Agent SDK (multi-agent)
- **Storage:** JSON files (local)
- **Spaced Repetition:** py-fsrs
- **Visualization:** Plotly 5.17.0
- **Math:** MathJax/LaTeX

### Custom MCP Tools (12)

Core functionality: quiz generation, progress tracking, FSRS scheduling, resource indexing, exam priority calculation, performance prediction

## 📊 Progress Metrics

**Conceptual (Con):** 0-100% - Understanding depth (the "WHY")
**Functional (Func):** 0-100% - Exam performance (the "HOW")

Improvement thresholds: 20% Con / 15% Func before moving on

## 🎯 Development Status

| Phase | Status | Description | Time |
|-------|--------|-------------|------|
| 1. Core Infrastructure | 🟡 Ready | Flask + coordinator + Physics | 1-2d |
| 2. Quiz System | ⏳ Pending | Question gen & submission | 2-3d |
| 3. Progress Tracking | ⏳ Pending | Con/Func scores & charts | 2-3d |
| 4. Multi-Subject | ⏳ Pending | All 6 subjects | 1-2d |
| 5. FSRS Integration | ⏳ Pending | Spaced repetition | 2d |
| 6. Study Sessions | ⏳ Pending | Timer & persistence | 1-2d |
| 7. UI Polish | ⏳ Pending | Charts, LaTeX, styling | 2-3d |
| 8. Sub-Agents | ⏳ Pending | Intelligent question gen | 3-4d |
| 9. Resources | ⏳ Pending | PDF organization | 2-3d |
| 10. Cross-Subject | ⏳ Pending | Study recommendations | 2-3d |

**Current:** Planning complete, Phase 1 ready
**Next Milestone:** Usable MVP (after Phase 4)

See [ROADMAP.md](ROADMAP.md) for detailed phase info.

## 📂 Project Structure

```
StudyBrain/
├── README.md              # This file
├── ROADMAP.md             # Development plan
├── DESIGN.md              # Technical architecture
├── CLAUDE.md              # AI assistant context
│
├── Phase-01-Core-Infrastructure/
├── Phase-02-Quiz-System/
├── ...
├── Phase-10-Cross-Subject/
│
└── studybrain_web/        # Flask application (Phase 1+)
    ├── app.py
    ├── agents/
    ├── mcp_tools/
    ├── templates/
    ├── static/
    └── data/
```

## 🎓 Student Context

**Primary User:** James (Year 11 → Year 12 2026)
**Location:** NSW, Australia (HSC curriculum)

**Learning Needs:**
- Fast learning but needs retention strategies
- Requires deep intuitive understanding
- Getting ahead of curriculum

## 🤝 Contributing

This is a personal HSC prep project. To adapt:

1. Fork the repository
2. Follow phase-by-phase approach in [ROADMAP.md](ROADMAP.md)
3. Adapt subject agents to your curriculum
4. Share improvements via PR (optional)

**Contribution Guidelines:**
- Follow PEP 8 (Python)
- Write tests for MCP tools
- Update phase docs when modifying
- Use conventional commits: `feat(phase-X): description`

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- **Anthropic** - Claude SDK
- **NESA** - NSW HSC curriculum
- **py-fsrs** - Open-source FSRS
- **Flask** - Python web framework

## 📧 Contact

**Questions?** Open an issue on GitHub

---

## Quick Links

- 📖 [Roadmap](ROADMAP.md) - Development plan
- 🏗️ [Design](DESIGN.md) - Technical details
- 🚀 [Phase 1](Phase-01-Core-Infrastructure/) - Start building

**Built with Claude AI · Designed for HSC Success** 🎓
