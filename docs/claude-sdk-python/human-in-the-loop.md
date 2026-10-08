---
url: https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:25.072191+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/

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

On this page

InteractivityHuman-in-the-loop

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

hitl_in_chat_agent.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """Claude Agent SDK backend for the In-Chat HITL (useHumanInTheLoop) demo.The `book_call` tool is defined on the FRONTEND via `useHumanInTheLoop`,so there is no backend tool here. The agent simply responds in chat andrelies on the standard frontend-tool / tool-call lifecycle to invoke`book_call` when the user asks to book.Mirrors the langgraph-python `hitl_in_chat_agent.py` reference."""from __future__ import annotationsimport jsonimport osimport tracebackfrom collections.abc import AsyncIteratorfrom textwrap import dedentfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunFinishedEvent,    RunStartedEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,    ToolCallArgsEvent,    ToolCallEndEvent,    ToolCallStartEvent,)from ag_ui.encoder import EventEncoderfrom agents.claude_agent_sdk_adapter import normalize_claude_modelSYSTEM_PROMPT = dedent("""    You help users book an onboarding call with the sales team. When they    ask to book a call, call the frontend-provided `book_call` tool with a    short topic and the user's name (use a sensible placeholder like    'Alice from Sales' if no attendee was specified). Keep any chat reply    to one short sentence.""").strip()async def run_hitl_in_chat_agent(input_data: RunAgentInput) -> AsyncIterator[str]:    """Stream a Claude response that may call the frontend `book_call` tool.    `book_call` is defined on the frontend via `useHumanInTheLoop`. AG-UI    forwards frontend tool definitions in `input_data.tools`, so we just    pass them straight to Claude and let the standard tool-call lifecycle    resolve the user's choice back through CopilotKit.    """    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    # Convert AG-UI messages to Anthropic format.    #    # AG-UI delivers three message roles:    #   - "user"      → plain user text    #   - "assistant" → assistant text + optional tool_use blocks    #   - "tool"      → tool result from a resolved frontend tool    #    # When the CopilotKit runtime re-invokes this agent after the user    # resolves a frontend tool (e.g. picks a time slot in the book_call    # HITL UI), the messages array includes:    #   1. assistant message with tool_use content (the original tool call)    #   2. tool message with the resolved result    #    # Anthropic's Messages API represents tool results as a "user" role    # message with content blocks of type "tool_result". We must convert    # AG-UI "tool" messages into that shape, and assistant messages with    # tool_use content into Anthropic's structured format, so the LLM    # sees the full conversation and aimock's ``hasToolResult`` matcher    # fires correctly.    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        # Handle tool result messages from AG-UI (resolved frontend tools).        if role == "tool":            tool_call_id = getattr(msg, "tool_call_id", None) or (                getattr(msg, "toolCallId", None)            )            raw = getattr(msg, "content", None)            result_text = ""            if isinstance(raw, str):                result_text = raw            elif isinstance(raw, list):                parts = []                for part in raw:                    if hasattr(part, "text"):                        parts.append(part.text)                    elif isinstance(part, dict) and "text" in part:                        parts.append(part["text"])                parts_text = "".join(parts)                if parts_text:                    result_text = parts_text                else:                    result_text = json.dumps(raw)            if tool_call_id:                messages.append(                    {                        "role": "user",                        "content": [                            {                                "type": "tool_result",                                "tool_use_id": tool_call_id,                                "content": result_text,                            }                        ],                    }                )            continue        if role not in ("user", "assistant"):            continue        raw = getattr(msg, "content", None)        # For assistant messages, check for tool calls (AG-UI's        # AssistantMessage stores them in `tool_calls`, not in `content`).        # Anthropic requires tool_use blocks in the assistant content so        # the subsequent tool_result can pair with them.        if role == "assistant":            msg_tool_calls = getattr(msg, "tool_calls", None)            text_content = ""            if isinstance(raw, str):                text_content = raw            elif isinstance(raw, list):                for part in raw:                    if hasattr(part, "text"):                        text_content += part.text                    elif isinstance(part, dict) and "text" in part:                        text_content += part["text"]            if msg_tool_calls:                content_blocks: list[dict[str, Any]] = []                if text_content:                    content_blocks.append({"type": "text", "text": text_content})                for tc in msg_tool_calls:                    tc_id = getattr(tc, "id", None) or (                        tc.get("id") if isinstance(tc, dict) else None                    )                    func = getattr(tc, "function", None) or (                        tc.get("function") if isinstance(tc, dict) else None                    )                    if func:                        tc_name = getattr(func, "name", None) or (                            func.get("name") if isinstance(func, dict) else "unknown"                        )                        tc_args_str = getattr(func, "arguments", None) or (                            func.get("arguments", "{}")                            if isinstance(func, dict)                            else "{}"                        )                    else:                        tc_name = "unknown"                        tc_args_str = "{}"                    try:                        tc_args = (                            json.loads(tc_args_str)                            if isinstance(tc_args_str, str)                            else tc_args_str                        )                    except json.JSONDecodeError:                        tc_args = {}                    content_blocks.append(                        {                            "type": "tool_use",                            "id": tc_id or "unknown",                            "name": tc_name,                            "input": tc_args,                        }                    )                messages.append({"role": "assistant", "content": content_blocks})                continue            elif text_content:                messages.append({"role": "assistant", "content": text_content})                continue        content = ""        if isinstance(raw, str):            content = raw        elif isinstance(raw, list):            parts = []            for part in raw:                if hasattr(part, "text"):                    parts.append(part.text)                elif isinstance(part, dict) and "text" in part:                    parts.append(part["text"])            content = "".join(parts)        if content:            messages.append({"role": role, "content": content})    # Forward frontend-defined tools (including useHumanInTheLoop's `book_call`)    # to Claude. AG-UI sends them in `input_data.tools` with JSON-Schema    # parameters; Claude expects `input_schema` of the same shape.    tools: list[dict[str, Any]] = []    for t in input_data.tools or []:        # AG-UI Tool schema: { name, description, parameters }        name = getattr(t, "name", None) or (            t.get("name") if isinstance(t, dict) else None        )        description = getattr(t, "description", None) or (            t.get("description", "") if isinstance(t, dict) else ""        )        parameters = getattr(t, "parameters", None) or (            t.get("parameters", {}) if isinstance(t, dict) else {}        )        if not name:            continue        tools.append(            {                "name": name,                "description": description or "",                "input_schema": parameters or {"type": "object", "properties": {}},            }        )    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    msg_id = f"msg-{run_id}-0"    yield encoder.encode(        TextMessageStartEvent(            type=EventType.TEXT_MESSAGE_START,            message_id=msg_id,            role="assistant",        )    )    stream_kwargs: dict[str, Any] = {        "model": normalize_claude_model(            os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")        ),        "max_tokens": 1024,        "system": SYSTEM_PROMPT,        "messages": messages,    }    if tools:        stream_kwargs["tools"] = tools  # type: ignore[assignment]    try:        async with client.messages.stream(**stream_kwargs) as stream:            current_tool_id: str | None = None            current_tool_name: str | None = None            async for event in stream:                etype = type(event).__name__                if etype == "RawContentBlockStartEvent":                    block = event.content_block  # type: ignore[attr-defined]                    if block.type == "tool_use":                        current_tool_id = block.id                        current_tool_name = block.name                        yield encoder.encode(                            ToolCallStartEvent(                                type=EventType.TOOL_CALL_START,                                tool_call_id=current_tool_id,                                tool_call_name=current_tool_name,                                parent_message_id=msg_id,                            )                        )                elif etype == "RawContentBlockDeltaEvent":                    delta = event.delta  # type: ignore[attr-defined]                    if delta.type == "text_delta":                        yield encoder.encode(                            TextMessageContentEvent(                                type=EventType.TEXT_MESSAGE_CONTENT,                                message_id=msg_id,                                delta=delta.text,                            )                        )                    elif delta.type == "input_json_delta":                        yield encoder.encode(                            ToolCallArgsEvent(                                type=EventType.TOOL_CALL_ARGS,                                tool_call_id=current_tool_id or "",                                delta=delta.partial_json,                            )                        )                elif etype in (                    "RawContentBlockStopEvent",                    "ParsedContentBlockStopEvent",                ):                    if current_tool_id:                        yield encoder.encode(                            ToolCallEndEvent(                                type=EventType.TOOL_CALL_END,                                tool_call_id=current_tool_id,                            )                        )                        current_tool_id = None                        current_tool_name = None    except Exception:        err_text = f"Agent error: {traceback.format_exc()}"        yield encoder.encode(            TextMessageContentEvent(                type=EventType.TEXT_MESSAGE_CONTENT,                message_id=msg_id,                delta=err_text,            )        )    yield encoder.encode(        TextMessageEndEvent(            type=EventType.TEXT_MESSAGE_END,            message_id=msg_id,        )    )    # Frontend (`useHumanInTheLoop`) resolves `book_call` and the runtime    # injects the resolution back into a follow-up turn. Each turn is its    # own POST so we don't loop here — emitting RUN_FINISHED returns control    # to the runtime, which will re-invoke us with the resolved tool result.    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/claude-sdk-python/inspector).

