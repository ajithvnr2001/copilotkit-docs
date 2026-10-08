---
url: https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents/
title: Sub-Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:37.644865+00:00
---

# Sub-Agents

> Source: https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Agent capabilities

# Sub-Agents

Decompose work across multiple specialized agents with a visible delegation log.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

subagents.py

page.tsx

delegation-log.tsx

route.ts
    
    
    """LangGraph agent backing the Sub-Agents demo.Demonstrates multi-agent delegation with a visible delegation log.A top-level "supervisor" LLM orchestrates three specialized sub-agents,exposed as tools:  - `research_agent`  — gathers facts  - `writing_agent`   — drafts prose  - `critique_agent`  — reviews draftsEach sub-agent is a full `create_agent(...)` under the hood. Everydelegation appends an entry to the `delegations` slot in shared agentstate so the UI can render a live "delegation log" as the supervisorfans work out and collects results. This is the canonical LangGraphsub-agents-as-tools pattern, adapted to surface delegation events tothe frontend via CopilotKit's shared-state channel."""import operatorimport uuidfrom typing import Annotated, Literal, TypedDictfrom langchain.agents import AgentState as BaseAgentState, create_agentfrom langchain.tools import ToolRuntime, toolfrom langchain_core.messages import AIMessage, HumanMessage, ToolMessagefrom langchain_openai import ChatOpenAIfrom langgraph.types import Commandfrom copilotkit import CopilotKitMiddlewarefrom src.agents._header_forwarding_middleware import HeaderForwardingMiddleware# ---------------------------------------------------------------------------# Shared state# ---------------------------------------------------------------------------class Delegation(TypedDict):    id: str    sub_agent: Literal["research_agent", "writing_agent", "critique_agent"]    task: str    status: Literal["completed"]    result: str# Cap the supervisor → critique sub-agent loop at a single iteration.# Without this, the supervisor LLM occasionally re-calls `critique_agent`# repeatedly on the same draft (visible as stacking 🧐 cards in the# chat). The critic only adds value once per draft, so we hard-stop# after `_MAX_CRITIQUE_ITERATIONS` invocations and return a no-op# result._MAX_CRITIQUE_ITERATIONS = 1class AgentState(BaseAgentState):    """Shared state. `delegations` is rendered as a live log in the UI.    `delegations` uses an `operator.add` reducer so that concurrent    sub-agent emissions in the same supervisor step accumulate into a    single list instead of conflicting (LangGraph would otherwise raise    `INVALID_CONCURRENT_GRAPH_UPDATE` — "Can receive only one value per    step. Use an Annotated key to handle multiple values.").    """    delegations: Annotated[list[Delegation], operator.add]# ---------------------------------------------------------------------------# Sub-agents (real LLM agents under the hood)# ---------------------------------------------------------------------------# Each sub-agent is a full-fledged `create_agent(...)` with its own# system prompt. They don't share memory or tools with the supervisor —# the supervisor only sees their return value._sub_model = ChatOpenAI(model="gpt-5.4")# Each sub-agent gets the minimal HeaderForwardingMiddleware so the# inbound x-aimock-context (and other x-*) headers from the supervisor's# inbound HTTP request propagate to the sub-agent's outbound LLM call.# We intentionally do NOT attach the full CopilotKitMiddleware here —# the supervisor handles App-Context / frontend-tool injection for the# whole run, and adding it on sub-agents would double-inject prompt# state. Header forwarding alone is enough to keep aimock matching._research_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),    middleware=[HeaderForwardingMiddleware()],)_writing_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),    middleware=[HeaderForwardingMiddleware()],)_critique_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),    middleware=[HeaderForwardingMiddleware()],)# Sentinel surfaced when a sub-agent run produces no usable text. Kept# as a module-level constant so the harness probe (and any UI fallback)# can match the exact phrase. The leading/trailing angle brackets keep# it out of plausible LLM phrasing.SUB_AGENT_EMPTY_SENTINEL = "<sub-agent produced no output>"def _invoke_sub_agent(agent, task: str) -> str:    """Run a sub-agent on `task` and return its final prose message."""    result = agent.invoke({"messages": [HumanMessage(content=task)]})    messages = result.get("messages", [])    # Walk newest -> oldest so we pick the answer for THIS task, not a stale    # intro. Skip empty AIMessages that only carry tool_calls.    for msg in reversed(messages):        if isinstance(msg, AIMessage):            content = msg.content            if isinstance(content, str) and content.strip():                return content            # Some providers stream content as a list of content blocks            # (e.g. {"type": "text", "text": "..."}); concatenate the text.            # The `isinstance(block.get("text"), str)` guard rejects            # `{"type": "text", "text": null}` payloads — a known provider            # quirk — that would otherwise crash `"".join(...)` with            # `TypeError: sequence item N: expected str instance, NoneType found`.            if isinstance(content, list):                parts = [                    block["text"]                    for block in content                    if isinstance(block, dict)                    and block.get("type") == "text"                    and isinstance(block.get("text"), str)                ]                joined = "".join(parts).strip()                if joined:                    return joined    return SUB_AGENT_EMPTY_SENTINELdef _delegation_update(    sub_agent: str,    task: str,    result: str,    tool_call_id: str,) -> Command:    """Append a completed delegation entry to shared state.    Returns just the new entry (a one-element list). The reducer on    `AgentState.delegations` is `operator.add`, which concatenates the    new list with the prior state — so we must NOT echo back the    existing delegations here, or they would be duplicated each step.    """    entry: Delegation = {        "id": str(uuid.uuid4()),        "sub_agent": sub_agent,  # type: ignore[typeddict-item]        "task": task,        "status": "completed",        "result": result,    }    return Command(        update={            "delegations": [entry],            "messages": [                ToolMessage(                    content=result,                    name=sub_agent,                    id=str(uuid.uuid4()),                    tool_call_id=tool_call_id,                )            ],        }    )# ---------------------------------------------------------------------------# Supervisor tools (each tool delegates to one sub-agent)# ---------------------------------------------------------------------------# Each @tool wraps a sub-agent invocation. The supervisor LLM "calls"# these tools to delegate work; each call synchronously runs the# matching sub-agent, records the delegation into shared state, and# returns the sub-agent's output as a ToolMessage the supervisor can# read on its next step.@tooldef research_agent(task: str, runtime: ToolRuntime) -> Command:    """Delegate a research task to the research sub-agent.    Use for: gathering facts, background, definitions, statistics.    Returns a bulleted list of key facts.    """    result = _invoke_sub_agent(_research_agent, task)    return _delegation_update("research_agent", task, result, runtime.tool_call_id)@tooldef writing_agent(task: str, runtime: ToolRuntime) -> Command:    """Delegate a drafting task to the writing sub-agent.    Use for: producing a polished paragraph, draft, or summary. Pass    relevant facts from prior research inside `task`.    """    result = _invoke_sub_agent(_writing_agent, task)    return _delegation_update("writing_agent", task, result, runtime.tool_call_id)@tooldef critique_agent(task: str, runtime: ToolRuntime) -> Command:    """Delegate a critique task to the critique sub-agent.    Use for: reviewing a draft and suggesting concrete improvements.    Capped at `_MAX_CRITIQUE_ITERATIONS` invocations per supervisor run    — the supervisor LLM occasionally re-calls the critic in a loop and    each rerun produces near-identical output, so additional calls are    short-circuited with a no-op result that nudges the supervisor to    finish.    """    state: AgentState = runtime.state  # type: ignore[assignment]    delegations = state.get("delegations") or []    prior_critiques = sum(        1 for d in delegations if d.get("sub_agent") == "critique_agent"    )    if prior_critiques >= _MAX_CRITIQUE_ITERATIONS:        # Short-circuit without appending another delegation entry — the        # UI renders one card per delegation and we want exactly one        # critic card per supervisor run, even if the LLM ignores the        # system prompt and re-issues the call.        skip_message = (            "Critique already produced for this run. "            "Stop calling critique_agent and return your final answer "            "to the user now."        )        return Command(            update={                "messages": [                    ToolMessage(                        content=skip_message,                        name="critique_agent",                        id=str(uuid.uuid4()),                        tool_call_id=runtime.tool_call_id,                    )                ],            }        )    result = _invoke_sub_agent(_critique_agent, task)    return _delegation_update("critique_agent", task, result, runtime.tool_call_id)# ---------------------------------------------------------------------------# Supervisor (the graph we export)# ---------------------------------------------------------------------------graph = create_agent(    model=ChatOpenAI(model="gpt-5.4"),    tools=[research_agent, writing_agent, critique_agent],    middleware=[CopilotKitMiddleware()],    state_schema=AgentState,    system_prompt=(        "You are a supervisor agent that coordinates three specialized "        "sub-agents to produce high-quality deliverables.\n\n"        "Available sub-agents (call them as tools):\n"        "  - research_agent: gathers facts on a topic.\n"        "  - writing_agent: turns facts + a brief into a polished draft.\n"        "  - critique_agent: reviews a draft and suggests improvements.\n\n"        "For every non-trivial user request, delegate in sequence: "        "research_agent -> writing_agent -> critique_agent. "        "IMPORTANT: call EACH sub-agent EXACTLY ONCE per user request. "        "After critique_agent returns, do NOT call any sub-agent "        "again — return a concise final answer to the user that "        "incorporates the critique. Pass the relevant facts/draft "        "through the `task` argument of each tool. Keep your own "        "messages short — explain the plan once, delegate, then return "        "a concise summary once done. The UI shows the user a live log "        "of every sub-agent delegation."    ),)

