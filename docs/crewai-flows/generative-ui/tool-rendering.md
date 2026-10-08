---
url: https://docs.copilotkit.ai/crewai-flows/generative-ui/tool-rendering/
title: Tool Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:35:52.376307+00:00
---

# Tool Rendering

> Source: https://docs.copilotkit.ai/crewai-flows/generative-ui/tool-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/crewai-crews/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Generative UIControlled

# Tool Rendering

Render your agent's tool calls with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates the implementation section applied in the CopilotKit feature viewer.

## What is this?

Tools are a way for the LLM to call predefined, typically, deterministic functions. CopilotKit allows you to render these tools in the UI as a custom component, which we call **Generative UI**.

## When should I use this?

Rendering tools in the UI is useful when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Render tool calls in your frontend

Use the `useRenderTool` hook to render tool calls in the UI. The name must match the name of the tool defined in your agent.

Important

In order to render a tool call in the UI, the name must match the name of the tool. [Learn more](https://docs.copilotkit.ai/server-tools).

app/page.tsx
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2"; 
    import { z } from "zod";
    // ...
    
    const weatherParams = z.object({
      location: z.string().describe("The location to get weather for"),
    });
    
    const YourMainContent = () => {
      // ...
      useRenderTool({
        name: "get_weather",
        parameters: weatherParams,
        render: ({ status, parameters }) => {
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

## Default Tool Rendering

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
