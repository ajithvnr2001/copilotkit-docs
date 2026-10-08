---
url: https://docs.copilotkit.ai/ms-agent-python/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:40.094844+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/ms-agent-python/shared-state/agent-readonly/

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

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)[Shared State](https://docs.copilotkit.ai/ms-agent-python/shared-state)

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """MS Agent Framework agent with sales todos state, weather tool, query data,and HITL schedule meeting tool.Adapted from examples/integrations/ms-agent-framework-python/agent/src/agent.py"""from __future__ import annotationsimport jsonfrom textwrap import dedentfrom typing import Annotatedfrom agent_framework import Agent, BaseChatClient, toolfrom agent_framework_ag_ui import AgentFrameworkAgentfrom pydantic import Field# =====================================================================# Shared tool implementations# =====================================================================from tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,)STATE_SCHEMA: dict[str, object] = {    "salesTodos": {        "type": "array",        "items": {            "type": "object",            "properties": {                "id": {"type": "string"},                "title": {"type": "string"},                "stage": {"type": "string"},                "value": {"type": "number"},                "dueDate": {"type": "string"},                "assignee": {"type": "string"},                "completed": {"type": "boolean"},            },        },        "description": "Ordered list of the user's sales pipeline todos.",    }}PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {    "salesTodos": {        "tool": "manage_sales_todos",        "tool_argument": "todos",    }}@tool(    name="manage_sales_todos",    description=(        "Replace the entire list of sales todos with the provided values. "        "Always include every todo you want to keep."    ),)def manage_sales_todos(    todos: Annotated[        list[dict],        Field(            description=(                "The complete source of truth for the user's sales todos. "                "Maintain ordering and include the full list on each call."            )        ),    ],) -> str:    """Persist the provided set of sales todos."""    result = manage_sales_todos_impl(todos)    return f"Sales todos updated. Tracking {len(result)} item(s)."@tool(    name="get_sales_todos",    description="Get the current list of sales todos.",)def get_sales_todos() -> str:    """Return the current sales todos or defaults."""    result = get_sales_todos_impl()    return json.dumps(result)@tool(    name="get_weather",    description="Get the current weather for a location. Use this to render the frontend weather card.",)def get_weather(    location: Annotated[        str,        Field(            description="The city or region to describe. Use fully spelled out names."        ),    ],) -> str:    """Return weather data as JSON for UI rendering."""    result = get_weather_impl(location)    return json.dumps(result)@tool(    name="query_data",    description="Query the database. Takes natural language. Always call before showing a chart or graph.",)def query_data(    query: Annotated[        str, Field(description="Natural language query to run against the database.")    ],) -> str:    """Query the database and return results as JSON."""    result = query_data_impl(query)    return json.dumps(result)@tool(    name="schedule_meeting",    description="Schedule a meeting. The user will be asked to pick a time via the meeting time picker UI.",    approval_mode="always_require",)def schedule_meeting(    reason: Annotated[str, Field(description="Reason for scheduling the meeting.")],    duration_minutes: Annotated[        int, Field(description="Duration of the meeting in minutes.")    ] = 30,) -> str:    """Request human approval to schedule a meeting."""    result = schedule_meeting_impl(reason, duration_minutes)    return json.dumps(result)@tool(    name="search_flights",    description=(        "Search for flights and display the results as rich A2UI cards. Return exactly 2 flights. "        "Each flight must have: airline, airlineLogo, flightNumber, origin, destination, "        "date, departureTime, arrivalTime, duration, status, statusColor, price, currency."    ),)def search_flights(    flights: Annotated[        list[dict],        Field(description="List of flight objects to search and display."),    ],) -> str:    """Search for flights and display as rich cards."""    result = search_flights_impl(flights)    return json.dumps(result)def create_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:    """Instantiate the CopilotKit demo agent backed by Microsoft Agent Framework."""    base_agent = Agent(        client=chat_client,        name="sales_agent",        instructions=dedent(            """            You help users manage their sales pipeline, check weather, query data, and schedule meetings.            State sync:            - The current list of sales todos is provided in the conversation context.            - When you add, remove, or reorder todos, call `manage_sales_todos` with the full list.              Never send partial updates--always include every todo that should exist.            - CRITICAL: When asked to "add" a todo, you must:              1. First, identify ALL existing todos from the conversation history              2. Create EXACTLY ONE new todo (never more than one unless explicitly requested)              3. Call manage_sales_todos with: [all existing todos] + [the one new todo]            - When asked to "remove" a todo, remove exactly ONE item unless user specifies otherwise.            Tool usage rules:            - When user asks to schedule a meeting, you MUST call the `schedule_meeting` tool immediately.              Do NOT ask for approval yourself--the tool's approval workflow and the client UI will handle it.            Frontend integrations:            - `get_weather` renders a weather card in the UI. Only call this tool when the user explicitly              asks for weather. Do NOT call it after unrelated tasks or approvals.            - `query_data` fetches database records. Always call before showing charts or graphs.            - `schedule_meeting` requires explicit user approval before you proceed. Only use it when a              user asks to schedule or set up a meeting. Always call the tool instead of asking manually.            Conversation tips:            - Reference the latest todo list before suggesting changes.            - Keep responses concise and friendly unless the user requests otherwise.            - After you finish executing tools for the user's request, provide a brief, final assistant              message summarizing exactly what changed. Do NOT call additional tools or switch topics              after that summary unless the user asks. ALWAYS send this conversational summary so the message persists.            """.strip()        ),        tools=[            manage_sales_todos,            get_sales_todos,            get_weather,            query_data,            schedule_meeting,            search_flights,        ],    )    return AgentFrameworkAgent(        agent=base_agent,        name="CopilotKitMicrosoftAgentFrameworkAgent",        description="Manages sales pipeline todos, weather, data queries, and meeting scheduling.",        predict_state_config=PREDICT_STATE_CONFIG,        require_confirmation=False,    )

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/ms-agent-python/inspector).

