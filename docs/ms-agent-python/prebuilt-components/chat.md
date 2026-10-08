---
url: https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/chat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:32.535776+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/chat/

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

On this page

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)[Prebuilt Components](https://docs.copilotkit.ai/ms-agent-python/prebuilt-components)

# CopilotChat

Inline chat component you can place anywhere and size as needed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """MS Agent Framework agent with sales todos state, weather tool, query data,and HITL schedule meeting tool.Adapted from examples/integrations/ms-agent-framework-python/agent/src/agent.py"""from __future__ import annotationsimport jsonfrom textwrap import dedentfrom typing import Annotatedfrom agent_framework import Agent, BaseChatClient, toolfrom agent_framework_ag_ui import AgentFrameworkAgentfrom pydantic import Field# =====================================================================# Shared tool implementations# =====================================================================from tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,)STATE_SCHEMA: dict[str, object] = {    "salesTodos": {        "type": "array",        "items": {            "type": "object",            "properties": {                "id": {"type": "string"},                "title": {"type": "string"},                "stage": {"type": "string"},                "value": {"type": "number"},                "dueDate": {"type": "string"},                "assignee": {"type": "string"},                "completed": {"type": "boolean"},            },        },        "description": "Ordered list of the user's sales pipeline todos.",    }}PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {    "salesTodos": {        "tool": "manage_sales_todos",        "tool_argument": "todos",    }}@tool(    name="manage_sales_todos",    description=(        "Replace the entire list of sales todos with the provided values. "        "Always include every todo you want to keep."    ),)def manage_sales_todos(    todos: Annotated[        list[dict],        Field(            description=(                "The complete source of truth for the user's sales todos. "                "Maintain ordering and include the full list on each call."            )        ),    ],) -> str:    """Persist the provided set of sales todos."""    result = manage_sales_todos_impl(todos)    return f"Sales todos updated. Tracking {len(result)} item(s)."@tool(    name="get_sales_todos",    description="Get the current list of sales todos.",)def get_sales_todos() -> str:    """Return the current sales todos or defaults."""    result = get_sales_todos_impl()    return json.dumps(result)@tool(    name="get_weather",    description="Get the current weather for a location. Use this to render the frontend weather card.",)def get_weather(    location: Annotated[        str,        Field(            description="The city or region to describe. Use fully spelled out names."        ),    ],) -> str:    """Return weather data as JSON for UI rendering."""    result = get_weather_impl(location)    return json.dumps(result)@tool(    name="query_data",    description="Query the database. Takes natural language. Always call before showing a chart or graph.",)def query_data(    query: Annotated[        str, Field(description="Natural language query to run against the database.")    ],) -> str:    """Query the database and return results as JSON."""    result = query_data_impl(query)    return json.dumps(result)@tool(    name="schedule_meeting",    description="Schedule a meeting. The user will be asked to pick a time via the meeting time picker UI.",    approval_mode="always_require",)def schedule_meeting(    reason: Annotated[str, Field(description="Reason for scheduling the meeting.")],    duration_minutes: Annotated[        int, Field(description="Duration of the meeting in minutes.")    ] = 30,) -> str:    """Request human approval to schedule a meeting."""    result = schedule_meeting_impl(reason, duration_minutes)    return json.dumps(result)@tool(    name="search_flights",    description=(        "Search for flights and display the results as rich A2UI cards. Return exactly 2 flights. "        "Each flight must have: airline, airlineLogo, flightNumber, origin, destination, "        "date, departureTime, arrivalTime, duration, status, statusColor, price, currency."    ),)def search_flights(    flights: Annotated[        list[dict],        Field(description="List of flight objects to search and display."),    ],) -> str:    """Search for flights and display as rich cards."""    result = search_flights_impl(flights)    return json.dumps(result)def create_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:    """Instantiate the CopilotKit demo agent backed by Microsoft Agent Framework."""    base_agent = Agent(        client=chat_client,        name="sales_agent",        instructions=dedent(            """            You help users manage their sales pipeline, check weather, query data, and schedule meetings.            State sync:            - The current list of sales todos is provided in the conversation context.            - When you add, remove, or reorder todos, call `manage_sales_todos` with the full list.              Never send partial updates--always include every todo that should exist.            - CRITICAL: When asked to "add" a todo, you must:              1. First, identify ALL existing todos from the conversation history              2. Create EXACTLY ONE new todo (never more than one unless explicitly requested)              3. Call manage_sales_todos with: [all existing todos] + [the one new todo]            - When asked to "remove" a todo, remove exactly ONE item unless user specifies otherwise.            Tool usage rules:            - When user asks to schedule a meeting, you MUST call the `schedule_meeting` tool immediately.              Do NOT ask for approval yourself--the tool's approval workflow and the client UI will handle it.            Frontend integrations:            - `get_weather` renders a weather card in the UI. Only call this tool when the user explicitly              asks for weather. Do NOT call it after unrelated tasks or approvals.            - `query_data` fetches database records. Always call before showing charts or graphs.            - `schedule_meeting` requires explicit user approval before you proceed. Only use it when a              user asks to schedule or set up a meeting. Always call the tool instead of asking manually.            Conversation tips:            - Reference the latest todo list before suggesting changes.            - Keep responses concise and friendly unless the user requests otherwise.            - After you finish executing tools for the user's request, provide a brief, final assistant              message summarizing exactly what changed. Do NOT call additional tools or switch topics              after that summary unless the user asks. ALWAYS send this conversational summary so the message persists.            """.strip()        ),        tools=[            manage_sales_todos,            get_sales_todos,            get_weather,            query_data,            schedule_meeting,            search_flights,        ],    )    return AgentFrameworkAgent(        agent=base_agent,        name="CopilotKitMicrosoftAgentFrameworkAgent",        description="Manages sales pipeline todos, weather, data queries, and meeting scheduling.",        predict_state_config=PREDICT_STATE_CONFIG,        require_confirmation=False,    )

## What is this?#

`<CopilotChat>` is the base prebuilt chat surface. Drop it in wherever you want the chat to render and size it to fit your layout. `<CopilotSidebar>` and `<CopilotPopup>` are both thin wrappers over the same primitives; if you need a dedicated chat page or an inline pane alongside other content, this is the component you want.

## When should I use this?#

Use `<CopilotChat>` when you want:

  * A full-bleed chat that fills its container
  * An inline chat pane as part of a larger page
  * A dedicated `/chat` route
  * Maximum layout freedom (no docked chrome or launcher)



For a collapsible docked chat, use [CopilotSidebar](https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/sidebar). For a floating bubble that overlays content, use [CopilotPopup](https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/popup). For saved conversations and switching between prior conversations, drop in the [Threads Drawer](https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/copilot-threads-drawer) (or go headless with [Headless Threads](https://docs.copilotkit.ai/ms-agent-python/headless-threads)).

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotChat>` inside the layout of your choosing:
    
    
    import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotChat`. That one is the [deprecated v1 chat](https://docs.copilotkit.ai/ms-agent-python/migrate/v2). This page documents the v2 chat, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

## Code example#

A self-contained component that renders the chat and wires in starter suggestions:

page.tsx
    
    
    function Chat() {  useAgenticChatSuggestions();  return <CopilotChat agentId="agentic_chat" />;}

## Common props#

`<CopilotChat>` is the root primitive. `<CopilotSidebar>` and `<CopilotPopup>` accept the same slots and labels, plus a few wrapper-specific props.

Prop| Description  
---|---  
`agentId`| Agent slug the chat should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy — header title, placeholder, welcome, disclaimer.  
`messageView`| Slot for the message list — see [slots](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/slots).  
`input`| Slot for the composer area (text area, send button, disclaimer).  
`scrollView`| Slot for the scroll container (e.g. custom feather/gradient).  
`suggestionView`| Slot for the suggestion pills shown below messages.  
`welcomeScreen`| Slot for the empty-state. Pass `false` to disable.  
  
## Styling#

`<CopilotChat>` is fully themable:

  * **CSS variables / class overrides** — see [CSS customization](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/css)
  * **Slots (subcomponents)** — see [slots](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/slots)
  * **Fully headless** — see [headless UI](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/headless-ui)



### On this page

What is this?When should I use this?Basic setupCode exampleCommon propsStyling
