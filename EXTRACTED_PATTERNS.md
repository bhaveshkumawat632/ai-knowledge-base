# AI Agent Patterns - Consolidated Extract
# Generated from 17 repos on 2026-08-10

---

## 1. HERMES AGENT (NousResearch)
**Source:** NousResearch/hermes-agent

### Core Design Principles
- Per-conversation prompt caching is sacred
- Core is a narrow waist; capability lives at the edges
- Extend, don't duplicate
- Fix real bugs, well
- E2E validation over green unit mocks
- Behavior contracts over snapshots
- Cache-, alternation-, and invariant-safe

### Skill System
- Skills are procedural memory, not just docs
- Skills self-improve during use
- Skills can be created from experience automatically
- Skills loaded per task, not globally
- Compatible with agentskills.io open standard

### Memory Architecture
- FTS5-backed session search with LLM summarization
- Cross-session recall
- Agent-curated memory with periodic nudges
- Honcho dialectic user modeling
- Persistent across sessions, compact format

### Tool Footprint Ladder (ordered preference)
1. Extend existing code
2. CLI command + skill
3. Service-gated tool (check_fn)
4. Plugin
5. MCP server in catalog
6. New core tool (last resort)

---

## 2. LANGGRAPH (LangChain)
**Source:** langchain-ai/langgraph

### StateGraph Pattern
- Graph whose nodes communicate by reading/writing shared state
- Each node: State -> Partial<State>
- Compile() creates executable graph with invoke(), stream(), astream()
- Supports checkpointing, streaming, retry policies
- Annotated reducers for state aggregation

### Execution Model
- Pregel execution engine
- Channel-based communication
- Supports async, streaming, interrupts
- Timeout and retry policies per node

---

## 3. AUTOGEN (Microsoft)
**Source:** microsoft/autogen

### Multi-Agent Orchestration
- AgentTool wrapper: one agent becomes a tool for another
- AssistantAgent with system_message, model_client, tools
- Console UI for streaming agent conversations
- MCP Workbench for external tool integration
- AgentTool(return_value_as_last_message=True) for clean chaining

### Pattern
```python
math_agent = AssistantAgent("math_expert", model_client=model_client, system_message="...")
math_tool = AgentTool(math_agent, return_value_as_last_message=True)
main_agent = AssistantAgent("assistant", tools=[math_tool], ...)
```

---

## 4. OPENHANDS (All-Hands-AI)
**Source:** All-Hands-AI/OpenHands

### Foundation Agent
- Sandboxed execution environment
- Action/observation loop
- Security: action class classification
- Browser registry for web interactions
- MicroSnapshots for state tracking
- Trajectory compression for training

### Key Insight
- Runtime: action -> sandbox -> observation -> next action
- Supports delegates and parallel workstreams
- Plugin system for extensibility

---

## 5. CREWAI
**Source:** crewAIInc/crewAI

### Role-Based Agents
- agents have roles, goals, backstories
- tasks have descriptions, expected outputs, assigned agents
- Sequential or hierarchical process
- Crew = agents + tasks + process
- Memory shared across crew

### Pattern
```python
agent = Agent(role='Researcher', goal='Find info', backstory='...')
task = Task(description='Research X', agent=agent, expected_output='...')
crew = Crew(agents=[agent], tasks=[task], process=Process.sequential)
result = crew.kickoff()
```

---

## 6. GEMINI CLI (Google)
**Source:** google-gemini/gemini-cli

### Terminal-First Design
- Context files (GEMINI.md) for project-specific behavior
- Built-in grounding with Google Search
- MCP server extensibility
- Non-interactive mode for scripts
- Free tier: 60 req/min, 1000 req/day
- Conversation checkpointing

### Key Pattern
- Project-specific context via GEMINI.md
- MCP servers for custom integrations
- Grounding for real-time information

---

## 7. AUTORESEARCH (Karpathy)
**Source:** karpathy/autoresearch

### Self-Improving Loop Pattern
- Program.md as lightweight skill file
- Fixed time budget per experiment (5 min)
- Keep/discard branching based on metric improvement
- git reset on regression, advance on improvement
- Autonomous loop: never stop until interrupted
- Single file modification scope (train.py only)

### Key Insight
- The human programs the agent via markdown, not Python
- Agent modifies code, runs experiment, evaluates, commits or reverts
- Results.tsv tracks all experiments
- ~12 experiments/hour autonomously

---

## 8. DEEPSEEK-REASONIX
**Source:** esengine/DeepSeek-Reasonix

### Reasoning Pattern
- Chain-of-thought with explicit reasoning steps
- Self-verification after reasoning
- Multi-turn reasoning refinement

---

## 9. AGENTGPT
**Source:** reworkd/AgentGPT

### Autonomous Loop
- Goal decomposition into tasks
- Task execution with observation
- Self-reflection on results
- Dynamic task generation based on progress

---

## 10. KHOJ
**Source:** khoj-ai/khoj

### RAG Pattern
- Local-first knowledge base
- Conversation indexing
- Multi-modal: text, images, PDFs
- Auto-discovery of new information

---

## IMMEDIATE IMPROVEMENTS TO ADOPT

1. **ReAct Loop** - Interleave reasoning and action
2. **StateGraph** - Structured state management with checkpointing
3. **AgentTool Pattern** - Wrap subagents as callable tools
4. **Program.md** - Lightweight skill definition format
5. **Keep/Discard** - Self-evaluation with rollback
6. **Sandboxed Execution** - Security boundaries
7. **FTS5 Memory** - Full-text search across sessions
8. **MCP Integration** - Extensible tool protocol
9. **Role-Based Agents** - Specialized agent personas
10. **Experiment Loop** - Autonomous iteration with fixed budget

---

## NEXT STEPS
1. Implement ReAct loop in backend
2. Add StateGraph for complex tasks
3. Create skill from program.md pattern
4. Add self-evaluation step after tasks
5. Implement sandboxed code execution
