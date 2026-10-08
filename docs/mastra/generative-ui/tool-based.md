---
url: https://docs.copilotkit.ai/mastra/generative-ui/tool-based/
title: Tool Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:33.406965+00:00
---

# Tool Rendering

> Source: https://docs.copilotkit.ai/mastra/generative-ui/tool-based/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/mastra/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/mastra/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/mastra/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

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

## What is this?#

Tools are a way for the LLM to call predefined, typically, deterministic functions. CopilotKit allows you to render these tools in the UI as a custom component, which we call **Generative UI**.

## When should I use this?#

Rendering tools in the UI is useful when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Give your agent a tool to call#

Add a new tool definition:

src/mastra/tools/weatherInfo.ts
    
    
    import { createTool } from "@mastra/core/tools";
    import { z } from "zod";
    
    export const weatherInfo = createTool({
      id: "weatherInfo",
      inputSchema: z.object({
        location: z.string(),
      }),
      description: `Fetches the current weather information for a given location`,
      execute: async ({ location }) => {
        // Tool logic here (e.g., API call)
        console.log("Using tool to fetch weather information for", location);
        return { temperature: 20, conditions: "Sunny" }; // Example return
      },
    });

Then, pass the tool to the agent:

src/mastra/agents/weatherAgent.ts
    
    
    import { Agent } from "@mastra/core/agent";
    import { openai } from "@ai-sdk/openai";
    import { weatherInfo } from "../tools/weatherInfo";
    
    export const weatherAgent = new Agent({
      id: "weather-agent",
      name: "Weather Agent",
      instructions:
        "You are a helpful assistant that provides current weather information. When asked about the weather, use the weather information tool to fetch the data.",
      model: openai("gpt-5.4-mini"),
      tools: {
        weatherInfo,
      },
    });

### Render the tool call in your frontend#

At this point, your agent will be able to call the `weatherInfo` tool. Now we just need to add a `useRenderTool` hook to render the tool call in the UI.

Important

In order to render a tool call in the UI, the name of the action must match the name of the tool.

app/page.tsx
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2"; 
    // ...
    
    const YourMainContent = () => {
      // ...
      useRenderTool({
        name: "weatherInfo",
        render: ({ status, args }) => {
          return (
            <p className="text-gray-500 mt-2">
              {status !== "complete" && "Calling weather API..."}
              {status === "complete" &&
                `Called the weather API for ${args.location}.`}
            </p>
          );
        },
      });
      // ...
    };

### Give it a try!#

Try asking the agent to get the weather for a location. You should see the custom UI component that we added render the tool call and display the arguments that were passed to the tool.

### On this page

What is this?When should I use this?ImplementationRun and connect your agentGive your agent a tool to callRender the tool call in your frontendGive it a try!