## What is this?#

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?#

Use HITL when you need:

  * **Quality control** — a human gate at high-stakes decision points
  * **Edge cases** — graceful fallbacks when the agent's confidence is low
  * **Expert input** — lean on the user for domain knowledge the model lacks
  * **Reliability** — a more robust loop for real-world, production traffic



## Two patterns for HITL in CopilotKit#

### Model approvals as async frontend tools

Claude Agent SDK human-in-the-loop demos use CopilotKit's promise-based frontend tool flow. The agent calls an approval tool, the UI resolves the tool result after the user decides, and the same Claude run continues with that result. Register the approval UI from the page component.

page.tsx - useHumanInTheLoop
    
    
    useHumanInTheLoop({
      agentId: "hitl-in-chat",
      name: "book_call",
      description:
        "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",
      parameters: z.object({
        topic: z
          .string()
          .describe("What the call is about (e.g. 'Intro with sales')"),
        attendee: z
          .string()
          .describe("Who the call is with (e.g. 'Alice from Sales')"),
      }),
      render: ({ args, status, respond }: any) => (
        <TimePickerCard
          topic={args?.topic ?? "a call"}
          attendee={args?.attendee}
          slots={slots}
          status={status}
          onSubmit={(result) => respond?.(result)}
        />
      ),
    });

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes) but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| The **graph** , by calling `interrupt(...)` during a node| A server-side `interrupt()` call in your LangGraph agent  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision — the model chose to ask the user — and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a _graph-enforced_ checkpoint — the code path deterministically requires a human answer — and you want `langgraph.interrupt()` as the server-side contract.

