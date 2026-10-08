---
url: https://docs.copilotkit.ai/llamaindex/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:47.189856+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/llamaindex/generative-ui/display/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)[Build Generative UI](https://docs.copilotkit.ai/llamaindex/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

gen_ui_tool_based_agent.py

page.tsx

bar-chart.tsx

pie-chart.tsx

route.ts
    
    
    """LlamaIndex agent for the Tool-Based Generative UI demo.The frontend registers `render_bar_chart` and `render_pie_chart` tools via`useComponent`. The AG-UI protocol forwards those tool definitions to theagent at request time, so the backend agent itself declares no bespoketools — the LLM sees the frontend tools through the AG-UI request payloadand picks one to call when the user asks for a chart.Mirrors `langgraph-python/src/agents/gen_ui_tool_based.py`."""from __future__ import annotationsimport osfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.router import get_ag_ui_workflow_routerSYSTEM_PROMPT = """You are a data visualization and creative assistant.When the user asks for a chart, call `render_bar_chart` or `render_pie_chart`with a concise title, short description, and a `data` array of`{label, value}` items. Pick bar for comparisons over a small set ofcategories; pick pie for composition / share-of-whole.When the user asks for a haiku, call `generate_haiku` with the Japanesetext, English translation, an image name, and a gradient color.Keep chat responses brief -- let the visual output do the talking."""_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]gen_ui_tool_based_router = get_ag_ui_workflow_router(    llm=OpenAI(model="gpt-5-mini", **_openai_kwargs),    frontend_tools=[],    backend_tools=[],    system_prompt=SYSTEM_PROMPT,    initial_state={},)

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

The AG-UI protocol forwards frontend tool definitions to the agent at request time, so the backend agent declares no bespoke tools. The LLM sees a component registered with `useComponent` through the AG-UI request payload and picks it when the user asks for what it draws.

src/agents/chart_agent.py
    
    
    from llama_index.llms.openai import OpenAI
    
    llm = OpenAI(model="gpt-5-mini")

### Tell the model when to call it

The tool arrives on every run, but a model with no instruction about it will answer in prose instead of calling it. Name the tool in the system prompt.

src/agents/chart_agent.py
    
    
    SYSTEM_PROMPT = """You are a data visualization assistant.
    
    When the user asks for a chart, call `render_bar_chart` with a concise
    title and a `data` array of `{label, value}` items."""

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