## What is this?#

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state (where the agent can call tools that mutate the state back to the UI), `useAgentContext` values are pure inputs. The agent sees them on every turn via the runtime's context injection, but it has no setter and no tool to write them back.

## When should I use this?#

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, scroll position).
  * You want the value to automatically unregister on unmount (e.g. the "current record" context disappears when you leave the page).



Think of it as "props for the agent".

## How it works in code#

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a dynamic context entry with the runtime that is:

  * Refreshed whenever `value` changes (React re-renders).
  * Automatically removed when the component unmounts.
  * Surfaced to the agent via the backend's `CopilotKitMiddleware`, which threads the entries into the model's message history on every turn.



page.tsx
    
    
      useAgentContext({    description: "The currently logged-in user's display name",    value: userName,  });  useAgentContext({    description: "The user's IANA timezone (used when mentioning times)",    value: userTimezone,  });  useAgentContext({    description: "The user's recent activity in the app, newest first",    value: recentActivity,  });

The `description` is important: it's a short human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring.

## Wire it to your own state#

`useAgentContext` doesn't care where the value comes from: local state, a React Context, Redux, a query cache, anything. The only requirement is that the identity of the value is stable enough for React to avoid a render loop. In the demo we use a handful of `useState` hooks; in a real app these would likely come from an auth provider, a router hook, and your domain state stores.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotPopup,  useAgentContext,} from "@copilotkit/react-core/v2";import { ACTIVITIES, DemoLayout } from "./demo-layout";import { useReadonlyStateAgentContextSuggestions } from "./suggestions";export default function ReadonlyStateAgentContextDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="readonly-state-agent-context"    >      <DemoContent />      <CopilotPopup        agentId="readonly-state-agent-context"        defaultOpen={true}        labels={{ chatInputPlaceholder: "Ask about your context..." }}      />    </CopilotKit>  );}function DemoContent() {  const [userName, setUserName] = useState("Atai");  const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");  const [recentActivity, setRecentActivity] = useState<string[]>([    ACTIVITIES[0],    ACTIVITIES[2],  ]);

## Read-only, by design#

Because the agent never sees a setter or a mutation tool for these values, there's no way for a confused LLM to "update" them. That makes `useAgentContext` the right tool whenever the value in question is an input, not a field: the "context object passed to the agent on every turn", rather than "shared workspace you both edit".

When you need both reads _and_ writes, you want full **[shared state](https://docs.copilotkit.ai/ms-agent-python/shared-state)** instead.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/ms-agent-python/shared-state)** — bidirectional reads + writes.
  * **[State streaming](https://docs.copilotkit.ai/ms-agent-python/shared-state/streaming)** — stream agent-written state back to the UI during a run.


