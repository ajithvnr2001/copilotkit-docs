---
url: https://docs.copilotkit.ai/deepagents/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:04.564423+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/deepagents/generative-ui/display/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Deep Agents](https://docs.copilotkit.ai/deepagents)[Build Generative UI](https://docs.copilotkit.ai/deepagents/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`gen-ui-tool-based`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/generative-ui/display), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/display), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/display).

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

### Wire CopilotKit middleware into your agent

Deep Agents compile to LangGraph graphs, and `CopilotKitMiddleware` is the bridge. It reads the forwarded tools off the request and merges them into the tool list the model sees, so a component registered with `useComponent` only reaches the model when the middleware is present.

agent.py
    
    
    from deepagents import create_deep_agent
    from copilotkit import CopilotKitMiddleware
    
    agent = create_deep_agent(
        model="openai:gpt-5.4",
        tools=[],  # Backend tools go here
        middleware=[CopilotKitMiddleware()],
        system_prompt=SYSTEM_PROMPT,
    )

Without the middleware the run still completes, and the component never renders, because the model was never told the tool exists.

### Tell the model when to call it

The forwarded tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in `system_prompt` and say what it is for.

agent.py
    
    
    SYSTEM_PROMPT = """
    You are a data visualization assistant.
    
    When the user asks for a chart, call `render_bar_chart` with a concise
    title and a `data` array of `{label, value}` items.
    
    Keep chat responses brief and let the chart do the talking.
    """

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

Missing snippet

No demo found for `deepagents::gen-ui-tool-based`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.
