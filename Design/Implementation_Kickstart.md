# StudyBrain V2 - Implementation Kickstart Guide

**Start Date:** October 2, 2025
**Target:** Working MVP by October 12, 2025

---

## Quick Start (5 Minutes)

### Step 1: Create Project Structure
```bash
cd /Users/james/Desktop/School/Year-12/
mkdir studybrain_web
cd studybrain_web

# Create directory structure
mkdir -p agents/subjects agents/subagents
mkdir -p mcp_tools routes services templates static/css static/js
mkdir -p data/{sessions,exams,progress,quiz_results,study_timer,resource_index}

# Create __init__.py files
touch agents/__init__.py mcp_tools/__init__.py routes/__init__.py services/__init__.py
```

### Step 2: Install Dependencies
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Create requirements.txt
cat > requirements.txt << EOF
Flask==3.0.0
flask-cors==4.0.0
claude-agent-sdk
py-fsrs
plotly==5.17.0
python-dotenv==1.0.0
EOF

# Install
pip install -r requirements.txt
```

### Step 3: Test Claude SDK Connection
```bash
# Create test file
cat > test_sdk.py << 'EOF'
import asyncio
from claude_agent_sdk import query

async def test():
    print("Testing Claude SDK connection...")
    async for message in query(prompt="Hello, Claude! Say 'StudyBrain online!' if you can hear me."):
        print(message)

asyncio.run(test())
EOF

# Run test
python test_sdk.py
```

**Expected output:** You should see Claude respond with "StudyBrain online!"

---

## Day 1-2: Minimal Flask App (Oct 2-3)

### Create Basic Flask App

**File: `app.py`**
```python
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

app = Flask(__name__)
CORS(app)

# Simple coordinator agent (will expand later)
async def ask_coordinator(user_message):
    """Send message to coordinator agent"""
    options = ClaudeAgentOptions(
        system_prompt="""You are the StudyBrain Coordinator.
        You help James with his HSC studies across all subjects.
        Be concise and helpful."""
    )

    responses = []
    async for message in query(prompt=user_message, options=options):
        responses.append(str(message))

    return " ".join(responses)

