---
url: https://docs.copilotkit.ai/mastra/agentic-protocols/ag-ui/
title: AG-UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:53.804907+00:00
---

# AG-UI

> Source: https://docs.copilotkit.ai/mastra/agentic-protocols/ag-ui/

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

[Mastra](https://docs.copilotkit.ai/mastra)[Agentic Protocols](https://docs.copilotkit.ai/mastra/agentic-protocols)

# AG-UI

Bring your agents from any framework to your users through AG-UI and CopilotKit.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is the AG-UI Protocol?#

AG-UI is a lightweight, event-based protocol that standardizes how AI agents connect to user-facing applications. Built for simplicity and flexibility, it enables seamless integration between AI agents, real time user context, and user interfaces. AG-UI is an open standard, developed by the CopilotKit team and several agent framework partners.

![AG-UI Ecosystem Diagram](https://docs.copilotkit.ai/images/agui-ecosystem-light.png)![AG-UI Ecosystem Diagram](https://docs.copilotkit.ai/images/agui-ecosystem-dark.png)

## How CopilotKit uses AG-UI#

CopilotKit uses AG-UI to abstract the connection between your applications and the AI Agents that power your copilots. Your agents can be built using any AG-UI supporting Agent Framework (a growing list, including LangGraph, Mastra, Pydantic AI and others). This abstraction has several advantages over bespoke framework integrations.

  * **Flexibility and Interoperability** : By adhering to the AG-UI standard, CopilotKit components become interchangeable, allowing developers to use them with any AG-UI-compatible agent or to switch between different backend models without changing the UI.
  * **Unified Communication** : CopilotKit uses the AG-UI protocol to manage all the back-and-forth communication between the frontend and the AI agent, replacing custom WebSocket formats and text parsing.
  * **Frontend Tool Calls** : When an agent needs to use a tool that's integrated into the frontend application, AG-UI events facilitate this interaction.


  * **UI Components** : CopilotKit provides React components that are built for the AG-UI protocol. These components use AG-UI events to receive and display streaming AI responses and other data from the agent, creating a rich user experience.


  * **State Management** : The AG-UI protocol includes events for managing shared state between the frontend and the agent. CopilotKit can then use these events to keep the application's UI and the agent's state synchronized in real-time.



To learn more, check out the [AG-UI](https://ag-ui.com) website.

### On this page

What is the AG-UI Protocol?How CopilotKit uses AG-UI
