---
url: https://docs.copilotkit.ai/ag2/generative-ui/tool-based/
title: Tool Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:11.110788+00:00
---

# Tool Rendering

> Source: https://docs.copilotkit.ai/ag2/generative-ui/tool-based/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/ag2/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/ag2/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/ag2/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Tool Call Rendering

Generative UIControlled

# Tool Rendering

Render your agent's tool calls with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Tools are a way for the LLM to call predefined, typically, deterministic functions. CopilotKit allows you to render these tools in the UI as a custom component, which we call **Generative UI**.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## When should I use this?#

Rendering tools in the UI is useful when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Run and connect your agent#

Start your AG2 backend with a `/chat` endpoint and connect CopilotKit to that endpoint.

### Give your agent a tool to call#

Python

agent.py
    
    
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    from pydantic import Field
    
    from ag2 import Agent, tool
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    @tool
    def get_weather(
        location: Annotated[str, Field(description="Fully spelled out location")],
    ) -> str:
        """Get the weather for a given location. Ensure location is fully spelled out."""
        return f"The weather in {location} is sunny."
    
    agent = Agent(
        name="assistant",
        prompt="You are a helpful assistant.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[get_weather],
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
    accept: str | None = Header(None),
    ) -> StreamingResponse:
        return StreamingResponse(
            stream.dispatch(message, accept=accept),
            media_type=accept or "text/event-stream",
        )

### Render the tool call in your frontend#

At this point, your agent will be able to call the `get_weather` tool. Now we just need to add a `useRenderTool` hook to render the tool call in the UI.

Important

In order to render a tool call in the UI, the name of the action must match the name of the tool.

app/page.tsx
    
    
    import { z } from "zod"; 
    import { useRenderTool } from "@copilotkit/react-core/v2"; 
    // ...
    
    const YourMainContent = () => {
      // ...
      useRenderTool({
        name: "get_weather",
        parameters: z.object({ location: z.string() }),
        render: ({status, parameters}) => {
          return (
            <p className="text-gray-500 mt-2">
              {status !== "complete" && "Calling weather API..."}
              {status === "complete" && `Called the weather API for ${parameters.location}.`}
            </p>
          );
        },
      });
      // ...
    }

#### Render structured results

A tool that returns structured data (a Pydantic model, a dict, a list) reaches the frontend as its serialized JSON in `result`, because the protocol has no JSON part. Parse it before rendering it as a card:

app/page.tsx
    
    
    useRenderTool({
      name: "get_weather",
      parameters: z.object({ location: z.string() }),
      render: ({ status, result }) => {
    if (status !== "complete" || typeof result !== "string") return <p>Calling weather API...</p>;
        const weather = JSON.parse(result) as { temperature: number; conditions: string };
        return <p>{weather.temperature}° · {weather.conditions}</p>;
      },
    });

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

What is this?When should I use this?ImplementationRun and connect your agentGive your agent a tool to callRender the tool call in your frontendGive it a try!Default Tool Rendering
