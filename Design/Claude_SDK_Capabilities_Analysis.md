# Claude SDK Capabilities Analysis for StudyBrain

**Purpose:** Map StudyBrain V1 features to Claude Agent SDK capabilities
**Date:** October 2025
**SDK Version:** Claude Agent SDK (Python & TypeScript)

---

## Overview

This document analyzes how Claude Agent SDK features can be leveraged to implement the StudyBrain system. Each V1 component is evaluated against SDK capabilities with implementation feasibility ratings.

**Legend:**
- ✅ **Fully Supported** - Direct SDK feature available
- 🔶 **Partially Supported** - Possible with SDK + custom code
- ⚠️ **Requires Custom Implementation** - SDK provides foundation only
- ❌ **Not Supported** - External tools required

---

## 1. Start/Opening System

### 1.1 Command-Line Interface (`sb physics`)

**V1 Requirement:** Simple CLI command to launch subject-specific agents

**SDK Capability:** ✅ **Fully Supported**

**Implementation:**
```python
# studybrain_cli.py
from claude_agent_sdk import query, ClaudeAgentOptions
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: sb <subject>")
        return

    subject = sys.argv[1]

    # Load subject-specific system prompt
    with open(f"./subjects/{subject}/agent.md") as f:
        system_prompt = f.read()

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        mcpConfig=f"./subjects/{subject}/.mcp.json"
    )

    # Start interactive session
    async for message in query(prompt=user_input_generator(), options=options):
        handle_response(message)

if __name__ == "__main__":
    main()
```

**Notes:**
- CLI wrapper is custom code
- SDK handles agent orchestration
- CLAUDE.md files in subject directories provide persistent context

---

### 1.2 Subject-Specific Agents

**V1 Requirement:** Separate agents for Physics, Math, Chemistry, etc.

**SDK Capability:** ✅ **Fully Supported** (via Subagents or Multiple Sessions)

**Implementation Approach 1: Subagents**
```python
# In main coordinator
agents = {
    "physics": {
        "description": "Physics tutor for HSC preparation",
        "prompt": load_agent_prompt("./subjects/physics/agent.md"),
        "tools": ["Read", "Write", "Edit", "WebSearch"],
        "model": "sonnet"
    },
    "maths": {
        "description": "Mathematics tutor for HSC preparation",
        "prompt": load_agent_prompt("./subjects/maths/agent.md"),
        "tools": ["Read", "Write", "Edit"],
        "model": "sonnet"
    }
}

result = query(
    prompt="Help with projectile motion",
    options=ClaudeAgentOptions(agents=agents)
)
```

**Implementation Approach 2: Separate Sessions**
```python
# Each subject runs as independent session
physics_session = start_subject_session("physics")
maths_session = start_subject_session("maths")
```

**Recommendation:** Use **separate sessions per subject** for better context isolation.

---

### 1.3 Session State Management

**V1 Requirement:** Restore previous session or start fresh

**SDK Capability:** 🔶 **Partially Supported**

**What SDK Provides:**
- Session management through Agent SDK
- Conversation history tracking
- Context preservation

**What Requires Custom Code:**
- Persistent session storage (database/JSON)
- Session selection UI
- State serialization/deserialization

**Implementation:**
```python
import json
from pathlib import Path

def load_session(subject, session_id=None):
    session_dir = Path(f"./sessions/{subject}")

    if session_id is None:
        # Get latest session
        sessions = sorted(session_dir.glob("*.json"))
        if not sessions:
            return None
        session_file = sessions[-1]
    else:
        session_file = session_dir / f"{session_id}.json"

    with open(session_file) as f:
        return json.load(f)

def save_session(subject, session_data):
    session_dir = Path(f"./sessions/{subject}")
    session_dir.mkdir(parents=True, exist_ok=True)

    session_file = session_dir / f"{session_data['id']}.json"
    with open(session_file, 'w') as f:
        json.dump(session_data, f, indent=2)
```

**Notes:**
- SDK manages conversation within session
- Custom code needed for cross-session persistence
- Consider using MCP memory tool for long-term context

---

## 2. Exam Preparation System

### 2.1 File Processing (PDF, Images)

**V1 Requirement:** Extract text and analyze PDFs (assessment notifications)

**SDK Capability:** ✅ **Fully Supported**

**PDF Support:**
- Claude SDK supports PDF processing natively
- Can provide PDFs via:
  - URL reference
  - Base64-encoded data
  - Files API

