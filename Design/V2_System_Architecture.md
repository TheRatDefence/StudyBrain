# StudyBrain V2 - Complete System Architecture

**Version:** 2.0
**Date:** October 1, 2025
**Target Delivery:** October 12, 2025 (Phase 1)
**Status:** Final Design Specification

---

## Executive Summary

StudyBrain V2 is a Flask-based web application powered by Claude Agent SDK, implementing a multi-agent AI tutoring system optimized for HSC preparation. The system uses specialized agents, custom MCP tools, and the FSRS spaced repetition algorithm to provide personalized, quantitative study management across all subjects.

**Key Upgrades from V1:**
- Web interface (Flask) instead of CLI
- Multi-agent coordinator architecture
- FSRS spaced repetition integration
- Real-time progress visualization with graphs
- Study timer and learning rate tracking
- Automated resource organization
- Cross-subject concept tracking

---

## 1. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│              Flask Web Application (Port 5000)              │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐     │
│  │  Dashboard  │  │ Study Session│  │ Progress Charts │     │
│  │  (Home)     │  │  Interface   │  │  & Analytics    │     │
│  └─────────────┘  └──────────────┘  └─────────────────┘     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ├─── Routes & Controllers
                         │
           ┌─────────────┴─────────────┐
           │                           │
           ▼                           ▼
┌──────────────────────┐    ┌──────────────────────┐
│ Claude Agent SDK     │    │  JSON Data Store     │
│ (Python)             │    │                      │
│                      │    │ - sessions/          │
│ ┌────────────────┐   │    │ - exams/             │
│ │ Coordinator    │   │    │ - progress/          │
│ │ Agent          │   │    │ - resources/         │
│ └───────┬────────┘   │    │ - study_timer/       │
│         │            │    └──────────────────────┘
│    ┌────┴─────┐      │
│    │          │      │
│    ▼          ▼      │
│ ┌───────┐  ┌──────┐  │ 
│ │Subject│  │Shared│  │
│ │Agents │  │Tools │  │
│ │       │  │      │  │
│ │Physics│  │Quiz  │  │
│ │Maths  │  │Mark  │  │
│ │Chem   │  │FSRS  │  │
│ │...    │Curriculum│ │
│ └───────┘  └──────┘  │
└──────────────────────┘
```

---

## 2. Multi-Agent Architecture

### 2.1 Coordinator Agent

**Role:** Central orchestrator for all StudyBrain operations

**Responsibilities:**
- Route requests to appropriate subject agents
- Manage cross-subject concept registry
- Answer non-subject queries ("What should I study next?")
- Coordinate multi-agent tasks
- Aggregate progress across subjects

**System Prompt:**
```
You are the StudyBrain Coordinator - a central AI system managing James's HSC study program.

RESPONSIBILITIES:
1. Route subject-specific queries to appropriate agents (Physics, Maths, etc.)
2. Answer meta-questions about study strategy and prioritization
3. Track cross-subject concepts and suggest connections
4. Coordinate multi-subject learning when topics overlap

AVAILABLE AGENTS:
- physics-agent: HSC Physics (Modules 1-4)
- maths-ext1-agent: Mathematics Extension 1
- maths-adv-agent: Mathematics Advanced
- software-agent: Software Engineering
- english-agent: English Standard
- music-agent: Music

CROSS-SUBJECT REGISTRY:
{cross_subject_concepts}

STUDENT CONTEXT:
- Name: James
- Year: 11 (entering Year 12)
- Graduation: 2026
- Learning style: Fast learner, needs reinforcement against forgetting
- Preferences: Deep intuitive understanding over memorization

When asked "What should I study next?", consider:
- Upcoming exam dates and priorities
- Weak areas across all subjects
- Time since last review (FSRS)
- Subject balance
```

**MCP Tools:**
- `get_all_subject_progress` - Aggregate scores across subjects
- `get_next_study_recommendation` - Priority algorithm
- `update_cross_subject_concept` - Track shared concepts
- `query_cross_subject_concept` - Find related topics

---

### 2.2 Subject Agents

**Pattern:** One agent per HSC subject

**Subjects (6 total):**
1. Physics
2. Mathematics Extension 1
3. Mathematics Advanced
4. Software Engineering
5. English Standard
6. Music

**Common Structure:**
```python
{
    "description": "Expert HSC {Subject} tutor for diagnostics, teaching, and exam prep",
    "prompt": """
You are an expert HSC {Subject} tutor specializing in the NSW NESA curriculum.

CURRICULUM KNOWLEDGE:
{loaded from ./subjects/{subject}/curriculum.json}

YOUR CAPABILITIES:
1. Conduct diagnostic quizzes to identify knowledge gaps
2. Teach concepts with deep intuitive explanations
3. Generate practice questions at appropriate difficulty
4. Mark student answers with detailed feedback
5. Track progress (Conceptual Understanding & Functional Knowledge)

AVAILABLE TOOLS:
- curriculum_expert (sub-agent): Deep curriculum knowledge
- question_generator (sub-agent): Create practice questions
- answer_evaluator (sub-agent): Mark and provide feedback
- progress_tracker (MCP tool): Update student scores

TEACHING PHILOSOPHY:
- Focus on WHY concepts work, not just HOW
- Use practical examples and applications
- Connect to real-world scenarios
- Identify and address misconceptions
- Build intuition before memorization

STUDENT PROFILE:
- Fast learner but struggles with retention
- Prefers understanding over rote learning
- Needs regular reinforcement
- Currently in Year 11, preparing for Year 12
    """,
    "tools": [
        "Read", "Grep", "Glob",  # Resource access
        "mcp__studybrain__generate_questions",
        "mcp__studybrain__save_quiz_result",
        "mcp__studybrain__update_progress",
        "mcp__studybrain__get_fsrs_review",
        "Task"  # Can invoke sub-agents
    ],
    "model": "sonnet"
}
```

---

### 2.3 Specialized Sub-Agents

**Purpose:** Handle specific complex tasks with focused expertise

#### 2.3.1 Curriculum Expert Sub-Agent

**When to use:** Deep curriculum knowledge, topic scoping, prerequisite identification

**System Prompt:**
```
You are a Curriculum Expert for HSC {Subject} with comprehensive knowledge of the NESA syllabus.