## What is this?#

Sub-agents are the canonical multi-agent pattern: a top-level **supervisor** LLM orchestrates one or more specialized **sub-agents** by exposing each of them as a tool. The supervisor decides what to delegate, the sub-agents do their narrow job, and their results flow back up to the supervisor's next step.

This is fundamentally the same shape as tool-calling, but each "tool" is itself a full-blown agent with its own system prompt and (often) its own tools, memory, and model.

## When should I use this?#

Reach for sub-agents when a task has distinct specialized sub-tasks that each benefit from their own focus:

  * **Research → Write → Critique** pipelines, where each stage needs a different system prompt and temperature.
  * **Router + specialists** , where one agent classifies the request and dispatches to the right expert.
  * **Divide-and-conquer** — any problem that fits cleanly into parallel or sequential sub-problems.



The example below uses the Research → Write → Critique shape as the canonical example.

## Setting up sub-agents#

### Install the LangGraph Python SDK

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

### Wire CopilotKit middleware into your graph

Sub-agents are wired as tools on a supervisor `create_agent` call. The supervisor's middleware list includes `CopilotKitMiddleware()` so the delegation log slot streams back to the UI through shared state.

subagents.py
    
    
    import operator
    import uuid
    from typing import Annotated, Literal, TypedDict
    
    from langchain.agents import AgentState as BaseAgentState, create_agent
    from langchain.tools import ToolRuntime, tool
    from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
    from langchain_openai import ChatOpenAI
    from langgraph.types import Command
    
    from copilotkit import CopilotKitMiddleware
    
    from src.agents._header_forwarding_middleware import HeaderForwardingMiddleware
    
    
    # ---------------------------------------------------------------------------
    # Shared state
    # ---------------------------------------------------------------------------
    
    
    class Delegation(TypedDict):
        id: str
        sub_agent: Literal["research_agent", "writing_agent", "critique_agent"]
        task: str
        status: Literal["completed"]
        result: str
    
    
    # Cap the supervisor → critique sub-agent loop at a single iteration.
    # Without this, the supervisor LLM occasionally re-calls `critique_agent`
    # repeatedly on the same draft (visible as stacking 🧐 cards in the
    # chat). The critic only adds value once per draft, so we hard-stop
    # after `_MAX_CRITIQUE_ITERATIONS` invocations and return a no-op
    # result.
    _MAX_CRITIQUE_ITERATIONS = 1
    
    
    class AgentState(BaseAgentState):
        """Shared state. `delegations` is rendered as a live log in the UI.
    
        `delegations` uses an `operator.add` reducer so that concurrent
        sub-agent emissions in the same supervisor step accumulate into a
        single list instead of conflicting (LangGraph would otherwise raise
        `INVALID_CONCURRENT_GRAPH_UPDATE` — "Can receive only one value per
        step. Use an Annotated key to handle multiple values.").
        """
    
        delegations: Annotated[list[Delegation], operator.add]
    
    
    # ---------------------------------------------------------------------------
    # Sub-agents (real LLM agents under the hood)
    # ---------------------------------------------------------------------------
    
    # Each sub-agent is a full-fledged `create_agent(...)` with its own
    # system prompt. They don't share memory or tools with the supervisor —
    # the supervisor only sees their return value.
    _sub_model = ChatOpenAI(model="gpt-5.4")
    
    # Each sub-agent gets the minimal HeaderForwardingMiddleware so the
    # inbound x-aimock-context (and other x-*) headers from the supervisor's
    # inbound HTTP request propagate to the sub-agent's outbound LLM call.
    # We intentionally do NOT attach the full CopilotKitMiddleware here —
    # the supervisor handles App-Context / frontend-tool injection for the
    # whole run, and adding it on sub-agents would double-inject prompt
    # state. Header forwarding alone is enough to keep aimock matching.
    _research_agent = create_agent(
        model=_sub_model,
        tools=[],
        system_prompt=(
            "You are a research sub-agent. Given a topic, produce a concise "
            "bulleted list of 3-5 key facts. No preamble, no closing."
        ),
        middleware=[HeaderForwardingMiddleware()],
    )
    
    _writing_agent = create_agent(
        model=_sub_model,
        tools=[],
        system_prompt=(
            "You are a writing sub-agent. Given a brief and optional source "
            "facts, produce a polished 1-paragraph draft. Be clear and "
            "concrete. No preamble."
        ),
        middleware=[HeaderForwardingMiddleware()],
    )
    
    _critique_agent = create_agent(
        model=_sub_model,
        tools=[],
        system_prompt=(
            "You are an editorial critique sub-agent. Given a draft, give "
            "2-3 crisp, actionable critiques. No preamble."
        ),
        middleware=[HeaderForwardingMiddleware()],
    )

