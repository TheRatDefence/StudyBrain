# StudyBrain - Development Plan

**Project Type:** AI-Powered HSC Study Management System
**Approach:** Agile, incremental development aligned with HSC Software Engineering curriculum
**Duration:** Year 12 (2026)
**Primary Use:** Year 12 HSC preparation + Software Engineering project

---

## Purpose & Vision

StudyBrain is both:
1. **A practical HSC study tool** - Manage 6 subjects, track progress, predict performance
2. **Your HSC Software Engineering project** - Demonstrates all Year 12 outcomes

**Key Principle:** Build features as you learn the technologies in class, creating a feedback loop between classroom learning and practical application.

---

## Current State (Foundation Complete)

### ✅ Implemented Features

**Flask Web Application:**
- Dashboard with 6 HSC subjects
- Study session page with AI chat
- Physics AI agent (working)
- Session conversation persistence
- Error handling
- Basic routing and templates

**Technology Stack:**
- Flask web framework
- Python 3.x
- Jinja2 templating
- Session management
- JSON file storage (temporary)

**File Structure:**
```
studybrain_web/
├── app.py                  # Main Flask application
├── agents/
│   └── subjects/
│       └── physics.py      # Physics AI agent
├── templates/
│   ├── dashboard.html      # Subject cards
│   ├── study_session.html  # AI chat interface
│   └── error.html          # Error handling
├── static/                 # CSS/JS/images
├── data/                   # JSON storage
└── requirements.txt        # Dependencies
```

---

## Development Roadmap

### Feature Domains (Not Sequential Phases)

The system is organized into **7 feature domains** that can be developed incrementally. Each domain contains multiple features that build upon each other.

---

## Domain 1: Performance Tracking (PRIORITY 1)

**Purpose:** Track real assessment performance alongside predicted performance

### Features to Implement

**1.1 Assessment Marks Tracking**
- Add new assessment results (task, exam, practical)
- Edit/delete assessments
- View marks history per subject
- Calculate statistics (average, trend, efficiency)

**1.2 Study Time Logging**
- Log study session duration and topics
- Track total study hours per subject
- Calculate marks-per-hour efficiency
- View study session history

**1.3 Performance Analysis**
- Compare predicted (Con/Func scores) vs actual (marks)
- Identify overconfidence/underconfidence patterns
- Generate performance insights
- Trend detection (improving/declining/stable)

**Technology Progression:**
- **Stage 1 (Now):** JSON file storage
- **Stage 2 (Term 2):** SQLite database with sqlite3 module
- **Stage 3 (Mid Year):** JavaScript for interactivity
- **Stage 4 (Later):** ML predictions

**HSC Curriculum Alignment:**
- Programming for the Web (SQL, databases)
- Secure Software Architecture (data validation, security)
- Software Engineering Project (project component)

**Templates Needed:**
- `marks_dashboard.html` - Overview of all subjects
- `marks_subject.html` - Detailed marks for one subject
- `marks_form.html` - Add/edit assessment
- `study_session_form.html` - Log study time
- `performance_comparison.html` - Con/Func vs actual

**Routes Needed:**
```
/marks                              # Dashboard
/marks/<subject>                    # Subject detail
/marks/<subject>/add                # Add assessment
/marks/<subject>/edit/<id>          # Edit assessment
/marks/<subject>/delete/<id>        # Delete assessment
/marks/<subject>/study-session/add  # Log study
/api/marks/<subject>/stats          # JSON API (for JS)
```

---

## Domain 2: AI Study System (CORE)

**Purpose:** Interactive AI tutor for all 6 HSC subjects

### Features to Implement

**2.1 Subject Agents**
- ✅ Physics agent (complete)
- Mathematics Extension 1 agent
- Mathematics Advanced agent
- Software Engineering agent
- Music agent
- English Standard agent

**2.2 Question Generation & Quizzing**
- Generate practice questions (multiple-choice, short answer)
- Submit answers and get feedback
- Confidence slider (how confident are you?)
- Save quiz results to progress data

