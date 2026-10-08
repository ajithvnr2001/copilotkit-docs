---
url: https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:18:28.827532+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Frontend-tools

Basics

# Frontend Tools

Create frontend tools and use them within your Microsoft Agent Framework agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

Frontend tools enable you to define client-side functions that your agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized to let your agent control the UI, power generative UI, or support Human-in-the-loop interactions.

In this guide, we cover the use of frontend tools driving and interacting with the UI.

## When should I use this?#

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Create a frontend tool#

First, you'll need to create a frontend tool using the [useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool) hook. Here's a simple one to get you started that says hello to the user.

page.tsx
    
    
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/react-core/v2"
    
    export function Page() {
      // ...
    
      useFrontendTool({
        name: "sayHello",
        description: "Say hello to the user",
        parameters: z.object({
          name: z.string().describe("The name of the user to say hello to"),
        }),
        handler: async ({ name }) => {
          alert(`Hello, ${name}!`);
          return `Said hello to ${name}!`;
        },
      });
    
      // ...
    }

### Modify your server#

Now, we'll ensure your AG-UI server can receive and pass these frontend actions to your agent logic.

### Create your AG-UI server#

Set up your AG-UI server to serve your agent. Frontend tools registered with `useFrontendTool` are automatically made available to your agent through the AG-UI protocol.

.NETPython

Program.cs
    
    
    using Microsoft.Agents.AI;
    using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;
    using OpenAI;
    using OpenAI.Chat;
    
    var builder = WebApplication.CreateBuilder(args);
    builder.Services.AddAGUIServer();
    var app = builder.Build();
    
    string openAiApiKey = builder.Configuration["OPENAI_API_KEY"]
        ?? throw new InvalidOperationException("Set OPENAI_API_KEY");
    
    // Create the agent
    var agent = new OpenAIClient(openAiApiKey)
        .GetChatClient("gpt-5.4-mini")
        .AsAIAgent(name: "AGUIAssistant", instructions: "You are a helpful assistant.");
    
    // Map the AG-UI endpoint
    app.MapAGUIServer("/", agent);
    await app.RunAsync();

agent/src/byo_agent.py
    
    
    from __future__ import annotations
    import os
    from fastapi import FastAPI
    from dotenv import load_dotenv
    from agent_framework import Agent
    from agent_framework import SupportsChatGetResponse
    from agent_framework.openai import OpenAIChatClient
    from agent_framework.ag_ui import add_agent_framework_fastapi_endpoint
    from azure.identity import DefaultAzureCredential
    
    load_dotenv()
    
    def _build_chat_client() -> SupportsChatGetResponse:
        if bool(os.getenv("AZURE_OPENAI_ENDPOINT")):
            azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
            return OpenAIChatClient(
                model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-5.4-mini"),
                api_key=azure_api_key,
                credential=None if azure_api_key else DefaultAzureCredential(),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )
        if bool(os.getenv("OPENAI_API_KEY")):
            return OpenAIChatClient(
                model=os.getenv("OPENAI_CHAT_MODEL_ID", "gpt-5.4-mini"),
                api_key=os.getenv("OPENAI_API_KEY"),
            )
        raise RuntimeError("Set AZURE_OPENAI_ENDPOINT (uses az login unless AZURE_OPENAI_API_KEY is set) or OPENAI_API_KEY")
    
    chat_client = _build_chat_client()
    agent = Agent(
        name="AGUIAssistant",
        instructions="You are a helpful assistant.",
        client=chat_client,
    )
    
    app = FastAPI(title="AG-UI Server (Python)")
    add_agent_framework_fastapi_endpoint(app=app, agent=agent, path="/")

Frontend tools registered with `useFrontendTool` are automatically forwarded to your agent by the AG-UI protocol. The agent can invoke them just like backend tools, but execution happens on the frontend.

### Give it a try!#

You've now given your agent the ability to directly call any frontend tools you've defined. These tools will be available to the agent where they can be used as needed.

### On this page

What is this?When should I use this?Implementation
