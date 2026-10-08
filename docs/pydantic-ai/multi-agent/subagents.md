---
url: https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents/
title: Sub-Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:22.339864+00:00
---

# Sub-Agents

> Source: https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

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
    
    
    """PydanticAI agent backing the Sub-Agents demo.Mirrors langgraph-python/src/agents/subagents.py andgoogle-adk/src/agents/subagents_agent.py: a top-level "supervisor":class:`Agent` orchestrates three specialised sub-:class:`Agent`instances (research / writing / critique) via tools. Each delegationappends an entry to the ``delegations`` slot of shared agent state sothe UI can render a live delegation log.PydanticAI specifics--------------------* Each sub-agent is a real ``Agent(model=..., system_prompt=...)`` that  the supervisor invokes via ``await Agent.run(...)``. The supervisor  itself runs inside an async event loop (the AG-UI handler awaits  ``agent.run``); calling ``run_sync`` from a tool would attempt to  start a nested loop and raise ``RuntimeError``.* Each delegation tool is an async ``@supervisor.tool`` that    1) appends a "running" entry to ``ctx.deps.state.delegations``       and emits a ``StateSnapshotEvent`` so the UI updates immediately,    2) runs the sub-agent,    3) flips the entry to ``"completed"`` (or ``"failed"``) and emits a       second ``StateSnapshotEvent`` with the final result.The supervisor and sub-agents do not share memory — only the supervisorsees a sub-agent's return value, exactly like the LangGraph-Python andGoogle ADK references."""from __future__ import annotationsimport loggingimport uuidfrom typing import Any, Literalfrom pydantic import BaseModel, Fieldfrom pydantic_ai import Agent, RunContextfrom pydantic_ai.ui import StateDepsfrom pydantic_ai.models.openai import OpenAIResponsesModellogger = logging.getLogger(__name__)SubAgentName = Literal["research_agent", "writing_agent", "critique_agent"]DelegationStatus = Literal["running", "completed", "failed"]# ── Shared state ────────────────────────────────────────────────────class Delegation(BaseModel):    """One sub-agent invocation, surfaced in the UI's delegation log."""    id: str    sub_agent: str  # SubAgentName at runtime; widened so model_dump round-trips    task: str    status: str  # DelegationStatus at runtime    result: str = ""class SubagentsState(BaseModel):    """Shared state. ``delegations`` is rendered as a live log in the UI."""    delegations: list[Delegation] = Field(default_factory=list)# ── Sub-agents (real PydanticAI Agents) ─────────────────────────────# Each sub-agent is a full-fledged ``Agent(model=..., system_prompt=...)``# with its own system prompt. They don't share memory or tools with the# supervisor — the supervisor only sees their return value._SUB_MODEL = OpenAIResponsesModel("gpt-5-mini")_research_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),)_writing_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),)_critique_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),)async def _invoke_sub_agent(sub_agent: Agent[None, str], task: str) -> str:    """Run a sub-agent on ``task`` and return its final text output.    Uses the async ``Agent.run`` API rather than ``run_sync`` because the    supervisor itself executes inside a running event loop (AG-UI awaits    ``agent.run``); ``run_sync`` from inside a running loop raises    ``RuntimeError: This event loop is already running``.    """    result = await sub_agent.run(task)    output: Any = result.output    return str(output) if output is not None else ""# ── Supervisor ──────────────────────────────────────────────────────_SUPERVISOR_PROMPT = (    "You are a supervisor agent that coordinates three specialized "    "sub-agents to produce high-quality deliverables.\n\n"    "Available sub-agents (call them as tools):\n"    "  - research_agent: gathers facts on a topic.\n"    "  - writing_agent: turns facts + a brief into a polished draft.\n"    "  - critique_agent: reviews a draft and suggests improvements.\n\n"    "For most non-trivial user requests, delegate in sequence: research -> "    "write -> critique. Pass the relevant facts/draft through the `task` "    "argument of each tool. Each tool returns the sub-agent's output as a "    "string. Keep your own messages short — explain the plan once, "    "delegate, then return a concise summary once done. The UI shows the "    "user a live log of every sub-agent delegation, including the "    "in-flight 'running' state.")agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    deps_type=StateDeps[SubagentsState],    system_prompt=_SUPERVISOR_PROMPT,)def _append_running(    ctx: RunContext[StateDeps[SubagentsState]],    *,    sub_agent: SubAgentName,    task: str,) -> str:    """Append a ``running`` delegation entry and return its id."""    entry = Delegation(        id=str(uuid.uuid4()),        sub_agent=sub_agent,        task=task,        status="running",        result="",    )    ctx.deps.state.delegations = [*ctx.deps.state.delegations, entry]    return entry.iddef _finalise(    ctx: RunContext[StateDeps[SubagentsState]],    *,    entry_id: str,    status: DelegationStatus,    result: str,) -> None:    """Mutate the delegation entry with ``entry_id`` to its terminal state.    If the entry has gone missing (e.g. another part of the system replaced    ``state.delegations`` mid-turn) we log a warning and skip rather than    appending a synthetic entry — same defensive choice as google-adk's    ``_update_delegation``.    """    delegations = list(ctx.deps.state.delegations)    for idx, entry in enumerate(delegations):        if entry.id == entry_id:            delegations[idx] = entry.model_copy(                update={"status": status, "result": result}            )            ctx.deps.state.delegations = delegations            return    logger.warning(        "subagents: delegation entry %s missing on update — final %s state "        "(result_length=%d) will not be rendered",        entry_id,        status,        len(result),    )# ── Delegation tools ────────────────────────────────────────────────async def _delegate(    ctx: RunContext[StateDeps[SubagentsState]],    *,    sub_agent: SubAgentName,    sub_agent_obj: Agent[None, str],    task: str,) -> str:    """Common delegation flow: append running → invoke → finalise.    Returns the sub-agent's output text so the supervisor LLM can read it    on its next step. State mutations (running entry + final entry) are    written through ``ctx.deps.state``; PydanticAI's AG-UI bridge syncs    those back to the frontend at end-of-turn so the delegation log    re-renders automatically.    """    entry_id = _append_running(ctx, sub_agent=sub_agent, task=task)    try:        result = await _invoke_sub_agent(sub_agent_obj, task)    except Exception as exc:  # noqa: BLE001 — surface failure to supervisor        logger.exception("subagents: %s failed", sub_agent)        message = (            f"sub-agent {sub_agent} failed: {exc.__class__.__name__} "            "(see server logs for details)"        )        _finalise(ctx, entry_id=entry_id, status="failed", result=message)        return message    _finalise(ctx, entry_id=entry_id, status="completed", result=result)    return result# Each ``@agent.tool`` wraps a sub-agent invocation. The supervisor LLM# "calls" these tools to delegate work; each call asynchronously runs the# matching sub-agent, records the delegation into shared state, and# returns the sub-agent's output as a string the supervisor can read on# its next step.@agent.toolasync def research_agent(    ctx: RunContext[StateDeps[SubagentsState]],    task: str,) -> str:    """Delegate a research task to the research sub-agent.    Use for: gathering facts, background, definitions, statistics.    Returns a bulleted list of key facts.    """    return await _delegate(        ctx,        sub_agent="research_agent",        sub_agent_obj=_research_agent,        task=task,    )@agent.toolasync def writing_agent(    ctx: RunContext[StateDeps[SubagentsState]],    task: str,) -> str:    """Delegate a drafting task to the writing sub-agent.    Use for: producing a polished paragraph, draft, or summary. Pass    relevant facts from prior research inside ``task``.    """    return await _delegate(        ctx,        sub_agent="writing_agent",        sub_agent_obj=_writing_agent,        task=task,    )@agent.toolasync def critique_agent(    ctx: RunContext[StateDeps[SubagentsState]],    task: str,) -> str:    """Delegate a critique task to the critique sub-agent.    Use for: reviewing a draft and suggesting concrete improvements.    """    return await _delegate(        ctx,        sub_agent="critique_agent",        sub_agent_obj=_critique_agent,        task=task,    )__all__: list[str] = [    "SubagentsState",    "Delegation",    "agent",]

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

