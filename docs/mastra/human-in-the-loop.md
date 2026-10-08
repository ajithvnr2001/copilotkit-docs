---
url: https://docs.copilotkit.ai/mastra/human-in-the-loop/
title: Human-in-the-Loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:38.210981+00:00
---

# Human-in-the-Loop

> Source: https://docs.copilotkit.ai/mastra/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

InteractivityHuman-in-the-loop

# Human-in-the-Loop

Learn how to implement Human-in-the-Loop (HITL) using Mastra Agents.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is Human-in-the-Loop (HITL)?#

Human-in-the-loop (HITL) allows agents to request human input or approval during execution, making AI systems more reliable and trustworthy. This pattern is essential when building AI applications that need to handle complex decisions or actions that require human judgment.

## When should I use this?#

HITL combines the efficiency of AI with human judgment, creating a system that's both powerful and reliable. The key advantages include:

  * **Quality Control** : Human oversight at critical decision points
  * **Edge Cases** : Graceful handling of low-confidence situations
  * **Expert Input** : Leverage human expertise when needed
  * **Reliability** : More robust system for real-world use



## How can I use this?#

Mastra supports HITL through frontend tools that render UI and collect user input.

### [Tool-based (Supported)Register frontend tools with useHumanInTheLoop that render UI and wait for user responses. This is the working approach for Mastra.](https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based)### [Interrupt-based (Not Supported)Mastra does not support native interrupt flow. See this page to understand why and learn about the tool-based alternative.](https://docs.copilotkit.ai/mastra/human-in-the-loop/interrupt-flow)

### On this page

What is Human-in-the-Loop (HITL)?When should I use this?How can I use this?
