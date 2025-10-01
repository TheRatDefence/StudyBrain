# StudyBrain V1 - System Design Overview

**Version:** 1.0
**Author:** James
**Date:** October 2025
**Status:** Initial Design Specification

---

## Executive Summary

StudyBrain is an intelligent study management system designed to optimize HSC preparation through AI-powered tutoring, diagnostics testing, and personalized study plans. The system breaks down into three core components: **Start/Opening**, **Exam Preparation**, and **Studying**, each designed to work together to provide comprehensive academic support.

---

## System Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   StudyBrain CLI                     │
│              Command: "sb physics"                   │
└────────────────────┬────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
┌─────────────────┐    ┌──────────────────┐
│  Study Mode     │    │  Exam Prep Mode  │
│  - Sessions     │    │  - Diagnostics   │
│  - Context      │    │  - Assessment    │
│  - Learning     │    │  - Results       │
└─────────────────┘    └──────────────────┘
```

---

## 1. System Components

### 1.1 Start/Opening System

The initialization layer that manages system startup and subject-specific agent instantiation.

**Functionality:**
- Command-line interface: `sb <subject>`
- Subject agent initialization (e.g., `sb physics`, `sb maths`)
- Session state detection and restoration
- User interface presentation

**User Flow:**
1. User executes: `sb physics`
2. System loads Physics StudyAgent
3. System checks for existing session data
4. Presents menu with available modes

**Example Output:**
```
StudyBrain - Physics Agent Initialized

OPTIONS:
[1] Study (Continue from: "Work done by moving charges in magnetic fields")
[2] Prepare for exam

Select option:
```

---

### 1.2 Exam Preparation System

Comprehensive assessment preparation module that identifies knowledge gaps and creates targeted improvement plans.

#### 1.2.1 Gathering Exam Data

**Initializing Data Collection:**
- Exam name (e.g., "PHY-TASK 2")
- Exam date and time (e.g., "Oct 13th at 10am")
- Assessment notification document (PDF format)

**Existing Progress Data:**
- Practice test directories and previous attempts
- Historical performance metrics

**Resource Collection:**
- Class materials (teacher-provided resources)
- Curriculum documentation (NESA syllabus)
- Student notes and summaries

**System Processing:**
1. Parse curriculum to identify areas/topics/concepts
2. Extract assessment scope from notification
3. Map assessment requirements to curriculum structure
4. Create hierarchical topic tree

#### 1.2.2 User Assessment

For each identified area/topic/concept, the system measures:
- **Conceptual Understanding:** Depth of comprehension (0-100%)
- **Functional Knowledge:** Practical application ability (0-100%)

**Diagnostics Quiz Process:**
1. Identify untested areas/topics/concepts
2. Select area for testing (priority-based)
3. Define scope boundaries
4. Research using:
   - Course curriculum
   - Past papers
   - External resources (internet)
5. Generate comprehensive question list
6. Administer quiz:
   ```
   For each question:
   - Present question to user
   - Collect answer + confidence rating
   - Mark response
   - Display result with explanation
   - Save to performance database
   ```

**Adaptive Testing:**
- Prioritizes practice papers over generated diagnostics
- Adjusts difficulty based on performance
- Targets knowledge gaps identified in previous sessions

#### 1.2.3 Results Processing

Generate comprehensive performance profile with hierarchical breakdown.

**Output Format:**
```
EXAM NAME: PHYS-Task-2
DATE: 13/10/26
TIME: 10:00 AM

RESULTS:
├── Module 1 - Motion                    [Con=95%|Func=80%]
├── Module 2 - Kinematics                [Con=72%|Func=70%]
├── Module 3 - Waves and Thermodynamics  [Con=94%|Func=96%]
└── Module 4 - Electricity and Magnetism [Con=30%|Func=20%]
    ├── Electricity                      [Con=20%|Func=10%]
    │   ├── Electric Potential           [Con=10%|Func=5%]
    │   │   └── ❌ "What is Electric Potential?"
    │   └── Power                        [Con=10%|Func=5%]
    │       ├── ❌ "What is Electrical Power?"
    │       └── ❌ "How do you calculate Electrical Power?"
    └── Magnetism                        [Con=10%|Func=10%]
        └── Solenoids                    [Con=10%|Func=10%]
            └── ❌ "Why do Solenoids create a magnetic field?"
```

**Data Structure:**
```
[Area/Topic/Concept] - [Conceptual Understanding | Functional Knowledge]
    └── Sub-topics (indented, recursive)
        └── Incorrect Questions (at leaf nodes)
```

---

### 1.3 Studying System

Personalized learning module that targets weak areas identified during exam preparation.

#### Study Session Workflow

**1. Topic Selection**
- Choose area/topic/concept from performance data
- Prioritize based on:
  - Lowest understanding scores
  - Upcoming assessment relevance
  - User preferences

**2. Scope Definition**
- Establish learning boundaries
- Identify prerequisite knowledge
- Set session objectives

**3. Content Research & Synthesis**
Research sources (in priority order):
- Student's personal study notes
- Class/teacher resources
- External educational content

Extract keypoints and synthesize into:
- Comprehensive explanation paragraph
- Practical examples
- Common misconceptions

**4. Knowledge Application**
- Generate practice questions from synthesized content
- Test user comprehension
- Mark responses
- Update Conceptual Understanding score

**5. Functional Knowledge Assessment**
- Retrieve incorrect questions for current topic
- Generate similar exam-style questions
- Administer assessment with confidence tracking
- Mark and update Functional Knowledge score

**6. Progress Evaluation**
Decision tree for session continuation:
```
IF post-study scores sufficient:
    → Move to next topic
