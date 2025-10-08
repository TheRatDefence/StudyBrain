# StudyBrain Agile Development Roadmap

**Approach:** Incremental, iterative development
**Structure:** 10 phases, each building on the previous
**Duration:** ~2-3 weeks (flexible)

---

## Philosophy

This roadmap follows an **agile/iterative approach** rather than waterfall:
- Each phase delivers something **functional and usable**
- You can **test and use** the system after each phase
- Phases build **incrementally** - no big bang integration
- Each phase can be handled by a **separate Claude instance**
- **Refinement happens continuously**, not at the end

---

## Phase Overview

```
Phase 1: Core Infrastructure
    ↓ (working web app with basic agent)
Phase 2: Quiz System
    ↓ (can generate & answer questions)
Phase 3: Progress Tracking
    ↓ (can see scores and improvement)
Phase 4: Multi-Subject
    ↓ (all 6 subjects working)
Phase 5: FSRS Integration
    ↓ (spaced repetition scheduling)
Phase 6: Study Sessions
    ↓ (timer, session management)
Phase 7: UI Visualization
    ↓ (charts, LaTeX, polished UI)
Phase 8: Sub-Agents
    ↓ (intelligent question generation)
Phase 9: Resource Management
    ↓ (organize and search materials)
Phase 10: Cross-Subject
    ↓ (optimal study recommendations)
```

---

## Phase 1: Core Infrastructure

**Goal:** Get a working Flask app with basic Claude agent integration

**Outcomes:**
- ✅ Flask app running on localhost:5000
- ✅ Basic coordinator agent responds to queries
- ✅ One subject agent (Physics) working
- ✅ Simple dashboard with subject cards
- ✅ Basic study session page (conversation only, no quizzes)
- ✅ Claude SDK connection verified

**Deliverable:**
Web app where you can ask Physics questions and get AI tutor responses

**Files Created:**
- `app.py` - Flask entry point
- `templates/dashboard.html` - Home page
- `templates/study_session.html` - Study page
- `agents/coordinator.py` - Coordinator config
- `agents/subjects/physics.py` - Physics agent config
- `requirements.txt` - Dependencies

**Test:** Can navigate to dashboard, click Physics, ask a question, get response

---

## Phase 2: Quiz System

**Goal:** Add quiz generation and answer submission

**Builds on:** Phase 1 (uses existing coordinator agent)

**Outcomes:**
- ✅ First MCP tool: `generate_practice_question`
- ✅ Second MCP tool: `save_quiz_result`
- ✅ Quiz interface (text-based questions)
- ✅ Answer submission form with confidence slider
- ✅ Quiz results saved to JSON files
- ✅ Basic marking (pass/fail, manual scoring)

**Deliverable:**
Can request a practice question on a topic, answer it, submit with confidence, and have result saved

**Files Created:**
- `mcp_tools/diagnostics.py` - Quiz tools
- `templates/quiz.html` - Quiz interface
- `routes/quiz.py` - Quiz routes
- `data/quiz_results/` - Storage for results

**Test:** Generate a Physics question, answer it, submit, check JSON file created

---

## Phase 3: Progress Tracking

**Goal:** Calculate and display conceptual/functional scores

**Builds on:** Phase 2 (uses quiz results from Phase 2)

**Outcomes:**
- ✅ Progress data structure (JSON schema)
- ✅ MCP tool: `update_progress_scores`
- ✅ MCP tool: `get_progress_summary`
- ✅ Score calculation algorithm (basic percentage)
- ✅ Progress view showing Con/Func scores by topic
- ✅ Improvement tracking (before/after)

**Deliverable:**
After completing quizzes, can see your scores organized by Module → Topic → Subtopic

**Files Created:**
- `mcp_tools/progress.py` - Progress tools
- `services/progress_calculator.py` - Scoring logic
- `templates/progress.html` - Progress view
- `routes/progress.py` - Progress routes
- `data/progress/physics.json` - Progress storage

**Test:** Complete 3 quizzes, check progress view shows scores correctly

---

## Phase 4: Multi-Subject

**Goal:** Expand from Physics-only to all 6 subjects

