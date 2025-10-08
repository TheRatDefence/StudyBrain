# Phase Connections & Dependencies

Visual guide to how each phase builds on previous work.

---

## Dependency Graph

```
Phase 1: Core Infrastructure
    │
    ├─────────────────────┐
    ↓                     ↓
Phase 2: Quiz System   Phase 4: Multi-Subject
    │                     │
    ↓                     ↓
Phase 3: Progress      Phase 5: FSRS
    │    Tracking          │
    │                     │
    └──────┬──────────────┘
           ↓
    Phase 6: Study Sessions
           │
           ↓
    Phase 7: UI Visualization
           │
           ↓
    Phase 8: Sub-Agents
           │
           ↓
    Phase 9: Resource Management
           │
           ↓
    Phase 10: Cross-Subject
```

---

## What Each Phase Adds

### Phase 1: Foundation 🏗️
**Adds:** Flask app, coordinator agent, Physics agent
**Enables:** Basic AI tutoring

### Phase 2: Quizzes 📝
**Adds:** Question generation, answer submission
**Uses from Phase 1:** Coordinator agent, routes
**Enables:** Practice questions

### Phase 3: Progress 📊
**Adds:** Score calculation, progress tracking
**Uses from Phase 2:** Quiz results
**Enables:** See how you're doing

### Phase 4: All Subjects 🎓
**Adds:** 5 more subject agents
**Uses from Phase 1-3:** Entire system structure
**Enables:** Study all HSC subjects

### Phase 5: FSRS 🧠
**Adds:** Spaced repetition scheduling
**Uses from Phase 3:** Progress data
**Enables:** Never forget what you learned

### Phase 6: Sessions ⏱️
**Adds:** Timer, session persistence
**Uses from Phase 3:** Progress tracking
**Enables:** Track study time and learning rate

### Phase 7: Beautiful UI ✨
**Adds:** Charts, LaTeX, styling
**Uses from Phase 3, 6:** Progress and session data
**Enables:** Professional, polished experience

### Phase 8: Smart Agents 🎯
**Adds:** Specialized sub-agents
**Uses from Phase 2:** Quiz system
**Enables:** HSC-quality questions and marking

### Phase 9: Resources 📚
**Adds:** PDF indexing, resource search
**Uses from Phase 8:** Curriculum expert
**Enables:** Organize all study materials

### Phase 10: Integration 🔗
**Adds:** Cross-subject connections, recommendations
**Uses from Phase 4, 5:** Multi-subject, FSRS data
**Enables:** Intelligent study planning

---

## Milestone Checkpoints

### After Phase 3: "Usable MVP" ✅
You can:
- Study Physics with AI tutor
- Take practice quizzes
- See your progress

### After Phase 4: "Multi-Subject MVP" ✅
You can:
- Study all 6 HSC subjects
- Everything from Phase 3, but for all subjects

### After Phase 7: "Polished Product" ✅
You can:
- Professional-looking interface
- Beautiful charts and graphs
- Time tracking
- Everything feels complete

### After Phase 10: "Complete Vision" ✅
You can:
- Optimal study recommendations
- Cross-subject integration
- Full resource library
- Everything works together intelligently

---

## Which Phases Can Be Done in Parallel?

**Parallel Track 1:** Phases 1 → 2 → 3 → 7 → 8
(Core quiz system → Visualization → Intelligence)

**Parallel Track 2:** Phase 4
(Can be done anytime after Phase 1)

**Parallel Track 3:** Phases 5 → 6
(Spaced repetition → Sessions, somewhat independent)

**Must Be Sequential:** Phase 9 → 10
(Resources need sub-agents, cross-subject needs all features)

---

## Simplified Dependency Rules

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

## Recommended Order

### Conservative Path (fully sequential):
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

### Optimized Path (some parallelism):
1 → 2 → 3 → 7 (UI polish)
     ↓
     4 (multi-subject)
     ↓
     5 (FSRS) + 6 (sessions) in parallel
     ↓
     8 → 9 → 10

### Fast Path to Usable Product:
1 → 2 → 3 → 4 → DONE (skip 5-10 for now, add later)

---

## Files Modified Across Phases

### `app.py`
- Phase 1: Created
- Phase 2: Add quiz routes
- Phase 3: Add progress routes
- Phase 6: Add session routes
- Phase 9: Add resource routes

### `agents/coordinator.py`
- Phase 1: Created
- Phase 2: Add MCP tools
- Phase 3: Add progress tools
- Phase 4: Add all subject agents
- Phase 10: Enhanced recommendation logic

### `templates/dashboard.html`
- Phase 1: Created
- Phase 4: All subject cards active
- Phase 5: Add FSRS due widget
- Phase 7: Visual polish
- Phase 10: Add recommendations widget

---

## Testing Strategy

**After Each Phase:**
1. Run full system (python app.py)
2. Test new features work
3. Verify old features still work
4. Check data files save correctly
5. Commit to git

**Integration Testing:**
- After Phase 4: Test all subjects
- After Phase 7: Test all visualizations
- After Phase 10: End-to-end workflow test

---

**Use this guide to plan your development path!**