**Implementation:**
```python
import anthropic
import base64

client = anthropic.Anthropic()

# Read PDF file
with open("./PHY-HSC-Assessment.pdf", "rb") as f:
    pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

# Send to Claude
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": pdf_data
                }
            },
            {
                "type": "text",
                "text": "Extract the exam topics, date, and assessment criteria from this notification."
            }
        ]
    }]
)
```

**Capabilities:**
- Full visual analysis of PDFs (charts, diagrams, equations)
- Text extraction included
- Max 100 pages, 32MB per request
- ~1,500-3,000 tokens per page

**Cost Considerations:**
- Use prompt caching for repeated analysis
- Consider batch processing for multiple documents

---

### 2.2 Custom Tools for Diagnostics

**V1 Requirement:** Generate questions, mark answers, track confidence

**SDK Capability:** ✅ **Fully Supported** (via Custom MCP Tools)

**Implementation:**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool(
    "generate_diagnostic_questions",
    "Generate diagnostic questions for a specific topic",
    {
        "topic": str,
        "difficulty": str,  # "easy", "medium", "hard"
        "count": int,
        "question_type": str  # "multiple_choice", "short_answer", "explanation"
    }
)
async def generate_diagnostic_questions(args):
    # Custom logic to generate questions
    questions = await generate_questions_logic(
        topic=args["topic"],
        difficulty=args["difficulty"],
        count=args["count"]
    )

    return {
        "content": [{
            "type": "text",
            "text": json.dumps(questions, indent=2)
        }]
    }

@tool(
    "save_quiz_result",
    "Save quiz results to database",
    {
        "topic": str,
        "question": str,
        "user_answer": str,
        "answer_is_correct": str,
        "confidence": int,  # 1-5
        "is_correct": bool
    }
)
async def save_quiz_result(args):
    # Save to database or JSON file
    result = await save_result_to_db(args)

    return {
        "content": [{
            "type": "text",
            "text": f"Result saved. Current understanding: {result['updated_score']}%"
        }]
    }

# Create MCP server with these tools
diagnostics_server = create_sdk_mcp_server(
    name="diagnostics-tools",
    version="1.0.0",
    tools=[generate_diagnostic_questions, save_quiz_result]
)
```

**Usage in Agent:**
```python
result = query(
    prompt="Start diagnostics quiz for Electric Potential",
    options=ClaudeAgentOptions(
        mcpServers={"diagnostics": diagnostics_server},
        allowedTools=[
            "mcp__diagnostics__generate_diagnostic_questions",
            "mcp__diagnostics__save_quiz_result"
        ]
    )
)
```

---

### 2.3 Resource Processing

**V1 Requirement:** Process curriculum docs, class materials, notes

**SDK Capability:** ✅ **Fully Supported**

**Built-in Tools:**
- `Read` - Read text files, PDFs
- `Glob` - Find files by pattern
- `Grep` - Search content in files
- `WebFetch` - Retrieve online resources

**Custom MCP Tools:**
```python
@tool(
    "index_study_resources",
    "Index all study resources for a subject",
    {"subject": str, "resource_type": str}
)
async def index_study_resources(args):
    resources = []
    base_path = f"./Resources/{args['subject']}/{args['resource_type']}"

    # Recursively find and index files
    for file in Path(base_path).rglob("*"):
        if file.is_file():
            resources.append({
                "path": str(file),
                "type": file.suffix,
                "size": file.stat().st_size
            })

    return {
        "content": [{
            "type": "text",
            "text": f"Indexed {len(resources)} resources:\n" +
                   json.dumps(resources, indent=2)
        }]
    }
```

---

### 2.4 Results Processing and Storage

**V1 Requirement:** Generate hierarchical performance profile

**SDK Capability:** 🔶 **Partially Supported**

**What SDK Provides:**
- Claude can generate structured JSON output
- File Write tool for saving results

**What Requires Custom Code:**
- Database schema design
- Query and aggregation logic
- Visualization generation

**Implementation:**
```python
@tool(
    "update_performance_data",
    "Update student performance for a topic",
    {
        "exam_name": str,
        "module": str,
        "topic": str,
        "conceptual_score": float,
        "functional_score": float,
        "incorrect_questions": list
    }
)
async def update_performance_data(args):
    # Load existing data
    data_file = f"./ExamPrep/{args['exam_name']}.json"

    if Path(data_file).exists():
        with open(data_file) as f:
            data = json.load(f)
    else:
        data = initialize_exam_data(args['exam_name'])

    # Update scores
    module_data = data['results'].setdefault(args['module'], {})
    topic_data = module_data.setdefault(args['topic'], {})

    topic_data['conceptual'] = args['conceptual_score']
    topic_data['functional'] = args['functional_score']
    topic_data['incorrect_questions'] = args['incorrect_questions']

    # Save updated data
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)

    return {
        "content": [{
            "type": "text",
            "text": f"Updated {args['topic']}: Con={args['conceptual_score']}%, Func={args['functional_score']}%"
        }]
    }
