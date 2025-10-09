# StudyBrain - System Design Specification

**Version:** 2.0
**Last Updated:** October 9, 2025
**Status:** Implementation Ready

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Architecture](#2-architecture)
3. [Multi-Agent System](#3-multi-agent-system)
4. [Custom MCP Tools](#4-custom-mcp-tools)
5. [Flask Application](#5-flask-application)
6. [Data Structures](#6-data-structures)
7. [Technology Stack](#7-technology-stack)
8. [Implementation Approach](#8-implementation-approach)

---

## 1. System Overview

### Mission

An AI-powered study system for HSC preparation that:
- Identifies knowledge gaps through diagnostic testing
- Teaches concepts with deep intuitive explanations
- Tracks progress with Conceptual and Functional Understanding metrics
- Optimizes study time through intelligent prioritization
- Prevents forgetting with FSRS spaced repetition

### Key Features

**Core Capabilities:**
- Multi-subject support (Physics, Maths Ext1, Maths Adv, Software Engineering, English, Music)
- Diagnostic quizzes with adaptive difficulty
- AI-powered answer evaluation and feedback
- Progress visualization with interactive charts
- Study timer with learning rate tracking
- FSRS-based review scheduling

**Target User:** James (Year 11 → 12, NSW HSC 2026)

---

## 2. Architecture

### System Diagram

```
┌─────────────────────────────────────────────────────┐
│         Flask Web Application (localhost:5000)      │
│  ┌──────────┐  ┌─────────────┐  ┌────────────────┐  │
│  │Dashboard │  │Study Session│  │Progress Charts │  │
│  └──────────┘  └─────────────┘  └────────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
┌──────────────────┐         ┌────────────────────┐
│ Claude Agent SDK │         │ JSON Data Storage  │
│                  │         │                    │
│ ┌──────────────┐ │         │ • sessions/        │
│ │ Coordinator  │ │         │ • progress/        │
│ │    Agent     │ │         │ • quiz_results/    │
│ └──────┬───────┘ │         │ • study_timer/     │
│        │         │         │ • resource_index/  │
│   ┌────┴────┐    │         └────────────────────┘
│   ▼         ▼    │
│ Subject  Custom  │
│ Agents   MCP     │
│          Tools   │
└──────────────────┘
```

### Core Components

1. **Flask Web Interface** - Browser-based UI for study sessions
2. **Claude Agent SDK** - Multi-agent coordination and AI processing
3. **JSON Data Store** - Local file-based storage
4. **FSRS Scheduler** - Spaced repetition algorithm (py-fsrs library)
5. **Plotly Charts** - Interactive progress visualization

---

## 3. Multi-Agent System

### 3.1 Coordinator Agent

**Role:** Central orchestrator managing all study operations

**Responsibilities:**
- Route subject queries to appropriate agents
- Answer meta-questions ("What should I study next?")
- Manage cross-subject concept registry
- Coordinate multi-agent workflows

**Available Tools:**
- All custom MCP tools
- Task (invoke sub-agents)
- Read/Write/Grep (resource access)

### 3.2 Subject Agents (6 Total)

**Subjects:**
1. Physics
2. Mathematics Extension 1
3. Mathematics Advanced
4. Software Engineering
5. English Standard
6. Music

**Common Pattern:**
```python
{
    "description": "Expert HSC {Subject} tutor",
    "system_prompt": """
        - Deep NESA curriculum knowledge
        - Diagnostic testing capabilities
        - Teaching with intuitive explanations
        - Practice question generation
        - Answer evaluation and feedback
    """,
    "tools": [
        "mcp__studybrain__generate_questions",
        "mcp__studybrain__save_quiz_result",
        "mcp__studybrain__update_progress",
        "Task"  # Can invoke sub-agents
    ],
    "model": "sonnet"
}
```

### 3.3 Specialized Sub-Agents

#### Curriculum Expert
- Deep syllabus knowledge and structure
- Prerequisites identification
- Learning progressions
- Assessment criteria interpretation

#### Question Generator
- Creates HSC-style practice questions
- Multiple question types (MC, short answer, extended)
- Difficulty calibration
- Marking criteria generation

#### Answer Evaluator
- Marks student responses
- Provides detailed feedback
- Identifies misconceptions
- Confidence calibration analysis

#### Progress Tracker
- Score calculations (Con/Func)
- Difficulty weighting
- Confidence adjustment
- Improvement threshold evaluation

---

## 4. Custom MCP Tools

### 4.1 Diagnostics Tools

**`generate_diagnostic_quiz`**
```python
Parameters:
  - subject: str
  - topics: list
  - difficulty: str (mixed/basic/standard/advanced)
  - question_count: int
  - include_past_papers: bool

Returns: Structured quiz with questions, answers, marking criteria
```

**`save_quiz_result`**
```python
Parameters:
  - subject, topic, question_id
  - student_answer, marks_awarded, marks_total
  - confidence: int (1-5)
  - time_taken_seconds: int

Returns: Updated progress scores
```

**`evaluate_answer`**
```python
Parameters:
  - question: dict
  - student_answer: str
  - student_confidence: int

Returns: Marks, feedback, misconceptions identified
```

### 4.2 Progress Tools

**`update_progress_scores`**
```python
Parameters:
  - subject, module, topic
  - quiz_results: list
  - recalculate_from_scratch: bool

Algorithm:
  Base score: (correct/total) × 100
  + Difficulty weighting
  + Confidence calibration
  + Recency weighting
```

**`get_progress_summary`**
```python
Parameters:
  - subject: str
  - module: str | None
  - include_chart_data: bool

Returns: Hierarchical tree with Con/Func scores, FSRS data
```

### 4.3 FSRS Tools

**`schedule_fsrs_review`**
```python
Parameters:
  - subject, topic
  - performance_rating: int (1-4: again/hard/good/easy)
  - current_stability, current_difficulty

Returns: {next_review: date, interval_days: int}
```

**`get_due_reviews`**
```python
Parameters:
  - subject: str | None
  - include_upcoming: bool
  - limit: int

Returns: List of topics due for review, sorted by priority
```

### 4.4 Resource Tools

**`index_resources`**
```python
Parameters:
  - subject: str
  - scan_directory: str
  - auto_organize: bool

Uses Claude vision to categorize PDFs, extract metadata
Creates index in ./data/resource_index/{subject}.json
```

**`search_resources`**
```python
Parameters:
  - subject: str
  - topic, keywords, resource_type

Returns: Relevant files from indexed resources
```

### 4.5 Timer Tools

**`start_study_session`**
```python
Parameters:
  - subject, session_type, topic

Returns: {session_id, started_at}
Stores in ./data/study_timer/
```

**`end_study_session`**
```python
Parameters:
  - session_id
  - progress_improvement: dict

Calculates: learning_rate = improvement / hours
```

### 4.6 Cross-Subject Tools

**`update_cross_subject_concept`**
```python
Parameters:
  - concept_name: str (e.g., "Calculus")
  - subjects: list
  - connections: dict

Stores shared concepts across subjects
```

**`suggest_cross_subject_study`**
```python
Parameters:
  - current_subject, current_topic

Returns: Related topics from other subjects
```

---

## 5. Flask Application

### 5.1 Directory Structure

```
studybrain_web/
├── app.py                      # Flask entry point
├── config.py
├── requirements.txt
├── agents/
│   ├── coordinator.py
│   ├── subjects/               # 6 subject agents
│   └── subagents/              # 4 specialized sub-agents
├── mcp_tools/                  # 12 custom MCP tools
│   ├── diagnostics.py
│   ├── progress.py
│   ├── fsrs_integration.py
│   ├── resources.py
│   └── study_timer.py
├── routes/
│   ├── dashboard.py
│   ├── study_session.py
│   ├── progress.py
│   └── api.py
├── services/
│   ├── agent_manager.py
│   ├── progress_calculator.py
│   └── fsrs_scheduler.py
├── templates/
│   ├── dashboard.html
│   ├── study_session.html
│   └── progress.html
├── static/
│   ├── css/
│   └── js/
└── data/                       # JSON storage
    ├── sessions/
    ├── exams/
    ├── progress/
    ├── quiz_results/
    ├── study_timer/
    └── resource_index/
```

### 5.2 Key Routes

```python
# Dashboard
GET  /                          # Home dashboard
GET  /api/dashboard/stats       # Dashboard data

# Study Sessions
GET  /study/<subject>           # Study session interface
POST /study/<subject>/quiz      # Submit quiz answer

# Progress
GET  /progress                  # Progress overview
GET  /progress/<subject>        # Subject-specific
GET  /api/progress/data         # Chart data
GET  /api/progress/fsrs-due     # Due reviews

# Exam Preparation
GET  /exam/new                  # New exam setup
POST /exam/create               # Submit exam details
GET  /exam/<exam_id>/diagnostics # Run diagnostics

# Timer
POST /api/timer/start
POST /api/timer/stop
GET  /api/timer/stats

# Resources
POST /api/resources/index
GET  /api/resources/search
```

### 5.3 UI Components

**Dashboard:**
- 6 subject cards with progress bars
- Study time statistics (weekly/monthly)
- Due reviews alert panel
- "What to study next?" recommendations

**Study Session:**
- Timer widget (Toggl-style)
- Session type tabs (Learn/Practice/Review)
- Quiz interface with LaTeX support
- Confidence slider (1-5)
- Real-time feedback display

**Progress Page:**
- Plotly charts:
  - Progress timeline (Date vs Score)
  - Module radar chart (Con/Func per module)
  - Learning velocity (Improvement per hour)
  - Retention forecast (FSRS predictions)
- Expandable topic tree
- Incorrect questions list

---

## 6. Data Structures

### 6.1 Progress Data

```json
{
  "subject": "Physics",
  "last_updated": "2025-10-09T14:30:00Z",
  "overall_scores": {
    "conceptual": 68.5,
    "functional": 62.3
  },
  "modules": [{
    "module_id": "module_4",
    "module_name": "Electricity and Magnetism",
    "scores": {"conceptual": 30.0, "functional": 20.0},
    "topics": [{
      "topic_id": "electric_potential",
      "topic_name": "Electric Potential",
      "scores": {"conceptual": 10.0, "functional": 5.0},
      "fsrs_data": {
        "stability": 1.2,
        "difficulty": 7.8,
        "last_review": "2025-09-28",
        "next_review": "2025-10-03",
        "review_count": 2
      },
      "incorrect_questions": [{
        "question_id": "Q_EP_001",
        "text": "What is Electric Potential?",
        "date": "2025-09-28",
        "marks": "0/2"
      }]
    }]
  }]
}
```

### 6.2 Quiz Result

```json
{
  "quiz_id": "quiz_001",
  "session_id": "session_456",
  "subject": "Physics",
  "topic": "Electric Potential",
  "timestamp": "2025-10-09T14:30:45Z",
  "results": [{
    "question_id": "Q1",
    "question_text": "Calculate electric potential...",
    "marks_total": 4,
    "student_answer": "V = kQ/r = ...",
    "marks_awarded": 3.5,
    "confidence": 4,
    "time_taken_seconds": 180,
    "feedback": "Correct method, minor rounding error",
    "misconceptions": []
  }],
  "summary": {
    "total_marks": 20,
    "marks_achieved": 16.5,
    "percentage": 82.5,
    "conceptual_estimate": 85.0,
    "functional_estimate": 80.0
  }
}
```

### 6.3 Study Session

```json
{
  "session_id": "session_456",
  "subject": "Physics",
  "topic": "Electric Potential",
  "session_type": "study",
  "started_at": "2025-10-09T14:00:00Z",
  "ended_at": "2025-10-09T15:30:00Z",
  "duration_minutes": 90,
  "progress_before": {"conceptual": 10.0, "functional": 5.0},
  "progress_after": {"conceptual": 33.0, "functional": 28.0},
  "improvement": {"conceptual": 23.0, "functional": 23.0},
  "learning_rate": 15.3,
  "activities": [
    {"type": "explanation", "duration_minutes": 30},
    {"type": "practice_questions", "duration_minutes": 45, "questions_completed": 8},
    {"type": "review", "duration_minutes": 15}
  ],
  "verdict": "sufficient",
  "next_action": "move_to_next_topic"
}
```

### 6.4 Exam Preparation

```json
{
  "exam_id": "PHY-TASK-2",
  "subject": "Physics",
  "exam_name": "PHYS-Task-2",
  "exam_date": "2025-10-13",
  "exam_time": "10:00",
  "notification_file": "./uploaded/PHY-HSC-Assessment.pdf",
  "scope": {
    "modules": ["Module 3", "Module 4"],
    "topics": ["Waves", "Electricity and Magnetism"],
    "question_types": [
      {"type": "multiple_choice", "count": 20, "marks": 20},
      {"type": "short_answer", "count": 5, "marks": 15},
      {"type": "extended_response", "count": 2, "marks": 15}
    ]
  },
  "resources": {
    "practice_tests": "./Practice_Tests/Physics/",
    "class_materials": "./Resources/Class_Materials/Physics/",
    "curriculum": "./Resources/Curriculum/Physics_Syllabus.pdf",
    "notes": "./Study_Notes/Physics/"
  },
  "diagnostics_completed": true,
  "results_file": "./data/progress/physics.json"
}
```

### 6.5 Cross-Subject Concepts

```json
{
  "concepts": [{
    "concept_id": "calculus",
    "concept_name": "Calculus",
    "subjects": ["Mathematics Extension 1", "Physics"],
    "connections": {
      "Maths Extension 1": {
        "topics": ["Derivatives", "Integration"],
        "role": "Primary teaching subject"
      },
      "Physics": {
        "topics": ["Kinematics", "Electric Fields"],
        "role": "Application in problem-solving"
      }
    },
    "recommendation": "Master derivatives in Maths before Physics kinematics",
    "priority": "high"
  }]
}
```

---

## 7. Technology Stack

### Core Dependencies

```python
# requirements.txt
Flask==3.0.0
flask-cors==4.0.0
claude-agent-sdk
py-fsrs                         # FSRS spaced repetition
plotly==5.17.0                  # Interactive charts
python-dotenv==1.0.0
```

### Key Libraries

**Web Framework:**
- Flask 3.0 (chosen for Year 12 Software Engineering learning)
- Jinja2 templates
- CORS support for API calls

**AI/ML:**
- Claude Agent SDK (multi-agent coordination)
- Custom MCP tools for StudyBrain features

**Spaced Repetition:**
- py-fsrs (Free Spaced Repetition Scheduler)
- Per-topic stability and difficulty tracking
- Adaptive review scheduling

**Visualization:**
- Plotly 5.17 (interactive charts)
- LaTeX/MathJax support for equations

**Storage:**
- JSON files (local, human-readable)
- No database required for MVP

### System Requirements

- **OS:** macOS (development), cross-platform capable
- **Python:** 3.9+
- **Claude Access:** Pro subscription (authenticated via Claude Code CLI)
- **Storage:** ~1GB for data (scales with usage)
- **Network:** Internet for Claude API calls

---

## 8. Implementation Approach

### 8.1 Development Philosophy

**Iterative Development:**
1. Build MVP with core features
2. Test with real study content (Physics)
3. Extend to all subjects
4. Add advanced features in phases

**Quality Priorities:**
1. Accuracy (correct marking and scoring)
2. Usability (intuitive interface)
3. Performance (fast response times)
4. Reliability (stable session management)

### 8.2 Phase 1 MVP (Oct 1-12)

**Core Features:**
- Diagnostics quizzes (at least Physics)
- Practice question generation
- Answer evaluation and marking
- Session persistence (resume capability)
- Multi-subject support (all 6 subjects)
- Basic progress tracking

**Optional for MVP:**
- FSRS review scheduling (basic)
- Study timer
- Progress charts
- Content synthesis

### 8.3 Phase 2 Enhancements (Oct 13-31)

**Week 1: Advanced Analytics**
- FSRS optimizer integration
- Learning rate calculations
- Retention forecasting

**Week 2: Cross-Subject Integration**
- Concept tracking across subjects
- Resource indexing and search
- External resource search (with permission)

**Week 3: Exam Strategy**
- Question strategy training
- Time management features
- Grade prediction
- Intelligent prioritization

### 8.4 Quick Start Guide

**Setup (5 minutes):**
```bash
cd /Users/james/Desktop/School/Year-12/StudyBrain
mkdir studybrain_web && cd studybrain_web

# Create structure
mkdir -p agents/{subjects,subagents} mcp_tools routes services templates static/{css,js}
mkdir -p data/{sessions,exams,progress,quiz_results,study_timer,resource_index}

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install Flask==3.0.0 flask-cors==4.0.0 claude-agent-sdk py-fsrs plotly==5.17.0
```

**Test SDK Connection:**
```python
# test_sdk.py
import asyncio
from claude_agent_sdk import query

async def test():
    async for message in query(prompt="Hello, Claude!"):
        print(message)

asyncio.run(test())
```

**Create Minimal Flask App:**
```python
# app.py
from flask import Flask, render_template, jsonify
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    response = asyncio.run(ask_coordinator(user_message))
    return jsonify({"response": response})

async def ask_coordinator(message):
    responses = []
    async for msg in query(prompt=message):
        responses.append(str(msg))
    return " ".join(responses)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### 8.5 Key Algorithms

**Progress Scoring:**
```python
def calculate_score(quiz_results):
    base_score = (correct / total) * 100

    # Difficulty weighting (harder questions worth more)
    difficulty_weight = sum(result.marks * result.difficulty for result in quiz_results)

    # Confidence calibration
    confidence_penalty = sum(
        abs(confidence - actual_performance) * 0.1
        for result in quiz_results
    )

    # Recency weighting (recent performance matters more)
    recency_weights = [0.5, 0.3, 0.15, 0.05]  # Most recent to oldest
    recency_score = sum(
        result.score * weight
        for result, weight in zip(sorted_results, recency_weights)
    )

    return base_score * difficulty_weight - confidence_penalty + recency_score
```

**Improvement Thresholds:**
- Minimum conceptual improvement: 20%
- Minimum functional improvement: 15%
- Both must be met for "sufficient progress"

**Topic Repetition Logic:**
```python
def should_repeat_topic(time_to_exam, topics_remaining, current_score, improvement):
    time_per_topic = time_to_exam / topics_remaining

    if improvement < 15:  # Insufficient improvement
        if time_per_topic > 2 and current_score < 70:
            return "repeat"  # Have time and still weak
        else:
            return "move_on"  # Mark for later review
    else:
        return "move_on"  # Sufficient improvement
```

**FSRS Integration:**
```python
from fsrs import FSRS, Card, Rating

def update_fsrs(topic_data, performance):
    card = Card(**topic_data['fsrs_data'])

    # Map performance to FSRS rating
    if performance < 50 or confidence_mismatch:
        rating = Rating.Again  # Need immediate review
    elif performance < 75:
        rating = Rating.Good   # Standard interval
    else:
        rating = Rating.Easy   # Extended interval

    scheduling_cards = fsrs.repeat(card, datetime.now())
    updated_card = scheduling_cards[rating].card

    return {
        "stability": updated_card.stability,
        "difficulty": updated_card.difficulty,
        "next_review": updated_card.due
    }
```

### 8.6 Success Criteria

**Technical:**
- Flask serves all routes without errors
- Claude agents respond within 10 seconds
- JSON data persists correctly
- Session state maintains across refreshes
- Charts render properly

**Functional:**
- Complete diagnostics → study → practice workflow
- Progress scores update accurately
- FSRS schedules reviews appropriately
- Timer tracks sessions correctly
- All 6 subjects operational

**User Experience:**
- Intuitive interface (no documentation needed)
- Fast response times (< 3s for most operations)
- LaTeX equations render properly
- Clear guidance for next steps

---

## 9. Architecture Decisions

### Decision 1: Web Interface (Flask)
**Chosen:** Flask web application
**Reason:** Learning Flask for Year 12 Software Engineering
**Benefits:** Browser-based, LaTeX support, interactive charts

### Decision 2: Local JSON Storage
**Chosen:** JSON files
**Reason:** Simple, human-readable, sufficient for single user
**Trade-off:** Won't scale to huge datasets, but adequate for 1-2 years HSC data

### Decision 3: Multi-Agent Architecture
**Chosen:** Coordinator + Subject agents + Sub-agents
**Reason:** Specialized expertise, parallel processing, clear separation of concerns
**Benefits:** Better quality responses, extensible design

### Decision 4: FSRS Algorithm
**Chosen:** py-fsrs library
**Reason:** Proven algorithm, actively maintained, adaptive scheduling
**Benefits:** Better retention than traditional spaced repetition

### Decision 5: No Authentication (MVP)
**Chosen:** No auth for initial version
**Reason:** Single user (localhost only)
**Future:** Add if sharing with others

---

## 10. Next Steps

**Immediate:**
1. Complete Phase 1 implementation (by Oct 12)
2. Test with real Physics content
3. Validate scoring algorithms against actual performance

**Short-term (Oct 13-31):**
1. Phase 2 enhancements (FSRS optimizer, cross-subject)
2. Advanced analytics and visualizations
3. Resource organization and indexing

**Long-term (Nov-Dec):**
1. Production hardening
2. Real-world validation with Year 12 content
3. Performance optimization

---

**END OF DESIGN SPECIFICATION**

*For implementation details, refer to:*
- *Implementation Kickstart Guide: `/Design/Implementation_Kickstart.md`*
- *Complete V2 Architecture: `/Design/V2_System_Architecture.md`*
- *Project Context: `CLAUDE.md`*
