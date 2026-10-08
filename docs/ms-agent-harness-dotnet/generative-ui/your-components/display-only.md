---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/display-only/
title: Display-only
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:37.494550+00:00
---

# Display-only

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/display-only/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

Your Components

[Display-only](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/display-only)[Interactive](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/interactive)

Declarative Generative UI (A2UI)

[Readables](https://docs.copilotkit.ai/ms-agent-harness-dotnet/agent-app-context)[Copilot Runtime](https://docs.copilotkit.ai/ms-agent-harness-dotnet/copilot-runtime)[AG-UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/ag-ui)

Troubleshooting Copilots

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Display-only

Agent capabilitiesMS Agent Harness (.NET)Your Components

# Display-only

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

`useComponent` lets you register a React component as a tool your agent can invoke. When the agent calls the tool, CopilotKit renders your component directly in the chat with the tool's arguments as props.

This is the simplest form of Generative UI — your agent decides when to show a component, and CopilotKit renders it. No handler logic, no user interaction required.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables) inline in the chat
  * Show structured data from agent responses
  * Render previews, status indicators, or visual feedback
  * Let the agent present information beyond plain text



For components that need user interaction, see the Interactive or Interrupt-based guides.

## Register a component#

Use the `useComponent` hook to register a React component. The agent will be able to call it by name, and CopilotKit will render it with the tool arguments as props.

app/page.tsx
    
    
    import { useComponent } from "@copilotkit/react-core/v2"; 
    import { z } from "zod";
    
    const weatherSchema = z.object({
      city: z.string().describe("City name"),
      temperature: z.number().describe("Temperature in Fahrenheit"),
      condition: z.string().describe("Weather condition"),
    });
    
    function WeatherCard({
      city,
      temperature,
      condition,
    }: z.infer<typeof weatherSchema>) {
      return (
        <div className="rounded-lg border p-4">
          <h3 className="font-semibold">{city}</h3>
          <p className="text-2xl">{temperature}°F</p>
          <p className="text-sm text-gray-500">{condition}</p>
        </div>
      );
    }
    
    function YourMainContent() {
      useComponent({
        name: "showWeather",
        description: "Display a weather card for a city.",
        parameters: weatherSchema,
        render: WeatherCard,
      });
    
      return <div>{/* ... */}</div>;
    }

## Without parameters#

For simple components that don't need typed parameters:
    
    
    useComponent({
      name: "showGreeting",
      render: ({ message }: { message: string }) => (
        <div className="rounded border p-3 bg-blue-50">
          <p>{message}</p>
        </div>
      ),
    });

## Scoping to an agent#

In multi-agent setups, scope a component to a specific agent:
    
    
    useComponent({
      name: "renderProfile",
      parameters: z.object({ userId: z.string() }),
      render: ProfileCard,
      agentId: "support-agent",
    });

### On this page

What is this?When should I use this?Register a componentWithout parametersScoping to an agent
