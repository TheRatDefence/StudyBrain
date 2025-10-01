# StudyBrain V1 - Design Clarification Questions

**Purpose:** Gather missing information to complete V2 design
**Date:** October 2025
**Status:** Awaiting Responses

---

## Instructions

Please answer these questions to help finalize the StudyBrain V2 design. Your answers will determine:
- Implementation approach
- Technology stack
- Feature prioritization
- Development timeline

For each question, provide as much detail as possible. If you're unsure, indicate your preferences or constraints.

---

## 1. Multi-Agent Architecture

### Q1.1: Agent Communication Patterns

**Current V1 Design:** Each subject has its own agent (Physics, Maths, Chemistry, etc.)

**Questions:**
1. Should agents be able to communicate with each other?
   - Example: Physics agent suggesting math revision when student struggles with projectile motion
   - Yes, this would be very useful for situations such as in the example and for future ideas.
   - I want to implement a coordinator agent at some point that can communicate with agents and handle non-subject specific things or queries such as "What subject should I study next?" 

2. If yes, what information should be shared between agents?
   - [X] Progress scores (conceptual/functional understanding)
   - [X] Recently studied topics
   - [X] Common weak areas across subjects
   - [x] Study session timestamps
   - [X] Other: Priority (which subject should take study priority based on exam timing and student ability)
   - [X] Other: Student details (anything that is student specific that would help an agent with teaching the student)

3. How should cross-subject concepts be handled?
   - Example: Calculus appears in both Maths and Physics
   - **Option A:** Each agent handles independently
   - **Option B:** Shared "concept registry" that both agents update
   - **Option C:** Dedicated "cross-subject coordinator" agent
   - Your choice: B but sometimes C depending on how important the concept/area/topic is.

---

### Q1.2: Agent Specialization

**Question:**
Should there be specialized sub-agents within each subject?

**Example Architecture:**
```
Physics Agent
├── Question Generator Sub-agent
├── Answer Evaluator Sub-agent
├── Study Planner Sub-agent
└── Concept Explainer Sub-agent
```

- **Option A:** One general agent per subject (simpler, slower)
- **Option B:** Multiple specialized sub-agents (complex, faster, better quality)
- **Option C:** Hybrid (general agent + specialized for specific tasks)

Your preference: Option B

**Follow-up:** If Option B or C, which tasks should have specialized agents?
- [X] Question generation
- [X] Answer marking/evaluation
- [ ] Study planning
- [ ] Concept explanation
- [X] Progress tracking
- [ ] Resource summarization
- Other: Curriculum expert - This specialized agent should be a sort of "librarian" which has a very indepth knowledge of the: Curriculum, Resources and Subject. 

---

## 2. User Interface

### Q2.1: Interface Type

**Question:** What interface should StudyBrain use?

**Options:**

**A) Pure CLI (Command Line Interface)**
- Pros: Simple to implement, works everywhere, fast
- Cons: Less intuitive for complex interactions, no visualizations
- Example: Current design (`sb physics`)

**B) TUI (Terminal User Interface)**
- Pros: Interactive menus in terminal, keyboard shortcuts, split panes
- Cons: Still text-only, no graphical visualizations
- Example: Tools like `htop`, `vim`

**C) GUI (Graphical User Interface)**
- Pros: Visual progress tracking, drag-and-drop files, charts/graphs
- Cons: More complex development, platform-specific
- Example: Desktop app with windows and buttons

**D) Web Interface**
- Pros: Works on any device, shareable, rich visualizations
- Cons: Requires web server, more complex architecture
- Example: Browser-based dashboard

**E) Hybrid**
- Example: CLI for quick commands + web dashboard for progress tracking
- Specify combination: _______________

Your preference: D - Web Interface. We are going to be creating websites in software engineering for Year 12 using Flask so I want to get a head start with learning it.
                    Web interface also allows for wider rendering support such as graphs, images and LaTeX
---

### Q2.2: Progress Visualization

**Question:** How should progress be displayed?

**For exam preparation results:**
- **Option A:** Text-based tree (current V1 design)
- **Option B:** ASCII charts/graphs in terminal
- **Option C:** Graphical charts (requires GUI/Web)
- **Option D:** JSON/CSV export for external visualization

Your preference: C - Graphical charts

**For study sessions:**
- **Option A:** Simple text summary after each session
- **Option B:** Real-time progress bar/percentage
- **Option C:** Detailed dashboard with graphs over time
- **Option D:** Combination: _______________

