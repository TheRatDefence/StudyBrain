# StudyBrain - AI-Powered HSC Study Management System

## Project Context

You are assisting with the design and development of **StudyBrain**, an intelligent study management system designed to help a Year 11 student (graduating 2026) excel in Year 12 HSC examinations.

---

## Student Profile

**Name:** James
**Current Year:** Year 11 (entering Year 12)
**Location:** NSW, Australia (HSC curriculum)
**Graduation:** 2026

**Learning Challenges:**
1. **Fast learning, fast forgetting** - Needs reinforcement and retention strategies
2. **Need for deep intuitive understanding** - Memorization alone insufficient
3. **Getting ahead of curriculum** - Wants to learn Year 12 content early

**Technical Background:**
- Strong Python programming skills (intermediate to advanced)
- Experience with AI/ML concepts
- Previous attempt at learning Claude SDK (partially successful)
- Has Claude Pro subscription account
- Comfortable with command-line tools

**Subjects (HSC):**
- Physics
- Mathematics Extension 1
- Mathematics Advanced
- Software Engineering
- English Standard
- Music

---

## Project Overview

### Mission Statement

Build an AI-powered study system that:
1. **Identifies knowledge gaps** through diagnostic testing
2. **Teaches concepts deeply** with intuitive explanations and examples
3. **Tracks progress quantitatively** with conceptual and functional understanding metrics
4. **Optimizes study time** through intelligent topic prioritization
5. **Prevents forgetting** with spaced repetition and cross-subject reinforcement

### Current Status

**Stage:** Implementation Phase (Ready for Day 1)
**Location:** `/Users/james/Desktop/School/Year-12/StudyBrainTemplate/`

**Completed:**
- ✅ V1 conceptual design (flowchart and documentation)
- ✅ Claude SDK documentation scraped and organized
- ✅ Professional V1 design overview
- ✅ Claude SDK capabilities analysis
- ✅ Design questionnaire created and answered
- ✅ V2 System Architecture document (complete technical specification)
- ✅ Implementation kickstart guide (Day 1-2 getting started)
- ✅ SDK access verification (confirmed Pro account provides full SDK access)

**In Progress:**
- 🔄 Day 1 implementation (Flask setup, basic coordinator agent)

**Upcoming:**
- ⏳ Subject agent development (Physics, Maths, etc.)
- ⏳ MCP tool implementation (diagnostics, progress tracking, FSRS)
- ⏳ Web interface development (study sessions, progress visualization)
- ⏳ Integration testing with real study content

---

## Key Documents for Implementation

**If you're starting Day 1 implementation, read these in order:**

1. **This file (CLAUDE.md)** - Project context and overview
2. **`Design/V2_System_Architecture.md`** ⭐ - Complete technical specification with:
   - Multi-agent architecture details
   - All 12 custom MCP tools
   - Flask application structure
   - JSON data schemas
   - Phase 1 implementation timeline
3. **`Design/Implementation_Kickstart.md`** - Day 1-2 getting started guide with:
   - 5-minute quick start commands
   - Minimal Flask app with SDK integration
   - First MCP tool implementation
   - Testing procedures

**Supporting documents:**
- `Design/V1_Design_Questions.md` - All design decisions with rationale
- `Design/SDK_Access_Verification.md` - Confirmed Claude Pro provides full SDK access
- `CLAUDE_DOCS/DOCUMENTATION_MAP.md` - Navigate complete Claude SDK documentation

---

## System Architecture

### V2 Architecture (Current - October 2025)

**Interface:** Flask web application (localhost:5000)
**Storage:** JSON files (local data directory)
**Spaced Repetition:** FSRS algorithm (py-fsrs library)
**Visualization:** Plotly charts (interactive progress tracking)

#### Multi-Agent Architecture

**Coordinator Agent:**
- Routes requests to appropriate subject agents
- Manages cross-subject integration
- Handles non-subject queries ("What should I study next?")
- Maintains shared concept registry

**Subject Agents (6):**
1. Physics
2. Mathematics Extension 1
3. Mathematics Advanced
4. Software Engineering
5. English Standard
6. Music

Each subject agent has access to specialized sub-agents:

**Specialized Sub-Agents (4):**
1. **Curriculum Expert** - Deep syllabus knowledge, resource librarian
2. **Question Generator** - Creates diagnostic quizzes and practice questions
3. **Answer Evaluator** - Marks responses, identifies misconceptions
4. **Progress Tracker** - Calculates scores, manages FSRS scheduling

