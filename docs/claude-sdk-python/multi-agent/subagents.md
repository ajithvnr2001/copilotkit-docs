---
url: https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents/
title: Sub-Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:44.462172+00:00
---

# Sub-Agents

> Source: https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Agent capabilities

# Sub-Agents

Decompose work across multiple specialized agents with a visible delegation log.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

subagents_agent.py

page.tsx

delegation-log.tsx

route.ts
    
    
    """Claude Agent SDK backing the Sub-Agents demo.A supervisor Claude call orchestrates three specialised sub-agentsexposed as tools:  - ``research_agent``  — gathers facts on a topic  - ``writing_agent``   — drafts polished prose from a brief + facts  - ``critique_agent``  — reviews a draft and suggests improvementsEach delegation issues its own single-shot Anthropic SDK call with asub-agent-specific system prompt. This mirrors the ``google-adk`` patternin ``subagents_agent.py`` (which uses ``client.models.generate_content``under the hood) — a much lighter approach than spinning up a full secondagent loop, but conceptually identical.Every delegation appends an entry to ``state["delegations"]`` with shape``{id, sub_agent, task, status, result}``. Entries are emitted as``running`` first and flipped to ``completed`` / ``failed`` once thesub-agent returns, so the UI's delegation log animates in real time."""from __future__ import annotationsimport jsonimport loggingimport osimport uuidfrom collections.abc import AsyncIteratorfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunErrorEvent,    RunFinishedEvent,    RunStartedEvent,    StateSnapshotEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,    ToolCallArgsEvent,    ToolCallEndEvent,    ToolCallResultEvent,    ToolCallStartEvent,)from ag_ui.encoder import EventEncoderfrom agents.claude_agent_sdk_adapter import normalize_claude_modellogger = logging.getLogger(__name__)# Default Anthropic model for this showcase. Override with the# ANTHROPIC_MODEL or ANTHROPIC_SUBAGENT_MODEL env vars.DEFAULT_ANTHROPIC_MODEL = "claude-opus-4-8"# Each sub-agent is defined by its own system prompt; `_invoke_sub_agent`# (below) issues a single-shot Anthropic call as that sub-agent. They# don't share memory or tools with the supervisor — the supervisor only# ever sees what the sub-agent returns as a tool result.SUB_AGENT_PROMPTS: dict[str, str] = {    "research_agent": (        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),    "writing_agent": (        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),    "critique_agent": (        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),}SUPERVISOR_SYSTEM_PROMPT = (    "You are a supervisor agent that coordinates three specialized "    "sub-agents to produce high-quality deliverables.\n\n"    "Available sub-agents (call them as tools):\n"    "  - research_agent: gathers facts on a topic.\n"    "  - writing_agent: turns facts + a brief into a polished draft.\n"    "  - critique_agent: reviews a draft and suggests improvements.\n\n"    "For most non-trivial user requests, delegate in sequence: "    "research -> write -> critique. Pass the relevant facts/draft "    "through the `task` argument of each tool. Keep your own messages "    "short — explain the plan once, delegate, then return a concise "    "summary once done. The UI shows the user a live log of every "    "sub-agent delegation, including the in-flight 'running' state.")# The supervisor delegates by calling tools. Each entry in# `SUPERVISOR_TOOLS` is an Anthropic tool schema that the supervisor LLM# "calls" to delegate work; the run loop in `run_subagents_agent` (see# the subagents-delegation-flow region) runs the matching sub-agent# synchronously, records the delegation into shared agent state, and# returns the sub-agent's output as a tool_result the supervisor can# read on its next step.def _delegation_tool_schema(name: str, description: str) -> dict[str, Any]:    return {        "name": name,        "description": description,        "input_schema": {            "type": "object",            "properties": {                "task": {                    "type": "string",                    "description": (                        "The full task description to hand to the "                        "sub-agent. Pass relevant prior facts/drafts "                        "verbatim — the sub-agent has no shared memory "                        "with the supervisor."                    ),                }            },            "required": ["task"],        },    }SUPERVISOR_TOOLS: list[dict[str, Any]] = [    _delegation_tool_schema(        "research_agent",        "Delegate a research task. Returns a bulleted list of key facts.",    ),    _delegation_tool_schema(        "writing_agent",        (            "Delegate a drafting task. Pass relevant facts in `task`. "            "Returns a polished paragraph."        ),    ),    _delegation_tool_schema(        "critique_agent",        "Delegate a critique task. Returns 2-3 actionable critiques.",    ),]async def _invoke_sub_agent(    client: anthropic.AsyncAnthropic,    sub_agent: str,    task: str,) -> str:    """Issue a single-shot Anthropic call as the named sub-agent.    Returns the concatenated text content of the response. Raises any    SDK exception so the caller can mark the delegation as ``failed``.    """    response = await client.messages.create(        model=normalize_claude_model(            os.getenv("ANTHROPIC_SUBAGENT_MODEL", DEFAULT_ANTHROPIC_MODEL)        ),        max_tokens=1024,        system=SUB_AGENT_PROMPTS[sub_agent],        messages=[{"role": "user", "content": task}],    )    parts: list[str] = []    for block in response.content:        if getattr(block, "type", None) == "text":            parts.append(getattr(block, "text", ""))    text = "".join(parts).strip()    if not text:        raise RuntimeError("sub-agent returned empty response")    return textdef _convert_messages(input_data: RunAgentInput) -> list[dict[str, Any]]:    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        if role not in ("user", "assistant"):            continue        raw_content = getattr(msg, "content", None)        content = ""        if isinstance(raw_content, str):            content = raw_content        elif isinstance(raw_content, list):            parts = []            for part in raw_content:                if hasattr(part, "text"):                    parts.append(part.text)                elif isinstance(part, dict) and "text" in part:                    parts.append(part["text"])            content = "".join(parts)        if content:            messages.append({"role": role, "content": content})    return messagesasync def run_subagents_agent(    input_data: RunAgentInput,) -> AsyncIterator[str]:    """Run the supervisor and yield AG-UI events.    Each delegation:      1. Appends a ``running`` entry to ``state['delegations']`` and         emits a StateSnapshotEvent.      2. Issues the sub-agent's Anthropic call.      3. Mutates the entry in place to ``completed`` / ``failed`` and         emits another StateSnapshotEvent.      4. Returns the sub-agent's text as a ToolCallResult so the         supervisor can use it on its next step.    """    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    state: dict[str, Any] = {        "delegations": list((input_data.state or {}).get("delegations") or [])        if isinstance(input_data.state, dict)        else []    }    messages = _convert_messages(input_data)    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    yield encoder.encode(        StateSnapshotEvent(type=EventType.STATE_SNAPSHOT, snapshot=state)    )    while True:        response_text = ""        tool_calls: list[dict[str, Any]] = []        msg_id = f"msg-{run_id}-{len(messages)}"        yield encoder.encode(            TextMessageStartEvent(                type=EventType.TEXT_MESSAGE_START,                message_id=msg_id,                role="assistant",            )        )        async with client.messages.stream(            model=normalize_claude_model(                os.getenv("ANTHROPIC_MODEL", DEFAULT_ANTHROPIC_MODEL)            ),            max_tokens=2048,            system=SUPERVISOR_SYSTEM_PROMPT,            messages=messages,            tools=SUPERVISOR_TOOLS,        ) as stream:            current_tool_id: str | None = None            current_tool_name: str | None = None            current_tool_args = ""            async for event in stream:                etype = type(event).__name__                if etype == "RawContentBlockStartEvent":                    block = event.content_block  # type: ignore[attr-defined]                    if block.type == "tool_use":                        current_tool_id = block.id                        current_tool_name = block.name                        current_tool_args = ""                        yield encoder.encode(                            ToolCallStartEvent(                                type=EventType.TOOL_CALL_START,                                tool_call_id=current_tool_id,                                tool_call_name=current_tool_name,                                parent_message_id=msg_id,                            )                        )                elif etype == "RawContentBlockDeltaEvent":                    delta = event.delta  # type: ignore[attr-defined]                    if delta.type == "text_delta":                        response_text += delta.text                        yield encoder.encode(                            TextMessageContentEvent(                                type=EventType.TEXT_MESSAGE_CONTENT,                                message_id=msg_id,                                delta=delta.text,                            )                        )                    elif delta.type == "input_json_delta":                        current_tool_args += delta.partial_json                        yield encoder.encode(                            ToolCallArgsEvent(                                type=EventType.TOOL_CALL_ARGS,                                tool_call_id=current_tool_id or "",                                delta=delta.partial_json,                            )                        )                elif etype in (                    "RawContentBlockStopEvent",                    "ParsedContentBlockStopEvent",                ):                    if current_tool_id and current_tool_name:                        yield encoder.encode(                            ToolCallEndEvent(                                type=EventType.TOOL_CALL_END,                                tool_call_id=current_tool_id,                            )                        )                        parsed_args: dict[str, Any] | None                        try:                            parsed_args = (                                json.loads(current_tool_args)                                if current_tool_args                                else {}                            )                        except json.JSONDecodeError as exc:                            # Surface malformed tool args loudly instead of                            # silently substituting an empty dict — calling                            # a sub-agent with empty arguments is worse than                            # skipping the delegation outright.                            logger.warning(                                "subagents: failed to parse tool args for "                                "%s (id=%s): %s; raw=%r",                                current_tool_name,                                current_tool_id,                                exc,                                current_tool_args,                            )                            yield encoder.encode(                                RunErrorEvent(                                    type=EventType.RUN_ERROR,                                    message=(                                        f"Failed to parse arguments for tool "                                        f"'{current_tool_name}': {exc}"                                    ),                                    code="TOOL_ARGS_PARSE_ERROR",                                )                            )                            parsed_args = None                        if parsed_args is not None:                            tool_calls.append(                                {                                    "id": current_tool_id,                                    "name": current_tool_name,                                    "input": parsed_args,                                }                            )                        # else: skip this delegation entirely rather than                        # invoking the sub-agent with an empty task.                        current_tool_id = None                        current_tool_name = None                        current_tool_args = ""        yield encoder.encode(            TextMessageEndEvent(type=EventType.TEXT_MESSAGE_END, message_id=msg_id)        )        if not tool_calls:            break        # Persist supervisor turn into the message history.        assistant_content: list[dict[str, Any]] = []        if response_text:            assistant_content.append({"type": "text", "text": response_text})        for tc in tool_calls:            assistant_content.append(                {                    "type": "tool_use",                    "id": tc["id"],                    "name": tc["name"],                    "input": tc["input"],                }            )        messages.append({"role": "assistant", "content": assistant_content})        tool_results: list[dict[str, Any]] = []        for tc in tool_calls:            sub_agent = tc["name"]            task = (tc["input"] or {}).get("task", "")            if sub_agent not in SUB_AGENT_PROMPTS:                err = f"unknown sub-agent: {sub_agent}"                yield encoder.encode(                    ToolCallResultEvent(                        type=EventType.TOOL_CALL_RESULT,                        tool_call_id=tc["id"],                        message_id=f"{msg_id}-tool-result-{tc['id']}",                        content=err,                    )                )                tool_results.append(                    {                        "type": "tool_result",                        "tool_use_id": tc["id"],                        "content": err,                    }                )                continue            entry_id = str(uuid.uuid4())            entry: dict[str, Any] = {                "id": entry_id,                "sub_agent": sub_agent,                "task": task,                "status": "running",                "result": "",            }            state["delegations"] = [*state["delegations"], entry]            yield encoder.encode(                StateSnapshotEvent(type=EventType.STATE_SNAPSHOT, snapshot=state)            )            try:                result_text = await _invoke_sub_agent(client, sub_agent, task)                final_status = "completed"            except Exception as exc:  # noqa: BLE001 — surface any failure to UI                logger.exception("subagent: %s failed", sub_agent)                result_text = (                    f"sub-agent call failed: {exc.__class__.__name__} "                    "(see server logs for details)"                )                final_status = "failed"            # Mutate the matching entry in place. Using identity over the            # entry dict is safe because we control both ends of the list.            updated_delegations = []            for d in state["delegations"]:                if d.get("id") == entry_id:                    updated_delegations.append(                        {**d, "status": final_status, "result": result_text}                    )                else:                    updated_delegations.append(d)            state["delegations"] = updated_delegations            yield encoder.encode(                StateSnapshotEvent(type=EventType.STATE_SNAPSHOT, snapshot=state)            )            yield encoder.encode(                ToolCallResultEvent(                    type=EventType.TOOL_CALL_RESULT,                    tool_call_id=tc["id"],                    message_id=f"{msg_id}-tool-result-{tc['id']}",                    content=result_text,                )            )            tool_results.append(                {                    "type": "tool_result",                    "tool_use_id": tc["id"],                    "content": result_text,                }            )        messages.append({"role": "user", "content": tool_results})    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

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

