# AI Agent Patterns Extracted from Top Repositories
## Source: 7 repos cloned on 2026-08-10

---

## 1. COGNITIVE ARCHITECTURES

### ReAct Loop (Reason + Act)
- Used by: Gemini CLI, Claude Code, OpenCode
- Pattern: Thought → Action → Observation → Thought → ...
- Implementation: Structured thinking blocks + tool calls + result parsing
- Adopt: YES - enhance my reasoning chain

### Chain-of-Thought + Tool Use
- Used by: OpenAI Codex, Claude Code
- Pattern: Break task → plan → execute with tools → verify → iterate
- Adopt: YES - formalize planning phase

### Multi-Model Orchestration
- Used by: Grok Build (8 parallel agents), Bernstein
- Pattern: Route subtasks to specialized models, aggregate results
- Adopt: YES - already partially doing this, need formal routing

---

## 2. AGENT DESIGN PATTERNS

### Autonomous Software Engineer
- Used by: Devin, SWE-Agent, OpenHands
- Key features:
  - Sandboxed execution environments
  - Iterative debugging and self-healing
  - Test-driven verification
  - Issue-to-PR workflow
- Adopt: YES - add sandboxing, test verification loops

### Browser/Desktop Control
- Used by: Manus, Claude Computer Use, Project Mariner
- Pattern: Screenshot → Action → Verify via new screenshot
- Tools: Playwright, Browser Use, Skyvern
- Adopt: YES - add screenshot-based verification

### Role-Based Multi-Agent
- Used by: CrewAI, AutoGen, MetaGPT
- Pattern: PM, Architect, Engineer, QA roles
- Communication: Structured messages with context
- Adopt: YES - formalize role assignments for complex tasks

---

## 3. EXECUTION PATTERNS

### Parallel Execution
- Used by: Grok Build, Windsurf (5 parallel agents)
- Pattern: Decompose → parallel workers → merge results
- Adopt: YES - maximize parallel tool/subagent use

### Self-Healing / Retry Loops
- Used by: SWE-Agent, OpenHands
- Pattern: Execute → Check error → Diagnose → Fix → Retry
- Adopt: YES - add automatic error recovery

### Human-in-the-Loop
- Used by: OpenAI Operator, Devin 2.0
- Pattern: Checkpoints at critical decisions
- Adopt: CONDITIONAL - only for high-risk actions

### Test-Driven Verification
- Used by: SWE-Agent, Bernstein
- Pattern: Run tests after each change → fix failures
- Adopt: YES - add verification step after changes

---

## 4. MEMORY & CONTEXT

### Short-Term Memory
- Pattern: Conversation window, recent actions
- Used by: All agents

### Long-Term Memory
- Pattern: Vector store + retrieval
- Used by: LlamaIndex, LangChain, RAG agents
- Adopt: YES - enhance memory with retrieval

### Agent Memory Guard
- Pattern: Detect/block memory poisoning attacks
- Used by: OWASP Agent Memory Guard
- Adopt: YES - add validation layer

---

## 5. TOOL USE PATTERNS

### Function Calling
- Pattern: Structured tool definitions → LLM selects tool → execute
- Used by: OpenAI, Anthropic, Google
- Adopt: YES - formalize tool schema

### MCP (Model Context Protocol)
- Pattern: Standardized tool interface
- Used by: Claude Code, Gemini CLI, Cline
- Adopt: YES - migrate tools to MCP where possible

### Tool Composition
- Pattern: Chain tools in sequence/parallel
- Used by: LangChain, LlamaIndex
- Adopt: YES - build tool pipelines

---

## 6. OBSERVABILITY

### Structured Logging
- Pattern: JSON logs with timestamps, levels, agent IDs
- Used by: All production agents
- Adopt: YES - already doing this

### Real-Time Streaming
- Pattern: WebSocket/SSE for live updates
- Used by: OpenHands, Devin
- Adopt: YES - already doing this

### Evaluation Metrics
- Pattern: SWE-bench score, task completion rate
- Used by: SWE-Agent, OpenHands
- Adopt: YES - add self-evaluation

---

## IMMEDIATE ACTIONS

1. Add ReAct loop to my reasoning
2. Add test-driven verification after changes
3. Add self-healing retry logic
4. Formalize parallel execution strategy
5. Add memory validation/guard
6. Migrate to MCP tool definitions
7. Add screenshot-based browser verification
8. Add role-based task decomposition
9. Add evaluation/self-score step
10. Enhance memory with retrieval