**Builds on:** Phases 1-3 (replicates working Physics setup for other subjects)

**Outcomes:**
- ✅ 5 additional subject agents created
  - Mathematics Extension 1
  - Mathematics Advanced
  - Software Engineering
  - English Standard
  - Music
- ✅ Coordinator routes to all 6 subjects correctly
- ✅ Dashboard shows all 6 subject cards
- ✅ Each subject has own data directories
- ✅ Progress tracking works for all subjects

**Deliverable:**
Full multi-subject system where you can study any HSC subject

**Files Created:**
- `agents/subjects/maths_ext1.py`
- `agents/subjects/maths_adv.py`
- `agents/subjects/software.py`
- `agents/subjects/english.py`
- `agents/subjects/music.py`
- `data/progress/{subject}.json` for each subject

**Test:** Click each subject card, ask questions, generate quizzes for each

---

## Phase 5: FSRS Integration

**Goal:** Add spaced repetition scheduling

**Builds on:** Phase 3 (enhances progress tracking with review dates)

**Outcomes:**
- ✅ `py-fsrs` library integrated
- ✅ FSRS data fields added to progress JSON
- ✅ MCP tool: `schedule_fsrs_review`
- ✅ MCP tool: `get_due_reviews`
- ✅ Dashboard widget: "Topics Due for Review"
- ✅ Review scheduling based on performance

**Deliverable:**
System tells you which topics need reviewing and when (spaced repetition)

**Files Created:**
- `services/fsrs_scheduler.py` - FSRS logic
- `mcp_tools/fsrs_integration.py` - FSRS tools
- `templates/components/due_reviews.html` - Dashboard widget

**Test:** Complete quiz with good score, check next review is scheduled 3+ days out; bad score = 1 day

---

## Phase 6: Study Sessions

**Goal:** Add session management with timer and persistence

**Builds on:** Phases 1-5 (adds session layer around existing study flow)

**Outcomes:**
- ✅ Study timer (Toggl-style start/stop)
- ✅ Session persistence (can resume interrupted sessions)
- ✅ Session data structure (JSON schema)
- ✅ MCP tools: `start_study_session`, `end_study_session`
- ✅ Learning rate calculation (improvement per hour)
- ✅ Session history view

**Deliverable:**
Proper study session workflow with time tracking and ability to resume where you left off

**Files Created:**
- `mcp_tools/study_timer.py` - Timer tools
- `services/session_manager.py` - Session logic
- `templates/components/timer_widget.html` - Timer UI
- `data/sessions/{subject}/` - Session storage

**Test:** Start session, answer 2 questions, close browser, reopen, can resume session

---

## Phase 7: UI Visualization

**Goal:** Polish the UI with charts and LaTeX support

**Builds on:** Phase 3 (visualizes progress data from Phase 3)

**Outcomes:**
- ✅ Plotly chart integration
- ✅ Progress timeline chart (score over time)
- ✅ Module breakdown radar chart
- ✅ Learning rate chart
- ✅ LaTeX/MathJax support for equations
- ✅ Improved quiz interface styling
- ✅ Responsive design

**Deliverable:**
Beautiful, professional-looking study system with graphs and proper math rendering

**Files Created:**
- `static/js/charts.js` - Chart rendering
- `static/css/main.css` - Styling
- `templates/components/progress_chart.html`
- Updated quiz templates with LaTeX support

**Test:** View progress page, see interactive charts; answer math question with equations displayed properly

---

## Phase 8: Sub-Agents

**Goal:** Add specialized sub-agents for better question generation and marking

**Builds on:** Phase 2 (replaces basic quiz tools with intelligent agents)

**Outcomes:**
- ✅ Curriculum Expert sub-agent
- ✅ Question Generator sub-agent
- ✅ Answer Evaluator sub-agent
- ✅ Progress Tracker sub-agent
- ✅ Improved question quality (HSC-style)
- ✅ Better marking with detailed feedback
- ✅ Misconception detection

**Deliverable:**
Questions feel like real HSC exams, marking provides detailed feedback like a real teacher