ELSE:
    IF time_remaining > threshold AND potential_benefit > threshold:
        → Repeat current topic (different approach)
    ELSE:
        → Move to next topic (mark for future review)
```

---

## 2. Data Management

### 2.1 Session State

**Persistent Data:**
- Last active topic
- Session timestamp
- Conversation context
- User preferences

**Session Recovery:**
- Automatic on system restart
- Option to discard and start fresh
- Context preservation across sessions

### 2.2 Exam Preparation Data

**Storage Format:**
```json
{
  "exam_name": "PHYS-Task-2",
  "date": "2026-10-13",
  "time": "10:00",
  "results": {
    "module_1": {
      "conceptual": 95,
      "functional": 80,
      "subtopics": { ... }
    },
    ...
  },
  "incorrect_questions": [ ... ]
}
```

---

## 3. User Interaction Patterns

### 3.1 Initial Setup Flow

```
User: sb physics

System:
┌────────────────────────────────────────┐
│    Physics StudyAgent - Main Menu      │
├────────────────────────────────────────┤
│ [1] Study                              │
│     └─ Continue: "Magnetic Fields"     │
│     └─ Start New Session               │
│                                        │
│ [2] Prepare for exam                   │
│     └─ Continue: "PHY-TASK 2"          │
│     └─ Start New Preparation           │
└────────────────────────────────────────┘
```

### 3.2 New Exam Preparation Flow

```
System: Enter exam name:
User: PHY-HSC

System: Enter time & date:
User: Oct 13th at 10am

System: Provide notification (path):
User: ./PHY-HSC-Assessment-task-notification.pdf

System: Enter practice test directory (optional):
User: ./Practice_Tests/

System: Enter class resources (optional):
User: ./Resources/Class_Materials/

System: Enter curriculum resources (optional):
User: ./Resources/Curriculum/

System: Enter notes (optional):
User: ./Study_Notes/

[System processes data and generates diagnostics quiz]
```

---

## 4. Outstanding Design Considerations

### 4.1 Multi-Agent Coordination
- How do subject agents communicate?
- Shared knowledge across subjects?
- Cross-subject concept reinforcement?

### 4.2 GUI vs CLI
- Current design assumes CLI
- Future GUI considerations?
- Mobile access requirements?

### 4.3 File Processing
- PDF → Text extraction requirements
- Image analysis (diagrams, equations)
- Handwritten notes processing?

### 4.4 Progress Tracking
- Long-term performance analytics
- Retention tracking over time
- Spaced repetition integration

---

## 5. Technical Requirements (To Be Determined)

### 5.1 File Handling
- PDF parsing and text extraction
- Image OCR capabilities
- Document structure analysis

### 5.2 Storage System
- Exam preparation data persistence
- Session state management
- User progress history

### 5.3 Natural Language Processing
- Question generation
- Answer evaluation
- Confidence calibration

### 5.4 Integration Points
- Curriculum database integration
- Practice paper repositories
- External learning resources

---

## 6. Success Metrics

### 6.1 Exam Preparation Quality
- Coverage completeness (% of syllabus assessed)
- Gap identification accuracy
- Time to completion

### 6.2 Study Effectiveness
- Conceptual understanding improvement rate
- Functional knowledge retention
- Transfer to actual exam performance

### 6.3 User Experience
- Session completion rates
- User engagement duration
- System recommendation acceptance rate

---

## 7. Appendix: Example Interaction

### Complete Physics Exam Prep Session

```
$ sb physics

=== Physics StudyAgent ===

OPTIONS:
[1] Study
[2] Prepare for exam

> 2

Existing exam preparations:
[1] PHY-TASK 2 (Oct 13)
[2] Start new exam preparation

> 2

=== New Exam Setup ===
Enter exam name: PHY-HSC
Enter date and time: Oct 13th at 10am
Provide assessment notification: ./PHY-HSC-Assessment.pdf

[Processing document...]
✓ Identified assessment scope: Modules 1-4
✓ Found 12 major topics
✓ Loaded curriculum standards

Enter practice test directory (optional): ./Practice_Tests/
✓ Found 3 previous attempts

Enter class resources (optional): ./Resources/Class/
✓ Loaded 47 teaching materials

Enter curriculum resources (optional): ./Resources/Curriculum/
✓ Loaded NESA Physics Stage 6 syllabus

Enter notes (optional): ./Study_Notes/
✓ Loaded 23 note documents

=== Diagnostics Quiz ===
Starting assessment for: Module 4 - Electricity and Magnetism

Question 1/15: What is the definition of electric potential?
> [User answers]

Correct! ✓
Confidence (1-5): 4

[... continues through quiz ...]

=== Results Generated ===
Exam preparation data saved to: ./ExamPrep/PHY-HSC-20251001.json

Ready to begin study sessions. Type 'study' to start.
```

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-10-01 | Initial design specification | James |

---

**End of Document**
