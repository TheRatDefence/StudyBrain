# StudyBrain Development Roadmap

**Approach:** Incremental, iterative development
**Structure:** 10 phases, each building on the previous
**Duration:** ~2-3 weeks (flexible)

---

## Philosophy

- Each phase delivers something **functional and usable**
- Test and use the system after each phase
- Build **incrementally** - no big bang integration
- Each phase can be handled by a **separate Claude instance**

---

## Phase Overview

```
Phase 1: Core Infrastructure (Flask + coordinator + Physics)
    ↓
Phase 2: Quiz System (question generation & submission)
    ↓
Phase 3: Progress Tracking (Con/Func scores)
    ↓
Phase 4: Multi-Subject (all 6 subjects)
    ↓
Phase 5: FSRS Integration (spaced repetition)
    ↓
Phase 6: Study Sessions (timer, persistence)
    ↓
Phase 7: UI Visualization (charts, LaTeX, polish)
    ↓
Phase 8: Sub-Agents (intelligent question gen)
    ↓
Phase 9: Resource Management (PDF organization)
    ↓
Phase 10: Cross-Subject (study recommendations)
```

---

## Phase Details

### Phase 1: Core Infrastructure (1-2d)
**Deliverable:** Working Flask app with Physics AI tutor

- ✅ Flask app on localhost:5000
- ✅ Coordinator agent
- ✅ Physics subject agent
- ✅ Simple dashboard
- ✅ Basic study session page

**Files:** `app.py`, `agents/`, `templates/dashboard.html`, `requirements.txt`

---

### Phase 2: Quiz System (2-3d)
**Deliverable:** Generate and submit practice questions

- MCP tool: `generate_practice_question`
- MCP tool: `save_quiz_result`
- Quiz interface with confidence slider
- Quiz results saved to JSON

**Files:** `mcp_tools/diagnostics.py`, `templates/quiz.html`, `data/quiz_results/`

---

### Phase 3: Progress Tracking (2-3d)
**Deliverable:** View Con/Func scores by topic

- Progress JSON schema
- MCP tool: `update_progress_scores`
- MCP tool: `get_progress_summary`
- Score calculation algorithm
- Progress view (Module → Topic → Subtopic)

**Files:** `mcp_tools/progress.py`, `services/progress_calculator.py`, `templates/progress.html`

---

### Phase 4: Multi-Subject (1-2d)
**Deliverable:** All 6 HSC subjects working

- 5 additional subject agents (Maths Ext1, Maths Adv, Software, English, Music)
- Coordinator routes all subjects
- Dashboard shows all 6 cards
- Progress tracking for all subjects

**Files:** `agents/subjects/*.py`, `data/progress/{subject}.json`

---

### Phase 5: FSRS Integration (2d)
**Deliverable:** Spaced repetition scheduling

- `py-fsrs` library integrated
- FSRS fields in progress JSON
- MCP tools: `schedule_fsrs_review`, `get_due_reviews`
- Dashboard: "Topics Due for Review" widget

**Files:** `services/fsrs_scheduler.py`, `mcp_tools/fsrs_integration.py`

---

### Phase 6: Study Sessions (1-2d)
**Deliverable:** Timer & session persistence

- Study timer (Toggl-style)
- Session persistence (resume capability)
- MCP tools: `start/end_study_session`
- Learning rate calculation
- Session history view

**Files:** `mcp_tools/study_timer.py`, `services/session_manager.py`, `data/sessions/`

---

### Phase 7: UI Visualization (2-3d)
**Deliverable:** Professional UI with charts

- Plotly chart integration
- Progress timeline & radar charts
- LaTeX/MathJax support
- Improved styling
- Responsive design

**Files:** `static/js/charts.js`, `static/css/main.css`, updated templates

---

### Phase 8: Sub-Agents (3-4d)
**Deliverable:** HSC-quality questions & marking

- Curriculum Expert sub-agent
- Question Generator sub-agent
- Answer Evaluator sub-agent
- Progress Tracker sub-agent
- Detailed feedback & misconception detection

**Files:** `agents/subagents/{curriculum_expert,question_generator,answer_evaluator,progress_tracker}.py`

---

### Phase 9: Resource Management (2-3d)
**Deliverable:** Organized study materials with search

- Resource indexing system
- MCP tools: `index_resources`, `search_resources`
- Auto-organize by subject/module/topic
- PDF text extraction (Claude vision)
- Resource library view

**Files:** `mcp_tools/resources.py`, `services/resource_indexer.py`, `templates/resources.html`

---

### Phase 10: Cross-Subject Integration (2-3d)
**Deliverable:** Intelligent study recommendations

- Cross-subject concept registry
- MCP tools: `update_cross_subject_concept`, `suggest_cross_subject_study`
- "What should I study next?" algorithm
- Exam priority calculator
- Multi-subject learning paths

**Files:** `mcp_tools/cross_subject.py`, `services/exam_priority.py`, `data/cross_subject_concepts.json`

---

## Dependency Rules

**Phase 1:** No dependencies (start here!)
**Phase 2:** Needs Phase 1 (coordinator agent)
**Phase 3:** Needs Phase 2 (quiz results)
**Phase 4:** Needs Phase 1 (can replicate structure)
**Phase 5:** Needs Phase 3 (progress data)
**Phase 6:** Needs Phase 3 (progress tracking)
**Phase 7:** Needs Phases 3, 6 (data to visualize)
**Phase 8:** Needs Phase 2 (quiz system)
**Phase 9:** Needs Phase 8 (curriculum expert)
**Phase 10:** Needs Phases 4, 5 (multi-subject + FSRS)

---

## Development Paths

### Conservative (fully sequential):
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

### Optimized (some parallelism):
1 → 2 → 3 → 7 (UI polish)
     ↓
     4 (multi-subject)
     ↓
     5 (FSRS) + 6 (sessions) in parallel
     ↓
     8 → 9 → 10

### Fast MVP:
1 → 2 → 3 → 4 → DONE (skip 5-10, add later)

---

## Milestones

### After Phase 3: "Usable MVP" ✅
- Study Physics with AI tutor
- Take practice quizzes
- See progress scores

### After Phase 4: "Multi-Subject MVP" ✅
- All 6 HSC subjects available
- Everything from Phase 3, for all subjects

### After Phase 7: "Polished Product" ✅
- Professional UI
- Charts and visualizations
- Time tracking

### After Phase 10: "Complete Vision" ✅
- Intelligent recommendations
- Cross-subject integration
- Full resource library

---

## Usage Guide

**For Each Phase:**
1. Read phase README in `Phase-XX/`
2. Focus only on that phase's outcomes
3. Build incrementally - make it work
4. Test thoroughly
5. Commit to git

**Testing Strategy:**
- After each phase: run full system, test new & old features
- After Phase 4: test all subjects
- After Phase 7: test all visualizations
- After Phase 10: end-to-end workflow test

---

## Timeline (Flexible)

**Week 1:** Phases 1-4 (Core + Multi-Subject)
**Week 2:** Phases 5-7 (FSRS + Sessions + UI)
**Week 3:** Phases 8-10 (Sub-Agents + Resources + Cross-Subject)

**Ready to build? Start with Phase 1!**