Each sub-agent is an isolated agent call with its own model, system prompt, and optional tools. They don't share memory or tools with the supervisor; the supervisor only ever sees what the sub-agent returns.

subagents.py
    
    
    from __future__ import annotationsimport loggingimport uuidfrom typing import Any, Literalfrom pydantic import BaseModel, Fieldfrom pydantic_ai import Agent, RunContextfrom pydantic_ai.ui import StateDepsfrom pydantic_ai.models.openai import OpenAIResponsesModellogger = logging.getLogger(__name__)SubAgentName = Literal["research_agent", "writing_agent", "critique_agent"]DelegationStatus = Literal["running", "completed", "failed"]# ── Shared state ────────────────────────────────────────────────────class Delegation(BaseModel):    """One sub-agent invocation, surfaced in the UI's delegation log."""    id: str    sub_agent: str  # SubAgentName at runtime; widened so model_dump round-trips    task: str    status: str  # DelegationStatus at runtime    result: str = ""class SubagentsState(BaseModel):    """Shared state. ``delegations`` is rendered as a live log in the UI."""    delegations: list[Delegation] = Field(default_factory=list)# ── Sub-agents (real PydanticAI Agents) ─────────────────────────────# Each sub-agent is a full-fledged ``Agent(model=..., system_prompt=...)``# with its own system prompt. They don't share memory or tools with the# supervisor — the supervisor only sees their return value._SUB_MODEL = OpenAIResponsesModel("gpt-5-mini")_research_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),)_writing_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),)_critique_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),)