@app.route('/')
def home():
    """Dashboard home page"""
    return render_template('dashboard.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    """API endpoint for asking questions"""
    data = request.json
    user_message = data.get('message', '')

    # Run async function in sync context
    response = asyncio.run(ask_coordinator(user_message))

    return jsonify({"response": response})

@app.route('/study/<subject>')
def study_session(subject):
    """Study session page"""
    return render_template('study_session.html', subject=subject)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**File: `templates/dashboard.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>StudyBrain</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .subject-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }
        .subject-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-decoration: none;
            color: #333;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .subject-card:hover {
            transform: translateY(-5px);
        }
        .test-area {
            background: white;
            padding: 20px;
            border-radius: 10px;
        }
        #response {
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 5px;
            min-height: 100px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>StudyBrain</h1>
        <p>Your AI-Powered HSC Study System</p>
    </div>

    <div class="subject-grid">
        <a href="/study/physics" class="subject-card">
            <h2>Physics</h2>
            <p>Modules 1-4</p>
        </a>
        <a href="/study/maths_ext1" class="subject-card">
            <h2>Maths Extension 1</h2>
            <p>Full Syllabus</p>
        </a>
        <a href="/study/maths_adv" class="subject-card">
            <h2>Maths Advanced</h2>
            <p>Full Syllabus</p>
        </a>
        <a href="/study/chemistry" class="subject-card">
            <h2>Chemistry</h2>
            <p>Full Syllabus</p>
        </a>
        <a href="/study/software" class="subject-card">
            <h2>Software Engineering</h2>
            <p>Full Syllabus</p>
        </a>
        <a href="/study/english" class="subject-card">
            <h2>English Standard</h2>
            <p>Full Syllabus</p>
        </a>
    </div>

    <div class="test-area">
        <h3>Test Claude Connection</h3>
        <input type="text" id="testInput" placeholder="Ask StudyBrain something..." style="width: 70%; padding: 10px;">
        <button onclick="testClaude()" style="padding: 10px 20px;">Ask</button>
        <div id="response">Response will appear here...</div>
    </div>

    <script>
        async function testClaude() {
            const input = document.getElementById('testInput').value;
            const responseDiv = document.getElementById('response');

            responseDiv.textContent = 'Thinking...';

            try {
                const response = await fetch('/api/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: input})
                });

                const data = await response.json();
                responseDiv.textContent = data.response;
            } catch (error) {
                responseDiv.textContent = 'Error: ' + error;
            }
        }
    </script>
</body>
</html>
```

**File: `templates/study_session.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Study Session - {{ subject }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background: #667eea;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{ subject|title }} Study Session</h1>
        <p><a href="/" style="color: white;">← Back to Dashboard</a></p>
    </div>

    <div>
        <h2>Coming Soon!</h2>
        <p>This will be your study interface for {{ subject }}.</p>
    </div>
</body>
</html>
```

### Test Your Flask App

```bash
# Run Flask
python app.py
```

Open browser to: http://localhost:5000

**You should see:**
- Dashboard with 6 subject cards
- Test input box at bottom
- Can ask Claude questions and get responses

---

## Day 3-4: First Agent (Physics)

**File: `agents/subjects/physics.py`**
```python
from claude_agent_sdk import ClaudeAgentOptions

def get_physics_agent_config():
    """Returns configuration for Physics agent"""
    return {
        "description": "Expert HSC Physics tutor for NSW NESA curriculum",
        "prompt": """
You are an expert HSC Physics tutor specializing in the NSW curriculum.

MODULES COVERED:
- Module 1: Kinematics
- Module 2: Dynamics
- Module 3: Waves and Thermodynamics
- Module 4: Electricity and Magnetism

YOUR ROLE:
1. Help students understand physics concepts deeply
2. Generate practice questions
3. Explain solutions step-by-step
4. Identify misconceptions

TEACHING STYLE:
- Focus on intuitive understanding before formulas
- Use real-world examples
- Break down complex problems
- Encourage curiosity

STUDENT: James (Year 11, fast learner, needs reinforcement)
        """,
        "tools": ["Read", "Grep", "Glob"],
        "model": "sonnet"
    }
```

**File: `agents/coordinator.py`**
```python
from claude_agent_sdk import ClaudeAgentOptions
from agents.subjects.physics import get_physics_agent_config

def get_coordinator_config():
    """Returns configuration for Coordinator agent"""

    # Register subject agents
    agents = {
        "physics": get_physics_agent_config(),
        # Add others later
    }

    return ClaudeAgentOptions(
        system_prompt="""
You are the StudyBrain Coordinator managing James's HSC study program.

AVAILABLE SUBJECT AGENTS:
- physics: For all Physics questions and study

ROUTING RULES:
- Physics questions → Use physics agent
- Other subjects → Say "Coming soon!"
- Meta questions (What to study next?) → Answer directly

STUDENT PROFILE:
- Name: James
- Year: 11 → 12
- Learns fast but forgets fast
- Needs deep understanding
        """,
        agents=agents,
        allowed_tools=["Task"]  # Can invoke sub-agents
    )
```

**Update `app.py` to use coordinator:**
```python
# Add at top
from agents.coordinator import get_coordinator_config

# Replace ask_coordinator function
async def ask_coordinator(user_message):
    """Send message to coordinator agent"""
    config = get_coordinator_config()

    responses = []
    async for message in query(prompt=user_message, options=config):
        responses.append(str(message))

    return " ".join(responses)
```

### Test Multi-Agent System

```bash
python app.py
```

**Test cases:**
1. Ask: "Explain Newton's second law" → Should route to Physics agent
2. Ask: "What should I study next?" → Coordinator answers directly

---

## Day 5-6: First MCP Tool (Quiz Generation)

**File: `mcp_tools/diagnostics.py`**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server
from typing import Any
import json
import random

@tool(
    "generate_practice_question",
    "Generate a practice question for a topic",
    {
        "subject": str,
        "topic": str,
        "difficulty": str,  # "easy", "medium", "hard"
        "question_type": str  # "multiple_choice", "short_answer"
    }
)
async def generate_practice_question(args: dict[str, Any]) -> dict[str, Any]:
    """
    Generate a practice question using Claude.
    In real implementation, this would use Question Generator sub-agent.
    For now, return a template.
    """

    # TODO: Replace with actual Claude generation
    if args["question_type"] == "multiple_choice":
        question = {
            "id": f"Q_{random.randint(1000, 9999)}",
            "type": "multiple_choice",
            "topic": args["topic"],
            "difficulty": args["difficulty"],
            "text": f"Sample question about {args['topic']}?",
            "options": {
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            },
            "correct_answer": "B",
            "marks": 1
        }
    else:
        question = {
            "id": f"Q_{random.randint(1000, 9999)}",
            "type": "short_answer",
            "topic": args["topic"],
            "difficulty": args["difficulty"],
            "text": f"Explain {args['topic']} in your own words.",
            "marks": 4
        }

    return {
        "content": [{
            "type": "text",
            "text": json.dumps(question, indent=2)
        }]
    }

@tool(
    "save_quiz_result",
    "Save quiz result to JSON storage",
    {
        "subject": str,
        "topic": str,
        "question_id": str,
        "student_answer": str,
        "marks_awarded": float,
        "marks_total": float,
        "confidence": int
    }
)
async def save_quiz_result(args: dict[str, Any]) -> dict[str, Any]:
    """Save quiz result to data/quiz_results/"""
    import os
    from datetime import datetime

    # Create directory if needed
    result_dir = f"./data/quiz_results/{args['subject']}/{args['topic']}"
    os.makedirs(result_dir, exist_ok=True)

    # Create result file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = f"{result_dir}/{timestamp}.json"

    result = {
        "question_id": args["question_id"],
        "student_answer": args["student_answer"],
        "marks_awarded": args["marks_awarded"],
        "marks_total": args["marks_total"],
        "confidence": args["confidence"],
        "percentage": (args["marks_awarded"] / args["marks_total"]) * 100,
        "timestamp": datetime.now().isoformat()
    }

    with open(result_file, 'w') as f:
        json.dump(result, f, indent=2)

    return {
        "content": [{
            "type": "text",
            "text": f"Saved result: {args['marks_awarded']}/{args['marks_total']} ({result['percentage']:.1f}%)"
        }]
    }

# Create MCP server
diagnostics_server = create_sdk_mcp_server(
    name="diagnostics",
    version="1.0.0",
    tools=[generate_practice_question, save_quiz_result]
)
```

**Update `agents/coordinator.py` to include MCP tools:**
```python
from mcp_tools.diagnostics import diagnostics_server

def get_coordinator_config():
    # ... existing code ...

    return ClaudeAgentOptions(
        system_prompt="""...""",
        agents=agents,
        mcp_servers={"diagnostics": diagnostics_server},
        allowed_tools=[
            "Task",
            "mcp__diagnostics__generate_practice_question",
            "mcp__diagnostics__save_quiz_result"
        ]
    )
```

### Test MCP Tools

Ask in dashboard: "Generate a physics practice question about Newton's laws"

Claude should use the `generate_practice_question` tool.

---

## Day 7-8: Quiz Interface

**File: `templates/quiz.html`** (simplified)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz - {{ subject }}</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
        .question { background: #f9f9f9; padding: 20px; border-radius: 10px; margin: 20px 0; }
        .answer-input { margin: 20px 0; }
        textarea { width: 100%; min-height: 100px; padding: 10px; }
        .confidence-slider { margin: 20px 0; }
        button { background: #667eea; color: white; padding: 10px 30px; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>{{ subject }} Quiz</h1>

    <div class="question" id="questionArea">
        <p><strong>Question 1</strong> (4 marks)</p>
        <p id="questionText">Loading...</p>
    </div>

    <div class="answer-input">
        <label>Your Answer:</label>
        <textarea id="answer" placeholder="Type your answer here..."></textarea>

        <div class="confidence-slider">
            <label>Confidence (1-5): <span id="confValue">3</span></label><br>
            <input type="range" min="1" max="5" value="3" id="confidence" oninput="document.getElementById('confValue').textContent = this.value">
        </div>

        <button onclick="submitAnswer()">Submit Answer</button>
    </div>

    <div id="result" style="display: none;">
        <h3>Result:</h3>
        <p id="resultText"></p>
        <button onclick="nextQuestion()">Next Question</button>
    </div>

    <script>
        let currentQuestion = null;

        async function loadQuestion() {
            // For now, generate via API
            const response = await fetch('/api/quiz/generate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    subject: '{{ subject }}',
                    topic: 'general',
                    difficulty: 'medium'
                })
            });

            const data = await response.json();
            currentQuestion = data.question;
            document.getElementById('questionText').textContent = currentQuestion.text;
        }

        async function submitAnswer() {
            const answer = document.getElementById('answer').value;
            const confidence = document.getElementById('confidence').value;

            // Submit to backend for marking
            const response = await fetch('/api/quiz/submit', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    question_id: currentQuestion.id,
                    answer: answer,
                    confidence: parseInt(confidence)
                })
            });

            const result = await response.json();
            document.getElementById('resultText').textContent = result.feedback;
            document.getElementById('result').style.display = 'block';
        }

        function nextQuestion() {
            document.getElementById('result').style.display = 'none';
            document.getElementById('answer').value = '';
            loadQuestion();
        }

        // Load first question on page load
        loadQuestion();
    </script>
</body>
</html>
```

**Add quiz routes to `app.py`:**
```python
@app.route('/quiz/<subject>')
def quiz(subject):
    return render_template('quiz.html', subject=subject)

@app.route('/api/quiz/generate', methods=['POST'])
def generate_quiz_question():
    data = request.json
    # Call MCP tool via coordinator
    # For now, return mock data
    return jsonify({
        "question": {
            "id": "Q001",
            "text": "Explain Newton's Second Law",
            "marks": 4
        }
    })

@app.route('/api/quiz/submit', methods=['POST'])
def submit_quiz_answer():
    data = request.json
    # Mark answer via coordinator/evaluator
    # For now, return mock feedback
    return jsonify({
        "marks_awarded": 3.5,
        "marks_total": 4,
        "feedback": "Good understanding! Minor detail missing about net force."
    })
```

---

## Day 9-10: Polish & Deploy

### Add Session Persistence
```python
# In app.py
import json
from datetime import datetime

@app.route('/api/session/save', methods=['POST'])
def save_session():
    data = request.json
    session_file = f"./data/sessions/{data['subject']}/session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    os.makedirs(os.path.dirname(session_file), exist_ok=True)

    with open(session_file, 'w') as f:
        json.dump(data, f, indent=2)

    return jsonify({"status": "saved"})
```

### Add Basic Progress View
```html
<!-- templates/progress.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Progress</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Your Progress</h1>
    <div id="progressChart"></div>

    <script>
        // Fetch progress data
        fetch('/api/progress/data')
            .then(r => r.json())
            .then(data => {
                var trace = {
                    x: data.dates,
                    y: data.scores,
                    type: 'scatter',
                    mode: 'lines+markers'
                };

                Plotly.newPlot('progressChart', [trace], {
                    title: 'Progress Over Time'
                });
            });
    </script>
</body>
</html>
```

---

## Quick Reference

### Start Development Server
```bash
cd /Users/james/Desktop/School/Year-12/studybrain_web
source venv/bin/activate
python app.py
```

### Check if Claude SDK Works
```bash
python test_sdk.py
```

### Common Issues

**Issue:** "Claude Code not found"
**Fix:** Make sure Claude Code CLI is installed: `which claude`

**Issue:** "Import error: claude_agent_sdk"
**Fix:** `pip install claude-agent-sdk`

**Issue:** Flask won't start
**Fix:** Check port 5000 isn't already in use: `lsof -i :5000`

---

## Next: Follow V2_System_Architecture.md

Once you have this working, follow the detailed day-by-day plan in `V2_System_Architecture.md` to build out:
- Remaining subject agents
- Sub-agents (curriculum expert, question generator, etc.)
- FSRS integration
- Progress tracking
- All MCP tools

---

**You're ready to start! Begin with Day 1-2 steps above.**