### Represent subagents as delegation tools

The Claude Agent SDK demo keeps a supervisor prompt and exposes delegation tools for specialist agents. CopilotKit can then render delegation progress while the supervisor coordinates the run. Start by giving the supervisor one tool schema per specialist.

subagents_agent.py - supervisor tool schemas
    
    
    def _delegation_tool_schema(name: str, description: str) -> dict[str, Any]:
        return {
            "name": name,
            "description": description,
            "input_schema": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": (
                            "The full task description to hand to the "
                            "sub-agent. Pass relevant prior facts/drafts "
                            "verbatim — the sub-agent has no shared memory "
                            "with the supervisor."
                        ),
                    }
                },
                "required": ["task"],
            },
        }
    
    
    SUPERVISOR_TOOLS: list[dict[str, Any]] = [
        _delegation_tool_schema(
            "research_agent",
            "Delegate a research task. Returns a bulleted list of key facts.",
        ),
        _delegation_tool_schema(
            "writing_agent",
            (
                "Delegate a drafting task. Pass relevant facts in `task`. "
                "Returns a polished paragraph."
            ),
        ),
        _delegation_tool_schema(
            "critique_agent",
            "Delegate a critique task. Returns 2-3 actionable critiques.",
        ),
    ]

Each sub-agent is an isolated agent call with its own model, system prompt, and optional tools. They don't share memory or tools with the supervisor; the supervisor only ever sees what the sub-agent returns.

