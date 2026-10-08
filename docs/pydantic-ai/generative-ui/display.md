---
url: https://docs.copilotkit.ai/pydantic-ai/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:59.869130+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/pydantic-ai/generative-ui/display/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)[Build Generative UI](https://docs.copilotkit.ai/pydantic-ai/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

gen_ui_tool_based.py

page.tsx

bar-chart.tsx

pie-chart.tsx

route.ts
    
    
    """PydanticAI agent backing the Tool-Based Generative UI demo.Mirrors showcase/integrations/langgraph-python/src/agents/gen_ui_tool_based.py.The frontend registers `render_bar_chart` and `render_pie_chart` tools via`useComponent`. CopilotKit's runtime injects those tool definitions into theagent request at runtime, so the agent does not need to declare them locally —PydanticAI's AG-UI bridge surfaces frontend-registered tools to the model oneach run, and the model decides when to call them."""from __future__ import annotationsfrom textwrap import dedentfrom pydantic_ai import Agentfrom pydantic_ai.models.openai import OpenAIResponsesModelSYSTEM_PROMPT = dedent(    """    You are a data visualization assistant.    When the user asks for a chart, call `render_bar_chart` or    `render_pie_chart` with a concise title, short description, and a    `data` array of `{label, value}` items. Pick bar for comparisons over    a small set of categories; pick pie for composition / share-of-whole.    Keep chat responses brief — let the chart do the talking.    """).strip()agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    system_prompt=SYSTEM_PROMPT,)

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

### Nothing to wire on the agent

PydanticAI's AG-UI bridge surfaces frontend-registered tools to the model on every run, so the agent declares no tools of its own. A component registered with `useComponent` reaches the model through the AG-UI request payload and the model calls it by name.

src/agents/chart_agent.py
    
    
    from pydantic_ai import Agent
    from pydantic_ai.models.openai import OpenAIResponsesModel
    
    agent = Agent(
        model=OpenAIResponsesModel("gpt-5-mini"),
        system_prompt=SYSTEM_PROMPT,
    )

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in the system prompt and say what it is for.

src/agents/chart_agent.py
    
    
    SYSTEM_PROMPT = """
    You are a data visualization assistant.
    
    When the user asks for a chart, call `render_bar_chart` with a concise
    title and a `data` array of `{label, value}` items.
    
    Keep chat responses brief — let the chart do the talking.
    """

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
