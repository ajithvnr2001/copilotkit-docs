---
url: https://docs.copilotkit.ai/pydantic-ai/intelligence/channels/
title: Channels
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:14.673855+00:00
---

# Channels

> Source: https://docs.copilotkit.ai/pydantic-ai/intelligence/channels/

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

Channels

IntelligenceFeatures

# Channels

Put the agent you already built into Slack or Microsoft Teams. Intelligence owns the connection; your agent stays where it runs.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

Channels lets the agent you already built answer in Slack or Microsoft Teams. Intelligence owns the connection; your agent stays where it runs.

![A Slack channel where a person mentions the agent and asks for a chart. The agent replies in the thread with a native bar chart and a short summary.](https://docs.copilotkit.ai/images/cloud-hosted/cloud-hosted-channels-slack.png)

Someone mentions the agent in a channel, it runs with the same tools and context it has in your app, and it replies in the thread with native messages, cards, and charts.

## What Channels does#

  * **One agent, every surface.** The agent process you run for your app also serves Slack and Teams. No second agent, no second prompt, no second set of tools.
  * **Native replies.** Text, buttons, approvals, and charts render as Slack Block Kit or Teams Adaptive Cards. In the screenshot the agent answers a question with a bar chart, not a link.
  * **Conversations that persist.** Each Slack or Teams conversation shares a stable thread id with the agent run, so Intelligence keeps its history and the run appears in Product Analytics like any other.
  * **Identity you control.** Your code maps the Slack or Teams user to your app user, so tools and permissions follow the person, and you decide when a run may use User Memory.



## How it works#

Intelligence sits between the platform and your agent. It holds the Slack or Teams credentials, receives each message event, and delivers the turn to a long-running Channels SDK process that you run. Your process runs the agent over AG-UI and sends the rendered reply back through Intelligence to the thread.

You never hand platform credentials to your agent, and CopilotKit never runs your agent or your tools. The full message path and the split of responsibilities are on the [Channels overview](https://docs.copilotkit.ai/channels).

Slack and Microsoft Teams are generally available on cloud-hosted Intelligence.

## Pick your channel and framework#

Choose where the agent should answer, then the framework it already runs on. The guide you land on starts from that framework and ends with the agent replying in a channel.

Your channel

SlackTeams

### Your agent backend

[CopilotKit](https://docs.copilotkit.ai/slack)[DeepAgents](https://docs.copilotkit.ai/slack/deepagents)LangChain[Google ADK](https://docs.copilotkit.ai/slack/google-adk)AWS StrandsMicrosoft Agent Framework[Mastra](https://docs.copilotkit.ai/slack/mastra)[Claude Agent SDK (Python)](https://docs.copilotkit.ai/slack/claude-sdk-python)[Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/slack/claude-sdk-typescript)[PydanticAI](https://docs.copilotkit.ai/slack/pydantic-ai)[MS Agent Harness (.NET)](https://docs.copilotkit.ai/slack/ms-agent-harness-dotnet)[AG2](https://docs.copilotkit.ai/slack/ag2)[Agno](https://docs.copilotkit.ai/slack/agno)[LlamaIndex](https://docs.copilotkit.ai/slack/llamaindex)[CrewAI Flows](https://docs.copilotkit.ai/slack/crewai-crews)

## Where to go next#

You want to| Read  
---|---  
Give the agent application actions and context| [Tools and context](https://docs.copilotkit.ai/channels/tools)  
Map Slack or Teams users to your app users| [Identity and Memory](https://docs.copilotkit.ai/channels/identity-and-memory)  
Send cards, charts, and formatted messages| [Rich messages and components](https://docs.copilotkit.ai/channels/rich-messages)  
Add buttons and approval steps| [Interactive messages and approvals](https://docs.copilotkit.ai/channels/interactive)  
Handle slash commands and emoji reactions| [Commands and reactions](https://docs.copilotkit.ai/channels/commands-and-reactions)  
Accept files and images from the conversation| [Files and multimodal input](https://docs.copilotkit.ai/channels/files-and-multimodality)  
See how a channel conversation relates to AG-UI Streams| [Threads and state](https://docs.copilotkit.ai/channels/threads-and-state)  
Make workflow state survive a restart| [Persistence and scaling](https://docs.copilotkit.ai/channels/persistence-and-scaling)  
Read conversation history or keep a transcript| [History and transcripts](https://docs.copilotkit.ai/channels/history-and-transcripts)  
Run the listener in production| [Deploy and operate](https://docs.copilotkit.ai/channels/deploy-and-operate)  
  
### On this page

OverviewWhat Channels doesHow it worksPick your channel and frameworkWhere to go next
