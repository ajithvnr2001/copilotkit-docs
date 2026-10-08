---
url: https://docs.copilotkit.ai/pydantic-ai/prebuilt-components/popup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:24.080513+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/pydantic-ai/prebuilt-components/popup/

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

On this page

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)[Prebuilt Components](https://docs.copilotkit.ai/pydantic-ai/prebuilt-components)

# CopilotPopup

Floating chat bubble that toggles open an overlay chat window.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """PydanticAI agent with sales todos state, weather/query tools, and HITL scheduling.Upgraded from proverbs demo to full feature parity with shared tool implementations."""import jsonfrom textwrap import dedentfrom typing import Anyfrom pydantic import BaseModel, Fieldfrom pydantic_ai import Agent, RunContextfrom pydantic_ai.ui import StateDepsfrom ag_ui.core import EventType, StateSnapshotEventfrom pydantic_ai.models.openai import OpenAIResponsesModelfrom dotenv import load_dotenvfrom tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)from tools.types import Flightload_dotenv()# =====# State# =====class SalesTodosState(BaseModel):    """Sales pipeline todos managed by the agent."""    todos: list[dict[str, Any]] = Field(        default_factory=list,        description="The list of sales pipeline todos",    )# =====# Agent# =====agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    deps_type=StateDeps[SalesTodosState],    system_prompt=dedent("""        You are a helpful sales assistant that helps manage a sales pipeline.        The user has a list of sales todos that you can help them manage.        You have tools available to add, update, or retrieve todos from the pipeline.        You can also look up weather and query financial data.        You can search flights and display rich A2UI cards (via search_flights tool).        You can generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool).        When discussing sales todos, ALWAYS use the get_sales_todos tool to see the current list        before mentioning, updating, or discussing todos with the user.    """).strip(),)# =====# Tools# =====@agent.tooldef get_weather(ctx: RunContext[StateDeps[SalesTodosState]], location: str) -> str:    """Get the weather for a given location. Ensure location is fully spelled out.    Useful on its own for weather questions, and a great companion to    `search_flights` — always consider checking the weather at a    destination the user is flying to, and checking flights to any    city whose weather the user has just asked about.    """    return json.dumps(get_weather_impl(location))@agent.tooldef query_data(ctx: RunContext[StateDeps[SalesTodosState]], query: str) -> str:    """Query financial database for chart data. Returns data suitable for pie or bar charts."""    return json.dumps(query_data_impl(query))@agent.toolasync def manage_sales_todos(    ctx: RunContext[StateDeps[SalesTodosState]], todos: list[dict[str, Any]]) -> StateSnapshotEvent:    """Manage the sales pipeline. Pass the complete list of sales todos."""    result = manage_sales_todos_impl(todos)    ctx.deps.state.todos = result    return StateSnapshotEvent(        type=EventType.STATE_SNAPSHOT,        snapshot=ctx.deps.state,    )@agent.tooldef get_sales_todos(ctx: RunContext[StateDeps[SalesTodosState]]) -> str:    """Get the current list of sales pipeline todos."""    return json.dumps(get_sales_todos_impl(ctx.deps.state.todos or None))@agent.tooldef schedule_meeting(    ctx: RunContext[StateDeps[SalesTodosState]], reason: str, duration_minutes: int = 30) -> str:    """Schedule a meeting. The user will be asked to pick a time via the UI."""    return json.dumps(schedule_meeting_impl(reason, duration_minutes))@agent.tooldef search_flights(    ctx: RunContext[StateDeps[SalesTodosState]], flights: list[dict[str, Any]]) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    result = search_flights_impl(flights)    return json.dumps(result)@agent.tooldef generate_a2ui(ctx: RunContext[StateDeps[SalesTodosState]]) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    """    from openai import OpenAI    # Extract conversation messages from deps    copilotkit_state = getattr(ctx.deps, "copilotkit", None)    conversation_messages: list[dict] = []    context_entries: list[dict] = []    if copilotkit_state:        if hasattr(copilotkit_state, "messages"):            for msg in copilotkit_state.messages or []:                role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)                if role in ("user", "assistant"):                    content = ""                    if hasattr(msg, "content"):                        if isinstance(msg.content, str):                            content = msg.content                        elif isinstance(msg.content, list):                            parts = []                            for part in msg.content:                                if hasattr(part, "text"):                                    parts.append(part.text)                                elif isinstance(part, dict) and "text" in part:                                    parts.append(part["text"])                            content = "".join(parts)                    if content:                        conversation_messages.append({"role": role, "content": content})        if hasattr(copilotkit_state, "context"):            context_entries = copilotkit_state.context or []    context_text = "\n\n".join(        entry.get("value", "")        for entry in context_entries        if isinstance(entry, dict) and entry.get("value")    )    client = OpenAI()    tool_schema = {        "type": "function",        "function": {            "name": "render_a2ui",            "description": "Render a dynamic A2UI v0.9 surface.",            "parameters": {                "type": "object",                "properties": {                    "surfaceId": {"type": "string"},                    "catalogId": {"type": "string"},                    "components": {"type": "array", "items": {"type": "object"}},                    "data": {"type": "object"},                },                "required": ["surfaceId", "catalogId", "components"],            },        },    }    llm_messages: list[dict] = [        {            "role": "system",            "content": context_text or "Generate a useful dashboard UI.",        },    ]    llm_messages.extend(conversation_messages)    response = client.chat.completions.create(        model="gpt-5-mini",        messages=llm_messages,        tools=[tool_schema],        tool_choice={"type": "function", "function": {"name": "render_a2ui"}},    )    if not response.choices[0].message.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    tool_call = response.choices[0].message.tool_calls[0]    args = json.loads(tool_call.function.arguments)    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)

## What is this?#

`<CopilotPopup>` is a prebuilt floating launcher that opens an overlay chat window on top of your page content. It's the lightest-weight way to add a copilot to an existing app. Drop it in once and a bubble appears in the corner ready to chat.

## When should I use this?#

Use the popup when you want:

  * A minimal-footprint copilot that overlays existing content on demand
  * A launcher you can place on top of any page without reflowing the layout
  * A quick assistant bubble that users open for short, task-focused chats



If you need chat to live alongside your content rather than on top of it, use [CopilotSidebar](https://docs.copilotkit.ai/pydantic-ai/prebuilt-components/sidebar). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/pydantic-ai/prebuilt-components/chat) directly.

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotPopup>` as a sibling of your main content. The example below opens the popup by default and customizes the input placeholder via `labels`:
    
    
    import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotPopup`. That one is the [deprecated v1 popup](https://docs.copilotkit.ai/pydantic-ai/migrate/v2). This page documents the v2 popup, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-popup">      <MainContent />      <CopilotPopup        agentId="prebuilt-popup"        defaultOpen={true}        labels={{          chatInputPlaceholder: "Ask the popup anything...",        }}      />      <Suggestions />    </CopilotKit>

## Configuring the popup#

`<CopilotPopup>` accepts the same props as `<CopilotChat>` plus a few of its own. Commonly used options:

Prop| Description  
---|---  
`defaultOpen`| Whether the popup starts open on first render.  
`agentId`| Agent slug the popup should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the popup header bar — see the [slot system](https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/slots).  
`toggleButton`| Slot for the floating launcher button.  
  
## Styling#

`CopilotPopup` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the popupStyling