```

---

## 3. Studying System

### 3.1 Content Synthesis

**V1 Requirement:** Research and synthesize learning materials

**SDK Capability:** ✅ **Fully Supported**

**Tools Available:**
- `Read` - Access notes and resources
- `Grep` - Search for specific concepts
- `WebSearch` - Find external explanations
- `WebFetch` - Retrieve educational content

**Implementation Pattern:**
```python
# Claude automatically uses these tools when prompted:
prompt = """
Research the topic "Electric Potential" using:
1. Student notes in ./Study_Notes/
2. Class materials in ./Resources/Class_Materials/
3. External educational resources

Synthesize into a comprehensive explanation with:
- Core definition
- Key equations and their derivations
- Common misconceptions
- Practical examples
"""

# Claude will use Read, Grep, WebSearch automatically
result = query(prompt=prompt, options=options)
```

---

### 3.2 Practice Question Generation

**V1 Requirement:** Generate exam-style practice questions

**SDK Capability:** ✅ **Fully Supported**

**Approach 1: Direct Claude Generation**
```python
# Claude can generate questions directly
prompt = """
Based on the topic "Electric Potential", generate 5 exam-style questions:
- 2 multiple choice (4 options each)
- 2 short answer (2-3 marks)
- 1 extended response (5-6 marks)

Format as JSON with answers and marking criteria.
"""
```

**Approach 2: Custom Tool with Templates**
```python
@tool(
    "generate_practice_questions",
    "Generate practice questions using exam paper templates",
    {"topic": str, "similar_to": str, "count": int}
)
async def generate_practice_questions(args):
    # Load past paper questions for this topic
    past_questions = load_past_questions(args['topic'])

    # Generate similar questions using templates
    questions = generate_from_templates(
        templates=past_questions,
        target=args['similar_to'],
        count=args['count']
    )

    return {"content": [{"type": "text", "text": json.dumps(questions)}]}
```

---

### 3.3 Progress Tracking

**V1 Requirement:** Track scores and decide on topic repetition

**SDK Capability:** 🔶 **Partially Supported**

**What SDK Provides:**
- Claude can make decisions based on data
- Access to stored performance metrics via tools

**What Requires Custom Code:**
- Decision algorithm implementation
- Time management logic
- Performance prediction models

**Implementation:**
```python
@tool(
    "evaluate_study_progress",
    "Evaluate if student should continue or move to next topic",
    {
        "topic": str,
        "pre_study_conceptual": float,
        "post_study_conceptual": float,
        "pre_study_functional": float,
        "post_study_functional": float,
        "time_remaining_days": int,
        "exam_topics_remaining": int
    }
)
async def evaluate_study_progress(args):
    # Calculate improvement
    con_improvement = args['post_study_conceptual'] - args['pre_study_conceptual']
    func_improvement = args['post_study_functional'] - args['pre_study_functional']

    # Decision logic
    if con_improvement < 15 and func_improvement < 20:
        # Insufficient improvement
        time_per_topic = args['time_remaining_days'] / args['exam_topics_remaining']

        if time_per_topic > 2 and (args['post_study_conceptual'] < 70 or args['post_study_functional'] < 70):
            recommendation = "repeat"
            reason = "More time available and scores still below threshold"
        else:
            recommendation = "next"
            reason = "Limited time remaining, mark for later review"
    else:
        recommendation = "next"
        reason = "Sufficient improvement achieved"

    return {
        "content": [{
            "type": "text",
            "text": json.dumps({
                "recommendation": recommendation,
                "reason": reason,
                "improvements": {
                    "conceptual": con_improvement,
                    "functional": func_improvement
                }
            })
        }]
    }
