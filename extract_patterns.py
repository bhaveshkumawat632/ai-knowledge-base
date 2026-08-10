#!/usr/bin/env python3
"""Extract actionable patterns from cloned AI agent repos."""

import os
import json
from pathlib import Path

BASE = Path.home() / "ai-knowledge-base"
OUT = BASE / "EXTRACTED_PATTERNS.md"

patterns = []

def add(title, source, content):
    patterns.append(f"### {title}\n**Source:** `{source}`\n```\n{content}\n```\n")

# Hermes Agent patterns
hermes = BASE / "repos-batch2" / "hermes-agent"
if hermes.exists():
    # Extract from AGENTS.md - design principles
    agents_md = hermes / "AGENTS.md"
    if agents_md.exists():
        content = agents_md.read_text()[:3000]
        add("Hermes Core Design", "NousResearch/hermes-agent", content)
    
    # Extract from key agent files
    for f in ["agent/transports/chat_completions.py", "agent/skill_commands.py"]:
        p = hermes / f
        if p.exists():
            content = "\n".join(p.read_text().splitlines()[:50])
            add(f"Hermes {f}", "NousResearch/hermes-agent", content)

# LangGraph patterns
langgraph = BASE / "repos-batch2" / "react-implementation" / "libs" / "langgraph" / "langgraph" / "graph"
if langgraph.exists():
    state_py = langgraph / "state.py"
    if state_py.exists():
        content = "\n".join(state_py.read_text().splitlines()[:80])
        add("LangGraph StateGraph", "langchain-ai/langgraph", content)

# AutoGen patterns  
autogen = BASE / "repos-batch2" / "multi-agent-fw"
if autogen.exists():
    agent_chat = autogen / "python" / "packages" / "pyautogen-agentchat" / "src" / "pyautogen_agentchat"
    # Find key files
    for pattern in ["**/agents/*.py", "**/tools/*.py"]:
        files = list(autogen.glob(f"python/packages/**/*.py"))[:3]
        for f in files:
            content = "\n".join(f.read_text().splitlines()[:40])
            add(f"AutoGen: {f.name}", "microsoft/autogen", content)

# OpenHands patterns
openhands = BASE / "repos-batch3" / "openhands" / "core" / "agent"
if openhands.exists():
    for f in openhands.glob("*.py"):
        if f.exists():
            content = "\n".join(f.read_text().splitlines()[:50])
            add(f"OpenHands {f.name}", "All-Hands-AI/OpenHands", content)
            break

# CrewAI patterns
crewai = BASE / "repos-batch3" / "crewAI"
if crewai.exists():
    for f in crewai.glob("**/*.py"):
        if "crew" in f.name.lower() and f.exists():
            content = "\n".join(f.read_text().splitlines()[:60])
            add(f"CrewAI {f.name}", "crewAIInc/crewAI", content)
            break

# Write consolidated patterns
with open(OUT, "w") as f:
    f.write("# AI Agent Patterns - Consolidated Extract\n")
    f.write(f"# Generated: {Path.home().expanduser()}\n")
    f.write(f"# Repos analyzed: {len(patterns)}\n\n")
    f.write("\n".join(patterns))

print(f"Extracted {len(patterns)} patterns to {OUT}")