**2.3 Intelligent Sub-Agents**
- Curriculum Expert (HSC syllabus knowledge)
- Question Generator (HSC-style questions)
- Answer Evaluator (mark and provide feedback)
- Progress Tracker (update Con/Func scores)

**2.4 Study Session Management**
- Timer for study sessions
- Session persistence (resume capability)
- Session history and analytics
- Learning rate calculation

**Technology Stack:**
- Claude SDK (already using)
- MCP tools for custom functions
- Agent-to-agent communication
- JSON for data persistence

**HSC Curriculum Alignment:**
- Object-Oriented Programming (agents as objects)
- Software Automation (AI/ML concepts)
- Secure Software Architecture (API security)

---

## Domain 3: Progress & Metrics (ANALYTICAL)

**Purpose:** Track conceptual understanding and functional performance

### Features to Implement

**3.1 Conceptual & Functional Scores**
- Con score: Understanding depth (0-100%)
- Func score: Exam performance ability (0-100%)
- Track by subject → module → topic → subtopic
- Update based on quiz performance

**3.2 FSRS Spaced Repetition**
- Integrate py-fsrs library
- Schedule topic reviews based on forgetting curve
- "Topics Due for Review" widget
- Optimal study scheduling

**3.3 Progress Visualization**
- Progress timeline (score over time)
- Radar chart (subject comparison)
- Topic heatmap (weak areas highlighted)
- Study time vs performance correlation

**3.4 Analytics Dashboard**
- Study patterns (best time of day, session length)
- Subject prioritization recommendations
- Exam readiness calculator
- Performance predictions

**Technology Progression:**
- **Stage 1:** JSON storage, manual calculations
- **Stage 2:** SQLite with SQL queries for analytics
- **Stage 3:** JavaScript charts (Chart.js, Plotly)
- **Stage 4:** ML-based predictions (scikit-learn)

**HSC Curriculum Alignment:**
- Software Automation (ML predictions)
- Programming for the Web (data visualization)
- Software Engineering Project (analytics features)

---

## Domain 4: Database & Storage (INFRASTRUCTURE)

**Purpose:** Persistent, secure data storage aligned with HSC SQL curriculum

### Migration Path

**Stage 1: JSON Files (Current)**
- Simple file-based storage
- Quick to implement
- Easy to debug
- Good for initial development

**Stage 2: SQLite Database (Term 2 - When Learning SQL)**
- Migrate all JSON to SQLite
- Create proper database schema
- Use sqlite3 module (Python standard library)
- Write SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Implement table joins

**Stage 3: Advanced SQL (Mid Year)**
- Database views for statistics
- Triggers for automatic calculations
- Indexes for performance
- Backup and recovery

**Database Schema (Future):**
```sql
-- Core tables
subjects
assessments
assessment_topics
study_sessions
quiz_results
progress_tracking
fsrs_cards
resources

-- Views for analytics
subject_statistics
performance_trends
study_efficiency
```

**HSC Curriculum Alignment:**
- **Programming for the Web** (SQL databases - MANDATORY)
- Table joins, GROUP BY, WHERE clauses
- Compare ORM vs SQL
- Data security and integrity

**Data to Store:**
- Assessment marks and metadata
- Study session logs
- Quiz results and confidence
- Progress scores (Con/Func)
- FSRS scheduling data
- Resource index
- Cross-subject concept mappings

---

## Domain 5: Web Interface (USER EXPERIENCE)

**Purpose:** Professional, responsive web interface with modern UX

### Features to Implement

**5.1 Enhanced UI Design**
- Responsive layout (mobile + desktop)
- Professional styling (CSS frameworks)
- Consistent design system
- Accessibility (WCAG standards)

**5.2 Interactive Features (JavaScript)**
- Auto-calculate percentages in forms
- Form validation (client-side)
- Interactive charts (Chart.js)
- AJAX form submissions (no page reload)
- Real-time updates
- Progress animations

**5.3 Progressive Web App (PWA)**
- Offline capability (service workers)
- Installable (add to home screen)
- Fast loading (caching)
- Push notifications for study reminders