#### Custom MCP Tools (12 total)

**Core Tools:**
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

#### Flask Web Interface

**Key Routes:**
- `GET /` - Dashboard (subject cards, stats, due reviews)
- `GET /study/<subject>` - Study session interface
- `POST /study/<subject>/quiz` - Submit quiz answer
- `GET /progress` - Progress visualization (charts, timeline)
- `POST /api/timer/start` - Start study timer
- `GET /api/progress/fsrs-due` - Topics due for review

**UI Components:**
- Dashboard with 6 subject cards + coordinator access
- Study session view (timer, quiz panel, explanation panel)
- Progress charts (Plotly timeline, radar, learning rate)
- Topic tree (expandable, Con/Func scores, FSRS due dates)

#### Data Structure (JSON)

**Progress Data:**
```json
{
  "subject": "Physics",
  "modules": [{
    "name": "Module 1: Kinematics",
    "topics": [{
      "name": "Projectile Motion",
      "conceptual": 75,
      "functional": 68,
      "fsrs_stability": 12.5,
      "fsrs_difficulty": 6.2,
      "next_review": "2025-10-15",
      "subtopics": []
    }]
  }]
}
```

### V1 Architecture (Historical - Conceptual Design)

#### Three Core Components

1. **Start/Opening System** - Subject agent initialization, session restoration
2. **Exam Preparation System** - Diagnostics quizzes, progress assessment
3. **Studying System** - Targeted learning, practice questions, evaluation

---

## Technology Stack

### Core Framework
**Claude Agent SDK** (Python - claude-agent-sdk)
- Authenticates via Claude Code CLI with Pro account
- Multi-agent architecture with coordinator pattern
- Custom MCP tools for StudyBrain features
- Subagents for specialized tasks
- Hooks for automation and logging
- PDF processing (native vision capabilities)

### Web Framework
**Flask 3.0.0** (chosen for Year 12 Software Engineering learning)
- RESTful API endpoints
- Template-based UI (Jinja2)
- CORS support for API calls
- Localhost deployment (no authentication for MVP)

### Storage Layer
**JSON files** (local data directory)
- Simple, human-readable format
- No database setup required
- Sufficient for single-user usage
- Data types:
  - `data/progress/` - Subject progress with Con/Func scores
  - `data/sessions/` - Study session logs
  - `data/quiz_results/` - Quiz responses and marks
  - `data/exams/` - Exam preparation results
  - `data/study_timer/` - Time tracking data
  - `data/resource_index/` - Organized study materials

### Spaced Repetition
**py-fsrs** (Free Spaced Repetition Scheduler)
- FSRS algorithm implementation
- Per-topic stability and difficulty tracking
- Adaptive scheduling based on performance
- Review prediction with confidence ranges

### Visualization
**Plotly 5.17.0** (interactive charts)
- Progress timeline charts
- Subject radar charts (Con/Func scores)
- Learning rate graphs
- Retention curves over time

### User Interface
**Flask web application** (browser-based)
- Dashboard for subject selection
- Study session interface with timer
- Progress visualization page
- LaTeX/MathJax support for math notation
- Responsive design (desktop-focused)

---

## Key Design Decisions (Finalized)

All design decisions have been made based on completed questionnaire (`Design/V1_Design_Questions.md`):

1. **Multi-agent architecture** ✅ - Coordinator + subject agents + specialized sub-agents; cross-subject concept registry
2. **User interface** ✅ - Flask web application (browser-based, chosen for learning Flask)
3. **File processing** ✅ - PDF extraction for assessments, textbooks; equation extraction; LaTeX/MathJax rendering
4. **Storage** ✅ - Local JSON files (simple, human-readable, sufficient for single user)
5. **Progress tracking** ✅ - Combination of percentage, difficulty weighting, confidence adjustment; 20% Con / 15% Func improvement thresholds
6. **Spaced repetition** ✅ - FSRS algorithm with adaptive scheduling (py-fsrs library)
7. **Resource management** ✅ - Auto-organize into StudyBrain structure; ask permission before searching online
8. **Study sessions** ✅ - Variable duration (task-based); session state persistence with resume capability
9. **Development priorities** ✅ - Phase 1 (by Oct 12): diagnostics, practice questions, marking, session persistence, multi-subject
10. **Timer feature** ✅ - Toggl-style time tracking for learning rate calculation

---

## Claude SDK Integration Strategy

### What Claude SDK Provides (✅ Fully Supported)