EXPERTISE:
- Complete syllabus structure (modules, topics, subtopics)
- Learning progressions and prerequisites
- Assessment criteria and marking guidelines
- Common student misconceptions
- Syllabus verb analysis ("discuss" vs "evaluate" vs "explain")

AVAILABLE RESOURCES:
{subject curriculum PDF, NESA documents, assessment matrices}

OUTPUT FORMAT:
Provide structured, hierarchical information:
- Module → Topic → Subtopic → Key concepts
- Prerequisites for each concept
- Connections to other subjects
- Common exam question types
```

#### 2.3.2 Question Generator Sub-Agent

**When to use:** Creating practice questions, diagnostics quizzes, exam-style assessments

**System Prompt:**
```
You are an expert at generating HSC-quality practice questions for {Subject}.

QUESTION TYPES:
- Multiple choice (4 options, 1 mark each)
- Short answer (2-4 marks, calculation or brief explanation)
- Extended response (5-8 marks, detailed analysis)

REQUIREMENTS:
- Match HSC style and difficulty
- Include mark allocations
- Provide marking criteria
- Use appropriate syllabus verbs
- Reference past HSC papers for inspiration

DIFFICULTY LEVELS:
- Basic: Test fundamental understanding
- Standard: Apply concepts to new situations
- Advanced: Synthesize multiple concepts, complex scenarios

OUTPUT FORMAT:
{
    "questions": [
        {
            "id": "Q1",
            "type": "multiple_choice",
            "marks": 1,
            "text": "...",
            "options": ["A", "B", "C", "D"],
            "correct_answer": "B",
            "explanation": "...",
            "difficulty": "standard"
        }
    ]
}
```

#### 2.3.3 Answer Evaluator Sub-Agent

**When to use:** Marking student answers, providing feedback, calculating scores

**System Prompt:**
```
You are an experienced HSC marker for {Subject} with expertise in NESA marking guidelines.