Your preference: Option C 

---

## 3. File Processing

### Q3.1: PDF Processing Requirements

**Question:** What should be extracted from PDFs?

**For assessment notifications:**
- [X] Exam name and date
- [X] Topics covered
- [X] Marking criteria/rubrics
- [X] Question types and weights
- [ ] Other: _______________

**For class materials:**
- [X] Full text extraction
- [ ] Image/diagram recognition
- [X] Equation extraction
- [X] Summary generation
- [ ] Other: _______________

---

### Q3.2: Handwritten Notes

**Question:** Do you need to process handwritten notes?

- **Maybe** - Would be nice to have but not essential

If yes:
- [ ] Full OCR (handwriting to text)
- [X] Diagram/equation recognition
- [ ] Summary generation only
- [ ] Other: _______________

---

### Q3.3: Image Processing

**Question:** What types of images need to be processed?

- [X] Diagrams from textbooks
- [ ] Photos of whiteboard/blackboard
- [ ] Screenshots of online resources
- [X] Graphs and charts
- [X] Chemical structures / circuit diagrams
- [X] Mathematical equations
- [ ] Other: _______________

**Priority level:**
- **Nice to have** - Can add later

---

## 4. Storage and Data Management

### Q4.1: Data Storage Preference

**Question:** Where should StudyBrain store data?

**Options:**

**A) Local Files (JSON)**
- Pros: Simple, no dependencies, human-readable
- Cons: Slower for large datasets, no complex queries
- Good for: < 1000 quiz results

**B) SQLite Database**
- Pros: Fast queries, ACID compliance, still local
- Cons: Binary format, needs schema management
- Good for: > 1000 quiz results

**C) Cloud Storage**
- Pros: Access from multiple devices, automatic backup
- Cons: Requires internet, privacy concerns, cost
- Good for: Multi-device usage

**D) Hybrid**
- Example: SQLite locally + optional cloud sync
- Specify: _______________

Your preference: A 

---

### Q4.2: Session Data Persistence

**Question:** How long should session data be kept?

- [ ] Current session only (deleted after exit)
- [ ] Last 7 days
- [ ] Last 30 days
- [ ] Entire school year
- [X] Forever (with manual cleanup option)
- [ ] Custom: _______________

**Question:** Should old sessions be:
- [ ] Archived (compressed but accessible)
- [X] Summarized (keep statistics only)
- [ ] Deleted (unrecoverable)

---

## 5. Progress Tracking Algorithms

### Q5.1: Score Calculation Method

**Question:** How should Conceptual Understanding and Functional Knowledge scores be calculated?

**Current V1 Design:** Percentage scores (0-100%)

**Scoring Method:**
- **Option A:** Simple percentage (correct/total × 100)
- **Option B:** Weighted by question difficulty
- **Option C:** Weighted by recency (recent performance matters more)
- **Option D:** Confidence-adjusted (lower confidence reduces score even if correct)
- **Option E:** Combination: a combination of options: A, B and D

Your preference: E

---

### Q5.2: Improvement Thresholds

**Question:** What counts as "sufficient improvement" in a study session?

**Scenario:** Student starts with Con=40%, Func=30%. After studying:

**Case 1:** Con=55%, Func=45% (15% improvement each)
- Should they:  **Move on** - BUT they should come back to it later 

**Case 2:** Con=60%, Func=35% (20% conceptual, 5% functional)
- Should they: **Repeat topic** - UNLESS very close to exam deadline 

**Your thresholds:**
- Minimum conceptual improvement: 20
- Minimum functional improvement: 15
- Acceptable if only one threshold met: **No**

---

### Q5.3: Topic Repetition Logic

**Question:** When should a topic be repeated vs. moved on?

**Consider:**
- Time remaining until exam
- Number of topics remaining
- Current score after study session
- Rate of improvement

**Your decision algorithm:**
(Describe in words or provide formula)

If the time to marks to difficulty ratio for topic A is less than the time to marks to difficulty ratio of moving on to the next topic, move on. 

---

## 6. Spaced Repetition Integration

### Q6.1: Spaced Repetition System

**Question:** Should StudyBrain include spaced repetition for long-term retention?

- **Yes, but optional** - Would be nice but not required for exam prep

If yes:

**Implementation:**
- **Option A:** Simple review reminders (e.g., "Review Electric Potential")
- **Option B:** Full SRS algorithm (Anki/SM-2 style with intervals)
- **Option C:** Adaptive based on performance trends