**5.4 Advanced Visualizations**
- LaTeX/MathJax for equations
- Interactive graphs (Plotly)
- Timeline visualizations
- Topic relationship diagrams

**Technology Progression:**
- **Stage 1 (Current):** Basic HTML/CSS
- **Stage 2 (Term 2):** Enhanced CSS, responsive design
- **Stage 3 (Mid Year):** JavaScript interactivity
- **Stage 4 (Later):** PWA features

**HSC Curriculum Alignment:**
- **Programming for the Web** (HTML, CSS, JavaScript - MANDATORY)
- PWA development (curriculum requirement)
- UI/UX principles (font, color, navigation)
- Accessibility and inclusivity

**JavaScript Examples:**
- Percentage auto-calculation
- Chart rendering
- Form validation
- AJAX requests
- DOM manipulation
- Event handling

---

## Domain 6: Security & Quality (PROFESSIONAL)

**Purpose:** Secure, maintainable code following industry best practices

### Features to Implement

**6.1 Security Features**
- User authentication (Flask-Login)
- Password hashing (bcrypt)
- CSRF protection (Flask-WTF)
- Input validation and sanitization
- Secure session management
- Data encryption for sensitive info

**6.2 Testing & Quality Assurance**
- Unit tests (pytest)
- Integration tests
- Black box testing
- White box testing
- Code review process
- Automated testing

**6.3 Documentation**
- Code docstrings
- API documentation
- User manual
- Installation guide
- Development journal
- Project report (HSC requirement)

**6.4 Version Control & Collaboration**
- Git branching strategy
- Commit message standards
- GitHub Issues for tracking
- Pull request workflow
- Code review checklist

**HSC Curriculum Alignment:**
- **Secure Software Architecture** (30 hours - MANDATORY)
- XSS/CSRF prevention
- Input validation
- Security testing (SAST, DAST)
- Privacy by design
- Testing methodologies

**Security Checklist:**
- [ ] All inputs validated
- [ ] Passwords hashed
- [ ] CSRF tokens on forms
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] Secure session handling
- [ ] Error handling (no sensitive data leaked)

---

## Domain 7: Intelligence & Automation (ADVANCED)

**Purpose:** ML-powered predictions and recommendations

### Features to Implement

**7.1 Performance Prediction**
- Predict next exam mark based on:
  - Study hours invested
  - Quiz performance (Con/Func scores)
  - Historical assessment results
- Use linear regression (scikit-learn)

**7.2 Study Recommendations**
- Which subject to study next?
- Optimal study duration
- Best time of day (based on patterns)
- Topic prioritization

**7.3 Pattern Recognition**
- Identify effective study patterns
- Cluster study sessions by effectiveness
- Detect learning plateaus
- Suggest improvements

**7.4 Cross-Subject Insights**
- Identify related concepts across subjects
- Suggest cross-subject study paths
- Optimize overall study schedule
- Exam priority calculator

**Technology Stack:**
- **scikit-learn:** Linear/logistic regression, K-nearest neighbors
- **TensorFlow/Keras:** Neural networks (optional, advanced)
- **NumPy/Pandas:** Data manipulation
- **Matplotlib:** Data visualization

**HSC Curriculum Alignment:**
- **Software Automation** (30 hours - MANDATORY)
- ML algorithms (regression, classification)
- Neural networks
- Impact of AI/ML on society
- Bias in ML systems

**ML Features:**
```python
# Example: Predict exam mark
predict_exam_mark(subject, study_hours, con_score, func_score)

# Example: Recommend study subject
recommend_study_subject(days_until_exams, current_performance)

# Example: Analyze study patterns
analyze_study_effectiveness(session_history)
```

---

## Technology Learning Progression

### Term 4 (2025) - Foundation
- **Focus:** Python, Flask, JSON storage
- **Learn:** Web routing, templates, basic forms
- **Build:** Marks tracking (JSON version)
- **Outcome:** Working marks tracker + AI tutor

