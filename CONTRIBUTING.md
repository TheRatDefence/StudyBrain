# Contributing to StudyBrain

Thank you for your interest in StudyBrain! This is primarily a personal educational project, but contributions are welcome.

---

## How to Contribute

### For Bug Fixes and Enhancements

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Follow the phase structure** - see which phase your contribution relates to
4. **Make your changes**
5. **Test thoroughly** - ensure existing phases still work
6. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
7. **Push to the branch** (`git push origin feature/AmazingFeature`)
8. **Open a Pull Request**

---

## Development Guidelines

### Code Style

- **Python:** Follow PEP 8
- **Docstrings:** Use Google-style docstrings
- **Comments:** Explain WHY, not WHAT
- **Naming:** Be descriptive and consistent

### Testing

- Write tests for new MCP tools
- Test agent interactions
- Validate with real HSC content
- Ensure all previous phases still work

### Documentation

- Update phase README if modifying a phase
- Add to ROADMAP.md if creating new features
- Document new MCP tools in V2_System_Architecture.md
- Keep PHASE_CONNECTIONS.md updated

---

## Phase-Based Development

StudyBrain follows a **10-phase agile approach**. When contributing:

1. **Identify which phase** your contribution affects
2. **Read the phase documentation** in the phase directory
3. **Check PHASE_CONNECTIONS.md** for dependencies
4. **Test integration** with previous phases

---

## Commit Message Format

```
<type>(<phase>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `style` - Code style changes
- `refactor` - Code refactoring
- `test` - Adding tests
- `chore` - Maintenance tasks

**Examples:**
```
feat(phase-2): Add multiple choice question support
fix(phase-3): Correct score calculation for partial credit
docs(roadmap): Update Phase 7 timeline estimates
```

---

## Pull Request Process

1. **Describe your changes** clearly in the PR description
2. **Reference any related issues** (e.g., "Fixes #123")
3. **Include test results** or screenshots if applicable
4. **Update documentation** as needed
5. **Wait for review** - I'll review as soon as possible

---

## Code Review Criteria

PRs will be reviewed for:

- **Correctness:** Does it work as intended?
- **Testing:** Are there tests? Do they pass?
- **Documentation:** Is it documented?
- **Phase Alignment:** Does it fit the phase structure?
- **HSC Relevance:** Is it useful for HSC study?
- **Code Quality:** Is it clean, readable, maintainable?

---

## What NOT to Contribute

- Changes that compromise data privacy
- Features unrelated to HSC study
- Breaking changes without discussion
- Code that doesn't follow the phase structure

---

## Questions?

- **General questions:** Open a GitHub issue
- **Design questions:** Reference Design/V2_System_Architecture.md
- **Phase questions:** Check the relevant phase README

---

## Recognition

Contributors will be acknowledged in:
- README.md (Contributors section)
- Relevant phase documentation
- Release notes

---

Thank you for helping make StudyBrain better! 🎓