subagents_agent.py
    
    
    # Each sub-agent is defined by its own system prompt; `_invoke_sub_agent`# (below) issues a single-shot Anthropic call as that sub-agent. They# don't share memory or tools with the supervisor — the supervisor only# ever sees what the sub-agent returns as a tool result.SUB_AGENT_PROMPTS: dict[str, str] = {    "research_agent": (        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),    "writing_agent": (        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),    "critique_agent": (        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),}SUPERVISOR_SYSTEM_PROMPT = (    "You are a supervisor agent that coordinates three specialized "    "sub-agents to produce high-quality deliverables.\n\n"    "Available sub-agents (call them as tools):\n"    "  - research_agent: gathers facts on a topic.\n"    "  - writing_agent: turns facts + a brief into a polished draft.\n"    "  - critique_agent: reviews a draft and suggests improvements.\n\n"    "For most non-trivial user requests, delegate in sequence: "    "research -> write -> critique. Pass the relevant facts/draft "    "through the `task` argument of each tool. Keep your own messages "    "short — explain the plan once, delegate, then return a concise "    "summary once done. The UI shows the user a live log of every "    "sub-agent delegation, including the in-flight 'running' state.")# The supervisor delegates by calling tools. Each entry in# `SUPERVISOR_TOOLS` is an Anthropic tool schema that the supervisor LLM# "calls" to delegate work; the run loop in `run_subagents_agent` (see# the subagents-delegation-flow region) runs the matching sub-agent# synchronously, records the delegation into shared agent state, and# returns the sub-agent's output as a tool_result the supervisor can# read on its next step.def _delegation_tool_schema(name: str, description: str) -> dict[str, Any]:    return {        "name": name,        "description": description,        "input_schema": {            "type": "object",            "properties": {                "task": {                    "type": "string",                    "description": (                        "The full task description to hand to the "                        "sub-agent. Pass relevant prior facts/drafts "                        "verbatim — the sub-agent has no shared memory "                        "with the supervisor."                    ),                }            },            "required": ["task"],        },    }SUPERVISOR_TOOLS: list[dict[str, Any]] = [    _delegation_tool_schema(        "research_agent",        "Delegate a research task. Returns a bulleted list of key facts.",    ),    _delegation_tool_schema(        "writing_agent",        (            "Delegate a drafting task. Pass relevant facts in `task`. "            "Returns a polished paragraph."        ),    ),    _delegation_tool_schema(        "critique_agent",        "Delegate a critique task. Returns 2-3 actionable critiques.",    ),]async def _invoke_sub_agent(    client: anthropic.AsyncAnthropic,    sub_agent: str,    task: str,) -> str:    """Issue a single-shot Anthropic call as the named sub-agent.    Returns the concatenated text content of the response. Raises any    SDK exception so the caller can mark the delegation as ``failed``.    """    response = await client.messages.create(        model=normalize_claude_model(            os.getenv("ANTHROPIC_SUBAGENT_MODEL", DEFAULT_ANTHROPIC_MODEL)        ),        max_tokens=1024,        system=SUB_AGENT_PROMPTS[sub_agent],        messages=[{"role": "user", "content": task}],    )    parts: list[str] = []    for block in response.content:        if getattr(block, "type", None) == "text":            parts.append(getattr(block, "text", ""))    text = "".join(parts).strip()    if not text:        raise RuntimeError("sub-agent returned empty response")    return text

