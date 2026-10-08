---
url: https://docs.copilotkit.ai/ms-agent-python/tutorials/ai-todo-app/next-steps/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:53.255394+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/ms-agent-python/tutorials/ai-todo-app/next-steps/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Quickstart

Turn your Microsoft Agent Framework agent into an agent-native application in 10 minutes.

## Start with your coding agent#

Use this prompt to connect your Microsoft Agent Framework agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An [OpenAI API key](https://platform.openai.com/api-keys) for the .NET starter
  * .NET 9.0 SDK or later
  * Node.js 20+
  * Your favorite package manager (npm, pnpm, yarn, or bun)



## Getting started#

### Set up CopilotKit Intelligence#

[Sign in to cloud-hosted Intelligence](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_microsoft_agent_framework_quickstart_step1&utm_frontend=react&utm_backend=ms-agent-python). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create it below.

### Choose your starting point#

You can either start fresh with our starter template or integrate CopilotKit into your existing Microsoft Agent Framework agent.

### 🎉 Start chatting!#

Your AI agent is now ready to use! Try asking it some questions:
    
    
    Can you tell me a joke?
    
    
    Can you help me understand AI?
    
    
    What do you think about .NET?

Troubleshooting

**Agent Connection Issues**

  * If you see "I'm having trouble connecting to my tools", make sure: 
    * The C# agent is running on port 8000
    * Your OpenAI API key is set via .NET user secrets
    * Both servers started successfully (check terminal output)



**OpenAI API Key Issues**

  * If the agent fails with "OPENAI_API_KEY not found": 
        
        cd agent
        dotnet user-secrets set OPENAI_API_KEY "<your-openai-api-key>"




**.NET SDK Issues**

  * Verify .NET SDK is installed: 
        
        dotnet --version  # Should be 9.0.x or higher

  * Restore packages manually if needed: 
        
        cd agent
        dotnet restore
        dotnet run




**Port Conflicts**

  * If port 8000 is already in use, you can change it in: 
    * `agent/Properties/launchSettings.json` \- Update `applicationUrl`
    * `src/app/api/copilotkit/route.ts` \- Update the remote endpoint URL



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/ms-agent-python/inspector).

## What's next?#

Now that you have your basic agent setup, explore these advanced features:

[👤Implement Human in the LoopAllow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/microsoft-agent-framework/human-in-the-loop)[🔄Utilize Shared StateLearn how to synchronize your agent's state with your UI's state, and vice versa.](https://docs.copilotkit.ai/microsoft-agent-framework/shared-state)[🎨Add some generative UIRender your agent's progress and output in the UI.](https://docs.copilotkit.ai/microsoft-agent-framework/generative-ui/tool-rendering)[🔧Setup frontend actionsGive your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/microsoft-agent-framework/frontend-tools)
