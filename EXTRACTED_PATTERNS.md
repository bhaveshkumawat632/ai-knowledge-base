# AI Agent Patterns - Consolidated Extract
# Generated from 36 repos on 2026-08-10

---

## 1. OPENCLAW (Gateway + Channel Architecture)
**Source:** openclaw/openclaw
**Pattern:** Personal AI assistant gateway connecting models, tools, messaging channels
**Key Concepts:**
- Gateway = local control plane for sessions, tools, events, channels
- Channels: WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage
- Self-extending skills: agent writes its own capabilities
- Multi-interface: Control UI + TUI + CLI
- Plugin/Skill marketplace via ClawHub
**Adoption:** Backend channel abstraction, multi-platform messaging, skill marketplace

## 2. BROWSER-USE (Browser Automation)
**Source:** browser-use/browser-use
**Pattern:** Make websites accessible for AI agents
**Key Concepts:**
- DOM-aware browser agent with accessibility tree parsing
- Handles dynamic elements, modals, login flows, JavaScript-heavy interfaces
- Vision-first automation with screenshot understanding
- Form filling, data retrieval, web scraping
**Adoption:** Add browser tool to backend for web automation tasks

## 3. METAGPT (SOP-Based Multi-Agent)
**Source:** FoundationAgents/MetaGPT
**Pattern:** Role-based agents with Standard Operating Procedures
**Key Concepts:**
- Software company simulation: product manager, architect, project manager, engineer
- "Code = SOP(Team)" - materialize SOPs and apply to LLM teams
- Structured outputs: user stories, competitive analysis, requirements, data structures, APIs
- Role-based message passing
**Adoption:** Implement role-based task decomposition in orchestrator

## 4. PLANNING-WITH-FILES (Persistent Planning)
**Source:** OthmanAdi/planning-with-files
**Pattern:** File-based working memory that survives context resets
**Key Concepts:**
- 3-file pattern: `task_plan.md`, `findings.md`, `progress.md`
- Context Window = RAM (volatile), Filesystem = Disk (persistent)
- Hooks re-inject plan each turn
- Survives /clear, crashes, compaction
- Session recovery: reads previous session store
- Benchmark: 96.7% pass rate, resumes in 5.0 turns vs 13.3 raw
**Adoption:** Add planning skill to backend, persistent task state

## 5. SCREENPIPE (Local Capture + Indexing)
**Source:** screenpipe/screenpipe
**Pattern:** 24/7 local screen/audio capture, searchable memory
**Key Concepts:**
- AGENTS.md loaded into every agent's context
- On-demand documentation pointers
- Multi-agent collaboration rules
- Parallel execution with safety boundaries
**Adoption:** Local memory capture, agent collaboration protocols

## 6. AGNO (Agent Platform Runtime)
**Source:** agno-agi/agno
**Pattern:** Production agent platform with full runtime
**Key Concepts:**
- 50+ REST endpoints with SSE and WebSockets
- JWT-based RBAC and multi-tenant isolation
- Context providers for live data
- Human approval gates
- Scheduling/cron background jobs
- Both sync and async variants required
- Cookbook pattern for examples
**Adoption:** Production-grade API patterns, security, observability

## 7. OPENAI-AGENTS-PYTHON (Agents SDK)
**Source:** openai/openai-agents-python
**Pattern:** Official lightweight multi-agent framework
**Key Concepts:**
- Agent handoffs between specialized agents
- Tool definitions with structured outputs
- Guardrails and human-in-the-loop
**Adoption:** AgentTool wrapper pattern in backend

## 8. KILOCODE (Code Agent)
**Source:** Kilo-Org/kilocode
**Pattern:** All-in-one agentic engineering platform
**Key Concepts:**
- Fast code generation + execution
- Multi-model support
- Ship and iterate quickly
**Adoption:** Add to model registry

