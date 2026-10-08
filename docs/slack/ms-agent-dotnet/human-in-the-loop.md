---
url: https://docs.copilotkit.ai/slack/ms-agent-dotnet/human-in-the-loop/
title: Human-in-the-Loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:46.195517+00:00
---

# Human-in-the-Loop

> Source: https://docs.copilotkit.ai/slack/ms-agent-dotnet/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/ms-agent-dotnet)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/ms-agent-dotnet/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/ms-agent-dotnet/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/ms-agent-dotnet/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/ms-agent-dotnet/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/ms-agent-dotnet/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/ms-agent-dotnet/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/ms-agent-dotnet/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/ms-agent-dotnet/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/ms-agent-dotnet/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/ms-agent-dotnet/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/ms-agent-dotnet/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/ms-agent-dotnet/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (.NET)](https://docs.copilotkit.ai/slack/ms-agent-dotnet)

# Human-in-the-Loop

Learn how to implement Human-in-the-Loop (HITL) using Microsoft Agent Framework agents.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is Human-in-the-Loop (HITL)?#

Human-in-the-loop (HITL) lets an agent ask for human input or approval while it runs. Use it when an action is expensive, destructive, or needs judgment the agent does not have.

## How can I use this?#

Microsoft Agent Framework supports two patterns, and they solve different problems.

Use **interrupt-based** HITL when the backend owns the decision. You mark a backend tool as approval-gated, and the agent pauses before it runs. The frontend does not need to know the tool's name.

Use **tool-based** HITL when the frontend owns the work. You define a tool that runs in the browser, and the agent calls it like any other tool.

### [Interrupt-basedMark a backend tool as approval-gated. The agent pauses, useInterrupt renders your approval UI, and your answer resumes the run.](https://docs.copilotkit.ai/slack/ms-agent-dotnet/human-in-the-loop/interrupt-flow)### [Tool-basedRegister a frontend tool with useHumanInTheLoop that renders UI and waits for the user's response before returning a result.](https://docs.copilotkit.ai/slack/ms-agent-dotnet/human-in-the-loop/tool-based)

### On this page

What is Human-in-the-Loop (HITL)?How can I use this?
