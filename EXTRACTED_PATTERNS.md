# AI Agent Patterns - Consolidated Extract
# Generated from 91 repos on 2026-08-10

---

## 1. OPENCLAW (Gateway + Channel Architecture)
**Source:** openclaw/openclaw
**Pattern:** Personal AI assistant gateway with channel abstraction, hook dispatch, and external webhook endpoints for tool integration.

## 2. TELEGRAM-AGENT-RELAY (File Queue)
**Source:** telegram-agent-relay
**Pattern:** Reliable 1-to-1 Telegram-to-agent bridge using file queue (`incoming.txt`/`outgoing.txt`) instead of blind polling. Avoids 409 conflicts via single poller + drop_pending_updates.

## 3. BROWSER-USE (Web Automation)
**Source:** browser-use/browser-use
**Pattern:** Browser automation via headless Chromium with task submission, completion scoring, and session replay. Cloud API + local Playwright modes.

## 4. COMPUTER-USE (Desktop Control)
**Source:** computer-use
**Pattern:** Background-first desktop GUI control using cua-driver. SOM mode for element-indexed clicks. Escalation ladder: background → px → foreground → page.

## 5. PLANNING-WITH-FILES
**Source:** planning-with-files/planning-with-files
**Pattern:** Plan-driven execution using three markdown files: plan.md, findings.md, progress.md. Loop template updates these files incrementally.

## 6. METAGPT (Multi-Agent Roles)
**Source:** GeoKwirk/MetaGPT
**Pattern:** Role-based multi-agent orchestration: ProductManager → Architect → Engineer → QA. Each role has distinct prompt template and output contract.

## 7. OPENCLAW HOOK DISPATCH
**Source:** openclaw/openclaw
**Pattern:** External webhook endpoint with Bearer token auth. Accepts JSON payloads and dispatches to agent runtime. Used for CI/CD, GitHub Actions, third-party integrations.

## 8. SCREENPIPE (Local Context/Memory)
**Source:** nick1udwig/screenpipe
**Pattern:** Continuous local screen/audio capture for agent memory. Stores timestamped context windows for retrieval-augmented generation.

## 9. AUTOGPT (Backend + SSE)
**Source:** Significant-Gravitas/AutoGPT
**Pattern:** FastAPI backend with WebSocket + SSE streaming. ExecutionManager pattern for process supervision. Block-based architecture for composable agent actions.

## 10. CREWAI (Crews + Flows)
**Source:** joaomdmoura/crewAI
**Pattern:** Crew = role-based agents collaborating on a shared objective. Flow = event-driven single-call workflow. YAML config for declarative crew definition.

## 11. AG2 (Subagent Delegation)
**Source:** ag2ai/ag2
**Pattern:** Two-agent conversation pattern with speaker-switching logic. Codeable agents that can be delegated specific subtasks with typed handoff messages.

## 12. ROO-CODE (Slash Commands + Tool Protocol)
**Source:** Roo-Code/Roo-Code
**Pattern:** Slash-command router (`/plan`, `/review`, `/test`) mapped to mode changes. Typed tool args schema with 60+ parameter names. Native tool args map for read_file, write_file, patch, execute_command.

## 13. LANGCHAIN (LCEL Chains)
**Source:** langchain-ai/langchain
**Pattern:** LangChain Expression Language (LCEL) for composing prompt → LLM → parser → retriever chains. Runnable protocol with `.invoke()`, `.batch()`, `.stream()`.

## 14. OPENAI AGENTS (Handoffs)
**Source:** openai/openai-agents-python
**Pattern:** Agent handoff pattern: agents can transfer control to specialized agents via function call. Built-in guardrails and tracing.

## 15. AUTORESEARCH / DEEPSEEK-REASONIX
**Source:** autoresearch/DeepSeek-Reasonix
**Pattern:** Deep reasoning with chain-of-thought templates. System prompts engineered for research depth.

## 16. GPT-RESEARCHER
**Source:** gpt-researcher/gpt-researcher
**Pattern:** Autonomous web research loop: search → scrape → summarize → report. Report generation with citations.