1. **PDF Processing:**
   - Native vision capabilities for PDFs
   - Text + image extraction
   - Max 100 pages, 32MB per document
   - Cost: ~1,500-3,000 tokens per page

2. **Multi-Agent System:**
   - Subagents with specialized prompts
   - Tool restrictions per agent
   - Parallel execution
   - Automatic invocation based on task

3. **Custom Tools (MCP):**
   - Create diagnostic quiz tools
   - Progress tracking database tools
   - Resource indexing tools
   - Question generation tools

4. **Hooks for Automation:**
   - `UserPromptSubmit` - Add context before processing
   - `PreToolUse` / `PostToolUse` - Validate and log tool usage
   - `Stop` - Save session data after completion
   - `SessionStart` / `SessionEnd` - Initialize and cleanup

5. **Built-in Tools:**
   - `Read` / `Write` / `Edit` - File operations
   - `Glob` / `Grep` - File search and content search
   - `WebSearch` / `WebFetch` - External resources
   - `Bash` - Command execution

### What Requires Custom Implementation (🔶 Partial Support)

1. **Session Persistence:**
   - SDK manages conversation within session
   - Custom: Cross-session state, session selection UI

2. **Performance Database:**
   - SDK provides tools
   - Custom: Database schema, query logic, aggregations

3. **Progress Algorithms:**
   - SDK can make decisions based on data
   - Custom: Score calculation formulas, improvement thresholds, repetition logic

4. **CLI/UI Layer:**
   - SDK is library-based
   - Custom: User interface, menu system, input handling

---

## File Organization

```
StudyBrainTemplate/
├── CLAUDE.md                                    # This file - project context
├── Design/                                      # Design documents
│   ├── V1_Design_Overview.md                    # Professional V1 specification
│   ├── Claude_SDK_Capabilities_Analysis.md      # SDK feature mapping
│   ├── V1_Design_Questions.md                   # Design questionnaire (answered)
│   ├── SDK_Access_Verification.md               # Confirmed Pro account SDK access
│   ├── V2_System_Architecture.md                # ⭐ Complete V2 technical spec
│   └── Implementation_Kickstart.md              # Day 1-2 getting started guide
├── ExamplePhysicsUsageV1/                       # Original flowchart and notes
│   ├── ExamplePhysicsUsageV1.md                 # Original V1 documentation
│   └── ExamplePhysicsUsageV1.drawio             # Flowchart (draw.io format)
├── CLAUDE_DOCS/                                 # Complete Claude documentation
│   ├── DOCUMENTATION_MAP.md                     # Navigation guide for docs
│   ├── Developer-Guide/                         # General Claude capabilities
│   ├── API-Guide/                               # API and SDK documentation
│   └── Claude-Code/                             # Claude Code CLI documentation
└── [Implementation - To Be Created]
    └── studybrain_web/                          # Flask web application
        ├── app.py                               # Flask entry point
        ├── agents/                              # Agent implementations
        │   ├── coordinator.py
        │   ├── subjects/                        # Subject agents
        │   │   ├── physics.py
        │   │   ├── mathematics_ext1.py
        │   │   ├── mathematics_adv.py
        │   │   ├── chemistry.py
        │   │   ├── software_engineering.py
        │   │   └── english.py
        │   └── subagents/                       # Specialized sub-agents
        │       ├── curriculum_expert.py
        │       ├── question_generator.py
        │       ├── answer_evaluator.py
        │       └── progress_tracker.py
        ├── mcp_tools/                           # Custom MCP tools
        │   ├── diagnostics.py
        │   ├── progress.py
        │   ├── fsrs_scheduler.py
        │   ├── resources.py
        │   └── timer.py
        ├── routes/                              # Flask routes
        │   ├── dashboard.py
        │   ├── study.py
        │   ├── progress.py
        │   └── api.py
        ├── services/                            # Business logic
        │   ├── score_calculator.py
        │   ├── exam_priority.py
        │   └── cross_subject.py
        ├── templates/                           # HTML templates
        │   ├── dashboard.html
        │   ├── study_session.html
        │   └── progress.html
        ├── static/                              # CSS, JS
        │   ├── css/
        │   └── js/
        └── data/                                # JSON storage
            ├── progress/
            ├── sessions/
            ├── quiz_results/
            ├── exams/
            ├── study_timer/
            └── resource_index/
```

---

## Development Workflow

### Current Phase: Implementation (Phase 1 - MVP)

**Timeline:** October 1-12, 2025 (12 days)
**Goal:** Working StudyBrain with core features for all 6 subjects

