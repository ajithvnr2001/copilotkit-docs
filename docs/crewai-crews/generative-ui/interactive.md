---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:02.038304+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/interactive/

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

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)[Build Generative UI](https://docs.copilotkit.ai/crewai-crews/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_flow.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """Native CrewAI async HITL Flow for inline and headless interrupts."""from __future__ import annotationsimport jsonfrom datetime import datetime, time, timedeltafrom typing import Anyfrom zoneinfo import ZoneInfofrom crewai.flow import Flow, HumanFeedbackResult, human_feedback, listen, startfrom litellm import acompletionfrom pydantic import Fieldfrom ag_ui_crewai import (    CopilotKitState,    agui_feedback_provider,    copilotkit_emit_tool_result,    copilotkit_stream,)SYSTEM_PROMPT = (    "You are a scheduling assistant. Whenever the user asks to book a call or "    "schedule a meeting, call schedule_meeting with a short topic and optional "    "attendee. After the tool result, briefly confirm the selected time or "    "that the user cancelled.")DEMO_TZ = ZoneInfo("America/Los_Angeles")SCHEDULE_MEETING_TOOL = {    "type": "function",    "function": {        "name": "schedule_meeting",        "description": "Ask the user to choose a meeting time.",        "parameters": {            "type": "object",            "properties": {                "topic": {"type": "string"},                "attendee": {"type": "string"},            },            "required": ["topic"],        },    },}def candidate_slots() -> list[dict[str, str]]:    """Return stable labels attached to future Pacific timestamps."""    now = datetime.now(DEMO_TZ)    tomorrow = (now + timedelta(days=1)).date()    days_to_monday = (7 - now.weekday()) % 7    if days_to_monday <= 1:        days_to_monday += 7    next_monday = (now + timedelta(days=days_to_monday)).date()    candidates = [        ("Tomorrow 10:00 AM", tomorrow, time(10, 0)),        ("Tomorrow 2:00 PM", tomorrow, time(14, 0)),        ("Monday 9:00 AM", next_monday, time(9, 0)),        ("Monday 3:30 PM", next_monday, time(15, 30)),    ]    return [        {"label": label, "iso": datetime.combine(day, at, DEMO_TZ).isoformat()}        for label, day, at in candidates    ]class InterruptState(CopilotKitState):    pending_tool_call_id: str | None = None    meeting: dict[str, Any] = Field(default_factory=dict)class InterruptFlow(Flow[InterruptState]):    """Pause after schedule_meeting and continue from a spec resume entry."""    @start()    @human_feedback(        message="Choose a meeting time or cancel the request.",        llm=None,        provider=agui_feedback_provider,    )    async def request_schedule(self) -> dict[str, Any]:        response = await copilotkit_stream(            await acompletion(                model="openai/gpt-5.4",                messages=[                    {"role": "system", "content": SYSTEM_PROMPT},                    *self.state.messages,                ],                tools=[SCHEDULE_MEETING_TOOL],                tool_choice={                    "type": "function",                    "function": {"name": "schedule_meeting"},                },                parallel_tool_calls=False,                stream=True,            )        )        message = response.choices[0].message        self.state.messages.append(message)        tool_calls = message.get("tool_calls") or []        schedule_call = next(            (                call                for call in tool_calls                if call.get("function", {}).get("name") == "schedule_meeting"            ),            None,        )        if schedule_call is None:            return {                "topic": "Meeting",                "attendee": None,                "slots": candidate_slots(),            }        try:            arguments = json.loads(                schedule_call.get("function", {}).get("arguments") or "{}"            )        except (TypeError, json.JSONDecodeError):            arguments = {}        self.state.pending_tool_call_id = schedule_call.get("id")        slots = arguments.get("slots")        return {            "topic": arguments.get("topic") or "Meeting",            "attendee": arguments.get("attendee"),            "slots": slots if isinstance(slots, list) and slots else candidate_slots(),        }    @listen("request_schedule")    async def confirm_schedule(self, result: HumanFeedbackResult) -> None:        feedback_text = result.feedback or ""        try:            feedback = json.loads(feedback_text or "{}")        except (TypeError, json.JSONDecodeError):            feedback = {}        if not isinstance(feedback, dict):            feedback = {}        output = result.output if isinstance(result.output, dict) else {}        # The AG-UI CrewAI provider resumes a cancelled protocol interrupt        # with an empty feedback string. Submitted choices are JSON objects,        # so an empty payload is the package's authoritative cancel signal.        cancelled = not feedback_text.strip() or bool(feedback.get("cancelled"))        self.state.meeting = {            "topic": output.get("topic") or "Meeting",            "attendee": output.get("attendee"),            "time": None if cancelled else feedback.get("chosen_time"),            "label": None if cancelled else feedback.get("chosen_label"),            "cancelled": cancelled,        }        if self.state.pending_tool_call_id:            result_content = json.dumps(self.state.meeting)            self.state.messages.append(                {                    "role": "tool",                    "tool_call_id": self.state.pending_tool_call_id,                    "content": result_content,                }            )            await copilotkit_emit_tool_result(                self.state.pending_tool_call_id, result_content            )        response = await copilotkit_stream(            await acompletion(                model="openai/gpt-5.4",                messages=[                    {                        "role": "system",                        "content": (                            f"{SYSTEM_PROMPT}\nScheduling outcome: "                            f"{json.dumps(self.state.meeting)}"                        ),                    },                    *self.state.messages,                ],                tools=[SCHEDULE_MEETING_TOOL],                parallel_tool_calls=False,                stream=True,            )        )        self.state.messages.append(response.choices[0].message)interrupt_flow = InterruptFlow()

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

> **Not available on this framework.** Interactive generative UI requires either a native interrupt primitive or a Promise-resolving frontend tool. For tool-call-based approval flows, use [Human-in-the-loop](https://docs.copilotkit.ai/crewai-crews/generative-ui/human-in-the-loop) instead.