Keep sub-agent system prompts narrow and focused. The point of this pattern is that each one does one thing well. If a sub-agent needs to know the whole user context to do its job, that's a signal the boundary is wrong.

## Exposing sub-agents as tools#

The supervisor delegates by calling tools. Each delegation tool is a thin wrapper around a specialized agent call that:

  1. Runs the sub-agent on the supplied `task` string.
  2. Records the delegation into a `delegations` slot in shared agent state (so the UI can render a live log).
  3. Returns the sub-agent's final message as the tool result, which the supervisor sees on its next turn.



subagents.py
    
    
    from __future__ import annotationsimport loggingimport uuidfrom typing import Any, Literalfrom pydantic import BaseModel, Fieldfrom pydantic_ai import Agent, RunContextfrom pydantic_ai.ui import StateDepsfrom pydantic_ai.models.openai import OpenAIResponsesModellogger = logging.getLogger(__name__)SubAgentName = Literal["research_agent", "writing_agent", "critique_agent"]DelegationStatus = Literal["running", "completed", "failed"]# ── Shared state ────────────────────────────────────────────────────class Delegation(BaseModel):    """One sub-agent invocation, surfaced in the UI's delegation log."""    id: str    sub_agent: str  # SubAgentName at runtime; widened so model_dump round-trips    task: str    status: str  # DelegationStatus at runtime    result: str = ""class SubagentsState(BaseModel):    """Shared state. ``delegations`` is rendered as a live log in the UI."""    delegations: list[Delegation] = Field(default_factory=list)# ── Sub-agents (real PydanticAI Agents) ─────────────────────────────# Each sub-agent is a full-fledged ``Agent(model=..., system_prompt=...)``# with its own system prompt. They don't share memory or tools with the# supervisor — the supervisor only sees their return value._SUB_MODEL = OpenAIResponsesModel("gpt-5-mini")_research_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are a research sub-agent. Given a topic, produce a concise "        "bulleted list of 3-5 key facts. No preamble, no closing."    ),)_writing_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are a writing sub-agent. Given a brief and optional source "        "facts, produce a polished 1-paragraph draft. Be clear and "        "concrete. No preamble."    ),)_critique_agent: Agent[None, str] = Agent(    model=_SUB_MODEL,    system_prompt=(        "You are an editorial critique sub-agent. Given a draft, give "        "2-3 crisp, actionable critiques. No preamble."    ),)async def _invoke_sub_agent(sub_agent: Agent[None, str], task: str) -> str:    """Run a sub-agent on ``task`` and return its final text output.    Uses the async ``Agent.run`` API rather than ``run_sync`` because the    supervisor itself executes inside a running event loop (AG-UI awaits    ``agent.run``); ``run_sync`` from inside a running loop raises    ``RuntimeError: This event loop is already running``.    """    result = await sub_agent.run(task)    output: Any = result.output    return str(output) if output is not None else ""# ── Supervisor ──────────────────────────────────────────────────────_SUPERVISOR_PROMPT = (    "You are a supervisor agent that coordinates three specialized "    "sub-agents to produce high-quality deliverables.\n\n"    "Available sub-agents (call them as tools):\n"    "  - research_agent: gathers facts on a topic.\n"    "  - writing_agent: turns facts + a brief into a polished draft.\n"    "  - critique_agent: reviews a draft and suggests improvements.\n\n"    "For most non-trivial user requests, delegate in sequence: research -> "    "write -> critique. Pass the relevant facts/draft through the `task` "    "argument of each tool. Each tool returns the sub-agent's output as a "    "string. Keep your own messages short — explain the plan once, "    "delegate, then return a concise summary once done. The UI shows the "    "user a live log of every sub-agent delegation, including the "    "in-flight 'running' state.")agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    deps_type=StateDeps[SubagentsState],    system_prompt=_SUPERVISOR_PROMPT,)def _append_running(    ctx: RunContext[StateDeps[SubagentsState]],    *,    sub_agent: SubAgentName,    task: str,) -> str:    """Append a ``running`` delegation entry and return its id."""    entry = Delegation(        id=str(uuid.uuid4()),        sub_agent=sub_agent,        task=task,        status="running",        result="",    )    ctx.deps.state.delegations = [*ctx.deps.state.delegations, entry]    return entry.iddef _finalise(    ctx: RunContext[StateDeps[SubagentsState]],    *,    entry_id: str,    status: DelegationStatus,    result: str,) -> None:    """Mutate the delegation entry with ``entry_id`` to its terminal state.    If the entry has gone missing (e.g. another part of the system replaced    ``state.delegations`` mid-turn) we log a warning and skip rather than    appending a synthetic entry — same defensive choice as google-adk's    ``_update_delegation``.    """    delegations = list(ctx.deps.state.delegations)    for idx, entry in enumerate(delegations):        if entry.id == entry_id:            delegations[idx] = entry.model_copy(                update={"status": status, "result": result}            )            ctx.deps.state.delegations = delegations            return    logger.warning(        "subagents: delegation entry %s missing on update — final %s state "        "(result_length=%d) will not be rendered",        entry_id,        status,        len(result),    )# ── Delegation tools ────────────────────────────────────────────────async def _delegate(    ctx: RunContext[StateDeps[SubagentsState]],    *,    sub_agent: SubAgentName,    sub_agent_obj: Agent[None, str],    task: str,) -> str:    """Common delegation flow: append running → invoke → finalise.    Returns the sub-agent's output text so the supervisor LLM can read it    on its next step. State mutations (running entry + final entry) are    written through ``ctx.deps.state``; PydanticAI's AG-UI bridge syncs    those back to the frontend at end-of-turn so the delegation log    re-renders automatically.    """    entry_id = _append_running(ctx, sub_agent=sub_agent, task=task)    try:        result = await _invoke_sub_agent(sub_agent_obj, task)    except Exception as exc:  # noqa: BLE001 — surface failure to supervisor        logger.exception("subagents: %s failed", sub_agent)        message = (            f"sub-agent {sub_agent} failed: {exc.__class__.__name__} "            "(see server logs for details)"        )        _finalise(ctx, entry_id=entry_id, status="failed", result=message)        return message    _finalise(ctx, entry_id=entry_id, status="completed", result=result)    return result# Each ``@agent.tool`` wraps a sub-agent invocation. The supervisor LLM# "calls" these tools to delegate work; each call asynchronously runs the# matching sub-agent, records the delegation into shared state, and# returns the sub-agent's output as a string the supervisor can read on# its next step.@agent.toolasync def research_agent(    ctx: RunContext[StateDeps[SubagentsState]],    task: str,) -> str:    """Delegate a research task to the research sub-agent.    Use for: gathering facts, background, definitions, statistics.    Returns a bulleted list of key facts.    """    return await _delegate(        ctx,        sub_agent="research_agent",        sub_agent_obj=_research_agent,        task=task,    )@agent.toolasync def writing_agent(    ctx: RunContext[StateDeps[SubagentsState]],    task: str,) -> str:    """Delegate a drafting task to the writing sub-agent.    Use for: producing a polished paragraph, draft, or summary. Pass    relevant facts from prior research inside ``task``.    """    return await _delegate(        ctx,        sub_agent="writing_agent",        sub_agent_obj=_writing_agent,        task=task,    )@agent.toolasync def critique_agent(    ctx: RunContext[StateDeps[SubagentsState]],    task: str,) -> str:    """Delegate a critique task to the critique sub-agent.    Use for: reviewing a draft and suggesting concrete improvements.    """    return await _delegate(        ctx,        sub_agent="critique_agent",        sub_agent_obj=_critique_agent,        task=task,    )

