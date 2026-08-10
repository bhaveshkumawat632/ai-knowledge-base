# AI Agent Patterns - Consolidated Extract
# Generated from 58 repos on 2026-08-10

---

## 1. OPENCLAW (Gateway + Channel Architecture)
**Source:** openclaw/openclaw
**Pattern:** Personal AI assistant with gateway/channel abstraction
**Adopted:** HookDispatch webhook endpoint in backend v5

## 2. HERMES-AGENT (Orchestration)
**Source:** NousResearch/hermes-agent
**Pattern:** Multi-model orchestration, terminal visibility, desktop control
**Adopted:** Backend patterns list, skill loader

## 3. BROWSER-USE (Web Automation)
**Source:** browser-use/browser-use
**Pattern:** Headless Chromium automation, task polling pattern
**Adopted:** POST /api/browser/task endpoint

## 4. COMPUTER-USE (Desktop GUI)
**Source:** anthropics/computer-use
**Pattern:** SOM/vision capture modes, background-first input, escalation ladder
**Adopted:** POST /api/desktop/action with xdotool backend

## 5. TELEGRAM-AGENT-RELAY (Messaging)
**Source:** telegram-agent-relay skill
**Pattern:** File-queue async messaging, 409 conflict avoidance, fast inline replies
**Adopted:** bot_queue/incoming.txt + outgoing.txt, telegram_bot.py

## 6. PLANNING-WITH-FILES (Planning)
**Source:** planning-with-files
**Pattern:** Plan/findings/progress markdown artifacts
**Adopted:** run_planned_task(), plan/findings/progress files

## 7. METAGPT (Multi-Agent SOP)
**Source:** SIG-GPT/MetaGPT
**Pattern:** Role-based multi-agent orchestration
**Adopted:** run_role_orchestrated_task(), ProductManager/Architect/Engineer/QA roles

## 8. AUTOGPT (Block-Based Backend)
**Source:** Significant-Gravitas/AutoGPT
**Pattern:**
- FastAPI + WebSocket + REST dual API
- Block-based architecture with typed Pydantic schemas
- PostgreSQL + Prisma ORM + pgvector for embeddings
- RabbitMQ queue for async task processing
- SSE protocol for frontend-parsed events
- File length limits: ~300 lines per file, ~40 lines per function
**Adopted:** SSE streaming endpoint, typed tool args, queue patterns

## 9. ROO-CODE (Typed Tool Protocol)
**Source:** Roo-Code/Roo-Code
**Pattern:**
- Native tool args typing with TypeScript
- ToolParamNames enum pattern
- Strict typed tool arguments
**Adopted:** Typed tool args schema in browser/desktop endpoints

## 10. CREWAI (Crew-Based Execution)
**Source:** joaomdmoura/crewAI
**Pattern:** Crew-based agent execution, YAML config for agents/tasks
**Adopted:** Role orchestration in multi-agent mode

## 11. OPENAI-AGENTS-PYTHON
**Pattern:** Python SDK for OpenAI agents, tool calling pattern
**Adopted:** Tool calling interface in backend

## 12. LANGCHAIN
**Pattern:** LangChain Expression Language, state management
**Adopted:** StateGraph-style task state in SQLite

## 13. AG2
**Pattern:** A2A protocol, AG-UI protocol, multi-transport
**Adopted:** Multi-transport support patterns

## 14. DIFY/LANGFLOW (RAG Platforms)
**Pattern:** RAG pipeline, knowledge base integration
**Adopted:** Skill loader pattern for dynamic discovery

## 15. SCREENPIPE
**Pattern:** Screen recording/analysis pipeline
**Adopted:** Screenshot capture in desktop control

## 16. OPENCLI/AGENTICSEEK (Local CLI)
**Pattern:** Terminal-native agent interfaces
**Adopted:** FastAPI terminal streaming

---

## KEY PATTERNS SUMMARY
1. ReAct loop reasoning
2. StateGraph task state
3. AgentTool wrapper
4. Persistent task queue
5. Skill loader/registry
6. Self-evaluation + scoring
7. Retry with backoff
8. Gateway + channel abstraction
9. Browser task polling pattern
10. SOP-based role decomposition
11. Planning loop templates
12. Local context/memory layer
13. MCP tool definitions
14. Multi-model orchestration
15. Parallel execution strategy
16. File-queue messaging
17. SSE streaming protocol
18. Typed tool args
19. Block-based execution
20. Desktop background-first input with escalation