## 17. OPENVIKING
**Source:** OpenViking/OpenViking
**Pattern:** Local-first research agent with offline fallback.

## 18. PONYTAIL
**Source:** platelminto/ponytail
**Pattern:** Minimal agent framework with tool-use loop.

## 19. SYSTEM-PROMPTS
**Source:** system-prompt/system-prompts
**Pattern:** Curated system prompt library for task-specific agent behavior tuning.

## 20. MEM0 (Memory Layer)
**Source:** mem0ai/mem0
**Pattern:** Persistent memory layer for agents with embedding-based retrieval. Cross-session context preservation.

## 21. CHATDEV (Workflow Graph)
**Source:** OpenBMB/ChatDev
**Pattern:** Graph-based workflow orchestration with DAG and cycle execution strategies. Memory + thinking management integrated into graph nodes. Human-in-the-loop prompt channels.

## 22. CAMEL (Role-Based Agents)
**Source:** camel-ai/camel
**Pattern:** Role-playing multi-agent framework with systematic "inception" prompting. Agent messages with role switching, memory factory, and thinking manager base classes.

## 23. AUTOGEN (ConversableAgent)
**Source:** microsoft/autogen
**Pattern:** ConversableAgent base class with human/agent message routing. Code block extraction from messages. Nested conversation support.

## 24. LLAMAINDEX (RAG Pipeline)
**Source:** run-llama/llama_index
**Pattern:** Index → Retriever → Query Engine pipeline for document ingestion. Vector stores + LLM rerankers for RAG.

## 25. FASTGPT (Knowledge QA)
**Source:** labring/FastGPT
**Pattern:** Knowledge base QA with vector search + workflow orchestration. API-first design for embedding-based question answering.

## 26. TRANSFORMERS (Hugging Face)
**Source:** huggingface/transformers
**Pattern:** Model hub pattern for downloading/tracking model versions. Pipeline abstraction for inference tasks.

## 27. CONTINVE (IDE Agent)
**Source:** continuedev/continue
**Pattern:** IDE-integrated agent with codebase context. Autocomplete + chat + edit loop.

## 28. PYDANTIC-AI (Structured Output)
**Source:** pydantic/pydantic-ai
**Pattern:** Type-safe agent output via Pydantic models. Run context with dependency injection.

## 29. DSPY (Programming vs Prompting)
**Source:** stanfordnlp/dspy
**Pattern:** Programming, not prompting. Optimizer-driven prompt and module selection with assertion-driven training.

## 30. OPENAI-QUICKSTART
**Source:** openai/openai-quickstart-python
**Pattern:** Minimal API integration pattern for OpenAI Assistants/Threads/Runs. File search + code interpreter quickstart.

---

## BACKEND v5.4 IMPLEMENTATION STATUS

| Pattern | Status | Endpoint/Feature |
|---------|--------|------------------|
| ReAct | ✅ | POST /api/task |
| StateGraph | ✅ | task_queue.db |
| AgentTool | ✅ | Tool protocol |
| Self-Eval | ✅ | scoring logic |
| Retry | ✅ | retry decorator |
| PersistentQueue | ✅ | SQLite tasks |
| SkillLoader | ✅ | /api/skills |
| HookDispatch | ✅ | POST /hooks |
| BrowserUse | ✅ | POST /api/browser/task |
| ComputerUse | ✅ | POST /api/desktop/action |
| FileQueue | ✅ | bot_queue/ |
| MultiAgent | ✅ | mode=multi |
| ToolProtocol | ✅ | /api/tools |
| Planning | ✅ | POST /api/task/plan |
| VoiceBot | 🔄 | queue ready, needs BOT_TOKEN |
| SandboxedExec | ✅ | subprocess backend |
| AgentMemory | ✅ | SQLite + broadcast |
| RoleBased | ✅ | mode=multi |
| AG2AgentDelegate | ✅ | POST /api/delegate |
| CrewAIFlow | ✅ | POST /api/flow |
| RooSlashCommand | ✅ | /api/commands + /api/command/{cmd} |
| LangChainLCEL | ✅ | POST /api/chain |
| OpenAIAgentHandoff | 🔄 | pattern documented |
