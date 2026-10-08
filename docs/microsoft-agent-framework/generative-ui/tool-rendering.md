---
url: https://docs.copilotkit.ai/microsoft-agent-framework/generative-ui/tool-rendering/
title: Tool Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:38:37.384171+00:00
---

# Tool Rendering

> Source: https://docs.copilotkit.ai/microsoft-agent-framework/generative-ui/tool-rendering/

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

[Components as Tools](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/state-rendering)

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

Tool Call Rendering

Generative UIControlled

# Tool Rendering

Render your agent's tool calls with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates the implementation section applied in the 

[CopilotKit feature viewer](https://feature-viewer.copilotkit.ai/microsoft-agent-framework-dotnet/feature/agentic_chat)

.

## What is this?#

Tools are a way for the LLM to call predefined, typically, deterministic functions. CopilotKit allows you to render these tools in the UI as a custom component, which we call **Generative UI**.

## When should I use this?#

Rendering tools in the UI is useful when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Give your agent a tool to call#

Define a tool function that your agent can call. Microsoft Agent Framework will automatically convert this into a tool the LLM can call.

.NETPython

Program.cs
    
    
    using System.ComponentModel;
    using Microsoft.Agents.AI;
    using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;
    using Microsoft.Extensions.AI;
    using OpenAI;
    using OpenAI.Chat;
    
    var builder = WebApplication.CreateBuilder(args);
    builder.Services.AddAGUIServer();
    var app = builder.Build();
    
    string openAiApiKey = builder.Configuration["OPENAI_API_KEY"]
        ?? throw new InvalidOperationException("Set OPENAI_API_KEY");
    
    // Define the weather tool function
    [Description("Get the weather for a given location.")]
    static string GetWeather([Description("The location to get weather for")] string location)
        => $"The weather for {location} is 70 degrees.";
    
    AITool getWeather = AIFunctionFactory.Create(GetWeather, name: "get_weather");
    
    // Create the agent with tools
    var agent = new OpenAIClient(openAiApiKey)
        .GetChatClient("gpt-5.4-mini")
        .AsAIAgent(
            name: "AGUIAssistant",
            tools: [getWeather]);
    
    // Map the AG-UI endpoint
    app.MapAGUIServer("/", agent);
    
    await app.RunAsync();

main.py
    
    
    from __future__ import annotations
    import os
    import uvicorn
    from agent_framework import Agent, tool
    from agent_framework.openai import OpenAIChatClient
    from agent_framework.ag_ui import add_agent_framework_fastapi_endpoint
    from azure.identity import DefaultAzureCredential
    from dotenv import load_dotenv
    from fastapi import FastAPI
    from typing import Annotated
    from pydantic import Field
    
    load_dotenv()
    
    @tool
    def get_weather(
        location: Annotated[str, Field(description="The location to get weather for")],
    ) -> str:
        normalized = location.strip() or "the requested location"
        return f"The weather for {normalized} is 70 degrees."
    
    
    def _build_chat_client():
        if os.getenv("AZURE_OPENAI_ENDPOINT"):
            azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
            return OpenAIChatClient(
                model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-4o-mini"),
                api_key=azure_api_key,
                credential=None if azure_api_key else DefaultAzureCredential(),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )
        if os.getenv("OPENAI_API_KEY"):
            return OpenAIChatClient(
                model=os.getenv("OPENAI_CHAT_MODEL_ID", "gpt-4o-mini"),
                api_key=os.getenv("OPENAI_API_KEY"),
            )
        raise RuntimeError(
            "Set AZURE_OPENAI_ENDPOINT (uses az login unless AZURE_OPENAI_API_KEY is set) or OPENAI_API_KEY."
        )
    
    chat_client = _build_chat_client()
    
    agent = Agent(
        name="MyAgent",
        instructions="You are a helpful assistant.",
        client=chat_client,
        tools=[get_weather]
    )
    
    app = FastAPI(title="Microsoft Agent Framework - Quickstart")
    add_agent_framework_fastapi_endpoint(app=app, agent=agent, path="/")
    
    if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

### Render the tool call in your frontend#

At this point, your agent will be able to call the `get_weather` tool. Now we just need to add a `useRenderTool` hook to render the tool call in the UI.

Important

In order to render a tool call in the UI, the name of the action must match the name of the tool.

app/page.tsx
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    // ...
    
    const YourMainContent = () => {
      // ...
      useRenderTool({
        name: "get_weather",
        parameters: z.object({ location: z.string() }),
        render: ({ status, parameters }) => {
          return (
            <p className="text-gray-500 mt-2">
              {status !== "complete" && "Calling weather API..."}
              {status === "complete" &&
                `Called the weather API for ${parameters.location}.`}
            </p>
          );
        },
      });
      // ...
    };

### Give it a try!#

Try asking the agent to get the weather for a location. You should see the custom UI component that we added render the tool call and display the arguments that were passed to the tool.

## Default Tool Rendering#

`useDefaultRenderTool` provides a catch-all renderer for **any tool** that doesn't have a specific `useRenderToolCall` defined. This is useful for:

  * Displaying all tool calls during development
  * Rendering MCP (Model Context Protocol) tools
  * Providing a generic fallback UI for unexpected tools



app/page.tsx
    
    
    import { useDefaultRenderTool } from "@copilotkit/react-core/v2"; 
    // ...
    
    const YourMainContent = () => {
      // ...
      useDefaultRenderTool({
        render: ({ name, args, status, result }) => {
          return (
            <div style={{ color: "black" }}>
              <span>
                {status === "complete" ? "✓" : "⏳"}
                {name}
              </span>
              {status === "complete" && result && (
                <pre>{JSON.stringify(result, null, 2)}</pre>
              )}
            </div>
          );
        },
      });
      // ...
    };

Unlike `useRenderToolCall`, which targets a specific tool by name, `useDefaultRenderTool` catches **all** tools that don't have a dedicated renderer.

In v2, use [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool) for wildcard fallback rendering, and [`useRenderTool`](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool) for named or wildcard renderer registration.

### On this page

What is this?When should I use this?ImplementationGive your agent a tool to callRender the tool call in your frontendGive it a try!Default Tool Rendering
