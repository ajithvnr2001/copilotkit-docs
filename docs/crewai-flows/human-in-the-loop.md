---
url: https://docs.copilotkit.ai/crewai-flows/human-in-the-loop/
title: Human in the Loop (HITL)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:35:51.836965+00:00
---

# Human in the Loop (HITL)

> Source: https://docs.copilotkit.ai/crewai-flows/human-in-the-loop/

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

On this page

InteractivityHuman-in-the-loop

# Human in the Loop (HITL)

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is Human-in-the-Loop (HITL)?#

Human-in-the-loop (HITL) allows agents to request human input or approval during execution, making AI systems more reliable and trustworthy. This pattern is essential when building AI applications that need to handle complex decisions or actions that require human judgment.

Conversational Flows

The frontend HITL APIs are unchanged in conversational mode. For native `useInterrupt` flows, register the AG-UI endpoint with `emit_interrupt_outcome=True` and `enable_legacy_on_interrupt_event=False`, in addition to `conversational=True`.

![Agentic Copilot Human in the Loop](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/coagents-hitl-infographic.png)

## When should I use this?#

HITL combines the efficiency of AI with human judgment, creating a system that's both powerful and reliable. The key advantages include:

  * **Quality Control** : Human oversight at critical decision points
  * **Edge Cases** : Graceful handling of low-confidence situations
  * **Expert Input** : Leverage human expertise when needed
  * **Reliability** : More robust system for real-world use



## How can I use this?#

Read more about the approach to HITL in CrewAI Flows.

### [Flow-basedUtilize CrewAI Flows to create Human-in-the-Loop workflows.](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/flow)

### On this page

What is Human-in-the-Loop (HITL)?When should I use this?How can I use this?
