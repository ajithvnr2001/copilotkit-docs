---
url: https://docs.copilotkit.ai/langgraph-python/generative-ui/your-components/display-only/
title: Display-only
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:15.274940+00:00
---

# Display-only

> Source: https://docs.copilotkit.ai/langgraph-python/generative-ui/your-components/display-only/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)[Build Generative UI](https://docs.copilotkit.ai/langgraph-python/generative-ui)Your Components

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



For components that need user interaction, see [Interactive](https://docs.copilotkit.ai/langgraph/generative-ui/your-components/interactive) or [Interrupt-based](https://docs.copilotkit.ai/langgraph/generative-ui/your-components/interrupt-based).

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Register a component#

Use the `useComponent` hook to register a React component. The agent will be able to call it by name, and CopilotKit will render it with the tool arguments as props.

app/page.tsx
    
    
    import { useComponent } from "@copilotkit/react-core/v2"; 
    import { z } from "zod";
    
    const weatherSchema = z.object({
      city: z.string().describe("City name"),
      temperature: z.number().describe("Temperature in Fahrenheit"),
      condition: z.string().describe("Weather condition"),
    });
    
    function WeatherCard({ city, temperature, condition }: z.infer<typeof weatherSchema>) {
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

### Install the CopilotKit SDK#

Now, we'll need to make sure your agent can access frontend tools. In your terminal, navigate to your agent's folder and continue from there.

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Inherit from CopilotKitState#

To access the frontend tools provided by CopilotKit, inherit from `CopilotKitState` in your agent's state definition:

PythonTypeScript

agent.py
    
    
    from copilotkit import CopilotKitState 
    
    class AgentState(CopilotKitState): 
        pass

agent-js/src/agent.ts
    
    
    import { StateSchema } from "@langchain/langgraph";
    import { CopilotKitStateSchema } from "@copilotkit/sdk-js/langgraph"; 
    
    export const AgentStateSchema = new StateSchema({
      ...CopilotKitStateSchema.fields, 
    });
    export type AgentState = typeof AgentStateSchema.State;

### Agent calls the component#

When your agent's LLM decides to use the tool, CopilotKit automatically renders your component in the chat. The tool is registered as a frontend tool that the agent can discover and call.

DemoCode

## What is this?#

Frontend tools enable you to define client-side functions that your agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized to let your agent control the UI, for generative UI, or for Human-in-the-loop interactions. In this guide, we cover the use of frontend tools driving and interacting with the UI.

## When should I use this?#

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Create a frontend tool#

Use the `useFrontendTool` hook to create a tool that your agent can call from the client side:

page.tsx
    
    
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/react-core/v2"; 
    
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

### Give it a try!#

Ask your agent something that would trigger the component (e.g. "What's the weather in San Francisco?"). You should see your `WeatherCard` rendered directly in the chat.

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

What is this?When should I use this?Implementation
