---
url: https://docs.copilotkit.ai/ms-agent-python/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:06.632287+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/ms-agent-python/generative-ui/display/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)[Build Generative UI](https://docs.copilotkit.ai/ms-agent-python/generative-ui)

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
    
    
    """MS Agent Framework agent backing the Tool-Based Generative UI demo.The frontend registers `render_bar_chart` and `render_pie_chart` tools via`useComponent`. CopilotKit's runtime forwards those frontend tool definitionsto the agent at request time, so the agent can call them by name.There are no backend tools here -- the agent's job is to recognize chartintent in the user's message and emit a tool call with structured chart data.The frontend then renders the result inline."""from __future__ import annotationsfrom textwrap import dedentfrom agent_framework import Agent, BaseChatClientfrom agent_framework_ag_ui import AgentFrameworkAgentSYSTEM_PROMPT = dedent(    """    You are a data visualization assistant.    When the user asks for a chart, call `render_bar_chart` or    `render_pie_chart` with a concise title, short description, and a `data`    array of `{label, value}` items. Pick bar for comparisons over a small set    of categories; pick pie for composition / share-of-whole.    Keep chat responses brief -- let the chart do the talking. After you    finish executing tools, send a brief final assistant message so it    persists in the conversation.    """).strip()def create_gen_ui_tool_based_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:    """Instantiate the Tool-Based Generative UI demo agent."""    base_agent = Agent(        client=chat_client,        name="gen_ui_tool_based_agent",        instructions=SYSTEM_PROMPT,        # Both rendering tools (`render_bar_chart`, `render_pie_chart`) are        # registered on the frontend via `useComponent`. The runtime forwards        # them as tool definitions at request time.        tools=[],    )    return AgentFrameworkAgent(        agent=base_agent,        name="CopilotKitMSAgentGenUiToolBasedAgent",        description=(            "Data-visualization assistant that turns chart requests into "            "frontend-rendered bar and pie charts via tool calls."        ),        require_confirmation=False,    )

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

CopilotKit's runtime forwards frontend tool definitions to the agent at request time, so the agent can call a component registered with `useComponent` by name. There are no backend tools to declare.

src/agents/chart_agent.py
    
    
    from agent_framework import Agent
    
    agent = Agent(
        chat_client=chat_client,
        instructions=SYSTEM_PROMPT,
    )

### Tell the model when to call it

The agent's job here is to recognize the intent in the user's message and emit a tool call with structured data. Say so in the instructions, or the model will answer in prose and the component will never render.

src/agents/chart_agent.py
    
    
    SYSTEM_PROMPT = """
    You are a data visualization assistant.
    
    When the user asks for a chart, call `render_bar_chart` with a concise
    title and a `data` array of `{label, value}` items.
    """

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