### Term 1 (2026) - Databases
- **Focus:** SQL, SQLite, sqlite3 module
- **Learn:** Database design, SQL queries, table joins
- **Build:** Migrate marks tracking to SQLite
- **Outcome:** Relational database with SQL queries
- **HSC Topic:** Programming for the Web (SQL)

### Term 2 (2026) - Interactivity
- **Focus:** JavaScript, DOM manipulation, AJAX
- **Learn:** Client-side programming, event handling
- **Build:** Interactive forms, charts, real-time updates
- **Outcome:** Dynamic web application
- **HSC Topic:** Programming for the Web (JavaScript, PWA)

### Term 3 (2026) - Security & Testing
- **Focus:** Security, testing, quality assurance
- **Learn:** Input validation, XSS/CSRF, unit testing
- **Build:** Secure authentication, comprehensive tests
- **Outcome:** Production-ready security
- **HSC Topic:** Secure Software Architecture

### Term 4 (2026) - Machine Learning
- **Focus:** ML, predictions, automation
- **Learn:** Regression, classification, neural networks
- **Build:** Performance predictions, study recommendations
- **Outcome:** AI-powered study system
- **HSC Topic:** Software Automation

---

## Development Approach

### Agile Methodology (Already Using!)

**Sprint Structure:**
- **Duration:** 1-2 weeks per sprint
- **Deliverable:** Working feature increment
- **Review:** Test and evaluate after each sprint
- **Adapt:** Refine based on feedback

**Current Sprint Planning:**
1. Plan feature(s) to implement
2. Design and code
3. Test thoroughly
4. Document changes
5. Commit to Git
6. Review and reflect

### Waterfall Elements (Hybrid - WAgile)

**Upfront Planning:**
- Overall system architecture (DESIGN.md)
- Database schema (planned for SQL migration)
- Security requirements (defined early)

**Why Hybrid?**
- **Waterfall:** Clear requirements, structured documentation (HSC requirement)
- **Agile:** Flexible features, iterative development (practical for learning)

### Project Management

**Tools:**
- **Git/GitHub:** Version control, code review
- **GitHub Issues:** Task tracking, bug reports
- **PyCharm TODO:** Implementation tasks in code
- **Markdown Docs:** Planning, documentation

**Documentation:**
- `README.md` - Project overview
- `DESIGN.md` - Technical architecture
- `DEVELOPMENT_PLAN.md` - This file
- `Year_12_Learning_Objectives.md` - HSC curriculum tracking
- `Year_12_Teaching_Guide.md` - Technology reference

---

## Implementation Priority

### Priority 1: Marks Tracking (NOW)
**Reason:** You're getting Year 11 results now, need to track them
**Duration:** 1-2 weeks
**Technology:** JSON → SQLite (later)
**Features:**
- Add/edit/delete assessments
- Log study hours
- View statistics
- Compare with Con/Func scores

### Priority 2: Multi-Subject AI (SOON)
**Reason:** Need all 6 subjects working for Year 12
**Duration:** 1 week
**Technology:** Python, Claude SDK
**Features:**
- 5 additional subject agents
- Quiz system for all subjects
- Progress tracking per subject

### Priority 3: SQL Migration (TERM 1 2026)
**Reason:** Learning SQL in class, practical application
**Duration:** 2 weeks
**Technology:** SQLite, sqlite3
**Features:**
- Database schema implementation
- JSON → SQL migration
- SQL queries for analytics
- Table joins for reporting

### Priority 4: JavaScript UI (TERM 2 2026)
**Reason:** Learning JavaScript in class
**Duration:** 2-3 weeks
**Technology:** JavaScript, Chart.js
**Features:**
- Interactive forms
- Data visualization
- AJAX requests
- PWA features

### Priority 5: Security (TERM 3 2026)
**Reason:** HSC requirement, secure data
**Duration:** 2 weeks
**Technology:** Flask-Login, bcrypt, Flask-WTF
**Features:**
- User authentication
- Input validation
- CSRF protection
- Security testing

