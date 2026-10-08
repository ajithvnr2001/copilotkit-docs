---
url: https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:09.930188+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/headless/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Headless Interrupts

Resolve agent interrupts from any UI, without a useInterrupt render slot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_flow.py

page.tsx

route.ts
    
    
    """Native CrewAI async HITL Flow for inline and headless interrupts."""from __future__ import annotationsimport jsonfrom datetime import datetime, time, timedeltafrom typing import Anyfrom zoneinfo import ZoneInfofrom crewai.flow import Flow, HumanFeedbackResult, human_feedback, listen, startfrom litellm import acompletionfrom pydantic import Fieldfrom ag_ui_crewai import (    CopilotKitState,    agui_feedback_provider,    copilotkit_emit_tool_result,    copilotkit_stream,)SYSTEM_PROMPT = (    "You are a scheduling assistant. Whenever the user asks to book a call or "    "schedule a meeting, call schedule_meeting with a short topic and optional "    "attendee. After the tool result, briefly confirm the selected time or "    "that the user cancelled.")DEMO_TZ = ZoneInfo("America/Los_Angeles")SCHEDULE_MEETING_TOOL = {    "type": "function",    "function": {        "name": "schedule_meeting",        "description": "Ask the user to choose a meeting time.",        "parameters": {            "type": "object",            "properties": {                "topic": {"type": "string"},                "attendee": {"type": "string"},            },            "required": ["topic"],        },    },}def candidate_slots() -> list[dict[str, str]]:    """Return stable labels attached to future Pacific timestamps."""    now = datetime.now(DEMO_TZ)    tomorrow = (now + timedelta(days=1)).date()    days_to_monday = (7 - now.weekday()) % 7    if days_to_monday <= 1:        days_to_monday += 7    next_monday = (now + timedelta(days=days_to_monday)).date()    candidates = [        ("Tomorrow 10:00 AM", tomorrow, time(10, 0)),        ("Tomorrow 2:00 PM", tomorrow, time(14, 0)),        ("Monday 9:00 AM", next_monday, time(9, 0)),        ("Monday 3:30 PM", next_monday, time(15, 30)),    ]    return [        {"label": label, "iso": datetime.combine(day, at, DEMO_TZ).isoformat()}        for label, day, at in candidates    ]class InterruptState(CopilotKitState):    pending_tool_call_id: str | None = None    meeting: dict[str, Any] = Field(default_factory=dict)class InterruptFlow(Flow[InterruptState]):    """Pause after schedule_meeting and continue from a spec resume entry."""    @start()    @human_feedback(        message="Choose a meeting time or cancel the request.",        llm=None,        provider=agui_feedback_provider,    )    async def request_schedule(self) -> dict[str, Any]:        response = await copilotkit_stream(            await acompletion(                model="openai/gpt-5.4",                messages=[                    {"role": "system", "content": SYSTEM_PROMPT},                    *self.state.messages,                ],                tools=[SCHEDULE_MEETING_TOOL],                tool_choice={                    "type": "function",                    "function": {"name": "schedule_meeting"},                },                parallel_tool_calls=False,                stream=True,            )        )        message = response.choices[0].message        self.state.messages.append(message)        tool_calls = message.get("tool_calls") or []        schedule_call = next(            (                call                for call in tool_calls                if call.get("function", {}).get("name") == "schedule_meeting"            ),            None,        )        if schedule_call is None:            return {                "topic": "Meeting",                "attendee": None,                "slots": candidate_slots(),            }        try:            arguments = json.loads(                schedule_call.get("function", {}).get("arguments") or "{}"            )        except (TypeError, json.JSONDecodeError):            arguments = {}        self.state.pending_tool_call_id = schedule_call.get("id")        slots = arguments.get("slots")        return {            "topic": arguments.get("topic") or "Meeting",            "attendee": arguments.get("attendee"),            "slots": slots if isinstance(slots, list) and slots else candidate_slots(),        }    @listen("request_schedule")    async def confirm_schedule(self, result: HumanFeedbackResult) -> None:        feedback_text = result.feedback or ""        try:            feedback = json.loads(feedback_text or "{}")        except (TypeError, json.JSONDecodeError):            feedback = {}        if not isinstance(feedback, dict):            feedback = {}        output = result.output if isinstance(result.output, dict) else {}        # The AG-UI CrewAI provider resumes a cancelled protocol interrupt        # with an empty feedback string. Submitted choices are JSON objects,        # so an empty payload is the package's authoritative cancel signal.        cancelled = not feedback_text.strip() or bool(feedback.get("cancelled"))        self.state.meeting = {            "topic": output.get("topic") or "Meeting",            "attendee": output.get("attendee"),            "time": None if cancelled else feedback.get("chosen_time"),            "label": None if cancelled else feedback.get("chosen_label"),            "cancelled": cancelled,        }        if self.state.pending_tool_call_id:            result_content = json.dumps(self.state.meeting)            self.state.messages.append(                {                    "role": "tool",                    "tool_call_id": self.state.pending_tool_call_id,                    "content": result_content,                }            )            await copilotkit_emit_tool_result(                self.state.pending_tool_call_id, result_content            )        response = await copilotkit_stream(            await acompletion(                model="openai/gpt-5.4",                messages=[                    {                        "role": "system",                        "content": (                            f"{SYSTEM_PROMPT}\nScheduling outcome: "                            f"{json.dumps(self.state.meeting)}"                        ),                    },                    *self.state.messages,                ],                tools=[SCHEDULE_MEETING_TOOL],                parallel_tool_calls=False,                stream=True,            )        )        self.state.messages.append(response.choices[0].message)interrupt_flow = InterruptFlow()

## What is this?#

`useInterrupt`'s `render` callback is the 80% path: it keeps the UI glued to a `<CopilotChat>` transcript and handles "when to show the picker" logic for you. This page covers the escape hatch: a **render-less** interrupt resolver you assemble from the same primitives `useInterrupt` uses internally — a pattern that lives anywhere in your React tree, takes any shape you like (button grid, form, modal, keyboard shortcut), and resolves the interrupt without mounting a chat at all.

> **Not available on this framework.** Headless interrupts are built on top of `useInterrupt` / `useFrontendTool` patterns that require the runtime to expose either a native `interrupt(...)` primitive (LangGraph) or a Promise-resolving frontend-tool path. For all other integrations, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/human-in-the-loop) instead — it's the standard hook for tool-call-based pause/resume flows and works on every framework that supports tool calls.

## When should I use this?#

  * **Testing / Playwright fixtures** — a deterministic, chat-less button grid is easier to drive than a chat surface where the picker only appears after an LLM call.
  * **Non-chat UIs** — dashboards, side panels, inspector surfaces, or any place where you want the _agent's interrupt_ without the _chat transcript_.
  * **Custom flow control** — when you need to know exactly when the interrupt arrived (e.g. to gate other UI) and when it was resolved.
  * **Research / debugging** — when you want to observe the raw AG-UI custom events without the abstraction layer.



If you just want "a picker in chat", just use [`useInterrupt`](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/headless/useInterrupt).

## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses where the model decides on the fly to ask the user, rather than the runtime forcing the pause itself.
  * [`useInterrupt`](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/headless/useInterrupt) — the render-prop version of this page, with `enabled` gating and `handler` preprocessing.


