---
url: https://docs.copilotkit.ai/google-adk/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:04.308891+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Google ADK](https://docs.copilotkit.ai/google-adk)[Build Generative UI](https://docs.copilotkit.ai/google-adk/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """ADK scheduling agent backing the gen-ui-interrupt demo (Strategy-B).In langgraph-python the gen-ui-interrupt demo relies on the native`interrupt()` primitive with checkpoint/resume. ADK has no such primitive,so we adapt with the same "Strategy B" pattern used by the agno andms-agent-framework ports: the agent's instruction tells Gemini to call the`schedule_meeting` tool, but NO backend tool is registered. CopilotKit's`AGUIToolset()` injects the frontend-registered `schedule_meeting`(`useHumanInTheLoop` in src/app/demos/gen-ui-interrupt/page.tsx) into themodel's tool list; the model's call is routed to the frontend, which rendersthe time-picker inline and resolves the call once the user picks a slot —equivalent to `interrupt()` in the LangGraph reference.`after_model_callback=stop_on_terminal_text` is the canonical ADK terminalguard (see shared_chat.py): without it the configured Gemini model(from `get_model()`) re-issues the same tool call indefinitely after thefrontend tool resolves."""from __future__ import annotations# region: setupfrom google.adk.agents import LlmAgentfrom ag_ui_adk import AGUIToolsetfrom agents.shared_chat import get_model, stop_on_terminal_text_INSTRUCTION = (    "You are a scheduling assistant. Whenever the user asks you to book a "    "call or schedule a meeting, you MUST call the `schedule_meeting` tool. "    "Pass a short `topic` describing the purpose of the meeting and, if "    "known, an `attendee` describing who the meeting is with.\n\n"    "The `schedule_meeting` tool is implemented on the client: it surfaces a "    "time-picker UI and returns the user's selection. After the tool "    "returns, briefly confirm whether the meeting was scheduled and at what "    "time, or note that the user cancelled. Do NOT ask for approval "    "yourself — always call the tool and let the picker handle the decision. "    "Keep responses short and friendly, and always send a brief final "    "assistant message summarising what happened so it persists.")interrupt_agent = LlmAgent(    name="InterruptAgent",    model=get_model(),    instruction=_INSTRUCTION,    # No backend tools. `schedule_meeting` is registered on the frontend via    # useHumanInTheLoop; AGUIToolset() exposes CopilotKit's frontend-tool    # channel to the model.    tools=[AGUIToolset()],    after_model_callback=stop_on_terminal_text,)# endregion

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

> **Not available on this framework.** Interactive generative UI requires either a native interrupt primitive or a Promise-resolving frontend tool. For tool-call-based approval flows, use [Human-in-the-loop](https://docs.copilotkit.ai/google-adk/generative-ui/human-in-the-loop) instead.
