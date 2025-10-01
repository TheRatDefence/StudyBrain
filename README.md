# StudyBrain - AI-Powered HSC Study Management System

**An intelligent study system designed to help Year 12 HSC students excel through diagnostic testing, targeted learning, and adaptive spaced repetition.**

---

## 🎯 Project Overview

StudyBrain is a Flask-based web application that uses Claude AI and custom MCP tools to provide:

- **Diagnostic Quizzes** - Identify knowledge gaps across the entire HSC curriculum
- **Targeted Practice** - Generate practice questions for weak areas
- **Intelligent Marking** - Detailed feedback and misconception identification
- **Progress Tracking** - Quantitative metrics (Conceptual Understanding + Functional Knowledge)
- **Spaced Repetition** - FSRS algorithm for optimal review scheduling
- **Cross-Subject Integration** - Connect concepts across Physics, Maths, Chemistry, etc.
- **Study Timer** - Toggl-style time tracking and learning rate calculation

---

## 📚 Subjects Supported

1. **Physics** (HSC)
2. **Mathematics Extension 1** (HSC)
3. **Mathematics Advanced** (HSC)
4. **Chemistry** (HSC)
5. **Software Engineering** (HSC)
6. **English Standard** (HSC)

Each subject has its own specialized agent with deep curriculum knowledge and NESA alignment.

---

## 🏗️ Architecture

### Multi-Agent System

**Coordinator Agent:**
- Routes requests to appropriate subject agents
- Manages cross-subject integration
- Handles study strategy and prioritization

**Subject Agents (6):**
- Deep HSC syllabus knowledge for each subject
- Access to specialized sub-agents

**Specialized Sub-Agents (4):**
1. **Curriculum Expert** - Syllabus navigation and resource management
2. **Question Generator** - Creates diagnostic quizzes and practice questions
3. **Answer Evaluator** - Marks responses with detailed feedback
4. **Progress Tracker** - Calculates scores and manages FSRS scheduling

### Technology Stack

- **Backend:** Flask 3.0.0 (Python web framework)
- **AI Engine:** Claude Agent SDK (via Claude Code CLI)
- **Storage:** JSON files (local data directory)
- **Spaced Repetition:** py-fsrs (FSRS algorithm)
- **Visualization:** Plotly 5.17.0 (interactive charts)
- **Math Rendering:** LaTeX/MathJax support

### Custom MCP Tools (12 total)

Core functionality implemented as Model Context Protocol tools:
- `generate_diagnostic_quiz` - Adaptive quiz generation
- `save_quiz_result` - Store results and calculate scores
- `schedule_fsrs_review` - FSRS-based review scheduling
- `get_progress_summary` - Retrieve progress across subjects
- `track_study_time` - Timer integration
- `index_resource` - Auto-organize study materials
- `search_resources` - Find relevant curriculum materials
- `calculate_exam_priority` - Time-to-marks-to-difficulty optimization
- `generate_practice_questions` - Targeted practice from weak areas
- `mark_answer` - Evaluate responses with feedback
- `update_cross_subject_concepts` - Maintain shared concept registry
- `predict_exam_performance` - Grade prediction with confidence ranges

---

## 📂 Project Structure

```
StudyBrain/
├── CLAUDE.md                      # Project context for AI assistants
├── README.md                      # This file
├── Design/                        # Design documents
│   ├── V2_System_Architecture.md  # Complete technical specification
│   ├── Implementation_Kickstart.md # Day 1-2 setup guide
│   ├── V1_Design_Overview.md      # Historical V1 design
│   ├── V1_Design_Questions.md     # Design decisions (answered)
│   ├── SDK_Access_Verification.md # Claude Pro SDK access confirmation
│   └── Claude_SDK_Capabilities_Analysis.md # SDK feature mapping
├── ExamplePhysicsUsageV1/         # Original V1 design flowchart
├── CLAUDE_DOCS/                   # Complete Claude SDK documentation
└── [Implementation TBD]
    └── studybrain_web/            # Flask web application (to be created)
```

---

## 🚀 Quick Start (Implementation)

### Prerequisites

- Python 3.9+
- Claude Pro subscription (for Claude Code CLI access)
- Claude Code CLI installed and authenticated

### Setup (5 minutes)

```bash
cd StudyBrain
mkdir studybrain_web && cd studybrain_web

# Create directory structure
mkdir -p agents/subjects agents/subagents mcp_tools routes services templates static/css static/js
mkdir -p data/{sessions,exams,progress,quiz_results,study_timer,resource_index}

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install Flask==3.0.0 flask-cors==4.0.0 claude-agent-sdk py-fsrs plotly==5.17.0

# Verify Claude SDK connection
python -c "from claude_agent_sdk import query; print('SDK ready!')"
```

