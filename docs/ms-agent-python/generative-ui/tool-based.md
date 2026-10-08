---
url: https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:14.071905+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-based/

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

[Components as Tools](https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/ms-agent-python/generative-ui/state-rendering)

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

Components as Tools

Generative UIControlled

# Components as Tools

Let your agent render rich React components directly in the chat by calling them as tools.

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

Tool-based Generative UI is the simplest form of Generative UI: you register a React component with `useComponent`, and CopilotKit exposes it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component inline in the chat, passing the tool's arguments straight through as typed props.

Unlike [tool rendering](https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-rendering), which wraps a real backend tool in a custom UI, tool-based GenUI is the component. There is no handler, no user interaction, no server-side execution. The agent decides when to show it, populates the data, and CopilotKit paints it.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables, dashboards) inline in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user interaction, see [Human-in-the-loop](https://docs.copilotkit.ai/ms-agent-python/human-in-the-loop). For operational transparency around a real backend tool, see [Tool rendering](https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-rendering).

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

It looks up the sibling `tool`-role message for each tool call and hands both to the registered renderer. For finer placement, call `useRenderToolCall()` and paint each tool call yourself — see [Headless UI](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/headless-ui).

### On this page

What is this?When should I use this?How it works in codeRendering in a headless chat