This is where CopilotKit's shared-state channel earns its keep: the supervisor's tool calls mutate `delegations` as they happen, and the frontend renders every new entry live.

Give every delegation a stable `id` and merge new entries by that `id`. The client sends its copy of shared state back as run input on every run, so a slot that blindly appends whatever it receives — a LangGraph `Annotated[list, operator.add]` reducer, for example — concatenates the entries the client just echoed onto the ones the agent already has, and the log doubles when a thread is continued.

## Rendering a live delegation log#

On the frontend, the delegation log is a reactive render of the `delegations` slot.

Subscribe with `useAgent({ updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged] })`, read `agent.state.delegations`, and render one card per entry.

delegation-log.tsx
    
    
    /** * Live delegation log — renders the `delegations` slot of agent state. * * Each entry corresponds to one invocation of a sub-agent. The list * grows in real time as the supervisor fans work out to its children. * The parent header shows how many sub-agents have been called and * whether the supervisor is still running. */// Fixed list of the three sub-agent roles the supervisor can call.// Rendered as always-visible indicator chips at the top of the log// (regardless of whether the supervisor has delegated yet) so the user// — and the e2e suite — can see at a glance which sub-agents exist and// which are currently active.const INDICATOR_ROLES: ReadonlyArray<{  role: "researcher" | "writer" | "critic";  subAgent: SubAgentName;}> = [  { role: "researcher", subAgent: "research_agent" },  { role: "writer", subAgent: "writing_agent" },  { role: "critic", subAgent: "critique_agent" },];export function DelegationLog({ delegations, isRunning }: DelegationLogProps) {  const calledRoles = new Set<SubAgentName>(    delegations.map((d) => d.sub_agent),  );  return (    <div      data-testid="delegation-log"      className="w-full h-full flex flex-col bg-white rounded-2xl shadow-sm border border-[#DBDBE5] overflow-hidden"    >      <div className="flex items-center justify-between px-6 py-3 border-b border-[#E9E9EF] bg-[#FAFAFC]">        <div className="flex items-center gap-3">          <span className="text-lg font-semibold text-[#010507]">            Sub-agent delegations          </span>          {isRunning && (            <span              data-testid="supervisor-running"              className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full border border-[#BEC2FF] bg-[#BEC2FF1A] text-[#010507] text-[10px] font-semibold uppercase tracking-[0.12em]"            >              <span className="w-1.5 h-1.5 rounded-full bg-[#010507] animate-pulse" />              Supervisor running            </span>          )}        </div>        <span          data-testid="delegation-count"          className="text-xs font-mono text-[#838389]"        >          {delegations.length} calls        </span>      </div>      <div        data-testid="subagent-indicators"        className="flex items-center gap-2 border-b border-[#E9E9EF] bg-white px-6 py-2"      >        {INDICATOR_ROLES.map(({ role, subAgent }) => {          const style = SUB_AGENT_STYLE[subAgent];          const fired = calledRoles.has(subAgent);          return (            <span              key={role}              data-testid={`subagent-indicator-${role}`}              data-role={role}              data-fired={fired ? "true" : "false"}              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color} ${                fired ? "" : "opacity-60"              }`}            >              <span aria-hidden>{style.emoji}</span>              <span>{style.label}</span>            </span>          );        })}      </div>      <div className="flex-1 overflow-y-auto p-4 space-y-3">        {delegations.length === 0 ? (          <p className="text-[#838389] italic text-sm">            Ask the supervisor to complete a task. Every sub-agent it calls will            appear here.          </p>        ) : (          delegations.map((d, idx) => {            const style = SUB_AGENT_STYLE[d.sub_agent];            return (              <div                key={d.id}                data-testid="delegation-entry"                className="border border-[#E9E9EF] rounded-xl p-3 bg-[#FAFAFC]"              >                <div className="flex items-center justify-between mb-2">                  <div className="flex items-center gap-2">                    <span className="text-xs font-mono text-[#AFAFB7]">                      #{idx + 1}                    </span>                    <span                      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color}`}                    >                      <span>{style.emoji}</span>                      <span>{style.label}</span>                    </span>                  </div>                  <span className="text-[10px] uppercase tracking-[0.12em] font-semibold text-[#189370]">                    {d.status}                  </span>                </div>                <div className="text-xs text-[#57575B] mb-2">                  <span className="font-semibold text-[#010507]">Task: </span>                  {d.task}                </div>                <div className="text-sm text-[#010507] whitespace-pre-wrap bg-white rounded-lg p-2.5 border border-[#E9E9EF]">                  {d.result}                </div>              </div>            );          })        )}      </div>    </div>  );}

The result: as the supervisor fans work out to its sub-agents, the log grows in real time, giving the user visibility into a process that would otherwise be a long opaque spinner.

## Related#

  * **[Shared State](https://docs.copilotkit.ai/pydantic-ai/shared-state)** — the channel that makes the delegation log live.
  * **[State streaming](https://docs.copilotkit.ai/pydantic-ai/shared-state/streaming)** — stream _individual_ sub-agent outputs token-by-token inside each log entry.


