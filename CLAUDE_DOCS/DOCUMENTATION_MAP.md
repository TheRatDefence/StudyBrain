# Claude Documentation Map

**Purpose**: This map helps AI agents quickly locate relevant documentation files based on information needs.
**Location**: `/Users/james/Desktop/School/Year-12/claude-mastery-course/CLAUDE_DOCS/`
**Last Updated**: 2025-09-30
**Total Files**: 145 markdown files across 3 main guides

---

## 🗺️ Quick Navigation by Topic

### When you need information about...

**Basic Claude Usage & Getting Started**
→ Read: `Developer-Guide/01-First-Steps/intro.md`
→ Read: `Developer-Guide/01-First-Steps/get-started.md`

**Claude Models & Pricing**
→ Read: `Developer-Guide/02-Models-Pricing/overview.md`
→ Read: `Developer-Guide/02-Models-Pricing/choosing-a-model.md`
→ Read: `Developer-Guide/02-Models-Pricing/pricing.md`

**API Usage & Integration**
→ Read: `API-Guide/01-Using-APIs/overview.md`
→ Read: `API-Guide/01-Using-APIs/rate-limits.md`
→ Read: `API-Guide/02-API-Reference-Messages/messages.md`

**Claude Code CLI & Installation**
→ Read: `Claude-Code/01-Getting-Started/overview.md`
→ Read: `Claude-Code/01-Getting-Started/quickstart.md`
→ Read: `Claude-Code/08-Reference/cli-reference.md`

**Prompt Engineering Techniques**
→ Read: `Developer-Guide/07-Prompt-Engineering/overview.md`
→ Read: `Developer-Guide/07-Prompt-Engineering/claude-4-best-practices.md`

**Tool Use & Function Calling**
→ Read: `Developer-Guide/05-Tools/overview.md`
→ Read: `Developer-Guide/05-Tools/implement-tool-use.md`

**Agent SDK Development**
→ Read: `API-Guide/05-Agent-SDK/overview.md`
→ Read: `API-Guide/05-Agent-SDK/typescript.md` or `python.md`

**MCP (Model Context Protocol)**
→ Read: `Developer-Guide/05-Tools/mcp.md`
→ Read: `Claude-Code/02-Build-With-Claude-Code/mcp.md`
→ Read: `API-Guide/05-Agent-SDK/mcp.md`

**Claude Code Configuration**
→ Read: `Claude-Code/07-Configuration/settings.md`
→ Read: `Claude-Code/07-Configuration/visual-studio-code.md`
→ Read: `Claude-Code/07-Configuration/jetbrains-ides.md`

**Deployment & Production**
→ Read: `Claude-Code/05-Deployment/overview.md`
→ Read: `Claude-Code/06-Administration/security.md`

---

## 📚 Complete Directory Structure