See `src/agents/subagents.py` for the canonical supervisor + three sub-agents pattern with a live delegation log.

Each sub-agent is an isolated agent call with its own model, system prompt, and optional tools. They don't share memory or tools with the supervisor; the supervisor only ever sees what the sub-agent returns.

subagents.py
    
    
    import operatorimport uuidfrom typing import Annotated, Literal, TypedDictfrom langchain.agents import AgentState as BaseAgentState, create_agentfrom langchain.tools import ToolRuntime, toolfrom langchain_core.messages import AIMessage, HumanMessage, ToolMessagefrom langchain_openai import ChatOpenAIfrom langgraph.types import Commandfrom copilotkit import CopilotKitMiddlewarefrom src.agents._header_forwarding_middleware import HeaderForwardingMiddleware# ---------------------------------------------------------------------------# Shared state# ---------------------------------------------------------------------------class Delegation(TypedDict):    id: str    sub_agent: Literal["research_agent", "writing_agent", "critique_agent"]    task: str    status: Literal["completed"]    result: str# Cap the supervisor → critique sub-agent loop at a single iteration.# Without this, the supervisor LLM occasionally re-calls `critique_agent`# repeatedly on the same draft (visible as stacking 🧐 cards in the# chat). The critic only adds value once per draft, so we hard-stop# after `_MAX_CRITIQUE_ITERATIONS` invocations and return a no-op# result._MAX_CRITIQUE_ITERATIONS = 1class AgentState(BaseAgentState):    """Shared state. `delegations` is rendered as a live log in the UI.    `delegations` uses an `operator.add` reducer so that concurrent    sub-agent emissions in the same supervisor step accumulate into a    single list instead of conflicting (LangGraph would otherwise raise    `INVALID_CONCURRENT_GRAPH_UPDATE` — "Can receive only one value per    step. Use an Annotated key to handle multiple values.").    """    delegations: Annotated[list[Delegation], operator.add]# ---------------------------------------------------------------------------# Sub-agents (real LLM agents under the hood)# ---------------------------------------------------------------------------# Each sub-agent is a full-fledged `create_agent(...)` with its own# system prompt. They don't share memory or tools with the supervisor —# the supervisor only sees their return value._sub_model = ChatOpenAI(model="gpt-5.4")# Each sub-agent gets the minimal HeaderForwardingMiddleware so the# inbound x-aimock-context (and other x-*) headers from the supervisor's# inbound HTTP request propagate to the sub-agent's outbound LLM call.# We intentionally do NOT attach the full CopilotKitMiddleware here —# the supervisor handles App-Context / frontend-tool injection for the# whole run, and adding it on sub-agents would double-inject prompt# state. Header forwarding alone is enough to keep aimock matching._research_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),    middleware=[HeaderForwardingMiddleware()],)_writing_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),    middleware=[HeaderForwardingMiddleware()],)_critique_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),    middleware=[HeaderForwardingMiddleware()],)

