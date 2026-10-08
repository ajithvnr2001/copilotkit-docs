---
url: https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/popup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:32.424172+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/popup/

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

# CopilotPopup

Floating chat bubble that toggles open an overlay chat window.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """MS Agent Framework agent with sales todos state, weather tool, query data,and HITL schedule meeting tool.Adapted from examples/integrations/ms-agent-framework-python/agent/src/agent.py"""from __future__ import annotationsimport jsonfrom textwrap import dedentfrom typing import Annotatedfrom agent_framework import Agent, BaseChatClient, toolfrom agent_framework_ag_ui import AgentFrameworkAgentfrom pydantic import Field# =====================================================================# Shared tool implementations# =====================================================================from tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,)STATE_SCHEMA: dict[str, object] = {    "salesTodos": {        "type": "array",        "items": {            "type": "object",            "properties": {                "id": {"type": "string"},                "title": {"type": "string"},                "stage": {"type": "string"},                "value": {"type": "number"},                "dueDate": {"type": "string"},                "assignee": {"type": "string"},                "completed": {"type": "boolean"},            },        },        "description": "Ordered list of the user's sales pipeline todos.",    }}PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {    "salesTodos": {        "tool": "manage_sales_todos",        "tool_argument": "todos",    }}@tool(    name="manage_sales_todos",    description=(        "Replace the entire list of sales todos with the provided values. "        "Always include every todo you want to keep."    ),)def manage_sales_todos(    todos: Annotated[        list[dict],        Field(            description=(                "The complete source of truth for the user's sales todos. "                "Maintain ordering and include the full list on each call."            )        ),    ],) -> str:    """Persist the provided set of sales todos."""    result = manage_sales_todos_impl(todos)    return f"Sales todos updated. Tracking {len(result)} item(s)."@tool(    name="get_sales_todos",    description="Get the current list of sales todos.",)def get_sales_todos() -> str:    """Return the current sales todos or defaults."""    result = get_sales_todos_impl()    return json.dumps(result)@tool(    name="get_weather",    description="Get the current weather for a location. Use this to render the frontend weather card.",)def get_weather(    location: Annotated[        str,        Field(            description="The city or region to describe. Use fully spelled out names."        ),    ],) -> str:    """Return weather data as JSON for UI rendering."""    result = get_weather_impl(location)    return json.dumps(result)@tool(    name="query_data",    description="Query the database. Takes natural language. Always call before showing a chart or graph.",)def query_data(    query: Annotated[        str, Field(description="Natural language query to run against the database.")    ],) -> str:    """Query the database and return results as JSON."""    result = query_data_impl(query)    return json.dumps(result)@tool(    name="schedule_meeting",    description="Schedule a meeting. The user will be asked to pick a time via the meeting time picker UI.",    approval_mode="always_require",)def schedule_meeting(    reason: Annotated[str, Field(description="Reason for scheduling the meeting.")],    duration_minutes: Annotated[        int, Field(description="Duration of the meeting in minutes.")    ] = 30,) -> str:    """Request human approval to schedule a meeting."""    result = schedule_meeting_impl(reason, duration_minutes)    return json.dumps(result)@tool(    name="search_flights",    description=(        "Search for flights and display the results as rich A2UI cards. Return exactly 2 flights. "        "Each flight must have: airline, airlineLogo, flightNumber, origin, destination, "        "date, departureTime, arrivalTime, duration, status, statusColor, price, currency."    ),)def search_flights(    flights: Annotated[        list[dict],        Field(description="List of flight objects to search and display."),    ],) -> str:    """Search for flights and display as rich cards."""    result = search_flights_impl(flights)    return json.dumps(result)def create_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:    """Instantiate the CopilotKit demo agent backed by Microsoft Agent Framework."""    base_agent = Agent(        client=chat_client,        name="sales_agent",        instructions=dedent(            """            You help users manage their sales pipeline, check weather, query data, and schedule meetings.            State sync:            - The current list of sales todos is provided in the conversation context.            - When you add, remove, or reorder todos, call `manage_sales_todos` with the full list.              Never send partial updates--always include every todo that should exist.            - CRITICAL: When asked to "add" a todo, you must:              1. First, identify ALL existing todos from the conversation history              2. Create EXACTLY ONE new todo (never more than one unless explicitly requested)              3. Call manage_sales_todos with: [all existing todos] + [the one new todo]            - When asked to "remove" a todo, remove exactly ONE item unless user specifies otherwise.            Tool usage rules:            - When user asks to schedule a meeting, you MUST call the `schedule_meeting` tool immediately.              Do NOT ask for approval yourself--the tool's approval workflow and the client UI will handle it.            Frontend integrations:            - `get_weather` renders a weather card in the UI. Only call this tool when the user explicitly              asks for weather. Do NOT call it after unrelated tasks or approvals.            - `query_data` fetches database records. Always call before showing charts or graphs.            - `schedule_meeting` requires explicit user approval before you proceed. Only use it when a              user asks to schedule or set up a meeting. Always call the tool instead of asking manually.            Conversation tips:            - Reference the latest todo list before suggesting changes.            - Keep responses concise and friendly unless the user requests otherwise.            - After you finish executing tools for the user's request, provide a brief, final assistant              message summarizing exactly what changed. Do NOT call additional tools or switch topics              after that summary unless the user asks. ALWAYS send this conversational summary so the message persists.            """.strip()        ),        tools=[            manage_sales_todos,            get_sales_todos,            get_weather,            query_data,            schedule_meeting,            search_flights,        ],    )    return AgentFrameworkAgent(        agent=base_agent,        name="CopilotKitMicrosoftAgentFrameworkAgent",        description="Manages sales pipeline todos, weather, data queries, and meeting scheduling.",        predict_state_config=PREDICT_STATE_CONFIG,        require_confirmation=False,    )

## What is this?#

`<CopilotPopup>` is a prebuilt floating launcher that opens an overlay chat window on top of your page content. It's the lightest-weight way to add a copilot to an existing app. Drop it in once and a bubble appears in the corner ready to chat.

## When should I use this?#

Use the popup when you want:

  * A minimal-footprint copilot that overlays existing content on demand
  * A launcher you can place on top of any page without reflowing the layout
  * A quick assistant bubble that users open for short, task-focused chats



If you need chat to live alongside your content rather than on top of it, use [CopilotSidebar](https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/sidebar). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/ms-agent-python/prebuilt-components/chat) directly.

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotPopup>` as a sibling of your main content. The example below opens the popup by default and customizes the input placeholder via `labels`:
    
    
    import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotPopup`. That one is the [deprecated v1 popup](https://docs.copilotkit.ai/ms-agent-python/migrate/v2). This page documents the v2 popup, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-popup">      <MainContent />      <CopilotPopup        agentId="prebuilt-popup"        defaultOpen={true}        labels={{          chatInputPlaceholder: "Ask the popup anything...",        }}      />      <Suggestions />    </CopilotKit>

## Configuring the popup#

`<CopilotPopup>` accepts the same props as `<CopilotChat>` plus a few of its own. Commonly used options:

Prop| Description  
---|---  
`defaultOpen`| Whether the popup starts open on first render.  
`agentId`| Agent slug the popup should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the popup header bar — see the [slot system](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/slots).  
`toggleButton`| Slot for the floating launcher button.  
  
## Styling#

`CopilotPopup` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the popupStyling