```
CLAUDE_DOCS/
├── Developer-Guide/               # General Claude usage, capabilities, prompt engineering
│   ├── 01-First-Steps/           # Getting started with Claude
│   │   ├── intro.md
│   │   └── get-started.md
│   │
│   ├── 02-Models-Pricing/        # Model selection, capabilities, costs
│   │   ├── overview.md
│   │   ├── choosing-a-model.md
│   │   ├── whats-new-sonnet-4-5.md
│   │   ├── migrating-to-claude-4.md
│   │   ├── model-deprecations.md
│   │   └── pricing.md
│   │
│   ├── 03-Learn-About-Claude/    # Core concepts and features
│   │   ├── overview.md           # Main features overview
│   │   ├── context-windows.md
│   │   └── glossary.md
│   │
│   ├── 04-Capabilities/          # Claude's built-in features
│   │   ├── prompt-caching.md
│   │   ├── context-editing.md
│   │   ├── extended-thinking.md
│   │   ├── streaming.md
│   │   ├── batch-processing.md
│   │   ├── citations.md
│   │   ├── multilingual-support.md
│   │   ├── token-counting.md
│   │   ├── embeddings.md
│   │   ├── vision.md
│   │   ├── pdf-support.md
│   │   ├── files.md
│   │   ├── search-results.md
│   │   ├── claude-for-sheets.md
│   │   └── text-generation.md
│   │
│   ├── 05-Tools/                 # Tool use, MCP, function calling
│   │   ├── overview.md
│   │   ├── implement-tool-use.md
│   │   ├── token-efficient-tool-use.md
│   │   ├── fine-grained-tool-streaming.md
│   │   ├── bash-tool.md
│   │   ├── code-execution-tool.md
│   │   ├── computer-use-tool.md
│   │   ├── text-editor-tool.md
│   │   ├── web-fetch-tool.md
│   │   ├── web-search-tool.md
│   │   ├── memory-tool.md
│   │   ├── mcp.md                # Model Context Protocol
│   │   ├── mcp-connector.md
│   │   └── remote-mcp-servers.md
│   │
│   ├── 06-Use-Cases/             # Example applications and implementations
│   │   ├── overview.md
│   │   ├── ticket-routing.md
│   │   ├── customer-support-chat.md
│   │   ├── content-moderation.md
│   │   └── legal-summarization.md
│   │
│   ├── 07-Prompt-Engineering/    # How to write effective prompts
│   │   ├── overview.md
│   │   ├── claude-4-best-practices.md
│   │   ├── prompt-generator.md
│   │   ├── prompt-templates-and-variables.md
│   │   ├── prompt-improver.md
│   │   ├── be-clear-and-direct.md
│   │   ├── multishot-prompting.md
│   │   ├── chain-of-thought.md
│   │   ├── use-xml-tags.md
│   │   ├── system-prompts.md
│   │   ├── prefill-claudes-response.md
│   │   ├── chain-prompts.md
│   │   ├── long-context-tips.md
│   │   └── extended-thinking-tips.md
│   │
│   ├── 08-Test-Evaluate/         # Testing, evaluation, and optimization
│   │   ├── define-success.md
│   │   ├── develop-tests.md
│   │   ├── eval-tool.md
│   │   ├── reduce-latency.md
│   │   ├── reduce-hallucinations.md
│   │   ├── increase-consistency.md
│   │   ├── mitigate-jailbreaks.md
│   │   ├── handle-streaming-refusals.md
│   │   ├── reduce-prompt-leak.md
│   │   └── keep-claude-in-character.md
│   │
│   └── 09-Legal/                 # Legal, privacy, compliance
│       ├── privacy-policy.md
│       └── security-and-compliance.md
│
├── API-Guide/                     # API usage, SDKs, programmatic access
│   ├── 01-Using-APIs/            # API basics and configuration
│   │   ├── overview.md
│   │   ├── rate-limits.md
│   │   ├── service-tiers.md
│   │   ├── errors.md
│   │   ├── handling-stop-reasons.md
│   │   └── beta-headers.md
│   │
│   ├── 02-API-Reference-Messages/ # Messages API (primary API)
│   │   ├── messages.md
│   │   ├── messages-examples.md
│   │   └── messages-batch-examples.md
│   │
│   ├── 03-Admin-API/             # Administrative and usage APIs
│   │   ├── administration-api.md
│   │   ├── usage-cost-api.md
│   │   └── claude-code-analytics-api.md
│   │
│   ├── 04-SDKs/                  # Client libraries
│   │   ├── client-sdks.md
│   │   └── openai-sdk.md
│   │
│   ├── 05-Agent-SDK/             # Building agents with Claude
│   │   ├── overview.md
│   │   ├── migration-guide.md
│   │   ├── typescript.md
│   │   ├── python.md
│   │   ├── streaming-input.md
│   │   ├── handling-permissions.md
│   │   ├── session-management.md
│   │   ├── modifying-system-prompts.md
│   │   ├── mcp.md
│   │   ├── custom-tools.md
│   │   ├── subagents.md
│   │   ├── slash-commands.md
│   │   ├── tracking-costs.md
│   │   └── todo-lists.md
│   │
│   ├── 06-Third-Party-APIs/      # Using Claude on other platforms
│   │   ├── claude-on-amazon-bedrock.md
│   │   └── claude-on-vertex-ai.md
│   │
│   ├── 07-Legacy/                # Deprecated APIs
│   │   └── migrating-from-text-completions.md
│   │
│   └── 08-Support-Config/        # Configuration and support
│       ├── versioning.md
│       ├── ip-addresses.md
│       ├── supported-regions.md
│       └── getting-help.md
│
└── Claude-Code/                   # Claude Code CLI tool (programming assistant)
    ├── 01-Getting-Started/        # Installation and basic usage
    │   ├── overview.md
    │   ├── quickstart.md
    │   └── common-workflows.md
    │
    ├── 02-Build-With-Claude-Code/ # Advanced features
    │   ├── subagents.md
    │   ├── output-styles.md
    │   ├── hooks.md
    │   ├── headless.md
    │   ├── github-actions.md
    │   ├── gitlab-ci-cd.md
    │   └── mcp.md
    │
    ├── 03-Troubleshooting/        # Common issues and solutions
    │   └── troubleshooting.md
    │
    ├── 04-SDK/                    # SDK information
    │   └── migration-guide.md
    │
    ├── 05-Deployment/             # Production deployment
    │   ├── overview.md
    │   ├── amazon-bedrock.md
    │   ├── google-vertex-ai.md
    │   ├── network-configuration.md
    │   ├── llm-gateway.md
    │   └── development-containers.md
    │
    ├── 06-Administration/         # Admin tasks
    │   ├── advanced-installation.md
    │   ├── identity-and-access-management.md
    │   ├── security.md
    │   ├── data-usage.md
    │   ├── monitoring.md
    │   ├── costs.md
    │   └── analytics.md
    │
    ├── 07-Configuration/          # Settings and customization
    │   ├── settings.md
    │   ├── visual-studio-code.md
    │   ├── jetbrains-ides.md
    │   ├── terminal-configuration.md
    │   ├── model-configuration.md
    │   ├── memory-management.md
    │   └── status-line-configuration.md
    │
    ├── 08-Reference/              # Technical reference
    │   ├── cli-reference.md
    │   ├── interactive-mode.md
    │   ├── slash-commands.md
    │   ├── checkpointing.md
    │   └── hooks-reference.md
    │
    └── 09-Resources/              # Additional resources
        └── legal-and-compliance.md
```