**Phase 1 Implementation Plan:**

**Days 1-2: Foundation**
- ✅ Design complete (V2 System Architecture)
- ⏳ Flask project setup with virtual environment
- ⏳ Basic coordinator agent with Claude SDK integration
- ⏳ Dashboard template with 6 subject cards
- ⏳ Test SDK connection and basic routing

**Days 3-4: Agent Architecture**
- Build coordinator agent with subject routing logic
- Create Physics agent (first subject implementation)
- Implement curriculum expert sub-agent
- Test multi-agent communication

**Days 5-6: Core MCP Tools**
- Implement `generate_diagnostic_quiz` tool
- Implement `save_quiz_result` tool
- Implement `get_progress_summary` tool
- Create JSON data schemas

**Days 7-8: Web Interface**
- Build study session page (quiz interface)
- Add LaTeX/MathJax support
- Implement timer functionality
- Create progress visualization page

**Days 9-10: Integration & Multi-Subject**
- Add remaining 5 subject agents
- Implement FSRS scheduling (py-fsrs)
- Build cross-subject concept registry
- End-to-end testing with Physics

**Days 11-12: Polish & Deploy**
- UI/UX improvements
- Plotly chart integration
- Bug fixes and optimization
- Documentation for usage

**Completed Phases:**

1. ✅ **V1 Conceptual Design** - Original flowchart and documentation
2. ✅ **Design Questionnaire** - All design decisions finalized
3. ✅ **V2 Technical Specification** - Complete architecture document
4. ✅ **Implementation Kickstart Guide** - Day 1-2 setup instructions

**Upcoming Phases:**

- **Phase 2** (By end of October): Cross-subject integration, advanced progress tracking, spaced repetition optimization
- **Phase 3** (November-December): External resource integration, exam prediction, performance optimization
- **Phase 4** (January 2026): Production hardening, real-world validation with Year 12 content

### Guiding Principles

1. **Build for the user (James):**
   - Design decisions should match actual study patterns
   - Interface should fit into existing workflow
   - System should be maintainable and extensible by James

2. **Start simple, iterate:**
   - MVP first, polish later
   - Validate core concept before adding features
   - Use real study content for testing

3. **Leverage Claude SDK fully:**
   - Use built-in features instead of reinventing
   - Custom tools only when necessary
   - Follow SDK best practices

4. **Quantitative approach:**
   - Track everything measurable
   - Evidence-based decisions
   - A/B test study strategies

---

## Key Concepts and Terminology

### Conceptual Understanding (Con)
- **Definition:** Depth of comprehension - the "WHY" behind concepts
- **Measurement:** 0-100% scale based on explanation quality, reasoning, and connections
- **Goal:** Deep, intuitive grasp that transfers to novel problems

### Functional Knowledge (Func)
- **Definition:** Practical application ability - the "HOW" in exam conditions
- **Measurement:** 0-100% scale based on correct answers under time pressure
- **Goal:** Consistent performance on exam-style questions

### Diagnostics Quiz
- **Purpose:** Identify knowledge gaps across curriculum
- **Method:** Systematic testing of untested areas
- **Output:** Hierarchical breakdown with Con/Func scores per topic
- **Adaptive:** Prioritizes practice papers, adjusts difficulty

### Study Session
- **Purpose:** Improve understanding and application for weak areas
- **Components:**
  1. Content research and synthesis
  2. Knowledge application (practice questions)
  3. Functional assessment (exam-style questions)
  4. Progress evaluation (repeat or move on)

### Session State
- **Data:** Last active topic, conversation context, user preferences
- **Persistence:** Saved between sessions for continuity
- **Recovery:** Option to continue or start fresh

---

## Success Metrics

### System Quality Metrics
- **Coverage completeness:** % of syllabus assessed
- **Gap identification accuracy:** Do weak areas align with actual exam performance?
- **Time efficiency:** Time to complete diagnostics vs. manual review

### Learning Effectiveness Metrics
- **Score improvement rate:** Con/Func increase per study hour
- **Retention over time:** Score degradation after 1 week, 1 month
- **Transfer to exams:** Diagnostics scores vs. actual test scores

### User Experience Metrics
- **Session completion rate:** % of started sessions finished
- **Engagement duration:** Average study time per session
- **Recommendation acceptance:** Does user follow system suggestions?

---

## Important Notes for AI Assistants

### When Working on This Project:

