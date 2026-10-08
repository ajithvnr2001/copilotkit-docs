---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:01.319775+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/display/

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

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)[Build Generative UI](https://docs.copilotkit.ai/crewai-crews/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

route.ts
    
    
    "use client";import React from "react";import {  CopilotChat,  CopilotKit,  useComponent,} from "@copilotkit/react-core/v2";import { BarChart, barChartPropsSchema } from "./bar-chart";import { PieChart, pieChartPropsSchema } from "./pie-chart";import { useSuggestions } from "./suggestions";function Chat() {  useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });  useComponent({    name: "render_pie_chart",    description: "Display a pie chart with labeled numeric values.",    parameters: pieChartPropsSchema,    render: PieChart,  });  useSuggestions();  return (    <div className="flex justify-center items-center h-screen w-full">      <div className="h-full w-full max-w-4xl">        <CopilotChat          agentId="gen-ui-tool-based"          className="h-full rounded-2xl"        />      </div>    </div>  );}export default function ControlledGenUiDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="gen-ui-tool-based">      <Chat />    </CopilotKit>  );}

## What is this?#

Render-only generative UI lets you register React components as tools your agent can invoke. When the agent calls the tool, CopilotKit renders your component directly in the chat with the tool's arguments as props; no handler logic or user interaction required.

page.tsxchart.tsx
    
    
    useComponent({
    name: "showChart",
    description: "Populate data and show the user a chart",
    parameters: ChartProps,
    render: Chart
    });
    
    
    
    export const ChartProps = z.object({
      title: z.string(),
      data: z.array(z.object({ label: z.string(), value: z.number() })),
    });
    
    export function Chart({ title, data }: z.infer<typeof ChartProps>) {
      return (
        <div>
          <h3>{title}</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <XAxis dataKey="label" /><YAxis /><Tooltip />
              <Bar dataKey="value" fill="#6366f1" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      );
    }

## When should I use this?#

Use render-only generative UI when you want to:

  * Display rich UI (cards, charts, tables) inline in the chat
  * Show structured data from agent responses
  * Render previews, status indicators, or visual feedback
  * Let the agent present information beyond plain text



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

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