### Priority 6: Machine Learning (TERM 4 2026)
**Reason:** HSC requirement, advanced features
**Duration:** 3 weeks
**Technology:** scikit-learn, TensorFlow
**Features:**
- Performance predictions
- Study recommendations
- Pattern recognition

---

## File Organization

### Simplified Structure (No Phase Directories)

```
StudyBrain/
├── studybrain_web/              # Main application
│   ├── app.py                   # Flask application
│   ├── requirements.txt         # Dependencies
│   │
│   ├── agents/                  # AI agents
│   │   ├── coordinator.py       # Study coordinator
│   │   ├── subjects/            # Subject-specific agents
│   │   │   ├── physics.py
│   │   │   ├── mathematics_ext1.py
│   │   │   ├── mathematics_adv.py
│   │   │   ├── software_engineering.py
│   │   │   ├── music.py
│   │   │   └── english.py
│   │   └── subagents/           # Specialized sub-agents
│   │       ├── curriculum_expert.py
│   │       ├── question_generator.py
│   │       ├── answer_evaluator.py
│   │       └── progress_tracker.py
│   │
│   ├── routes/                  # Flask routes
│   │   ├── dashboard.py
│   │   ├── study.py
│   │   ├── marks.py             # Marks tracking routes
│   │   ├── progress.py
│   │   └── api.py               # JSON API endpoints
│   │
│   ├── services/                # Business logic
│   │   ├── marks_manager.py     # Marks CRUD operations
│   │   ├── progress_calculator.py
│   │   ├── fsrs_scheduler.py
│   │   ├── session_manager.py
│   │   └── ml_predictor.py      # ML predictions
│   │
│   ├── mcp_tools/               # Custom MCP tools
│   │   ├── diagnostics.py       # Quiz generation
│   │   ├── progress.py          # Progress tracking
│   │   ├── fsrs_integration.py
│   │   ├── study_timer.py
│   │   └── resources.py
│   │
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── dashboard.html
│   │   ├── study_session.html
│   │   ├── marks_dashboard.html
│   │   ├── marks_subject.html
│   │   ├── marks_form.html
│   │   ├── progress.html
│   │   └── error.html
│   │
│   ├── static/                  # CSS, JS, images
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   └── marks.css
│   │   ├── js/
│   │   │   ├── charts.js
│   │   │   ├── forms.js
│   │   │   └── marks.js
│   │   └── images/
│   │
│   ├── data/                    # Data storage
│   │   ├── marks/               # JSON (temp) or SQLite DB here
│   │   │   ├── studybrain.db    # SQLite database (future)
│   │   │   └── *.json           # JSON files (current)
│   │   ├── progress/
│   │   ├── sessions/
│   │   ├── quiz_results/
│   │   └── resources/
│   │
│   └── tests/                   # Unit tests
│       ├── test_marks_manager.py
│       ├── test_progress.py
│       └── test_ml_predictions.py
│
├── Resources/                   # Reference materials
│   ├── Year_12_Learning_Objectives.md
│   ├── Year_12_Teaching_Guide.md
│   ├── Yr11-12_Software_Engineering_Curriculum_NESA.md
│   └── TEMP_Research_Findings.md
│
├── Design/                      # Design diagrams and mockups
│   └── ExamplePhysicsUsageV1/
│
├── CLAUDE_DOCS/                 # Claude API documentation
│
├── README.md                    # Project overview
├── DESIGN.md                    # Technical architecture
├── DEVELOPMENT_PLAN.md          # This file
├── ROADMAP.md                   # Old roadmap (replaced by this)
├── CLAUDE.md                    # Teaching methodology
├── .gitignore
└── LICENSE
```

---

## HSC Project Requirements

### Assessment Component (30% of Year 12 mark)

**Required Deliverables:**

**1. Project Documentation:**
- Requirements specification
- Design documentation (architecture, database schema, UI mockups)
- User manual
- Test plan and results
- Project report (development process, challenges, evaluation)

**2. Working Software:**
- Functional web application
- Demonstrates all Year 12 outcomes
- Secure, tested, documented code