Keep sub-agent system prompts narrow and focused. The point of this pattern is that each one does one thing well. If a sub-agent needs to know the whole user context to do its job, that's a signal the boundary is wrong.

## Exposing sub-agents as tools#

The supervisor delegates by calling tools. Each delegation tool is a thin wrapper around a specialized agent call that:

  1. Runs the sub-agent on the supplied `task` string.
  2. Records the delegation into a `delegations` slot in shared agent state (so the UI can render a live log).
  3. Returns the sub-agent's final message as the tool result, which the supervisor sees on its next turn.



subagents_agent.py
    
    
    def _delegation_tool_schema(name: str, description: str) -> dict[str, Any]:    return {        "name": name,        "description": description,        "input_schema": {            "type": "object",            "properties": {                "task": {                    "type": "string",                    "description": (                        "The full task description to hand to the "                        "sub-agent. Pass relevant prior facts/drafts "                        "verbatim — the sub-agent has no shared memory "                        "with the supervisor."                    ),                }            },            "required": ["task"],        },    }SUPERVISOR_TOOLS: list[dict[str, Any]] = [    _delegation_tool_schema(        "research_agent",        "Delegate a research task. Returns a bulleted list of key facts.",    ),    _delegation_tool_schema(        "writing_agent",        (            "Delegate a drafting task. Pass relevant facts in `task`. "            "Returns a polished paragraph."        ),    ),    _delegation_tool_schema(        "critique_agent",        "Delegate a critique task. Returns 2-3 actionable critiques.",    ),]

