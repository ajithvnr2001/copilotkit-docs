---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:05.161635+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based/

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

Components as Tools

Generative UIControlled

# Components as Tools

Let your agent render rich React components directly in the chat by calling them as tools.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

route.ts
    
    
    "use client";import React from "react";import {  CopilotChat,  CopilotKit,  useComponent,} from "@copilotkit/react-core/v2";import { BarChart, barChartPropsSchema } from "./bar-chart";import { PieChart, pieChartPropsSchema } from "./pie-chart";import { useSuggestions } from "./suggestions";function Chat() {  useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });  useComponent({    name: "render_pie_chart",    description: "Display a pie chart with labeled numeric values.",    parameters: pieChartPropsSchema,    render: PieChart,  });  useSuggestions();  return (    <div className="flex justify-center items-center h-screen w-full">      <div className="h-full w-full max-w-4xl">        <CopilotChat          agentId="gen-ui-tool-based"          className="h-full rounded-2xl"        />      </div>    </div>  );}export default function ControlledGenUiDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="gen-ui-tool-based">      <Chat />    </CopilotKit>  );}

## What is this?#

Tool-based Generative UI is the simplest form of Generative UI: you register a React component with `useComponent`, and CopilotKit exposes it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component inline in the chat, passing the tool's arguments straight through as typed props.

Unlike [tool rendering](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-rendering), which wraps a real backend tool in a custom UI, tool-based GenUI is the component. There is no handler, no user interaction, no server-side execution. The agent decides when to show it, populates the data, and CopilotKit paints it.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables, dashboards) inline in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user interaction, see [Human-in-the-loop](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop). For operational transparency around a real backend tool, see [Tool rendering](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-rendering).

## How it works in code#

### Take the forwarded tools off the Flow's state

A Flow owns its own model call, so unlike a chat agent it has to hand the forwarded tools to the model itself. Type the Flow on `CopilotKitState` and read `state.copilotkit.actions` — that is where a component registered with `useComponent` arrives.

src/agents/chart_flow.py
    
    
    from crewai.flow.flow import Flow, start
    from litellm import acompletion
    
    from ag_ui_crewai import CopilotKitState, copilotkit_stream
    
    
    class ChartFlow(Flow[CopilotKitState]):
        @start()
        async def chat(self) -> None:
            actions = self.state.copilotkit.actions or None
            response = await copilotkit_stream(
                await acompletion(
                    model="openai/gpt-5-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *self.state.messages,
                    ],
                    tools=actions,
                    parallel_tool_calls=False,
                    stream=True,
                )
            )
            self.state.messages.append(response.choices[0].message)

Wrap the call in `copilotkit_stream` so the tool call reaches the browser as it streams. A Flow that returns only when the model is finished renders nothing until the turn ends.

### Decide when the component is required

The Flow controls `tool_choice`, which is the lever a chat agent does not have. Forcing the call on the user's turn and leaving it on `auto` afterwards is what renders the component immediately and still lets the run end: the follow-up turn is plain narration once the browser has returned the result.

src/agents/chart_flow.py
    
    
    on_user_turn = bool(
        self.state.messages and self.state.messages[-1].get("role") == "user"
    )
    tool_choice = "required" if actions and on_user_turn else "auto"

Leaving `tool_choice` on `auto` for every turn is the usual reason a Flow answers in prose and the component never appears.

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

It looks up the sibling `tool`-role message for each tool call and hands both to the registered renderer. For finer placement, call `useRenderToolCall()` and paint each tool call yourself — see [Headless UI](https://docs.copilotkit.ai/crewai-crews/custom-look-and-feel/headless-ui).

### On this page

What is this?When should I use this?How it works in codeRendering in a headless chat
