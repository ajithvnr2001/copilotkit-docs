---
url: https://docs.copilotkit.ai/mastra/cookbook/
title: Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:13.392987+00:00
---

# Overview

> Source: https://docs.copilotkit.ai/mastra/cookbook/

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

Learn

# Overview

Focused, copy-pasteable recipes for wiring CopilotKit up to the tools and platforms you already use.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Cookbook#

Short, actionable recipes that connect CopilotKit to a specific tool or platform. Each one starts from a working CopilotKit app and adds a single capability — nothing more than you need to get it running.

[![](https://docs.copilotkit.ai/logos/manufact.svg)Ship an MCP App with ManufactBuild an MCP App with the open-source mcp-use SDK, render it inline in CopilotKit's chat, and deploy it to Manufact Cloud.](https://docs.copilotkit.ai/mastra/cookbook/manufact)[![](https://docs.copilotkit.ai/logos/typesafe.svg)Choose fast generative UI with JevBatch structured decisions, render interactive controls over AG-UI, and optionally improve choices with Automatic Learning.](https://docs.copilotkit.ai/mastra/cookbook/jev-generative-ui)[![](https://docs.copilotkit.ai/logos/daytona.png)Run agent code in a Daytona sandboxGive the Built-in Agent a tool that executes code in an isolated Daytona sandbox.](https://docs.copilotkit.ai/mastra/cookbook/daytona)[![](https://docs.copilotkit.ai/logos/claude.svg)Connect CopilotKit to Claude Managed AgentsStream a hosted Claude Managed Agent over AG-UI and render its tool call as an interactive growth projection.](https://docs.copilotkit.ai/mastra/cookbook/claude-managed-agents)[![](https://docs.copilotkit.ai/logos/oracle-agent-spec.png)Build a portable agent with memory using Oracle Agent SpecDefine an agent once in Oracle Agent Spec, run it on LangGraph over AG-UI, and give it long-term memory on Oracle AI Database.](https://docs.copilotkit.ai/mastra/cookbook/oracle-agent-spec-memory)[![](https://docs.copilotkit.ai/logos/arcade.png)Take authenticated actions with ArcadeGive the Built-in Agent OAuth-backed tools (Gmail, Google News) through Arcade, with the authorization step rendered as generative UI.](https://docs.copilotkit.ai/mastra/cookbook/arcade)[![](https://docs.copilotkit.ai/logos/google-adk.png)Build an agentic app on Angular + Google ADKWire an Angular frontend to a Google ADK agent over AG-UI, with optional threads and memory. The production gotchas, as symptom, cause, and fix.](https://docs.copilotkit.ai/mastra/cookbook/angular-adk-agentic-app)[![](https://docs.copilotkit.ai/logos/openbox.png)Govern agent actions with OpenBoxAdd OpenBox runtime governance — guardrails, policies, and human-in-the-loop approvals — to a CopilotKit + LangGraph agent, with decisions rendered as generative UI.](https://docs.copilotkit.ai/mastra/cookbook/openbox-governed-copilotkit)