**Files Created:**
- `agents/subagents/curriculum_expert.py`
- `agents/subagents/question_generator.py`
- `agents/subagents/answer_evaluator.py`
- `agents/subagents/progress_tracker.py`

**Test:** Generate question - should be HSC quality; submit answer - should get detailed feedback with specific errors identified

---

## Phase 9: Resource Management

**Goal:** Organize and search study materials

**Builds on:** Phase 8 (curriculum expert uses resources for question generation)

**Outcomes:**
- ✅ Resource indexing system
- ✅ MCP tools: `index_resources`, `search_resources`
- ✅ Auto-organize files by subject/module/topic
- ✅ PDF text extraction (Claude vision)
- ✅ Resource library view
- ✅ Link resources to questions/topics

**Deliverable:**
Can dump all study materials into a folder and system organizes them; can search by topic

**Files Created:**
- `mcp_tools/resources.py` - Resource tools
- `services/resource_indexer.py` - Indexing logic
- `templates/resources.html` - Resource library view
- `data/resource_index/{subject}.json` - Resource metadata

**Test:** Upload 10 PDFs, run indexing, search for "electricity", find relevant resources

---

## Phase 10: Cross-Subject Integration

**Goal:** Connect concepts across subjects and optimize study recommendations

**Builds on:** Phase 4 (uses multi-subject data from Phase 4)

**Outcomes:**
- ✅ Cross-subject concept registry
- ✅ MCP tools: `update_cross_subject_concept`, `suggest_cross_subject_study`
- ✅ Coordinator can recommend study order
- ✅ "What should I study next?" algorithm
- ✅ Exam priority calculator
- ✅ Multi-subject learning paths

**Deliverable:**
System intelligently suggests what to study next considering all subjects, exam dates, and weak areas

**Files Created:**
- `mcp_tools/cross_subject.py` - Cross-subject tools
- `services/exam_priority.py` - Priority algorithm
- `data/cross_subject_concepts.json` - Concept registry
- Enhanced coordinator agent

**Test:** Ask "What should I study next?" - system considers Physics exam in 5 days with 30% score vs Maths in 2 weeks at 80%

---

## How to Use This Roadmap

### For Each Phase:

1. **Read the phase README** (you'll create one for each phase)
2. **Focus only on that phase's outcomes** - don't worry about future phases
3. **Build incrementally** - make it work, then move to next phase
4. **Test thoroughly** - make sure phase works before continuing
5. **Commit to git** after each phase

### Working with Different Claude Instances:

Each phase folder will have a `CLAUDE.md` that contains:
- Phase goals and outcomes
- What you need from previous phases
- Implementation checklist
- Testing instructions
- Files to create/modify

You can open a new Claude Code instance for each phase, it reads the phase CLAUDE.md, and it knows exactly what to build.

### Iteration and Refinement:

- You can **revisit earlier phases** to improve them
- **Don't aim for perfection** in each phase - aim for functional
- **Refactor as you go** - code quality improves with each phase
- **Test with real content** - use actual HSC materials

---

## Timeline (Flexible)

**Week 1:** Phases 1-4 (Core + Multi-Subject)
**Week 2:** Phases 5-7 (FSRS + Sessions + UI)
**Week 3:** Phases 8-10 (Sub-Agents + Resources + Cross-Subject)

**This is flexible!** You can spend more time on phases you find valuable, skip phases you don't need yet, or split phases into smaller chunks.

---

## Success Criteria

After **Phase 4**, you should have a **usable study system**:
- Can study all 6 subjects
- Can generate and answer questions
- Can track progress

After **Phase 7**, you should have a **polished MVP**:
- Professional UI
- Charts and visualizations
- Time tracking

After **Phase 10**, you should have the **complete vision**:
- Intelligent recommendations
- Cross-subject integration
- Resource management

---

## Getting Started

1. **Start with Phase 1**
2. Create a `CLAUDE.md` in `Phase-01-Core-Infrastructure/` based on outcomes listed above
3. Open that phase in Claude Code
4. Build the phase
5. Test it works
6. Move to Phase 2

**Ready to build? Start with Phase 1!**