Your preference: C - If the data structure could be updated to include SRS data such as:

     [Area/Topic/Concept] - [Conceptual Understanding | Functional Knowledge] - [Last reviewed | any other SRS data]
        └── Sub-topics (indented, recursive)
            └── Incorrect Questions (at leaf nodes)"

---

### Q6.2: Review Frequency

**Question:** How often should topics be reviewed?

**Scenario:** Student completes "Electric Potential" on Day 1

**Review Schedule:**
- Day 1: Initial learning
- Day ___: First review
- Day ___: Second review
- Day ___: Third review
- ... (describe pattern)

**Or:**
- [ ] Use standard SRS algorithm (e.g., Anki defaults)
- [X] Custom schedule: FSRS Algorithm + FSRS Optimiser - But this is advanced: https://github.com/open-spaced-repetition/py-fsrs, https://github.com/open-spaced-repetition/fsrs-optimizer

---

## 7. Resource Management

### Q7.1: Resource Organization

**Question:** How are your study resources currently organized?

**Directory structure:**
```
Example:
Resources/
├── Physics/
│   ├── Class_Materials/
│   ├── Curriculum/
│   └── Notes/
├── Maths/
│   └── ...
```

**Your structure:**
```
Year-11/
├── Physics/
│   ├── Practice Papers/
│   ├── PracticeQuestions/
│   ├── Module1/
│   ├── Module2/
│   ├── Module3/
│   ├── Module4/
│   ├── Skills/
│   ├── PhysicsCiriculumn.pdf
│   └── StudyNotes/
│
├── Math/
 ```
This is a very very poor structure


**Question:** Should StudyBrain auto-organize resources or use your existing structure?
- [X] Auto-organize (StudyBrain creates structure)
- [ ] Use existing structure (specify paths manually)
- [ ] Hybrid: _______________

---

### Q7.2: External Resources

**Question:** Should StudyBrain search for external resources (online)?

**When studying a topic, should it:**
- [ ] Only use provided local resources
- [ ] Search for additional explanations online (automatically)
- [X] Ask permission before searching online
- [ ] Provide links for you to review separately

**Resource types to search:**
- [X] Khan Academy explanations
- [X] Past HSC papers
- [X] Educational videos (YouTube)
- [X] University lecture notes
- [X] Other: ScienceReady

---

## 8. Study Session Management

### Q8.1: Session Duration

**Question:** How long should a typical study session last?

- **Diagnostics quiz:** 30 minutes
- **Study session (learning new content):** Depends minutes
- **Practice questions:** Depends minutes

**Should sessions have:**
- [ ] Fixed duration (timer-based)
- [X] Variable duration (task-based)
- [ ] Break reminders every _______________ minutes
- [ ] Pomodoro technique integration (25 min work / 5 min break)

---

### Q8.2: Session Interruption Handling

**Question:** What happens if you need to stop mid-session?

**Scenario:** Halfway through diagnostics quiz with 7/15 questions complete

**Options:**
- [X] Save progress, resume later from question 8
- [ ] Save progress, restart quiz from beginning
- [ ] Discard session, start fresh next time
- [ ] Ask user what to do


---

## 9. Exam Strategy Features

### Q9.1: Time Management Training

**Question:** Should StudyBrain help with exam time management?

**Features:**
- [ ] Timed practice tests (strict exam conditions)
- [X] Time allocation suggestions per question type
- [X] Speed tracking over time
- [X] "Quick answer" vs. "thorough answer" training
- [ ] Not needed

---

### Q9.2: Question Strategy Training

**Question:** Should StudyBrain teach exam strategies?

**Examples:**
- [X] How to read questions carefully (identify keywords)
- [X] When to skip and return to questions
- [X] How to structure extended responses
- [X] Command word analysis ("discuss" vs. "evaluate")
- [ ] Not needed

---

## 10. Performance Prediction

### Q10.1: Grade Prediction

**Question:** Should StudyBrain predict your likely exam grade?

- **Yes** - Would help with goal setting and motivation

If yes:
- [X] Simple prediction (based on current scores)
- [X] Trend-based (based on improvement rate)
- [X] Confidence ranges (e.g., "likely between 85-92")

---

### Q10.2: Gap Analysis

**Question:** What should StudyBrain prioritize fixing?

**Scenario:** 10 days until exam, 20 topics to cover

