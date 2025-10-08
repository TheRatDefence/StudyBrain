# StudyBrain - AI-Powered HSC Study Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Claude SDK](https://img.shields.io/badge/Claude%20SDK-latest-purple.svg)](https://github.com/anthropics/claude-agent-sdk-python)
[![Development Status](https://img.shields.io/badge/status-planning-yellow.svg)]()

An intelligent, AI-powered study management system designed to help NSW HSC students excel through personalized diagnostics, adaptive learning, and spaced repetition.

---

## 🎯 What is StudyBrain?

StudyBrain is a Flask-based web application powered by Claude's Agent SDK that provides:

- **Diagnostic Testing** - Identify knowledge gaps across the entire HSC syllabus
- **Personalized Learning** - AI tutors for each subject with deep curriculum knowledge
- **Progress Tracking** - Quantitative metrics for Conceptual Understanding and Functional Knowledge
- **Spaced Repetition** - FSRS algorithm ensures you never forget what you've learned
- **Study Optimization** - Intelligent recommendations on what to study next
- **Resource Management** - Organize and search all your study materials

---

## 📚 Subjects Supported

- **Physics** (HSC)
- **Mathematics Extension 1** (HSC)
- **Mathematics Advanced** (HSC)
- **Software Engineering** (HSC)
- **English Standard** (HSC)
- **Music** (HSC)

Each subject has its own specialized agent with deep curriculum knowledge and NESA alignment.

---

## 🚀 Getting Started

### New to this project?

**Start with these documents in order:**

1. **[START_HERE.md](START_HERE.md)** ⭐ - Project overview and entry point
2. **[ROADMAP.md](ROADMAP.md)** - Complete 10-phase development plan
3. **[PHASE_CONNECTIONS.md](PHASE_CONNECTIONS.md)** - How phases connect
4. **[Phase 01: Core Infrastructure](Phase-01-Core-Infrastructure/)** - Begin building

### Prerequisites

- Python 3.10 or higher
- Claude Pro subscription (for SDK access)
- Claude Code CLI installed and authenticated

### Quick Installation (once Phase 1 is complete)

```bash
# Clone the repository
git clone https://github.com/yourusername/studybrain.git
cd studybrain

# Navigate to the web app
cd studybrain_web

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🏗️ Architecture

### Multi-Agent System

**Coordinator Agent:**
- Routes requests to appropriate subject agents
- Manages cross-subject integration
- Handles study strategy and prioritization

**Subject Agents (6):**
- Physics, Mathematics Extension 1, Mathematics Advanced, Software Engineering, English Standard, Music
- Deep HSC syllabus knowledge
- Access to specialized sub-agents

**Specialized Sub-Agents (4):**
1. **Curriculum Expert** - Deep syllabus knowledge, resource librarian
2. **Question Generator** - Creates HSC-quality practice questions
3. **Answer Evaluator** - Marks responses with detailed feedback
4. **Progress Tracker** - Calculates scores, manages FSRS scheduling

### Technology Stack

- **Backend:** Flask 3.0.0 (Python web framework)
- **AI Engine:** Claude Agent SDK (multi-agent system)
- **Storage:** JSON files (local data directory)
- **Spaced Repetition:** py-fsrs (FSRS algorithm implementation)
- **Visualization:** Plotly 5.17.0 (interactive charts)
- **Math Rendering:** MathJax (LaTeX support)

### Custom MCP Tools (12 total)

Core functionality implemented as Model Context Protocol tools:
- `generate_diagnostic_quiz` - Adaptive quiz generation from curriculum
- `save_quiz_result` - Store results, calculate Con/Func scores
- `schedule_fsrs_review` - FSRS-based review scheduling
- `get_progress_summary` - Retrieve progress across all subjects
- `track_study_time` - Timer integration (Toggl-style)
- `index_resource` - Auto-organize study materials
- `search_resources` - Find relevant curriculum/class materials
- `calculate_exam_priority` - Time-to-marks-to-difficulty optimization
- `generate_practice_questions` - Targeted practice from weak areas
- `mark_answer` - Evaluate responses with detailed feedback
- `update_cross_subject_concepts` - Maintain shared concept registry
- `predict_exam_performance` - Grade prediction with confidence ranges

---

## 📂 Project Structure

```
StudyBrain/
├── README.md                          # This file
├── START_HERE.md                      # Entry point - read this first!
├── ROADMAP.md                         # 10-phase development plan
├── PHASE_CONNECTIONS.md               # How phases depend on each other
├── CLAUDE.md                          # Project context for AI assistants
│
├── Design/                            # Design documents
│   ├── V2_System_Architecture.md      # Complete technical specification
│   ├── Implementation_Kickstart.md    # Day 1-2 setup guide
│   ├── V1_Design_Overview.md          # Historical V1 design
│   ├── V1_Design_Questions.md         # Design decisions (answered)
│   ├── SDK_Access_Verification.md     # Claude Pro SDK access
│   └── Claude_SDK_Capabilities_Analysis.md # SDK feature mapping
│
├── Phase-01-Core-Infrastructure/      # Phase 1: Flask + coordinator
├── Phase-02-Quiz-System/              # Phase 2: Quizzes
├── Phase-03-Progress-Tracking/        # Phase 3: Con/Func scores
├── Phase-04-Multi-Subject/            # Phase 4: All subjects
├── Phase-05-FSRS-Integration/         # Phase 5: Spaced repetition
├── Phase-06-Study-Sessions/           # Phase 6: Timer & sessions
├── Phase-07-UI-Visualization/         # Phase 7: Charts & LaTeX
├── Phase-08-Sub-Agents/               # Phase 8: Intelligent agents
├── Phase-09-Resource-Management/      # Phase 9: PDF organization
└── Phase-10-Cross-Subject/            # Phase 10: Recommendations
```

---

## 🎯 Development Status

This project follows an **agile, incremental development approach** with 10 phases:

| Phase | Status | Description | Time |
|-------|--------|-------------|------|
| 1. Core Infrastructure | 🟡 Ready | Flask + coordinator + Physics agent | 1-2d |
| 2. Quiz System | ⏳ Pending | Question generation & submission | 2-3d |
| 3. Progress Tracking | ⏳ Pending | Con/Func scores & progress view | 2-3d |
| 4. Multi-Subject | ⏳ Pending | Expand to all 6 subjects | 1-2d |
| 5. FSRS Integration | ⏳ Pending | Spaced repetition scheduling | 2d |
| 6. Study Sessions | ⏳ Pending | Timer & session management | 1-2d |
| 7. UI Visualization | ⏳ Pending | Charts, LaTeX, polished UI | 2-3d |
| 8. Sub-Agents | ⏳ Pending | Intelligent question generation | 3-4d |
| 9. Resource Management | ⏳ Pending | PDF organization & search | 2-3d |
| 10. Cross-Subject | ⏳ Pending | Study recommendations | 2-3d |

**Current Status:** Planning phase complete, ready to start Phase 1
**Next Milestone:** Usable MVP (after Phase 4)

See [ROADMAP.md](ROADMAP.md) for detailed phase descriptions and timelines.

---

## 🗺️ Roadmap & Milestones

### Milestone 1: Usable MVP (After Phase 4) ⏳
- Study Physics with AI tutor
- Take practice quizzes
- Track progress (Con/Func scores)
- All 6 HSC subjects available

### Milestone 2: Polished Product (After Phase 7) ⏳
- Professional UI with charts
- LaTeX equation rendering
- Study time tracking
- Spaced repetition scheduling

### Milestone 3: Complete Vision (After Phase 10) ⏳
- HSC-quality question generation
- Detailed marking with feedback
- Resource library with search
- Cross-subject study recommendations

---

## 📊 Key Metrics

StudyBrain tracks two primary metrics:

### Conceptual Understanding (Con)
- **What it measures:** Depth of comprehension - the "WHY" behind concepts
- **Scale:** 0-100%
- **Goal:** Deep, intuitive grasp that transfers to novel problems

### Functional Knowledge (Func)
- **What it measures:** Practical application ability - the "HOW" in exam conditions
- **Scale:** 0-100%
- **Goal:** Consistent performance on exam-style questions

**Improvement Thresholds:**
- Conceptual: 20% minimum improvement before moving on
- Functional: 15% minimum improvement before moving on

---

## 📖 Documentation

### Main Documents
- **[START_HERE.md](START_HERE.md)** - Your entry point, read this first!
- **[ROADMAP.md](ROADMAP.md)** - Complete 10-phase development roadmap
- **[PHASE_CONNECTIONS.md](PHASE_CONNECTIONS.md)** - How phases depend on each other
- **[CLAUDE.md](CLAUDE.md)** - Project context, goals, and student profile

### Design Documents
- **[V2_System_Architecture.md](Design/V2_System_Architecture.md)** - Complete technical specification
- **[Implementation_Kickstart.md](Design/Implementation_Kickstart.md)** - Day 1-2 getting started guide
- **[V1_Design_Questions.md](Design/V1_Design_Questions.md)** - Design decisions and rationale

### Phase Documentation
Each phase has its own directory with implementation details:
- [Phase 01: Core Infrastructure](Phase-01-Core-Infrastructure/) - Flask + coordinator + Physics
- [Phase 02: Quiz System](Phase-02-Quiz-System/) - Question generation & submission
- [Phase 03: Progress Tracking](Phase-03-Progress-Tracking/) - Con/Func scores
- [Phase 04: Multi-Subject](Phase-04-Multi-Subject/) - Expand to all subjects
- [Phase 05: FSRS Integration](Phase-05-FSRS-Integration/) - Spaced repetition
- [Phase 06: Study Sessions](Phase-06-Study-Sessions/) - Timer & sessions
- [Phase 07: UI Visualization](Phase-07-UI-Visualization/) - Charts & LaTeX
- [Phase 08: Sub-Agents](Phase-08-Sub-Agents/) - Intelligent agents
- [Phase 09: Resource Management](Phase-09-Resource-Management/) - PDF organization
- [Phase 10: Cross-Subject](Phase-10-Cross-Subject/) - Recommendations

---

## 🎓 Student Context

**Primary User:** James
**Current Year:** Year 11 (entering Year 12 in 2026)
**Location:** NSW, Australia (HSC curriculum)

**Learning Challenges:**
1. Fast learning but fast forgetting (needs retention strategies)
2. Requires deep intuitive understanding (not just memorization)
3. Getting ahead of curriculum (accelerated learning)

**Technical Background:**
- Strong Python programming skills (intermediate to advanced)
- Completed Flask web development course
- Experience with command-line tools and Git/GitHub

---

## 🧪 Testing

Testing strategy is integrated into each phase:
- **Unit tests** for MCP tools and services
- **Integration tests** for agent communication
- **End-to-end tests** for complete workflows
- **Real-world validation** with actual HSC content

Run tests (once implemented):
```bash
pytest tests/
```

---

## 🤝 Contributing

This is currently a personal project for HSC preparation. If you're interested in adapting it for your own use:

1. Fork the repository
2. Follow the phase-by-phase development approach in [ROADMAP.md](ROADMAP.md)
3. Adapt subject agents to your curriculum
4. Share improvements via pull requests (optional)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Anthropic** - For Claude SDK and AI capabilities
- **NESA** - NSW Education Standards Authority (HSC curriculum)
- **py-fsrs** - Open-source FSRS implementation
- **Flask** - Python web framework
- **Plotly** - Interactive visualization library

---

## 📧 Contact

**Student:** James
**Year:** Year 11 (entering Year 12 in 2026)
**Location:** NSW, Australia

For questions about the project, open an issue on GitHub.

---

## 🔄 Project Status

**Version:** 2.0 (Complete Design Phase)
**Last Updated:** October 8, 2025
**Next Step:** Begin Phase 1 implementation

**Ready to ace the HSC!** 🎓

---

## Quick Links

- 📖 [Start Here](START_HERE.md) - Project overview
- 🗺️ [Roadmap](ROADMAP.md) - Development plan
- 🏗️ [Architecture](Design/V2_System_Architecture.md) - Technical details
- 🚀 [Phase 1](Phase-01-Core-Infrastructure/) - Begin building

---

**Built with Claude AI · Designed for HSC Success**