---

## 🎯 Task-Based File Lookup

### Task: "Build an AI agent that can use tools"
**Read in order**:
1. `Developer-Guide/05-Tools/overview.md` - Understand tool use
2. `Developer-Guide/05-Tools/implement-tool-use.md` - Implementation guide
3. `API-Guide/05-Agent-SDK/overview.md` - Agent SDK concepts
4. `API-Guide/05-Agent-SDK/python.md` or `typescript.md` - Language-specific implementation
5. `API-Guide/05-Agent-SDK/custom-tools.md` - Creating custom tools

### Task: "Set up Claude Code CLI"
**Read in order**:
1. `Claude-Code/01-Getting-Started/overview.md` - What is Claude Code
2. `Claude-Code/01-Getting-Started/quickstart.md` - Installation steps
3. `Claude-Code/07-Configuration/settings.md` - Configure settings
4. `Claude-Code/07-Configuration/visual-studio-code.md` or `jetbrains-ides.md` - IDE-specific setup

### Task: "Optimize prompts for better responses"
**Read in order**:
1. `Developer-Guide/07-Prompt-Engineering/overview.md` - Core concepts
2. `Developer-Guide/07-Prompt-Engineering/claude-4-best-practices.md` - Latest best practices
3. `Developer-Guide/07-Prompt-Engineering/be-clear-and-direct.md` - Clear communication
4. `Developer-Guide/07-Prompt-Engineering/use-xml-tags.md` - Structure with XML
5. `Developer-Guide/07-Prompt-Engineering/chain-of-thought.md` - Reasoning techniques

### Task: "Integrate Claude API into application"
**Read in order**:
1. `API-Guide/01-Using-APIs/overview.md` - API basics
2. `API-Guide/04-SDKs/client-sdks.md` - Available SDKs
3. `API-Guide/02-API-Reference-Messages/messages.md` - Messages API reference
4. `API-Guide/01-Using-APIs/rate-limits.md` - Rate limiting
5. `API-Guide/01-Using-APIs/errors.md` - Error handling

### Task: "Use MCP (Model Context Protocol)"
**Read in order**:
1. `Developer-Guide/05-Tools/mcp.md` - MCP overview
2. `Claude-Code/02-Build-With-Claude-Code/mcp.md` - MCP in Claude Code
3. `API-Guide/05-Agent-SDK/mcp.md` - MCP in Agent SDK
4. `Developer-Guide/05-Tools/mcp-connector.md` - MCP connector usage