**3. Presentation:**
- 15-minute presentation
- Live demonstration
- Technical discussion
- Q&A

**4. Code Quality:**
- Version control history (Git)
- Code comments and docstrings
- Consistent style
- Testing evidence

### HSC Outcomes Demonstrated

**SE-12-01:** Project management (Agile/Waterfall/WAgile)
**SE-12-02:** Code structure (functions, classes, modules)
**SE-12-03:** Technology analysis (Flask, SQLite, JavaScript, ML)
**SE-12-04:** Data security (validation, encryption, CSRF)
**SE-12-05:** Social/ethical implications (AI in education, data privacy)
**SE-12-06:** Tools and resources (Git, PyCharm, libraries)
**SE-12-07:** Secure code implementation (all security features)
**SE-12-08:** Code testing and refinement (unit tests, debugging)
**SE-12-09:** Documentation (comprehensive project docs)

---

## Success Metrics

### Technical Metrics
- [ ] All 6 subjects have working AI agents
- [ ] All assessment marks tracked in database
- [ ] SQL queries working correctly (joins, GROUP BY, WHERE)
- [ ] JavaScript features working (charts, AJAX, validation)
- [ ] Security features implemented (auth, CSRF, validation)
- [ ] ML predictions functional (marks prediction, recommendations)
- [ ] PWA features working (offline, installable)
- [ ] All tests passing (unit, integration, system)

### Educational Metrics
- [ ] All Year 12 HSC outcomes demonstrated
- [ ] SQL skills mastered (can write complex queries)
- [ ] JavaScript proficiency (can build interactive UIs)
- [ ] Security awareness (understand common vulnerabilities)
- [ ] ML fundamentals (understand regression, classification)
- [ ] Project management experience (Agile, documentation)

### Personal Metrics
- [ ] Actually using StudyBrain for HSC study
- [ ] Marks tracking helping identify weak areas
- [ ] ML predictions accurate (within 10% of actual marks)
- [ ] Study recommendations effective (better results)
- [ ] System saves time (faster than manual tracking)
- [ ] Confidence improved (better exam preparation)

---

## Next Steps (Immediate Actions)

### Week 1: Marks Tracking Foundation
1. Create `marks_manager.py` service class
2. Design JSON schema for marks storage
3. Create Flask routes for marks CRUD
4. Build HTML templates (dashboard, subject, form)
5. Test with Physics marks data

### Week 2: Multi-Subject Expansion
1. Implement 5 additional subject agents
2. Update dashboard for all subjects
3. Create progress tracking for all subjects
4. Test end-to-end workflow

### Week 3: Polish & Documentation
1. Improve UI styling
2. Add error handling
3. Write initial documentation
4. Create user manual draft
5. Set up testing framework

### Term 1 2026: SQL Migration
1. Learn SQL in class
2. Design database schema
3. Create migration script (JSON → SQLite)
4. Rewrite `marks_manager.py` to use SQL
5. Test thoroughly

### Beyond
- Continue following Technology Learning Progression
- Align new features with classroom learning
- Document everything for HSC project
- Regular testing and refinement

---

## Flexibility & Adaptation

**This plan is a guide, not a rigid schedule.**

As you progress:
- Features may be added, removed, or reprioritized
- Technologies may change based on classroom learning
- Implementation details will be refined iteratively
- Timeline will adjust to your learning pace

**Key Principle:** Always have a working system. Build incrementally, test frequently, document thoroughly.

---

## Questions to Answer as You Build

**For each feature:**
1. What problem does this solve?
2. How does it help with HSC study?
3. Which HSC outcome does it demonstrate?
4. What technology will I learn?
5. How will I test it?
6. What could go wrong (security, bugs)?

**For the overall project:**
1. Is this the best approach? Why?
2. What alternatives did I consider?
3. How does this compare to existing solutions?
4. What would I do differently next time?

---

**Ready to build? Start with Domain 1: Performance Tracking (Marks Tracker)**

See `Year_12_Teaching_Guide.md` for technology examples and teaching methodology.