```

---

## 4. Advanced SDK Features for StudyBrain

### 4.1 Hooks for Automation

**Use Case:** Auto-save session data, trigger notifications, run cleanup

**SDK Capability:** ✅ **Fully Supported**

**Example: Save Session After Each Response**
```json
// .claude/settings.json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "python ./scripts/save_session.py"
      }]
    }],
    "PostToolUse": [{
      "matcher": "mcp__diagnostics__save_quiz_result",
      "hooks": [{
        "type": "command",
        "command": "python ./scripts/update_progress_dashboard.py"
      }]
    }]
  }
}
```

**Available Hook Events:**
- `UserPromptSubmit` - Before processing user input
- `PreToolUse` - Before using any tool
- `PostToolUse` - After tool completes
- `Stop` - When agent finishes response
- `SessionStart` - When session begins
- `SessionEnd` - When session ends

---

### 4.2 Prompt Caching

**Use Case:** Cache curriculum documents, study materials for cost savings

**SDK Capability:** ✅ **Fully Supported**

**Implementation:**
```python
# Cache curriculum document
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": curriculum_pdf_base64
                },
                "cache_control": {"type": "ephemeral"}  # Cache this
            },
            {
                "type": "text",
                "text": "What topics are covered in Module 4?"
            }
        ]
    }]
)
```

**Cost Savings:**
- First request: Full token cost
- Subsequent requests: 10% cost for cached content
- Cache lasts 5 minutes

---

### 4.3 Subagents for Specialized Tasks

**Use Case:** Specialized agents for different study activities

**SDK Capability:** ✅ **Fully Supported**

**Example Architecture:**
```python
agents = {
    "question-generator": {
        "description": "Generates exam-style practice questions",
        "prompt": "You are an expert at creating HSC exam questions...",
        "tools": ["Read", "Grep"],
        "model": "sonnet"
    },
    "answer-evaluator": {
        "description": "Evaluates student answers and provides feedback",
        "prompt": "You are an experienced HSC marker...",
        "tools": ["Read"],
        "model": "opus"  # Use higher quality for marking
    },
    "study-planner": {
        "description": "Creates personalized study schedules",
        "prompt": "You are a study planning expert...",
        "tools": ["Read", "Write"],
        "model": "sonnet"
    }
}

# Claude automatically invokes appropriate subagent
result = query(
    prompt="Generate 5 questions on kinematics and mark my answers",
    options=ClaudeAgentOptions(agents=agents)
)
```

---

## 5. Implementation Feasibility Summary

| Feature | SDK Support | Implementation Effort | Notes |
|---------|-------------|----------------------|-------|
| CLI Interface | ✅ Full | Low | Simple wrapper script |
| Subject Agents | ✅ Full | Low | Use subagents or sessions |
| Session Management | 🔶 Partial | Medium | Custom persistence layer |
| PDF Processing | ✅ Full | Low | Native SDK support |
| Custom Tools | ✅ Full | Medium | MCP tool creation |
| Resource Indexing | ✅ Full | Low | Built-in Read/Glob/Grep |
| Performance Tracking | 🔶 Partial | Medium | Custom database + tools |
| Question Generation | ✅ Full | Low | Claude native capability |
| Answer Evaluation | ✅ Full | Low | Claude native capability |
| Progress Decisions | 🔶 Partial | Medium | Custom logic + Claude |
| Hooks/Automation | ✅ Full | Low | Built-in hook system |
| Cost Optimization | ✅ Full | Low | Prompt caching built-in |

---

## 6. Recommended Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    StudyBrain CLI                        │
│                 (Custom Python Script)                   │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
┌─────────────────┐         ┌─────────────────┐
│  Claude Agent   │         │   Custom MCP    │
│      SDK        │◄────────│    Servers      │
│                 │         │                 │
│  - Subagents    │         │  - Diagnostics  │
│  - Sessions     │         │  - Progress DB  │
│  - Hooks        │         │  - Resources    │
└────────┬────────┘         └─────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│         Storage Layer               │
│                                     │
│  - Session Data (JSON/SQLite)      │
│  - Exam Prep Results (JSON)        │
│  - Performance History (DB)        │
│  - Cached Resources                │
└─────────────────────────────────────┘
```

---

## 7. What You Need to Clarify

See `V1_Design_Questions.md` for specific questions about:
- Multi-agent coordination patterns
- GUI requirements
- Storage preferences
- Performance tracking algorithms
- Spaced repetition integration

---

## 8. Next Steps

1. **Answer design questions** to finalize requirements
2. **Create V2 design** incorporating SDK patterns
3. **Build prototype** of core loop (diagnostics → study → assessment)
4. **Test and iterate** with real study content

---

**End of Analysis**