### Task: "Deploy Claude Code to production"
**Read in order**:
1. `Claude-Code/05-Deployment/overview.md` - Deployment concepts
2. `Claude-Code/06-Administration/security.md` - Security considerations
3. `Claude-Code/05-Deployment/network-configuration.md` - Network setup
4. `Claude-Code/06-Administration/monitoring.md` - Monitoring in production

### Task: "Reduce costs and optimize usage"
**Read in order**:
1. `Developer-Guide/02-Models-Pricing/choosing-a-model.md` - Choose right model
2. `Developer-Guide/04-Capabilities/prompt-caching.md` - Use prompt caching
3. `Developer-Guide/05-Tools/token-efficient-tool-use.md` - Efficient tool patterns
4. `API-Guide/03-Admin-API/usage-cost-api.md` - Track usage
5. `Claude-Code/06-Administration/costs.md` - Monitor Claude Code costs

---

## 🔍 Search Patterns for AI Agents

When you need information about a topic, use these glob patterns:

### Finding Configuration Info
```bash
# Find all configuration-related files
glob: "Claude-Code/07-Configuration/*.md"

# Find IDE-specific configs
glob: "Claude-Code/07-Configuration/*ide*.md"
```

### Finding Tool Documentation
```bash
# All tool use docs
glob: "Developer-Guide/05-Tools/*.md"

# Specific tool docs (e.g., bash)
glob: "Developer-Guide/05-Tools/*bash*.md"
```

### Finding Prompt Engineering Guides
```bash
# All prompt engineering docs
glob: "Developer-Guide/07-Prompt-Engineering/*.md"

# Best practices specifically
glob: "Developer-Guide/07-Prompt-Engineering/*best-practices*.md"
```

### Finding API Reference
```bash
# All API docs
glob: "API-Guide/**/*.md"

# Agent SDK specifically
glob: "API-Guide/05-Agent-SDK/*.md"
```

### Finding Deployment Guides
```bash
# All deployment docs
glob: "Claude-Code/05-Deployment/*.md"

# Cloud-specific (Bedrock, Vertex)
glob: "Claude-Code/05-Deployment/*bedrock*.md"
glob: "Claude-Code/05-Deployment/*vertex*.md"
```

---

## 📖 Reading Strategy for AI Agents

### When building a feature:
1. **Start broad**: Read overview/intro files first
2. **Get specific**: Read implementation guides
3. **Reference details**: Check API reference or CLI reference
4. **Optimize**: Read best practices and performance guides

### When debugging:
1. **Check troubleshooting**: `Claude-Code/03-Troubleshooting/troubleshooting.md`
2. **Review config**: Relevant files in `Claude-Code/07-Configuration/`
3. **Check errors**: `API-Guide/01-Using-APIs/errors.md`

### When learning a new concept:
1. **Overview first**: Look for `overview.md` in relevant section
2. **Examples second**: Look for `*-examples.md` files
3. **Deep dive**: Read implementation-specific docs
4. **Reference**: Keep `08-Reference` sections bookmarked

---

## 🎓 Documentation Quality Notes

**Most comprehensive sections**:
- Developer-Guide/07-Prompt-Engineering (14 files)
- Claude-Code/07-Configuration (7 files)
- API-Guide/05-Agent-SDK (14 files)

**Single-file sections** (may need external resources):
- Claude-Code/03-Troubleshooting (1 file)
- Claude-Code/04-SDK (1 file)

**Cross-referenced topics** (multiple files across sections):
- **MCP**: 3 files across Developer-Guide, API-Guide, Claude-Code
- **Security**: Scattered across Legal, Administration, Deployment
- **Configuration**: Spans Claude-Code/07-Configuration and API-Guide settings

---

## 🔄 Update Instructions

When new documentation is scraped:
1. Run `/Users/james/Desktop/School/Year-12/documentation-scraper/docs-scraper.py`
2. Files auto-organized by `reorganize_files.py` into this structure
3. Update this map if new sections are added
4. Update "Last Updated" date at top

---

**Pro tip for AI agents**: When uncertain which file to read, start with files named `overview.md` or `intro.md` in the relevant section. These provide context and links to deeper documentation.