This is where CopilotKit's shared-state channel earns its keep: the supervisor's tool calls mutate `delegations` as they happen, and the frontend renders every new entry live.

Give every delegation a stable `id` and merge new entries by that `id`. The client sends its copy of shared state back as run input on every run, so a slot that blindly appends whatever it receives — a LangGraph `Annotated[list, operator.add]` reducer, for example — concatenates the entries the client just echoed onto the ones the agent already has, and the log doubles when a thread is continued.

## Rendering a live delegation log#

On the frontend, the delegation log is a reactive render of the `delegations` slot.

Subscribe with `useAgent({ updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged] })`, read `agent.state.delegations`, and render one card per entry.

delegation-log.tsx
    
    
    /** * Live delegation log — renders the `delegations` slot of agent state. * * Each entry corresponds to one invocation of a sub-agent. The list * grows in real time as the supervisor fans work out to its children. * The parent header shows how many sub-agents have been called and * whether the supervisor is still running. */// Fixed list of the three sub-agent roles the supervisor can call.// Rendered as always-visible indicator chips at the top of the log// (regardless of whether the supervisor has delegated yet) so the user// — and the e2e suite — can see at a glance which sub-agents exist and// which are currently active.const INDICATOR_ROLES: ReadonlyArray<{  role: "researcher" | "writer" | "critic";  subAgent: SubAgentName;}> = [  { role: "researcher", subAgent: "research_agent" },  { role: "writer", subAgent: "writing_agent" },  { role: "critic", subAgent: "critique_agent" },];export function DelegationLog({ delegations, isRunning }: DelegationLogProps) {  const calledRoles = new Set<SubAgentName>(    delegations.map((d) => d.sub_agent),  );  return (    <div      data-testid="delegation-log"      className="w-full h-full flex flex-col bg-white rounded-2xl shadow-sm border border-[#DBDBE5] overflow-hidden"    >      <div className="flex items-center justify-between px-6 py-3 border-b border-[#E9E9EF] bg-[#FAFAFC]">        <div className="flex items-center gap-3">          <span className="text-lg font-semibold text-[#010507]">            Sub-agent delegations          </span>          {isRunning && (            <span              data-testid="supervisor-running"              className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full border border-[#BEC2FF] bg-[#BEC2FF1A] text-[#010507] text-[10px] font-semibold uppercase tracking-[0.12em]"            >              <span className="w-1.5 h-1.5 rounded-full bg-[#010507] animate-pulse" />              Supervisor running            </span>          )}        </div>        <span          data-testid="delegation-count"          className="text-xs font-mono text-[#838389]"        >          {delegations.length} calls        </span>      </div>      <div        data-testid="subagent-indicators"        className="flex items-center gap-2 border-b border-[#E9E9EF] bg-white px-6 py-2"      >        {INDICATOR_ROLES.map(({ role, subAgent }) => {          const style = SUB_AGENT_STYLE[subAgent];          const fired = calledRoles.has(subAgent);          return (            <span              key={role}              data-testid={`subagent-indicator-${role}`}              data-role={role}              data-fired={fired ? "true" : "false"}              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color} ${                fired ? "" : "opacity-60"              }`}            >              <span aria-hidden>{style.emoji}</span>              <span>{style.label}</span>            </span>          );        })}      </div>      <div className="flex-1 overflow-y-auto p-4 space-y-3">        {delegations.length === 0 ? (          <p className="text-[#838389] italic text-sm">            Ask the supervisor to complete a task. Every sub-agent it calls will            appear here.          </p>        ) : (          delegations.map((d, idx) => {            const style = SUB_AGENT_STYLE[d.sub_agent];            return (              <div                key={d.id}                data-testid="delegation-entry"                className="border border-[#E9E9EF] rounded-xl p-3 bg-[#FAFAFC]"              >                <div className="flex items-center justify-between mb-2">                  <div className="flex items-center gap-2">                    <span className="text-xs font-mono text-[#AFAFB7]">                      #{idx + 1}                    </span>                    <span                      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color}`}                    >                      <span>{style.emoji}</span>                      <span>{style.label}</span>                    </span>                  </div>                  <span className="text-[10px] uppercase tracking-[0.12em] font-semibold text-[#189370]">                    {d.status}                  </span>                </div>                <div className="text-xs text-[#57575B] mb-2">                  <span className="font-semibold text-[#010507]">Task: </span>                  {d.task}                </div>                <div className="text-sm text-[#010507] whitespace-pre-wrap bg-white rounded-lg p-2.5 border border-[#E9E9EF]">                  {d.result}                </div>              </div>            );          })        )}      </div>    </div>  );}

The result: as the supervisor fans work out to its sub-agents, the log grows in real time, giving the user visibility into a process that would otherwise be a long opaque spinner.

## Related#

  * **[Shared State](https://docs.copilotkit.ai/claude-sdk-python/shared-state)** — the channel that makes the delegation log live.
  * **[State streaming](https://docs.copilotkit.ai/claude-sdk-python/shared-state/streaming)** — stream _individual_ sub-agent outputs token-by-token inside each log entry.