Keep sub-agent system prompts narrow and focused. The point of this pattern is that each one does one thing well. If a sub-agent needs to know the whole user context to do its job, that's a signal the boundary is wrong.

## Exposing sub-agents as tools#

The supervisor delegates by calling tools. Each delegation tool is a thin wrapper around a specialized agent call that:

  1. Runs the sub-agent on the supplied `task` string.
  2. Records the delegation into a `delegations` slot in shared agent state (so the UI can render a live log).
  3. Returns the sub-agent's final message as the tool result, which the supervisor sees on its next turn.



subagents.py
    
    
    import operatorimport uuidfrom typing import Annotated, Literal, TypedDictfrom langchain.agents import AgentState as BaseAgentState, create_agentfrom langchain.tools import ToolRuntime, toolfrom langchain_core.messages import AIMessage, HumanMessage, ToolMessagefrom langchain_openai import ChatOpenAIfrom langgraph.types import Commandfrom copilotkit import CopilotKitMiddlewarefrom src.agents._header_forwarding_middleware import HeaderForwardingMiddleware# ---------------------------------------------------------------------------# Shared state# ---------------------------------------------------------------------------class Delegation(TypedDict):    id: str    sub_agent: Literal["research_agent", "writing_agent", "critique_agent"]    task: str    status: Literal["completed"]    result: str# Cap the supervisor → critique sub-agent loop at a single iteration.# Without this, the supervisor LLM occasionally re-calls `critique_agent`# repeatedly on the same draft (visible as stacking 🧐 cards in the# chat). The critic only adds value once per draft, so we hard-stop# after `_MAX_CRITIQUE_ITERATIONS` invocations and return a no-op# result._MAX_CRITIQUE_ITERATIONS = 1class AgentState(BaseAgentState):    """Shared state. `delegations` is rendered as a live log in the UI.    `delegations` uses an `operator.add` reducer so that concurrent    sub-agent emissions in the same supervisor step accumulate into a    single list instead of conflicting (LangGraph would otherwise raise    `INVALID_CONCURRENT_GRAPH_UPDATE` — "Can receive only one value per    step. Use an Annotated key to handle multiple values.").    """    delegations: Annotated[list[Delegation], operator.add]# ---------------------------------------------------------------------------# Sub-agents (real LLM agents under the hood)# ---------------------------------------------------------------------------# Each sub-agent is a full-fledged `create_agent(...)` with its own# system prompt. They don't share memory or tools with the supervisor —# the supervisor only sees their return value._sub_model = ChatOpenAI(model="gpt-5.4")# Each sub-agent gets the minimal HeaderForwardingMiddleware so the# inbound x-aimock-context (and other x-*) headers from the supervisor's# inbound HTTP request propagate to the sub-agent's outbound LLM call.# We intentionally do NOT attach the full CopilotKitMiddleware here —# the supervisor handles App-Context / frontend-tool injection for the# whole run, and adding it on sub-agents would double-inject prompt# state. Header forwarding alone is enough to keep aimock matching._research_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),    middleware=[HeaderForwardingMiddleware()],)_writing_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),    middleware=[HeaderForwardingMiddleware()],)_critique_agent = create_agent(    model=_sub_model,    tools=[],    system_prompt=(        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),    middleware=[HeaderForwardingMiddleware()],)# Sentinel surfaced when a sub-agent run produces no usable text. Kept# as a module-level constant so the harness probe (and any UI fallback)# can match the exact phrase. The leading/trailing angle brackets keep# it out of plausible LLM phrasing.SUB_AGENT_EMPTY_SENTINEL = "<sub-agent produced no output>"def _invoke_sub_agent(agent, task: str) -> str:    """Run a sub-agent on `task` and return its final prose message."""    result = agent.invoke({"messages": [HumanMessage(content=task)]})    messages = result.get("messages", [])    # Walk newest -> oldest so we pick the answer for THIS task, not a stale    # intro. Skip empty AIMessages that only carry tool_calls.    for msg in reversed(messages):        if isinstance(msg, AIMessage):            content = msg.content            if isinstance(content, str) and content.strip():                return content            # Some providers stream content as a list of content blocks            # (e.g. {"type": "text", "text": "..."}); concatenate the text.            # The `isinstance(block.get("text"), str)` guard rejects            # `{"type": "text", "text": null}` payloads — a known provider            # quirk — that would otherwise crash `"".join(...)` with            # `TypeError: sequence item N: expected str instance, NoneType found`.            if isinstance(content, list):                parts = [                    block["text"]                    for block in content                    if isinstance(block, dict)                    and block.get("type") == "text"                    and isinstance(block.get("text"), str)                ]                joined = "".join(parts).strip()                if joined:                    return joined    return SUB_AGENT_EMPTY_SENTINELdef _delegation_update(    sub_agent: str,    task: str,    result: str,    tool_call_id: str,) -> Command:    """Append a completed delegation entry to shared state.    Returns just the new entry (a one-element list). The reducer on    `AgentState.delegations` is `operator.add`, which concatenates the    new list with the prior state — so we must NOT echo back the    existing delegations here, or they would be duplicated each step.    """    entry: Delegation = {        "id": str(uuid.uuid4()),        "sub_agent": sub_agent,  # type: ignore[typeddict-item]        "task": task,        "status": "completed",        "result": result,    }    return Command(        update={            "delegations": [entry],            "messages": [                ToolMessage(                    content=result,                    name=sub_agent,                    id=str(uuid.uuid4()),                    tool_call_id=tool_call_id,                )            ],        }    )# ---------------------------------------------------------------------------# Supervisor tools (each tool delegates to one sub-agent)# ---------------------------------------------------------------------------# Each @tool wraps a sub-agent invocation. The supervisor LLM "calls"# these tools to delegate work; each call synchronously runs the# matching sub-agent, records the delegation into shared state, and# returns the sub-agent's output as a ToolMessage the supervisor can# read on its next step.@tooldef research_agent(task: str, runtime: ToolRuntime) -> Command:    """Delegate a research task to the research sub-agent.    Use for: gathering facts, background, definitions, statistics.    Returns a bulleted list of key facts.    """    result = _invoke_sub_agent(_research_agent, task)    return _delegation_update("research_agent", task, result, runtime.tool_call_id)@tooldef writing_agent(task: str, runtime: ToolRuntime) -> Command:    """Delegate a drafting task to the writing sub-agent.    Use for: producing a polished paragraph, draft, or summary. Pass    relevant facts from prior research inside `task`.    """    result = _invoke_sub_agent(_writing_agent, task)    return _delegation_update("writing_agent", task, result, runtime.tool_call_id)@tooldef critique_agent(task: str, runtime: ToolRuntime) -> Command:    """Delegate a critique task to the critique sub-agent.    Use for: reviewing a draft and suggesting concrete improvements.    Capped at `_MAX_CRITIQUE_ITERATIONS` invocations per supervisor run    — the supervisor LLM occasionally re-calls the critic in a loop and    each rerun produces near-identical output, so additional calls are    short-circuited with a no-op result that nudges the supervisor to    finish.    """    state: AgentState = runtime.state  # type: ignore[assignment]    delegations = state.get("delegations") or []    prior_critiques = sum(        1 for d in delegations if d.get("sub_agent") == "critique_agent"    )    if prior_critiques >= _MAX_CRITIQUE_ITERATIONS:        # Short-circuit without appending another delegation entry — the        # UI renders one card per delegation and we want exactly one        # critic card per supervisor run, even if the LLM ignores the        # system prompt and re-issues the call.        skip_message = (            "Critique already produced for this run. "            "Stop calling critique_agent and return your final answer "            "to the user now."        )        return Command(            update={                "messages": [                    ToolMessage(                        content=skip_message,                        name="critique_agent",                        id=str(uuid.uuid4()),                        tool_call_id=runtime.tool_call_id,                    )                ],            }        )    result = _invoke_sub_agent(_critique_agent, task)    return _delegation_update("critique_agent", task, result, runtime.tool_call_id)

