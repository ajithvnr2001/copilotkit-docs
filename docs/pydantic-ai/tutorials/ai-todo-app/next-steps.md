---
url: https://docs.copilotkit.ai/pydantic-ai/tutorials/ai-todo-app/next-steps/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:42.405144+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/pydantic-ai/tutorials/ai-todo-app/next-steps/

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

# Quickstart

Turn your Pydantic AI agent into an agent-native application in 10 minutes.

## Start with your coding agent#

Use this prompt to connect your Pydantic AI agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An OpenAI API key
  * Node.js 20+
  * Python 3.9+
  * Your favorite package manager



## Getting started#

### Set up CopilotKit Intelligence#

[Sign in to cloud-hosted Intelligence](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_pydantic_ai_quickstart_step1&utm_frontend=react&utm_backend=pydantic-ai). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create it below.

### Choose your starting point#

You can either start fresh with our starter template or integrate CopilotKit into your existing Pydantic AI agent.

### 🎉 Start chatting!#

Your AI agent is now ready to use! Navigate to `localhost:3000` and try asking it some questions:
    
    
    Can you tell me a joke?
    
    
    Can you help me understand AI?
    
    
    What do you think about React?

Troubleshooting

  * If you're having connection issues, try using `0.0.0.0` or `127.0.0.1` instead of `localhost`
  * Make sure your agent is running on port 8000
  * Check that your OpenAI API key is correctly set
  * Verify that the `@ag-ui/client` package is installed in your frontend



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/pydantic-ai/inspector).

## What's next?#

Now that you have your basic agent setup, explore these advanced features:

[👤Implement Human in the LoopAllow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/pydantic-ai/human-in-the-loop)[🔄Utilize the Shared StateLearn how to synchronize your agent's state with your UI's state, and vice versa.](https://docs.copilotkit.ai/pydantic-ai/shared-state)[🎨Add some generative UIRender your agent's progress and output in the UI.](https://docs.copilotkit.ai/pydantic-ai/generative-ui/tool-rendering)[🔧Setup frontend actionsGive your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)
