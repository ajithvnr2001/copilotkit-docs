---
url: https://docs.copilotkit.ai/agno/generative-ui/tool-rendering/
title: Tool Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:47:04.005049+00:00
---

# Tool Rendering

> Source: https://docs.copilotkit.ai/agno/generative-ui/tool-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agno/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/agno/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/agno/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/agno/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agno/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agno/learning)

[User Memories](https://docs.copilotkit.ai/agno/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agno/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

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

This example demonstrates the implementation section applied in the [CopilotKit feature viewer](https://feature-viewer.copilotkit.ai/langgraph/feature/agentic_chat).

## What is this?#

Tools are a way for the LLM to call predefined, typically, deterministic functions. CopilotKit allows you to render these tools in the UI as a custom component, which we call **Generative UI**.

## When should I use this?#

Rendering tools in the UI is useful when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Give your agent a tool to call#

Python

agent.py
    
    
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.tools import tool
    # ...
    
    @tool
    def get_weather(location: str):
        """
        Get the weather for a given location.
        """
        return f"The weather for {location} is 70 degrees."
    
    # ...
    
    agent = Agent(
        model=OpenAIChat(id="gpt-5.4"),
        tools=[get_weather], 
        description="A helpful assistant that can answer questions and provide information.",
        instructions="Be helpful and friendly. Format your responses using markdown where appropriate.",
    )

### Render the tool call in your frontend#

At this point, your agent will be able to call the `get_weather` tool. Now we just need to add a `useRenderTool` hook to render the tool call in the UI.

Important

In order to render a tool call in the UI, the name of the action must match the name of the tool.

app/page.tsx
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2"; 
    // ...
    
    const YourMainContent = () => {
      // ...
      useRenderTool({
        name: "get_weather",
        render: ({status, args}) => {
          return (
            <p className="text-gray-500 mt-2">
              {status !== "complete" && "Calling weather API..."}
              {status === "complete" && `Called the weather API for ${args.location}.`}
            </p>
          );
        },
      });
      // ...
    }

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
