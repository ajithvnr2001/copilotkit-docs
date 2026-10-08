---
url: https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:14.326765+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-based/

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

[Components as Tools](https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/langgraph-python/generative-ui/state-rendering)

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

Components as Tools

Generative UIControlled

# Components as Tools

Let your agent render rich React components directly in the chat by calling them as tools.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

gen_ui_tool_based.py

page.tsx

bar-chart.tsx

route.ts
    
    
    """LangGraph agent backing the Tool-Based Generative UI demo.The frontend registers `render_bar_chart` and `render_pie_chart` tools via`useComponent`. CopilotKit's LangGraph middleware injects those tools intothe model request at runtime so the agent can call them."""from langchain.agents import create_agentfrom langchain_openai import ChatOpenAIfrom copilotkit import CopilotKitMiddlewareSYSTEM_PROMPT = """You are a data visualization assistant.When the user asks for a chart, call `render_bar_chart` or `render_pie_chart`with a concise title, short description, and a `data` array of`{label, value}` items. Pick bar for comparisons over a small set ofcategories; pick pie for composition / share-of-whole.If the user names a chart subject but does NOT supply concrete numbers(e.g. "show me a pie chart of website traffic by source"), do NOT askthem for data. Invent plausible illustrative sample values yourself,call the appropriate `render_*` tool immediately, and briefly note inthe follow-up that the values are illustrative samples. Always renderthe chart on the first turn -- never reply with a clarifying questionasking for the data.Keep chat responses brief -- let the chart do the talking."""graph = create_agent(    model=ChatOpenAI(model="gpt-5.4"),    tools=[],    middleware=[CopilotKitMiddleware()],    system_prompt=SYSTEM_PROMPT,)

## What is this?#

Tool-based Generative UI is the simplest form of Generative UI: you register a React component with `useComponent`, and CopilotKit exposes it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component inline in the chat, passing the tool's arguments straight through as typed props.

Unlike [tool rendering](https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-rendering), which wraps a real backend tool in a custom UI, tool-based GenUI is the component. There is no handler, no user interaction, no server-side execution. The agent decides when to show it, populates the data, and CopilotKit paints it.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables, dashboards) inline in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user interaction, see [Human-in-the-loop](https://docs.copilotkit.ai/langgraph-python/human-in-the-loop). For operational transparency around a real backend tool, see [Tool rendering](https://docs.copilotkit.ai/langgraph-python/generative-ui/tool-rendering).

## How it works in code#

### Install the LangGraph Python SDK

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

### Wire CopilotKit middleware into your graph

Frontend tools registered with `useFrontendTool` are forwarded to your agent at runtime. `CopilotKitMiddleware` is the bridge — drop it into `create_agent`'s `middleware` list and the LLM sees the forwarded tool definitions on every turn.

frontend_tools.py
    
    
    from langchain.agents import create_agent
    from langchain_openai import ChatOpenAI
    from copilotkit import CopilotKitMiddleware
    
    graph = create_agent(
        model=ChatOpenAI(model="gpt-5.4"),
        tools=[],
        middleware=[CopilotKitMiddleware()],
        system_prompt="You are a helpful, concise assistant.",
    )

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

It looks up the sibling `tool`-role message for each tool call and hands both to the registered renderer. For finer placement, call `useRenderToolCall()` and paint each tool call yourself — see [Headless UI](https://docs.copilotkit.ai/langgraph-python/custom-look-and-feel/headless-ui).

### On this page

What is this?When should I use this?How it works in codeRendering in a headless chat
