# AI Agent Patterns - Consolidated Extract
# Generated from 36 repos on 2026-08-10

---

## 1. OPENCLAW (Gateway/Channel Architecture)
**Source:** openclaw/openclaw
**Pattern:** Multi-channel gateway with unified message bus
**Adoption:** Backend can use similar channel abstraction for multi-model routing

## 2. BROWSER-USE (Browser Automation)
**Source:** browser-use/browser-use
**Pattern:** DOM-aware browser agent with accessibility tree parsing
**Adoption:** Add browser tool to backend for web automation tasks

## 3. METAGPT (SOP-Based Multi-Agent)
**Source:** FoundationAgents/MetaGPT
**Pattern:** Role-based agents with SOPs (product manager, architect, engineer)
**Code:** `from metagpt.software_company import generate_repo`
**Adoption:** Implement role-based task decomposition in orchestrator

## 4. PLANNING-WITH-FILES (Persistent Planning)
**Source:** OthmanAdi/planning-with-files
**Pattern:** Persistent `task_plan.md` across sessions
**Skills:** 6 languages (en, ar, de, es, zh, zht)
**Adoption:** Add planning skill to backend

## 5. SCREENPIPE (Local Capture + Indexing)
**Source:** screenpipe/screenpipe
**Pattern:** 24/7 local screen/audio capture, searchable memory
**Adoption:** Add local memory capture to agent platform

## 6. OPENAI-AGENTS-PYTHON (Agents SDK)
**Source:** openai/openai-agents-python
**Pattern:** Official Python agents SDK with handoffs/tools
**Adoption:** Reference for AgentTool pattern implementation

## 7. KILOCODE (Code Agent)
**Source:** Kilo-Org/kilocode
**Pattern:** Fast code generation + execution
**Adoption:** Add to model registry

## 8. SERENA (Coding Agent)
**Source:** oraios/serena
**Pattern:** Semantic code understanding + editing
**Adoption:** Enhance code task handling

## 9. PRIMEINTELLECT-PRIME-AGENT (Training + Inference)
**Source:** PrimeIntellect-ai/prime-agent
**Pattern:** Unified training and inference agent
**Adoption:** Self-improvement loop reference

## 10. FLOWISE (Visual Agent Builder)
**Source:** FlowiseAI/Flowise
**Pattern:** Drag-drop agent flow builder
**Adoption:** Frontend flow designer

## 11. LIBRECHAT (Chat Platform)
**Source:** danny-avila/LibreChat
**Pattern:** Multi-provider chat interface
**Adoption:** UI patterns for chat

## 12. PAGE-AGENT (Web Page Agent)
**Source:** alibaba/page-agent
**Pattern:** Page-level understanding and interaction
**Adoption:** Web automation

## 13. AGNO (AGI Framework)
**Source:** agno-agi/agno
**Pattern:** Modular AGI components
**Adoption:** Architecture reference

## 14. GOOGLE-SKILLS (Skills Library)
**Source:** google/skills
**Pattern:** Official Google skills collection
**Adoption:** Expand skills loader

## 15. ROO-CODE (Code Execution)
**Source:** RooCodeInc/Roo-Code
**Pattern:** Safe code execution in sandbox
**Adoption:** Sandboxed execution in backend

---

## EXISTING PATTERNS (from 17 earlier repos)
1. ReAct loop reasoning
2. Test-driven verification
3. Self-healing retry logic
4. Parallel execution strategy
5. Memory validation/guard
6. MCP tool definitions
7. Screenshot-based browser verification
8. Role-based task decomposition
9. Self-evaluation/score step
10. Memory with retrieval

---

## READY-TO-ADOPT IMPROVEMENTS
1. Multi-channel gateway (openclaw)
2. Browser automation (browser-use)
3. SOP-based roles (MetaGPT)
4. Persistent planning files (planning-with-files)
5. Local screen memory (screenpipe)
6. OpenAI Agents SDK patterns
7. Sandboxed code execution (Roo-Code)
8. Visual flow builder (Flowise)
9. Semantic code editing (serena)
10. Expanded skills library (google-skills)