**Prioritization:**
- **Option A:** Lowest scores first (fix worst areas)
- **Option B:** Highest mark potential (topics worth most marks)
- **Option C:** Quick wins (easy improvements)
- **Option D:** User preference (you choose order)
- **Option E:** Balanced algorithm considering all factors

Your preference: E - The longer time there is before exams, the more difficult areas can be learnt, as exam gets closer more marks should be prioritied

---

## 11. Collaboration Features

### Q11.1: Multiple Users

**Question:** Will StudyBrain be used by multiple students?

- **Maybe** - Future consideration

If yes:
- [X] Separate profiles
- [ ] Compare progress between users
- [ ] Shared question pools
- [ ] Collaborative study sessions
- [ ] Leaderboards / gamification

---

### Q11.2: Teacher/Tutor Access

**Question:** Should teachers or tutors be able to access your progress?

- **No** - Private data only

---

## 12. Development Priorities

### Q12.1: MVP Features

**Question:** What are the MUST-HAVE features for initial version?

**Rank in order of importance (1 = most important):**

- 1   Diagnostics quizzes
- 2   Practice question generation
- 3   Answer evaluation and marking
- 4   Session persistence
- 5   Multi-subject support
- 6   Study content synthesis
- 7   PDF processing (assessment notifications)
- 8   Cross-subject integration
- 9   Progress tracking (scores over time)
- 10  Spaced repetition reminders

---

### Q12.2: Development Timeline

**Question:** When do you need StudyBrain operational?

- **Critical deadline:** Before Term 1 of Year 12 (late January) (e.g., "Before trials in Term 3")
- **Preferred timeline:** End of next week (12th october)
- **Current stage:** Holidays (2nd Oct), End of Year 11, starting year 12 end of next week (e.g., "Year 11, starting Year 12 content")

**Which features are needed by when?**

**Phase 1 (By 12th October):**
- Feature: Diagnostics Quizzes
- Feature: Practice Question Generation
- Feature: Answer evaluation and marking
- Feature: Session persistence
- Feature: Multi-subject support
- Feature: Study content Synthesis
 
- Feature: PDF processing - Maybe

**Phase 2 (By at least halfway into next term (End of october)):**
- Feature: Cross-subject integration 
- Feature: Progress tracking
- Feature: Spaced repetition reminders

---

## 13. Technical Constraints

### Q13.1: Development Environment

**Question:** What is your technical setup?

**Your programming experience:**
- **Python:** Intermediate / Low - Advanced
- **JavaScript/TypeScript:** Beginner - Never used
- **Databases:** Beginner - Not very familiar
- **Web development:** Beginner - Not super familiar

**Preferred language for StudyBrain:**
- [X] Python (easier for you to modify/extend)
- [ ] TypeScript (better for web interfaces)
- [ ] Either (doesn't matter)

---

### Q13.2: Deployment Environment

**Question:** Where will StudyBrain run?

- **Operating System:** macOS
- **Internet access:** Sometimes
- **Computational resources:**
  - RAM: 16gb
  - Storage: 1 Terabyte
  - GPU: Available 

---

### Q13.3: API Access

**Question:** What Claude/Anthropic access do you have?

- **Account type:** Pro 
- **API access:** No
- **Budget for API usage:** $0 per month
- **Token limit concerns:** Yes 

---

## 14. Additional Features

### Q14.1: Feature Requests

**Question:** Are there features not mentioned that you want?

**Your ideas:**

1. I was thinking that a timer feature (similar functionality to toggl) would be good so that I can track how much i'm studying each subject, how often and calculate learning rate.

---

### Q14.2: Inspiration

**Question:** Are there existing tools that StudyBrain should emulate?

**Examples you like:**
- [X] Anki (spaced repetition flashcards)
- [ ] Quizlet (online quizzes)
- [X] Khan Academy (video lessons + practice)
- [ ] Notion (organization + notes)
- [ ] Other: _______________

**What you like about them:**
Anki - I liked the spaced repetition
Khan Academy - I like the methodology, information then practice

---

## 15. Open Questions

**Any other considerations, requirements, or concerns?**

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## Submission

**Please complete this questionnaire and save your responses.**

Once complete:
1. Save this file as `V1_Design_Questions_ANSWERED.md`
2. Review your answers for consistency
3. Submit for V2 design creation

**Estimated time to complete:** 30-45 minutes

---

**Thank you! Your answers will shape StudyBrain V2.**