## Pattern 1 — `useHumanInTheLoop` (tool-based)#

The agent registers a HITL tool on the client with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit routes the call through your `render` function, which shows a custom component and calls `respond` with the user's answer. The agent sees the answer as the tool result and continues from there.

page.tsx
    
    
    import React, { useMemo } from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";function buildDefaultSlots(now = new Date()): TimeSlot[] {  const tomorrow = new Date(now);  tomorrow.setDate(tomorrow.getDate() + 1);  const monday = new Date(now);  const daysUntilMonday = (8 - monday.getDay()) % 7 || 7;  monday.setDate(monday.getDate() + daysUntilMonday);  return [    buildSlot(tomorrow, "Tomorrow", 10, 0),    buildSlot(tomorrow, "Tomorrow", 14, 0),    buildSlot(monday, "Monday", 9, 0),    buildSlot(monday, "Monday", 15, 30),  ];}function buildSlot(  date: Date,  labelPrefix: string,  hour: number,  minute: number,): TimeSlot {  const slotDate = new Date(date);  slotDate.setHours(hour, minute, 0, 0);  return {    label: `${labelPrefix} ${formatTime(slotDate)}`,    iso: slotDate.toISOString(),  };}function formatTime(date: Date): string {  return date.toLocaleTimeString([], {    hour: "numeric",    minute: "2-digit",  });}export default function HitlInChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  const slots = useMemo(() => buildDefaultSlots(), []);  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message:          "Please book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  useHumanInTheLoop({    agentId: "hitl-in-chat",    name: "book_call",    description:      "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",    parameters: z.object({      topic: z        .string()        .describe("What the call is about (e.g. 'Intro with sales')"),      attendee: z        .string()        .describe("Who the call is with (e.g. 'Alice from Sales')"),    }),    render: ({ args, status, respond }: any) => (      <TimePickerCard        topic={args?.topic ?? "a call"}        attendee={args?.attendee}        slots={slots}        status={status}        onSubmit={(result) => respond?.(result)}      />    ),  });

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

page.tsx
    
    
    import React, { useMemo } from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";function buildDefaultSlots(now = new Date()): TimeSlot[] {  const tomorrow = new Date(now);  tomorrow.setDate(tomorrow.getDate() + 1);  const monday = new Date(now);  const daysUntilMonday = (8 - monday.getDay()) % 7 || 7;  monday.setDate(monday.getDate() + daysUntilMonday);  return [    buildSlot(tomorrow, "Tomorrow", 10, 0),    buildSlot(tomorrow, "Tomorrow", 14, 0),    buildSlot(monday, "Monday", 9, 0),    buildSlot(monday, "Monday", 15, 30),  ];}function buildSlot(  date: Date,  labelPrefix: string,  hour: number,  minute: number,): TimeSlot {  const slotDate = new Date(date);  slotDate.setHours(hour, minute, 0, 0);  return {    label: `${labelPrefix} ${formatTime(slotDate)}`,    iso: slotDate.toISOString(),  };}function formatTime(date: Date): string {  return date.toLocaleTimeString([], {    hour: "numeric",    minute: "2-digit",  });}

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

Not supported on Claude Agent SDK (Python)

Claude Agent SDK (Python) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
