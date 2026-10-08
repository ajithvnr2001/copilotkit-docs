---
url: https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:44.802344+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)

# Prebuilt Components

Drop-in chat components with a full customization ladder, from pure CSS to fully headless.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """LangGraph agent for the CopilotKit Showcase (FastAPI variant).Uses copilotkit's create_agent (wrapping langgraph) with CopilotKitMiddlewareso frontend-registered tools (useHumanInTheLoop, useFrontendTool) are properlyinjected into the LLM's tool list and executed on the frontend rather thanlocally."""from tools import (    get_weather_impl,    query_data_impl,    schedule_meeting_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)from tools.types import SalesTodo, Flightimport jsonimport timefrom typing import Anyfrom langchain_openai import ChatOpenAIfrom langchain_core.tools import tool as lc_toolfrom langchain_core.messages import SystemMessagefrom langchain.agents import AgentState as BaseAgentState, create_agentfrom langchain.tools import ToolRuntime, toolfrom langchain.messages import ToolMessagefrom langgraph.types import Commandfrom copilotkit import CopilotKitMiddlewareclass AgentState(BaseAgentState):    todos: list[SalesTodo]@lc_tooldef get_weather(location: str):    """Get the current weather for a location."""    return get_weather_impl(location)@lc_tooldef query_data(query: str):    """Query the database. Takes natural language. Always call before showing a chart."""    return query_data_impl(query)@lc_tooldef schedule_meeting(reason: str, duration_minutes: int = 30):    """Schedule a meeting. The user will be asked to pick a time via the UI."""    return schedule_meeting_impl(reason, duration_minutes)@lc_tooldef search_flights(flights: list[Flight]) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    result = search_flights_impl(flights)    return json.dumps(result)@tooldef manage_sales_todos(todos: list[SalesTodo], runtime: ToolRuntime) -> Command:    """    Manage the current sales todos. Pass the full updated list.    """    updated = manage_sales_todos_impl(todos)    return Command(        update={            "todos": updated,            "messages": [                ToolMessage(                    content="Successfully updated sales todos",                    tool_call_id=runtime.tool_call_id,                )            ],        }    )@tooldef get_sales_todos(runtime: ToolRuntime):    """    Get the current sales todos.    """    current = runtime.state.get("todos", [])    return get_sales_todos_impl(current if current else None)@lc_tooldef render_a2ui(    surfaceId: str,    catalogId: str,    components: list[dict],    data: dict | None = None,) -> str:    """Render a dynamic A2UI v0.9 surface."""    return "rendered"@tool()def generate_a2ui(runtime: ToolRuntime[Any]) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data.    """    t0 = time.time()    messages = runtime.state["messages"][:-1]    context_entries = runtime.state.get("copilotkit", {}).get("context", [])    context_text = "\n\n".join(        entry.get("value", "")        for entry in context_entries        if isinstance(entry, dict) and entry.get("value")    )    model = ChatOpenAI(model="gpt-5-mini")    model_with_tool = model.bind_tools([render_a2ui], tool_choice="render_a2ui")    response = model_with_tool.invoke(        [SystemMessage(content=context_text), *messages],    )    if not response.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    args = response.tool_calls[0]["args"]    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)model = ChatOpenAI(model="gpt-5-mini")SYSTEM_PROMPT = """You are a polished, professional demo assistant for CopilotKit.Keep responses brief and clear -- 1 to 2 sentences max.You can:- Chat naturally with the user- Change the UI background when asked (via frontend tool)- Query data and render charts (via query_data tool)- Get weather information (via get_weather tool)- Schedule meetings with the user (via schedule_meeting tool -- the user picks a time in the UI)- Manage sales pipeline todos (via manage_sales_todos / get_sales_todos tools)- Search flights and display rich A2UI cards (via search_flights tool)- Generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool)- Generate step-by-step plans for user review (human-in-the-loop)"""graph = create_agent(    model=model,    tools=[        get_weather,        query_data,        schedule_meeting,        search_flights,        generate_a2ui,        manage_sales_todos,        get_sales_todos,    ],    middleware=[CopilotKitMiddleware()],    state_schema=AgentState,    system_prompt=SYSTEM_PROMPT,)

[Want users to resume conversations across sessions?Persistent threads ship with CopilotKit Intelligence. Try it for free.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_prebuilt_components&utm_frontend=react&utm_backend=langgraph-fastapi)

## Pre-built components for agentic chat#

CopilotKit ships three prebuilt chat surfaces that connect directly to your agent: [**CopilotChat**](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/chat), [**CopilotSidebar**](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/sidebar), and [**CopilotPopup**](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/popup). Each is a wrapper around the same primitives with a different layout. Pick the one that fits your app; they all handle streaming, generative UI, and deep customization.

If your chat surface needs saved conversations, history, or thread switching, drop in the [**Threads Drawer**](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/copilot-threads-drawer) next to any of them — or build your own switcher with [Headless Threads](https://docs.copilotkit.ai/langgraph-fastapi/headless-threads).

## The customization ladder#

One of CopilotKit's design principles is that **you should never have to throw the prebuilt UI away** to get the look you want. Start at the top of this ladder and step down only when you need more control.

[Level 1 · EasiestDrop in as-isRender `<CopilotChat>`, `<CopilotSidebar>`, or `<CopilotPopup>` and ship. Streaming, tool calls, generative UI, and suggestions, all wired up.](https://docs.copilotkit.ai/prebuilt-components/chat)[Level 2 · Re-skinCustomize with CSSOverride theme tokens (`--copilot-kit-primary-color`, etc.) or target `.copilotKit...` classes. Keep every feature, change every color.](https://docs.copilotkit.ai/custom-look-and-feel/css)[Level 3 · RecomposeCustomize via slots (subcomponents)Swap the welcome screen, message bubble, composer, disclaimer, header, or toggle button with your own React component. Recursive; drill down as deep as you want.](https://docs.copilotkit.ai/custom-look-and-feel/slots)[Level 4 · Full controlGo fully headlessCompose your own chat from the low-level hooks (`useAgent`, `useCopilotKit`, `useRenderToolCall`). Any layout, any design system, or even non-chat surfaces.](https://docs.copilotkit.ai/custom-look-and-feel/headless-ui)

Everything below Level 1 is incremental: you can freely mix CSS variables, a custom welcome slot, and headless tool-call renderers in the same app. Nothing forces you to throw work away as your needs grow.

## Drop-in chat in a few lines#

Wrap your app in `<CopilotKit>` and drop `<CopilotChat>` where the chat should live. The provider wires the runtime, the session, and the agent registry. Everything else is optional configuration:

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

## Starter suggestions#

`useConfigureSuggestions` lets you seed the chat with contextual prompts the moment a user arrives. The example below uses a single "Write a sonnet" suggestion:

suggestions.ts
    
    
    export function useAgenticChatSuggestions() {  useConfigureSuggestions({    suggestions: [      { title: "Write a sonnet", message: "Write a short sonnet about AI." },      {        title: "Tell me a joke",        message: "Tell me a one-line joke.",      },      {        title: "Is 17 prime?",        message: "Walk me through whether 17 is prime.",      },    ],    available: "always",  });}

## Pick a surface#

Each surface is a drop-in component with the same underlying primitives, differing only in layout.

  * [`<CopilotChat>`](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/chat): inline chat pane you can place anywhere and size to fit.
  * [`<CopilotSidebar>`](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/sidebar): collapsible sidebar docked to the edge of your app.
  * [`<CopilotPopup>`](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/popup): floating bubble that overlays your page content.



Add a conversation-history sidebar next to any of these with [Threads Drawer](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/copilot-threads-drawer) — a drop-in thread switcher with no active-thread wiring.

Need to open/close the chat from your own button, or capture thumbs-up/down feedback? See [Open, close, and feedback](https://docs.copilotkit.ai/langgraph-fastapi/prebuilt-components/chat-controls).
