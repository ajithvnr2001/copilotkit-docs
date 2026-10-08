---
url: https://docs.copilotkit.ai/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:08.002806+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/generative-ui/tool-based/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Components as Tools

Generative UIControlled

# Components as Tools

Let your agent render rich React components directly in the chat by calling them as tools.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

bar-chart.tsx

tanstack-factory.ts

route.ts
    
    
    "use client";import React from "react";import {  CopilotChat,  CopilotKit,  useComponent,} from "@copilotkit/react-core/v2";import { BarChart, barChartPropsSchema } from "./bar-chart";import { PieChart, pieChartPropsSchema } from "./pie-chart";import { useSuggestions } from "./suggestions";function Chat() {  useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });  useComponent({    name: "render_pie_chart",    description: "Display a pie chart with labeled numeric values.",    parameters: pieChartPropsSchema,    render: PieChart,  });  useSuggestions();  return (    <div className="flex justify-center items-center h-screen w-full">      <div className="h-full w-full max-w-4xl">        <CopilotChat          agentId="gen-ui-tool-based"          className="h-full rounded-2xl"        />      </div>    </div>  );}export default function ControlledGenUiDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="gen-ui-tool-based">      <Chat />    </CopilotKit>  );}

## What is this?#

Tool-based Generative UI is the simplest form of Generative UI: you register a React component with `useComponent`, and CopilotKit exposes it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component inline in the chat, passing the tool's arguments straight through as typed props.

Unlike [tool rendering](https://docs.copilotkit.ai/generative-ui/tool-rendering), which wraps a real backend tool in a custom UI, tool-based GenUI is the component. There is no handler, no user interaction, no server-side execution. The agent decides when to show it, populates the data, and CopilotKit paints it.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables, dashboards) inline in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user interaction, see [Human-in-the-loop](https://docs.copilotkit.ai/human-in-the-loop). For operational transparency around a real backend tool, see [Tool rendering](https://docs.copilotkit.ai/generative-ui/tool-rendering).

## How it works in code#

### Nothing to wire in config mode

A `BuiltInAgent` built from configuration merges the request's tool definitions into the tool list it hands the model, so the agent declares none of its own. A component registered with `useComponent` reaches the model by name with no extra wiring.

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      prompt: SYSTEM_PROMPT,
    });

Keep the `useComponent` name distinct from every tool in `config.tools`. The runtime layers the configured tools over the forwarded ones, so a shared name resolves to the backend tool and the component never renders.

### In factory mode you pass the tools yourself

A factory owns the model call, so `BuiltInAgent` ignores `config.tools` and forwards nothing on your behalf. Read the tools off `input` and pass them to the model, or the component never renders.

app/api/copilotkit/factory.ts
    
    
    import {
      BuiltInAgent,
      convertMessagesToVercelAISDKMessages,
      convertToolsToVercelAITools,
    } from "@copilotkit/runtime/v2";
    import { openai } from "@ai-sdk/openai";
    import { streamText } from "ai";
    
    const agent = new BuiltInAgent({
      type: "aisdk",
      factory: ({ input, abortSignal }) =>
        streamText({
          model: openai("gpt-4o"),
          messages: convertMessagesToVercelAISDKMessages(input.messages),
          tools: convertToolsToVercelAITools(input.tools),
          abortSignal,
        }),
    });

The factory owns precedence here. Nothing merges the two lists for you, so a backend tool and a `useComponent` registration that share a name is your conflict to resolve. Keep the names distinct.

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in the prompt and say what it is for.

app/api/copilotkit/prompts.ts
    
    
    export const SYSTEM_PROMPT = `You are a data visualization assistant.
    
    When the user asks for a chart, call \`render_bar_chart\` with a concise
    title and a \`data\` array of \`{label, value}\` items.
    
    If the user names a subject but supplies no numbers, invent plausible
    sample values and render the chart on the first turn. Never reply with a
    clarifying question asking for the data.`;

Import the React hook and Zod in the component that registers the tool. This also applies to the built-in agent, which needs no backend tool-registration step.
    
    
    import { useComponent } from "@copilotkit/react-core/v2";
    import { z } from "zod";

`useComponent` takes a name, a Zod schema for its props, and the component to render. The runtime registers it as a frontend tool so the agent can discover it, and the schema becomes that tool's parameter definition — it is what tells the model which arguments to send.

`parameters` is optional, but leaving it out advertises the tool with an empty parameter schema (`{ "type": "object", "properties": {} }`). The model then has nothing to fill in, so it calls the tool with no arguments and your component renders with no props. Pass a schema for any component that needs data.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });

The component itself is ordinary React: it reads only its props and can stream in as the agent fills the payload. The example above uses [Recharts](https://recharts.org) for the bar chart; it doesn't know anything about CopilotKit.

The `name` you pass to `useComponent` is what the agent sees as the tool name. Make it a verb like `render_bar_chart` or `show_weather` so the LLM reliably picks it when the user asks for that visualization.

## Rendering in a headless chat#

CopilotKit's built-in chat components paint registered components for you. A headless or custom chat renders the message list itself, so nothing paints a tool call unless you render it — the component is registered and the agent calls it, but the chat stays empty.

Render the tool calls on each assistant message with `CopilotChatToolCallsView`:
    
    
    import { CopilotChatToolCallsView } from "@copilotkit/react-core/v2";
    
    <CopilotChatToolCallsView message={assistantMessage} messages={allMessages} />;

It looks up the sibling `tool`-role message for each tool call and hands both to the registered renderer. For finer placement, call `useRenderToolCall()` and paint each tool call yourself — see [Headless UI](https://docs.copilotkit.ai/custom-look-and-feel/headless-ui).

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/tool-based).

### On this page

What is this?When should I use this?How it works in codeRendering in a headless chat
