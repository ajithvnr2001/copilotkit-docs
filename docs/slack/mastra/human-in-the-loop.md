---
url: https://docs.copilotkit.ai/slack/mastra/human-in-the-loop/
title: Human-in-the-Loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:45.933180+00:00
---

# Human-in-the-Loop

> Source: https://docs.copilotkit.ai/slack/mastra/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/mastra)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/mastra/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/mastra/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/mastra/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/mastra/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/mastra/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/mastra/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/mastra/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/mastra/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/mastra/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/mastra/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/mastra/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/mastra/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Mastra](https://docs.copilotkit.ai/slack/mastra)

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

### [Tool-based (Supported)Register frontend tools with useHumanInTheLoop that render UI and wait for user responses. This is the working approach for Mastra.](https://docs.copilotkit.ai/slack/mastra/human-in-the-loop/tool-based)### [Interrupt-based (Not Supported)Mastra does not support native interrupt flow. See this page to understand why and learn about the tool-based alternative.](https://docs.copilotkit.ai/slack/mastra/human-in-the-loop/interrupt-flow)

### On this page

What is Human-in-the-Loop (HITL)?When should I use this?How can I use this?