1. **Read relevant design docs first:**
   - Start with `Design/V1_Design_Overview.md` for high-level understanding
   - Check `Design/Claude_SDK_Capabilities_Analysis.md` for implementation patterns
   - Reference `CLAUDE_DOCS/DOCUMENTATION_MAP.md` for SDK feature lookup

2. **Understand the student context:**
   - HSC is high-stakes (determines university admission)
   - James is proactive but needs retention help
   - System must be practical for daily use during school year

3. **Prioritize effectiveness over complexity:**
   - Evidence-based approaches (track what works)
   - Simple UX for daily usage
   - Extensible architecture for future additions

4. **Respect data privacy:**
   - Study data is personal and sensitive
   - Default to local storage
   - Encryption for sensitive information

5. **Design for maintainability:**
   - James will need to modify and extend the system
   - Clear code structure and documentation
   - Python preferred for accessibility

### Common Tasks:

**When designing new features:**
- Check if Claude SDK has built-in support
- Look for similar patterns in SDK documentation
- Consider cost implications (API tokens)
- Map to existing V1 design concepts

**When implementing:**
- Follow SDK best practices (see `CLAUDE_DOCS/`)
- Use MCP custom tools for StudyBrain-specific logic
- Leverage subagents for specialized tasks
- Test with realistic study content

**When debugging:**
- Check SDK hook outputs (use `--debug` flag)
- Validate tool parameter schemas
- Review conversation history for context issues
- Test error handling with edge cases

---

## Resources

### Documentation
- **Claude SDK:** `CLAUDE_DOCS/` directory (comprehensive local copy)
- **V1 Design:** `Design/V1_Design_Overview.md` (historical reference)
- **V2 Architecture:** `Design/V2_System_Architecture.md` ⭐ (complete technical specification)
- **Implementation Guide:** `Design/Implementation_Kickstart.md` (Day 1-2 setup)
- **SDK Analysis:** `Design/Claude_SDK_Capabilities_Analysis.md`
- **SDK Access:** `Design/SDK_Access_Verification.md` (Pro account confirmation)
- **Design Questions:** `Design/V1_Design_Questions.md` (answered questionnaire)

### External References
- **NESA HSC Syllabus:** [educationstandards.nsw.edu.au](https://educationstandards.nsw.edu.au)
- **Claude Agent SDK (Python):** [github.com/anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)
- **Model Context Protocol:** [modelcontextprotocol.io](https://modelcontextprotocol.io)

### Student Resources (To Be Organized)
- Practice papers
- Class materials
- Curriculum documents
- Personal study notes

---

## Immediate Next Steps (For Implementation)

**START HERE:** Follow `Design/Implementation_Kickstart.md` for complete Day 1-2 setup

### Quick Start (5 minutes)
```bash
cd StudyBrainTemplate
mkdir studybrain_web && cd studybrain_web
mkdir -p agents/subjects agents/subagents mcp_tools routes services templates static/css static/js
mkdir -p data/{sessions,exams,progress,quiz_results,study_timer,resource_index}
python3 -m venv venv
source venv/bin/activate
pip install Flask==3.0.0 flask-cors==4.0.0 claude-agent-sdk py-fsrs plotly==5.17.0
```

### Day 1 Tasks
1. ✅ **Read CLAUDE.md** - Understand project context
2. ✅ **Review V2_System_Architecture.md** - Understand complete technical design
3. ⏳ **Set up Flask project** - Follow kickstart guide
4. ⏳ **Create minimal app.py** - Basic coordinator agent integration
5. ⏳ **Test SDK connection** - Verify Claude Pro authentication works

### Day 2 Tasks
1. Build dashboard template with 6 subject cards
2. Implement coordinator agent routing
3. Create first subject agent (Physics)
4. Test end-to-end: Dashboard → Physics agent → response

### Completed Design Phase
1. ✅ **V1 conceptual design**
2. ✅ **Design questionnaire answered**
3. ✅ **V2 technical specification created**
4. ✅ **Implementation guide prepared**

---

## Contact and Communication

**Primary User:** James (Year 11 student)
**Usage Context:** Academic/Educational
**Timeline:** Needs working system before Year 12 trials (mid-2026)
**Support:** Claude Pro subscription for development and usage

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-10-01 | Initial CLAUDE.md creation | Claude (Assistant) |
| 2.0 | 2025-10-01 | Design phase complete: V2 architecture finalized, all decisions made, implementation guide created | Claude (Assistant) |

---

**End of Context Document**

*This file serves as the primary context for all AI assistants working on the StudyBrain project. Keep it updated as the project evolves.*