### Implementation Guide

**For complete Day 1-2 implementation instructions, see:** `Design/Implementation_Kickstart.md`

**For full technical specification, see:** `Design/V2_System_Architecture.md`

---

## 📊 Key Metrics

### Progress Tracking

**Conceptual Understanding (Con):** 0-100% scale measuring depth of comprehension (the "WHY")
- Based on explanation quality, reasoning, and connections
- Goal: Deep intuitive understanding that transfers to novel problems

**Functional Knowledge (Func):** 0-100% scale measuring practical application (the "HOW")
- Based on correct answers under exam conditions
- Goal: Consistent performance on HSC-style questions

### Score Calculation

Combines three factors:
1. **Percentage correctness** (base score)
2. **Difficulty weighting** (harder questions worth more)
3. **Confidence adjustment** (low confidence reduces score)

### FSRS Integration

- Per-topic stability and difficulty tracking
- Adaptive scheduling based on performance
- Review predictions with confidence ranges
- Retention curve optimization

---

## 🎓 Student Context

**Primary User:** James (Year 11 → Year 12 HSC student)
**Graduation:** 2026
**Location:** NSW, Australia

**Learning Challenges:**
1. Fast learning but fast forgetting (needs retention strategies)
2. Requires deep intuitive understanding (not just memorization)
3. Getting ahead of curriculum (accelerated learning)

**Technical Background:**
- Strong Python programming skills (intermediate-advanced)
- Comfortable with command-line tools
- Learning Flask for Year 12 Software Engineering

---

## 📅 Development Timeline

### Phase 1: MVP (October 1-12, 2025) - **IN PROGRESS**

**Core Features:**
- Diagnostics quizzes for all subjects
- Practice question generation
- Answer evaluation and marking
- Session persistence
- Multi-subject support
- Study content synthesis
- Basic progress tracking

### Phase 2: Advanced Features (By End October 2025)

- Cross-subject integration
- Advanced progress tracking with visualization
- Spaced repetition optimization
- Resource auto-organization

### Phase 3: Production (November-December 2025)

- External resource integration
- Exam performance prediction
- Performance optimization
- Real-world validation with Year 12 content

### Phase 4: Hardening (January 2026)

- Production deployment
- Integration with actual HSC study workflow
- Final testing before Year 12 trials

---

## 📖 Documentation

### For Implementation

1. **`CLAUDE.md`** - Complete project context for AI assistants
2. **`Design/V2_System_Architecture.md`** - Comprehensive technical specification
3. **`Design/Implementation_Kickstart.md`** - Step-by-step Day 1-2 guide

### For Design Understanding

1. **`Design/V1_Design_Overview.md`** - Original conceptual design
2. **`Design/V1_Design_Questions.md`** - All design decisions with rationale
3. **`Design/Claude_SDK_Capabilities_Analysis.md`** - SDK feature mapping

### Claude SDK Reference

Complete Claude documentation available in `CLAUDE_DOCS/` directory.
Navigation guide: `CLAUDE_DOCS/DOCUMENTATION_MAP.md`

---

## 🔐 Authentication & Access

**Claude SDK Access:**
- Uses Claude Code CLI (authenticated with Claude Pro account)
- Python Agent SDK wraps CLI internally
- No separate API key required
- Usage charged against Pro subscription ($20/month)

**Application Access:**
- MVP: localhost only (no authentication)
- Future: optional user profiles for multi-student usage

---

## 🎯 Success Metrics

### System Quality
- Coverage completeness (% of syllabus assessed)
- Gap identification accuracy
- Time efficiency vs. manual review

### Learning Effectiveness
- Score improvement rate (Con/Func increase per study hour)
- Retention over time (1 week, 1 month)
- Transfer to actual exams (diagnostics vs. real test scores)

### User Experience
- Session completion rate
- Average study time per session
- Recommendation acceptance rate

---

## 🤝 Contributing

This is a personal educational project for HSC preparation. Not currently accepting external contributions.

---

## 📄 License

Private educational project. © 2025 James

---

## 🆘 Support

For questions or issues related to this project:
- Check `CLAUDE.md` for AI assistant context
- Review `Design/V2_System_Architecture.md` for technical details
- Consult `CLAUDE_DOCS/` for Claude SDK documentation

---

## 📝 Version History

| Version | Date | Status |
|---------|------|--------|
| 0.1 | 2025-10-01 | Design phase complete, ready for implementation |
| 1.0 | 2025-10-12 | Phase 1 MVP target completion |

---

**Built with Claude AI · Designed for HSC Success**
