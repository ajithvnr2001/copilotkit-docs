---
url: https://docs.copilotkit.ai/angular/intelligence/bring-your-own-thread-system/
title: Bring your own thread system
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:37.340709+00:00
---

# Bring your own thread system

> Source: https://docs.copilotkit.ai/angular/intelligence/bring-your-own-thread-system/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Bring your own thread system](https://docs.copilotkit.ai/angular/intelligence/bring-your-own-thread-system)[Streams & Framework Threads](https://docs.copilotkit.ai/angular/intelligence/threads-explained)

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Bring your own thread system

IntelligenceFeaturesAG-UI Streams

# Bring your own thread system

Keep your existing thread storage while Intelligence records a separate copy of your AG-UI interactions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Keep your existing thread system when you connect CopilotKit Intelligence. You do not need to replace your thread storage or move your agent state.

Your framework continues managing the original conversation and agent state. Intelligence automatically records its own copy of the supported AG-UI interaction history that passes through your connected CopilotKit runtime.

## How recording works#

Sending a message that starts an agent run through the connected runtime creates the Intelligence thread record if it does not exist. Intelligence then records the interaction under that thread ID. Selecting a thread ID or opening the chat alone does not record a conversation.

Recording covers traffic through that runtime after you connect Intelligence. Runs that bypass it do not appear automatically. Connecting Intelligence does not scan your framework database or copy all its older conversations. If the agent sends earlier messages during a new run, Intelligence can record those messages too.

## What Intelligence records#

Intelligence records the supported interaction data sent through the connected runtime:

  * Messages sent by the user and agent.
  * Tool calls, their arguments, and tool results.
  * Application state sent as AG-UI state events.
  * Supported UI content, such as generative UI and activity messages, sent as part of the interaction.



The copy contains what the integration sends through AG-UI. It is not a copy of your framework database, internal checkpoints, or arbitrary browser state. Restoring UI content also requires the matching renderers in your app.

## Older history and lifecycle actions#

To include older history, use the optional [supported import flow](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless) for LangGraph, ADK, or Mastra. Import copies the supported content that the source still exposes. Future runs record automatically without an import. Import does not keep the two databases in sync.

Intelligence rename, archive, and delete actions affect only Intelligence records. They do not rename, archive, or delete the original conversation in your native framework store. Neither automatic recording nor historical import keeps the two databases in sync.

### On this page

How recording worksWhat Intelligence recordsOlder history and lifecycle actions