MARKING APPROACH:
1. Compare student answer to marking criteria
2. Award partial credit where appropriate
3. Identify specific errors or misconceptions
4. Provide constructive, actionable feedback
5. Assess confidence alignment (was student's confidence justified?)

SCORING RUBRIC:
- Correctness: Is the answer factually accurate?
- Completeness: Did they address all parts?
- Method: Was the approach appropriate?
- Communication: Is it clearly explained?

OUTPUT FORMAT:
{
    "marks_awarded": 7,
    "marks_total": 8,
    "percentage": 87.5,
    "feedback": "Excellent understanding of..., but missed...",
    "misconceptions": ["Confused electric field with potential"],
    "confidence_analysis": "Student was appropriately confident (4/5)"
}
```

#### 2.3.4 Progress Tracker Sub-Agent

**When to use:** Complex progress calculations, score aggregation, trend analysis

**System Prompt:**
```
You are a progress tracking specialist using advanced scoring algorithms.

SCORING METHOD (per questionnaire):
- Base score: Correct/Total × 100
- Difficulty adjustment: Harder questions weighted more
- Confidence calibration: Overconfidence penalty, underconfidence bonus
- Recency weighting: Recent performance matters more

METRICS:
- Conceptual Understanding: Depth of "why" knowledge
- Functional Knowledge: Practical "how" application
- Retention rate: Score degradation over time
- Learning velocity: Improvement per study hour

THRESHOLDS:
- Minimum conceptual improvement: 20%
- Minimum functional improvement: 15%
- Both must be met for "sufficient progress"

OUTPUT:
{
    "current_scores": {"con": 75, "func": 68},
    "improvement": {"con": +23, "func": +18},
    "verdict": "sufficient - move to next topic",
    "reasoning": "..."
}
```

---

## 3. Custom MCP Tools

### 3.1 Diagnostics & Assessment Tools

#### `generate_diagnostic_quiz`
```python
@tool(
    "generate_diagnostic_quiz",
    "Generate diagnostic quiz for untested topics",
    {
        "subject": str,
        "topics": list,  # List of topics to test
        "difficulty": str,  # "mixed", "basic", "standard", "advanced"
        "question_count": int,
        "include_past_papers": bool
    }
)
async def generate_diagnostic_quiz(args):
    # 1. Load curriculum for topics
    # 2. Search past papers for similar questions
    # 3. Generate new questions using Question Generator agent
    # 4. Mix question types (MC, short answer, extended)
    # 5. Return structured quiz
    pass
```

#### `save_quiz_result`
```python
@tool(
    "save_quiz_result",
    "Save quiz result and update progress",
    {
        "subject": str,
        "topic": str,
        "question_id": str,
        "student_answer": str,
        "answer_is_correct": str,
        "marks_awarded": float,
        "marks_total": float,
        "confidence": int,  # 1-5
        "time_taken_seconds": int
    }
)
async def save_quiz_result(args):
    # 1. Calculate is_correct
    # 2. Store to JSON: ./data/quiz_results/{subject}/{topic}/{timestamp}.json
    # 3. Update progress scores with new result
    # 4. Check FSRS for next review date
    # 5. Return updated progress summary
    pass
```

#### `evaluate_answer`
```python
@tool(
    "evaluate_answer",
    "Mark student answer using Answer Evaluator agent",
    {
        "question": dict,  # Full question object
        "student_answer": str,
        "student_confidence": int  # 1-5
    }
)
async def evaluate_answer(args):
    # Invoke Answer Evaluator sub-agent
    # Return marks, feedback, misconceptions
    pass
```

---

### 3.2 Progress & Analytics Tools

#### `update_progress_scores`
```python
@tool(
    "update_progress_scores",
    "Update conceptual/functional scores for a topic",
    {
        "subject": str,
        "module": str,
        "topic": str,
        "quiz_results": list,  # Recent quiz results
        "recalculate_from_scratch": bool
    }
)
async def update_progress_scores(args):
    # 1. Load all quiz results for topic
    # 2. Apply scoring algorithm:
    #    - Base: correct/total * 100
    #    - Difficulty weighting
    #    - Confidence calibration
    #    - Recency weighting
    # 3. Calculate conceptual vs functional separately
    # 4. Store updated scores
    # 5. Update FSRS review schedule
    pass
```

#### `get_progress_summary`
```python
@tool(
    "get_progress_summary",
    "Get comprehensive progress summary",
    {
        "subject": str,
        "module": str | None,  # Optional: specific module
        "include_chart_data": bool  # For web visualization
    }
)
async def get_progress_summary(args):
    # Return hierarchical progress tree:
    # Subject → Module → Topic → Subtopic
    # With scores, FSRS data, incorrect questions
    pass
```

---

### 3.3 FSRS Integration Tools

#### `schedule_fsrs_review`
```python
@tool(
    "schedule_fsrs_review",
    "Schedule topic review using FSRS algorithm",
    {
        "subject": str,
        "topic": str,
        "performance_rating": int,  # 1-4 (again, hard, good, easy)
        "current_stability": float | None,
        "current_difficulty": float | None
    }
)
async def schedule_fsrs_review(args):
    # 1. Load py-fsrs library
    # 2. Update card parameters
    # 3. Calculate next review date
    # 4. Store FSRS data in progress JSON
    # 5. Return: {next_review: "2025-10-05", interval_days: 3}
    pass
```

#### `get_due_reviews`
```python
@tool(
    "get_due_reviews",
    "Get topics due for FSRS review",
    {
        "subject": str | None,  # Optional: filter by subject
        "include_upcoming": bool,  # Include reviews due in next 3 days
        "limit": int
    }
)
async def get_due_reviews(args):
    # Query all topics, filter by review_date <= today
    # Sort by priority (overdue first, then difficulty)
    # Return list of topics ready for review
    pass
```

---

### 3.4 Resource Management Tools

#### `index_resources`
```python
@tool(
    "index_resources",
    "Index and organize study resources",
    {
        "subject": str,
        "scan_directory": str,  # User's current resource folder
        "auto_organize": bool  # Move files to proper structure
    }
)
async def index_resources(args):
    # 1. Scan directory for PDFs, images, notes
    # 2. Use Claude vision to categorize (curriculum, class notes, practice papers)
    # 3. Extract metadata (module, topic)
    # 4. If auto_organize: move to ./resources/{subject}/{type}/{module}/
    # 5. Create index: ./data/resource_index/{subject}.json
    # 6. Return: {indexed: 47, organized: 47, errors: 0}
    pass
```

#### `search_resources`
```python
@tool(
    "search_resources",
    "Search indexed resources by topic/keyword",
    {
        "subject": str,
        "topic": str | None,
        "keywords": list | None,
        "resource_type": str | None  # "curriculum", "notes", "practice_papers"
    }
)
async def search_resources(args):
    # Query resource index
    # Return list of relevant files with paths
    pass
```

---

### 3.5 Session & Timer Tools

#### `start_study_session`
```python
@tool(
    "start_study_session",
    "Start timed study session (Toggl-like)",
    {
        "subject": str,
        "session_type": str,  # "diagnostics", "study", "practice", "review"
        "topic": str | None
    }
)
async def start_study_session(args):
    # 1. Create session record
    # 2. Start timer
    # 3. Store: ./data/study_timer/{subject}/{date}.json
    # 4. Return: {session_id: "...", started_at: "2025-10-01T14:30:00"}
    pass
```

#### `end_study_session`
```python
@tool(
    "end_study_session",
    "End study session and calculate learning rate",
    {
        "session_id": str,
        "progress_improvement": dict | None  # {con: +15, func: +20}
    }
)
async def end_study_session(args):
    # 1. Stop timer
    # 2. Calculate duration
    # 3. If progress provided: learning_rate = improvement / hours
    # 4. Store session summary
    # 5. Return: {duration_minutes: 45, learning_rate: 26.7}
    pass
```

#### `get_study_time_stats`
```python
@tool(
    "get_study_time_stats",
    "Get study time statistics",
    {
        "subject": str | None,
        "date_range": dict  # {from: "2025-09-01", to: "2025-10-01"}
    }
)
async def get_study_time_stats(args):
    # Aggregate all sessions in range
    # Return: {
    #   total_hours: 45.5,
    #   by_subject: {...},
    #   by_session_type: {...},
    #   avg_session_duration: 38,
    #   learning_rate: 18.2
    # }
    pass
```

---

### 3.6 Cross-Subject Tools

#### `update_cross_subject_concept`
```python
@tool(
    "update_cross_subject_concept",
    "Track concept that appears in multiple subjects",
    {
        "concept_name": str,  # e.g., "Calculus", "Vectors"
        "subjects": list,  # ["Physics", "Mathematics Extension 1"]
        "connections": dict  # How subjects relate
    }
)
async def update_cross_subject_concept(args):
    # Store in ./data/cross_subject_concepts.json
    # Return updated registry
    pass
```

#### `suggest_cross_subject_study`
```python
@tool(
    "suggest_cross_subject_study",
    "Suggest related topics from other subjects",
    {
        "current_subject": str,
        "current_topic": str
    }
)
async def suggest_cross_subject_study(args):
    # Query cross-subject registry
    # Find related topics
    # Return suggestions: [
    #   {subject: "Maths Ext1", topic: "Derivatives", reason: "Used in Physics kinematics"}
    # ]
    pass
```

---

## 4. Flask Web Application

### 4.1 Technology Stack

```python
# requirements.txt
Flask==3.0.0
flask-cors==4.0.0
claude-agent-sdk==latest
py-fsrs==latest
plotly==5.17.0  # For interactive charts
python-dotenv==1.0.0
```

### 4.2 Directory Structure

```
studybrain_web/
├── app.py                      # Flask application entry point
├── config.py                   # Configuration management
├── requirements.txt
├── .env                        # Environment variables (not committed)
├── agents/                     # Agent definitions
│   ├── coordinator.py
│   ├── subjects/
│   │   ├── physics.py
│   │   ├── maths_ext1.py
│   │   └── ...
│   └── subagents/
│       ├── curriculum_expert.py
│       ├── question_generator.py
│       ├── answer_evaluator.py
│       └── progress_tracker.py
├── mcp_tools/                  # Custom MCP tools
│   ├── __init__.py
│   ├── diagnostics.py
│   ├── progress.py
│   ├── fsrs_integration.py
│   ├── resources.py
│   └── study_timer.py
├── routes/                     # Flask routes
│   ├── __init__.py
│   ├── dashboard.py
│   ├── study_session.py
│   ├── progress.py
│   └── admin.py
├── services/                   # Business logic
│   ├── __init__.py
│   ├── agent_manager.py        # Manages Claude agents
│   ├── progress_calculator.py  # Scoring algorithms
│   └── fsrs_scheduler.py       # FSRS implementation
├── templates/                  # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── study_session.html
│   ├── progress.html
│   └── components/
│       ├── progress_chart.html
│       ├── quiz_interface.html
│       └── timer_widget.html
├── static/                     # CSS, JS, images
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   ├── charts.js
│   │   ├── quiz.js
│   │   └── timer.js
│   └── img/
└── data/                       # JSON storage (not committed)
    ├── sessions/
    ├── exams/
    ├── progress/
    ├── quiz_results/
    ├── study_timer/
    ├── cross_subject_concepts.json
    └── resource_index/
```

### 4.3 Key Routes

```python
# routes/__init__.py
from flask import Blueprint

# Dashboard
GET  /                          # Home dashboard
GET  /api/dashboard/stats       # Dashboard data (JSON)

# Study Sessions
GET  /study/<subject>           # Start study session
POST /study/<subject>/quiz      # Submit quiz answer
GET  /study/<subject>/topic/<topic>  # Study specific topic

# Progress & Analytics
GET  /progress                  # Progress overview (all subjects)
GET  /progress/<subject>        # Subject-specific progress
GET  /api/progress/data         # Chart data (JSON)
GET  /api/progress/fsrs-due     # Topics due for review

# Exam Preparation
GET  /exam/new                  # Create new exam prep
POST /exam/create               # Submit exam details
GET  /exam/<exam_id>            # View exam prep data
GET  /exam/<exam_id>/diagnostics  # Run diagnostics

# Study Timer
POST /api/timer/start           # Start timer
POST /api/timer/stop            # Stop timer
GET  /api/timer/stats           # Get time statistics

# Resources
GET  /resources                 # Resource library
POST /api/resources/upload      # Upload resources
POST /api/resources/index       # Trigger indexing

# Settings
GET  /settings                  # User preferences
POST /settings/update           # Update preferences
```

### 4.4 Dashboard UI

**Home Dashboard (`templates/dashboard.html`):**

```html
<!-- Quick Stats -->
<div class="stats-grid">
    <div class="stat-card">
        <h3>Overall Progress</h3>
        <div class="progress-circle">78%</div>
        <p>Conceptual: 82% | Functional: 74%</p>
    </div>

    <div class="stat-card">
        <h3>Study Time (This Week)</h3>
        <p>12.5 hours</p>
        <canvas id="timeBySubject"></canvas>
    </div>

    <div class="stat-card urgent">
        <h3>Due for Review</h3>
        <ul>
            <li>Physics: Electric Potential (2 days overdue)</li>
            <li>Maths: Derivatives (due today)</li>
        </ul>
    </div>
</div>

<!-- Subject Cards -->
<div class="subject-grid">
    <a href="/study/physics" class="subject-card">
        <h2>Physics</h2>
        <div class="mini-progress">
            <div class="bar" style="width: 65%"></div>
        </div>
        <p>Con: 68% | Func: 62%</p>
        <span class="status">3 topics need review</span>
    </a>

    <!-- Repeat for each subject -->
</div>

<!-- Recommendations -->
<div class="recommendations">
    <h3>What should you study next?</h3>
    <div class="recommendation-card priority-high">
        <h4>Physics - Module 4: Electricity</h4>
        <p>Exam in 8 days, current score: 30%</p>
        <p>Estimated time needed: 4 hours</p>
        <button>Start Now</button>
    </div>
</div>
```

### 4.5 Study Session UI

```html
<!-- Study Session Interface -->
<div class="study-session">
    <!-- Header with timer -->
    <div class="session-header">
        <h1>Physics - Electric Potential</h1>
        <div class="timer-widget">
            <span class="time">00:23:45</span>
            <button id="pauseTimer">Pause</button>
        </div>
    </div>

    <!-- Session type selector -->
    <div class="session-type-tabs">
        <button class="active">Learn</button>
        <button>Practice</button>
        <button>Review</button>
    </div>

    <!-- Content area (changes based on session type) -->
    <div class="content-area">
        <!-- For "Learn" mode -->
        <div class="explanation-panel">
            <div class="claude-response">
                <!-- AI-generated explanation with LaTeX -->
                <p>Electric potential is defined as...</p>
                $$ V = \frac{kQ}{r} $$
            </div>

            <div class="resources">
                <h4>Related Resources:</h4>
                <ul>
                    <li>Curriculum Page 23</li>
                    <li>Class Notes - Sept 15</li>
                </ul>
            </div>
        </div>

        <!-- For "Practice" mode -->
        <div class="quiz-interface">
            <div class="question">
                <p><strong>Question 3 of 10</strong> (4 marks)</p>
                <p>Calculate the electric potential at point P...</p>
                <img src="diagram.png" />
            </div>

            <div class="answer-input">
                <textarea placeholder="Your answer..."></textarea>
                <div class="confidence-slider">
                    <label>How confident are you? (1-5)</label>
                    <input type="range" min="1" max="5" value="3">
                </div>
                <button>Submit Answer</button>
            </div>
        </div>
    </div>

    <!-- Progress indicator -->
    <div class="session-progress">
        <div class="progress-bar">
            <div style="width: 30%"></div>
        </div>
        <p>3 / 10 questions completed</p>
    </div>
</div>
```

### 4.6 Progress Visualization UI

```html
<!-- Progress Charts -->
<div class="progress-page">
    <h1>Progress Overview</h1>

    <!-- Subject selector -->
    <select id="subjectFilter">
        <option value="all">All Subjects</option>
        <option value="physics">Physics</option>
        <!-- ... -->
    </select>

    <!-- Chart grid -->
    <div class="chart-grid">
        <!-- Progress over time -->
        <div class="chart-card">
            <h3>Progress Over Time</h3>
            <canvas id="progressTimeline"></canvas>
            <!-- Plotly line chart: Date vs Score -->
        </div>

        <!-- Module breakdown -->
        <div class="chart-card">
            <h3>Module Breakdown</h3>
            <canvas id="moduleRadar"></canvas>
            <!-- Radar chart: Each module's Con/Func scores -->
        </div>

        <!-- Learning rate -->
        <div class="chart-card">
            <h3>Learning Velocity</h3>
            <canvas id="learningRate"></canvas>
            <!-- Bar chart: Improvement per study hour by subject -->
        </div>

        <!-- FSRS predictions -->
        <div class="chart-card">
            <h3>Retention Forecast</h3>
            <canvas id="retentionForecast"></canvas>
            <!-- Line chart: Predicted retention over next 30 days -->
        </div>
    </div>

    <!-- Detailed topic tree -->
    <div class="topic-tree">
        <h3>Detailed Breakdown</h3>
        <div class="tree-node" data-level="0">
            <div class="node-header">
                <span class="expand-icon">▼</span>
                <h4>Module 1 - Motion</h4>
                <span class="score">Con: 95% | Func: 80%</span>
            </div>

            <div class="tree-children">
                <div class="tree-node" data-level="1">
                    <div class="node-header">
                        <span class="expand-icon">▼</span>
                        <h5>Kinematics</h5>
                        <span class="score">Con: 92% | Func: 78%</span>
                    </div>

                    <div class="tree-children">
                        <!-- Leaf nodes with incorrect questions -->
                        <div class="tree-node incorrect">
                            <p>❌ "What is displacement vs distance?"</p>
                            <button class="review-btn">Review Now</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

---

## 5. Data Structures (JSON Schemas)

### 5.1 Progress Data

```json
// data/progress/physics.json
{
  "subject": "Physics",
  "last_updated": "2025-10-01T14:30:00Z",
  "overall_scores": {
    "conceptual": 68.5,
    "functional": 62.3
  },
  "modules": [
    {
      "module_id": "module_4",
      "module_name": "Electricity and Magnetism",
      "scores": {
        "conceptual": 30.0,
        "functional": 20.0
      },
      "topics": [
        {
          "topic_id": "electricity",
          "topic_name": "Electricity",
          "scores": {
            "conceptual": 20.0,
            "functional": 10.0
          },
          "subtopics": [
            {
              "subtopic_id": "electric_potential",
              "subtopic_name": "Electric Potential",
              "scores": {
                "conceptual": 10.0,
                "functional": 5.0
              },
              "fsrs_data": {
                "stability": 1.2,
                "difficulty": 7.8,
                "last_review": "2025-09-28",
                "next_review": "2025-10-03",
                "review_count": 2
              },
              "incorrect_questions": [
                {
                  "question_id": "Q_EP_001",
                  "text": "What is Electric Potential?",
                  "date": "2025-09-28",
                  "marks": "0/2"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### 5.2 Quiz Result

```json
// data/quiz_results/physics/electricity/20251001_143045.json
{
  "quiz_id": "quiz_001",
  "session_id": "session_456",
  "subject": "Physics",
  "topic": "Electric Potential",
  "timestamp": "2025-10-01T14:30:45Z",
  "results": [
    {
      "question_id": "Q1",
      "question_text": "Calculate the electric potential...",
      "question_type": "short_answer",
      "marks_total": 4,
      "student_answer": "V = kQ/r = ...",
      "correct_answer": "V = 18000 V",
      "marks_awarded": 3.5,
      "confidence": 4,
      "time_taken_seconds": 180,
      "feedback": "Correct method and calculation, minor rounding error",
      "misconceptions": []
    }
  ],
  "summary": {
    "total_marks": 20,
    "marks_achieved": 16.5,
    "percentage": 82.5,
    "conceptual_estimate": 85.0,
    "functional_estimate": 80.0
  }
}
```

### 5.3 Study Session

```json
// data/sessions/physics/20251001_session.json
{
  "session_id": "session_456",
  "subject": "Physics",
  "topic": "Electric Potential",
  "session_type": "study",  // "diagnostics", "practice", "review"
  "started_at": "2025-10-01T14:00:00Z",
  "ended_at": "2025-10-01T15:30:00Z",
  "duration_minutes": 90,
  "progress_before": {
    "conceptual": 10.0,
    "functional": 5.0
  },
  "progress_after": {
    "conceptual": 33.0,
    "functional": 28.0
  },
  "improvement": {
    "conceptual": 23.0,
    "functional": 23.0
  },
  "learning_rate": 15.3,  // improvement per hour
  "activities": [
    {
      "type": "explanation",
      "duration_minutes": 30,
      "content_summary": "Learned definition, formula derivation, units"
    },
    {
      "type": "practice_questions",
      "duration_minutes": 45,
      "questions_completed": 8,
      "accuracy": 75.0
    },
    {
      "type": "review",
      "duration_minutes": 15,
      "topics_reviewed": ["Electric field vs potential"]
    }
  ],
  "verdict": "sufficient",  // "sufficient", "repeat", "review_later"
  "next_action": "move_to_next_topic"
}
```

### 5.4 Exam Preparation

```json
// data/exams/PHY-TASK-2.json
{
  "exam_id": "PHY-TASK-2",
  "subject": "Physics",
  "exam_name": "PHYS-Task-2",
  "exam_date": "2025-10-13",
  "exam_time": "10:00",
  "notification_file": "./uploaded/PHY-HSC-Assessment.pdf",
  "scope": {
    "modules": ["Module 3", "Module 4"],
    "topics": [
      "Waves and Thermodynamics",
      "Electricity and Magnetism"
    ],
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
  "diagnostics_date": "2025-09-28",
  "results_file": "./data/progress/physics.json"
}
```

### 5.5 Cross-Subject Concepts

```json
// data/cross_subject_concepts.json
{
  "concepts": [
    {
      "concept_id": "calculus",
      "concept_name": "Calculus",
      "subjects": ["Mathematics Extension 1", "Physics"],
      "connections": {
        "Maths Extension 1": {
          "topics": ["Derivatives", "Integration", "Rates of Change"],
          "role": "Primary teaching subject"
        },
        "Physics": {
          "topics": ["Kinematics", "Projectile Motion", "Electric Fields"],
          "role": "Application in problem-solving"
        }
      },
      "recommendation": "Master derivatives in Maths before Physics kinematics",
      "priority": "high"
    },
    {
      "concept_id": "vectors",
      "concept_name": "Vectors",
      "subjects": ["Mathematics Extension 1", "Physics"],
      "connections": {
        "Maths Extension 1": {
          "topics": ["Vector Operations", "Dot Product", "Cross Product"],
          "role": "Formal mathematical treatment"
        },
        "Physics": {
          "topics": ["Forces", "Momentum", "Electric/Magnetic Fields"],
          "role": "Physical interpretation and application"
        }
      },
      "recommendation": "Study in parallel - physics provides intuition, maths provides rigor",
      "priority": "high"
    }
  ]
}
```

---

## 6. FSRS Integration

**Library:** `py-fsrs` (https://github.com/open-spaced-repetition/py-fsrs)

**Implementation:** `services/fsrs_scheduler.py`

```python
from fsrs import FSRS, Card, Rating, ReviewLog

class FSRSScheduler:
    def __init__(self):
        self.fsrs = FSRS()

    def initialize_card(self, topic_id):
        """Create new FSRS card for a topic"""
        return Card()

    def review(self, card_data, rating):
        """
        Update card after review

        rating (int): 1=Again, 2=Hard, 3=Good, 4=Easy
        Based on student performance and confidence
        """
        card = Card(**card_data)

        # Map our score to FSRS rating
        # <50% correct or confidence mismatch = Hard
        # 50-75% = Good
        # >75% with high confidence = Easy

        rating_enum = Rating(rating)
        scheduling_cards = self.fsrs.repeat(card, datetime.now())

        # Get the specific scheduling for this rating
        updated_card = scheduling_cards[rating_enum].card

        return {
            "stability": updated_card.stability,
            "difficulty": updated_card.difficulty,
            "elapsed_days": updated_card.elapsed_days,
            "scheduled_days": updated_card.scheduled_days,
            "due": updated_card.due,
            "last_review": updated_card.last_review
        }

    def get_retention_probability(self, card_data):
        """Estimate current retention probability"""
        card = Card(**card_data)
        days_since_review = (datetime.now() - card.last_review).days
        return self.fsrs.calculate_retention(card.stability, days_since_review)
```

**Data Structure Addition to Progress:**
```json
{
  "subtopic_id": "electric_potential",
  "fsrs_data": {
    "stability": 1.2,      // How well-learned (higher = longer retention)
    "difficulty": 7.8,     // Intrinsic difficulty (higher = harder)
    "elapsed_days": 3,     // Days since last review
    "scheduled_days": 5,   // Optimal interval
    "due": "2025-10-06",   // Next review date
    "last_review": "2025-10-01",
    "review_count": 3,
    "state": "review"      // new, learning, review, relearning
  }
}
```

---

## 7. Phase 1 Implementation Plan (Oct 1-12)

### Day-by-Day Breakdown

#### **Day 1-2 (Oct 1-2): Foundation**
- [x] Set up Flask project structure
- [x] Install Claude Agent SDK
- [x] Create basic Flask routes (home, study)
- [x] Test SDK connection with simple query
- [x] Create JSON storage directories
- [x] Basic HTML templates (base, dashboard)

**Deliverables:**
- Flask app runs on localhost:5000
- Can query Claude and get response
- Basic dashboard loads

---

#### **Day 3-4 (Oct 3-4): Agent Architecture**
- [ ] Implement coordinator agent
- [ ] Create one subject agent (Physics as test case)
- [ ] Create curriculum expert sub-agent
- [ ] Test agent communication
- [ ] Implement agent routing logic

**Deliverables:**
- Coordinator can route to Physics agent
- Curriculum expert can answer syllabus questions
- Multi-agent system working

---

#### **Day 5-6 (Oct 5-6): Core MCP Tools**
- [ ] Implement diagnostics tools:
  - generate_diagnostic_quiz
  - save_quiz_result
  - evaluate_answer
- [ ] Implement progress tools:
  - update_progress_scores
  - get_progress_summary
- [ ] Test quiz workflow end-to-end

**Deliverables:**
- Can generate quiz questions
- Can submit answers and get marked
- Progress updates correctly

---

#### **Day 7-8 (Oct 7-8): Web Interface**
- [ ] Build study session UI
- [ ] Build quiz interface with LaTeX support
- [ ] Implement AJAX for real-time updates
- [ ] Add timer widget
- [ ] Basic progress visualization

**Deliverables:**
- Can start study session via web
- Quiz questions display properly
- Timer tracks session duration
- See basic progress charts

---

#### **Day 9-10 (Oct 9-10): Integration & Testing**
- [ ] Add remaining subject agents
- [ ] Implement session persistence
- [ ] Add FSRS integration (basic)
- [ ] Comprehensive testing
- [ ] Bug fixes

**Deliverables:**
- All 6 subjects available
- Sessions save and resume
- FSRS schedules reviews
- System stable and usable

---

#### **Day 11-12 (Oct 11-12): Polish**
- [ ] Improve UI/UX
- [ ] Add progress charts
- [ ] Create user guide
- [ ] Performance optimization
- [ ] Deploy for daily use

**Deliverables:**
- Production-ready system
- Documented usage
- Ready for daily study sessions

---

### Minimum Viable Product (MVP) Features

**MUST HAVE by Oct 12:**
1. ✅ Diagnostics quizzes for at least Physics
2. ✅ Practice question generation
3. ✅ Answer evaluation and marking
4. ✅ Session persistence (can resume)
5. ✅ Multi-subject support (all 6 subjects)
6. ✅ Basic progress tracking with scores

**NICE TO HAVE by Oct 12:**
7. ⚠️ FSRS review scheduling (basic)
8. ⚠️ Study timer
9. ⚠️ Progress charts
10. ⚠️ Content synthesis from resources

**DEFER TO PHASE 2 (Late October):**
- Advanced FSRS optimization
- Cross-subject integration
- Resource auto-organization
- Advanced analytics
- PDF processing for handwritten notes

---

## 8. Phase 2 Enhancements (Oct 13-31)

### Week 1 (Oct 13-19)
- [ ] FSRS optimizer integration
- [ ] Advanced progress analytics
- [ ] Learning rate calculations
- [ ] Retention forecasting

### Week 2 (Oct 20-26)
- [ ] Cross-subject concept tracking
- [ ] Coordinator improvements
- [ ] Resource indexing and search
- [ ] External resource search (with permission)

### Week 3 (Oct 27-31)
- [ ] Question strategy training
- [ ] Time management features
- [ ] Grade prediction
- [ ] Gap analysis prioritization

---

## 9. Success Criteria

### Technical
- [x] Flask app serves all routes without errors
- [x] Claude agents respond within 10 seconds
- [x] JSON data persists correctly
- [x] Session state maintains across browser refreshes
- [x] Charts render properly with Plotly

### Functional
- [x] Can complete full diagnostics → study → practice workflow
- [x] Progress scores update accurately
- [x] FSRS schedules reviews appropriately
- [x] Timer tracks study sessions correctly
- [x] All 6 subjects have working agents

### User Experience
- [x] Interface is intuitive (you can use without documentation)
- [x] Response times feel fast (< 3s for most operations)
- [x] LaTeX equations render properly
- [x] Charts are readable and informative
- [x] System guides next steps clearly

---

## 10. Architecture Decisions Record

### Decision 1: Flask vs FastAPI
**Chosen:** Flask
**Reason:** You want to learn Flask for Year 12 Software Engineering
**Trade-off:** FastAPI has better async support, but Flask is simpler to learn

### Decision 2: Local JSON vs SQLite
**Chosen:** Local JSON
**Reason:** Simpler for <1000 records, human-readable, easier debugging
**Trade-off:** Won't scale to huge datasets, but sufficient for 1-2 years of HSC data

### Decision 3: Synchronous vs Async Flask
**Chosen:** Async where needed (Claude SDK calls)
**Reason:** Claude SDK is async, but Flask routes can be sync
**Implementation:** Use `asyncio.run()` in route handlers

### Decision 4: Frontend Framework
**Chosen:** Vanilla JS + Plotly
**Reason:** Learning Flask, don't want to also learn React
**Trade-off:** More manual DOM manipulation, but simpler stack

### Decision 5: Authentication
**Chosen:** None for MVP
**Reason:** Single user (you), localhost only
**Future:** Add if sharing with others

---

## 11. Risk Mitigation

### Risk 1: Claude SDK Rate Limits
**Mitigation:**
- Cache responses where possible
- Use Haiku for simple tasks
- Implement request queuing
- Monitor usage in dashboard

### Risk 2: October 12 Deadline Too Tight
**Mitigation:**
- MVP scope clearly defined
- Can defer Phase 2 features
- Already have Flask basics from School project
- Focus on Physics first, add other subjects after

### Risk 3: FSRS Complexity
**Mitigation:**
- Use py-fsrs library (don't implement from scratch)
- Basic integration for MVP
- Optimize algorithm in Phase 2
- Manual review scheduling as fallback

### Risk 4: Progress Algorithm Accuracy
**Mitigation:**
- Start with simple percentage
- Add weighting incrementally
- Validate against actual exam results
- Allow manual score adjustment

---

## 12. Next Steps

**Immediate (Now):**
1. Create Flask project structure
2. Install dependencies
3. Test Claude SDK connection
4. Build basic "Hello World" with agent

**Tomorrow (Oct 2):**
1. Implement coordinator agent
2. Create Physics agent
3. Build first MCP tool (quiz generation)
4. Test end-to-end quiz flow

**This Week:**
1. Complete agent architecture
2. Build all core MCP tools
3. Create study session UI
4. Test complete workflow

**Next Week:**
1. Add remaining subjects
2. Implement FSRS
3. Build progress visualization
4. Polish and deploy

---

**END OF V2 ARCHITECTURE**

*This document is the complete technical specification for StudyBrain V2. All implementation should follow this architecture.*