This is where CopilotKit's shared-state channel earns its keep: the supervisor's tool calls mutate `delegations` as they happen, and the frontend renders every new entry live.

Give every delegation a stable `id` and merge new entries by that `id`. The client sends its copy of shared state back as run input on every run, so a slot that blindly appends whatever it receives — a LangGraph `Annotated[list, operator.add]` reducer, for example — concatenates the entries the client just echoed onto the ones the agent already has, and the log doubles when a thread is continued.

## Rendering a live delegation log#

On the frontend, the delegation log is a reactive render of the `delegations` slot.

Subscribe with `useAgent({ updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged] })`, read `agent.state.delegations`, and render one card per entry.

delegation-log.tsx
    
    
    /** * Live delegation log — renders the `delegations` slot of agent state. * * Each entry corresponds to one invocation of a sub-agent. The list * grows in real time as the supervisor fans work out to its children. * The parent header shows how many sub-agents have been called and * whether the supervisor is still running. */// Fixed list of the three sub-agent roles the supervisor can call.// Rendered as always-visible indicator chips at the top of the log// (regardless of whether the supervisor has delegated yet) so the user// — and the e2e suite — can see at a glance which sub-agents exist and// which are currently active.const INDICATOR_ROLES: ReadonlyArray<{  role: "researcher" | "writer" | "critic";  subAgent: SubAgentName;}> = [  { role: "researcher", subAgent: "research_agent" },  { role: "writer", subAgent: "writing_agent" },  { role: "critic", subAgent: "critique_agent" },];export function DelegationLog({ delegations, isRunning }: DelegationLogProps) {  const calledRoles = new Set<SubAgentName>(    delegations.map((d) => d.sub_agent),  );  return (    <div      data-testid="delegation-log"      className="w-full h-full flex flex-col bg-white rounded-2xl shadow-sm border border-[#DBDBE5] overflow-hidden"    >      <div className="flex items-center justify-between px-6 py-3 border-b border-[#E9E9EF] bg-[#FAFAFC]">        <div className="flex items-center gap-3">          <span className="text-lg font-semibold text-[#010507]">            Sub-agent delegations          </span>          {isRunning && (            <span              data-testid="supervisor-running"              className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full border border-[#BEC2FF] bg-[#BEC2FF1A] text-[#010507] text-[10px] font-semibold uppercase tracking-[0.12em]"            >              <span className="w-1.5 h-1.5 rounded-full bg-[#010507] animate-pulse" />              Supervisor running            </span>          )}        </div>        <span          data-testid="delegation-count"          className="text-xs font-mono text-[#838389]"        >          {delegations.length} calls        </span>      </div>      <div        data-testid="subagent-indicators"        className="flex items-center gap-2 border-b border-[#E9E9EF] bg-white px-6 py-2"      >        {INDICATOR_ROLES.map(({ role, subAgent }) => {          const style = SUB_AGENT_STYLE[subAgent];          const fired = calledRoles.has(subAgent);          return (            <span              key={role}              data-testid={`subagent-indicator-${role}`}              data-role={role}              data-fired={fired ? "true" : "false"}              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color} ${                fired ? "" : "opacity-60"              }`}            >              <span aria-hidden>{style.emoji}</span>              <span>{style.label}</span>            </span>          );        })}      </div>      <div className="flex-1 overflow-y-auto p-4 space-y-3">        {delegations.length === 0 ? (          <p className="text-[#838389] italic text-sm">            Ask the supervisor to complete a task. Every sub-agent it calls will            appear here.          </p>        ) : (          delegations.map((d, idx) => {            const style = SUB_AGENT_STYLE[d.sub_agent];            return (              <div                key={d.id}                data-testid="delegation-entry"                className="border border-[#E9E9EF] rounded-xl p-3 bg-[#FAFAFC]"              >                <div className="flex items-center justify-between mb-2">                  <div className="flex items-center gap-2">                    <span className="text-xs font-mono text-[#AFAFB7]">                      #{idx + 1}                    </span>                    <span                      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color}`}                    >                      <span>{style.emoji}</span>                      <span>{style.label}</span>                    </span>                  </div>                  <span className="text-[10px] uppercase tracking-[0.12em] font-semibold text-[#189370]">                    {d.status}                  </span>                </div>                <div className="text-xs text-[#57575B] mb-2">                  <span className="font-semibold text-[#010507]">Task: </span>                  {d.task}                </div>                <div className="text-sm text-[#010507] whitespace-pre-wrap bg-white rounded-lg p-2.5 border border-[#E9E9EF]">                  {d.result}                </div>              </div>            );          })        )}      </div>    </div>  );}

The result: as the supervisor fans work out to its sub-agents, the log grows in real time, giving the user visibility into a process that would otherwise be a long opaque spinner.

## Related#

  * **[Shared State](https://docs.copilotkit.ai/langgraph-python/shared-state)** — the channel that makes the delegation log live.
  * **[State streaming](https://docs.copilotkit.ai/langgraph-python/shared-state/streaming)** — stream _individual_ sub-agent outputs token-by-token inside each log entry.