## 9. SERENA (Semantic Code Editing)
**Source:** oraios/serena
**Pattern:** MCP toolkit for semantic code retrieval and editing
**Key Concepts:**
- Symbol-level code understanding
- IDE-like editing capabilities for agents
- MCP-based tool design
**Adoption:** Enhance code task handling

## 10. PRIMEINTELLECT-PRIME-AGENT (Self-Improving)
**Source:** PrimeIntellect-ai/prime-agent
**Pattern:** Self-improving reasoning language model agent
**Key Concepts:**
- Training + inference unified
- Recursive self-improvement
- Reflection and evaluation loops
**Adoption:** Self-improvement loop reference

## 11. FLOWISE (Visual Agent Builder)
**Source:** FlowiseAI/Flowise
**Pattern:** Drag-drop visual AI agent builder
**Key Concepts:**
- No-code agent construction
- Flow-based agent design
**Adoption:** Frontend flow designer

## 12. LIBRECHAT (Chat Platform)
**Source:** danny-avila/LibreChat
**Pattern:** Multi-provider chat interface
**Key Concepts:**
- Multi-model switching
- MCP support
- Code interpreter
- Message search
- Multi-user auth
**Adoption:** UI patterns for chat

## 13. PAGE-AGENT (Web Page Agent)
**Source:** alibaba/page-agent
**Pattern:** JavaScript in-page GUI agent
**Key Concepts:**
- Control web interfaces with natural language
- In-page execution
**Adoption:** Web automation

## 14. AGNO (AGI Framework)
**Source:** agno-agi/agno
**Pattern:** Modular AGI platform components
**Key Concepts:**
- Agent teams and workflows
- Knowledge/RAG integration
- Vector database support
- Observability with OpenTelemetry
**Adoption:** Architecture reference

## 15. GOOGLE-SKILLS (Skills Library)
**Source:** google/skills
**Pattern:** Official Google skills collection
**Key Concepts:**
- Standardized skill format
- Cross-platform compatibility
**Adoption:** Expand skills loader

## 16. ROO-CODE (Sandboxed Execution)
**Source:** RooCodeInc/Roo-Code
**Pattern:** Safe code execution in sandbox
**Key Concepts:**
- Permission-gated steps
- Sandboxed execution environment
- Error recovery
**Adoption:** Sandboxed execution in backend

## 17. AGENT MEMORY / CLAUDE-MEM (Persistent Context)
**Source:** thedotmack/claude-mem
**Pattern:** Persistent context across sessions
**Key Concepts:**
- Captures agent actions during sessions
- Compresses with AI
- Injects relevant context into future sessions
- Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot
**Adoption:** Cross-session memory persistence

## 18. SYSTEM PROMPTS & MODELS (Prompt Library)
**Source:** x1xhlol/system-prompts-and-models-of-ai-tools
**Pattern:** Collection of production system prompts
**Key Concepts:**
- Augment Code, Claude Code, Cursor, Devin, Kiro, Replit prompts
- Internal tools and AI models documentation
- Prompt engineering best practices
**Adoption:** Improve prompt engineering in backend

---

## EXISTING PATTERNS (from earlier repos)
1. ReAct loop reasoning
2. StateGraph task state
3. AgentTool wrapper
4. Persistent task queue
5. Skill loader/registry
6. Self-evaluation + scoring
7. Retry with backoff
8. Parallel orchestration
9. Browser/screen capture
10. SOP-based role decomposition

---

## READY-TO-ADOPT IMPROVEMENTS
1. Multi-channel gateway (OpenClaw)
2. Browser automation (browser-use)
3. SOP-based roles (MetaGPT)
4. Persistent planning files (planning-with-files)
5. Local screen memory (screenpipe)
6. OpenAI Agents SDK patterns
7. Sandboxed code execution (Roo-Code)
8. Visual flow builder (Flowise)
9. Semantic code editing (serena)
10. Expanded skills library (google-skills)
11. Production API patterns (Agno)
12. Persistent context across sessions (claude-mem)
13. Prompt library integration (system-prompts-and-models)
