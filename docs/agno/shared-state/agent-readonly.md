---
url: https://docs.copilotkit.ai/agno/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:47:48.720720+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/agno/shared-state/agent-readonly/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agno/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Shared State](https://docs.copilotkit.ai/agno/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/agno/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/agno/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/agno/shared-state/agent-readonly)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agno/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agno/learning)

[User Memories](https://docs.copilotkit.ai/agno/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agno/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityShared state

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

main.py

page.tsx

route.ts
    
    
    """Agno Sales Pipeline Agent with shared tools for showcase demos."""import jsonfrom agno.agent.agent import Agentfrom agno.models.openai import OpenAIChatfrom agno.tools import toolfrom dotenv import load_dotenvfrom tools import (    RENDER_A2UI_TOOL_SCHEMA,    build_a2ui_operations_from_tool_call,    get_weather_impl,    query_data_impl,    schedule_meeting_impl,    search_flights_impl,)from tools.types import Flightload_dotenv()@tooldef get_weather(location: str):    """    Get the weather for a given location. Ensure location is fully spelled out.    Args:        location (str): The location to get the weather for.    Returns:        str: Weather data as JSON.    """    return json.dumps(get_weather_impl(location))@tooldef query_data(query: str):    """    Query financial database for chart data. Returns data suitable for pie or bar charts.    Args:        query (str): The query to run against the financial database.    Returns:        str: Query results as JSON.    """    return json.dumps(query_data_impl(query))@tool(external_execution=True)def manage_sales_todos(todos: list[dict]):    """    Manage the sales pipeline. Pass the complete list of sales todos.    Always pass the COMPLETE list of todos.    Args:        todos (list[dict]): The complete list of sales todos to maintain.    """@tooldef schedule_meeting(reason: str):    """    Schedule a meeting with user approval. Returns available time slots.    Args:        reason (str): Reason for scheduling the meeting.    Returns:        str: Meeting scheduling data as JSON.    """    return json.dumps(schedule_meeting_impl(reason))@tool(external_execution=True, external_execution_silent=True)def request_user_approval(message: str, context: str = ""):    """    Ask the operator to approve or reject an action before you take it.    The operator will respond via an in-app modal dialog that appears    OUTSIDE the chat surface. The tool returns an object of the shape    { approved: boolean, reason?: string }.    Args:        message (str): Short summary of the action needing approval (include concrete numbers / IDs).        context (str): Optional extra context — e.g. the ticket ID or policy rule.    """@tool(external_execution=True)def change_background(background: str):    """    Change the background color of the chat.    ONLY call this tool when the user explicitly asks to change the background.    Never call it proactively or as part of another response.    Can be anything that the CSS background attribute accepts. Prefer gradients.    Args:        background (str): The CSS background value. Prefer gradients.    """@tool(external_execution=True, external_execution_silent=True)def book_call(topic: str, name: str):    """    Ask the user to pick a time slot for a call. The picker UI presents    fixed candidate slots; the user's choice is returned to the agent.    Args:        topic (str): What the call is about (e.g. "Intro with sales").        name (str): Name of the attendee (e.g. "Alice").    """@tool(external_execution=True, external_execution_silent=True)def generate_task_steps(steps: list[dict]):    """    Generates a list of steps for the user to perform.    Each step should have a description and status.    Args:        steps (list[dict]): A list of step objects, each with 'description' (str)                            and 'status' ('enabled' or 'disabled').    """@tooldef search_flights(flights: list[dict]):    """    Search for flights and display the results as rich A2UI cards.    Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18"),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    Args:        flights (list[dict]): List of flight objects to display.    Returns:        str: A2UI operations as JSON.    """    typed_flights = [Flight(**f) for f in flights]    result = search_flights_impl(typed_flights)    return json.dumps(result)@tooldef get_stock_price(ticker: str):    """    Get a mock current price for a stock ticker.    When the user asks about a single ticker, also consider pulling a    related ticker for context (e.g. if they ask about 'AAPL', also    fetch 'MSFT' or 'GOOGL' so the reply can compare).    Args:        ticker (str): The ticker symbol to look up.    Returns:        str: Mock price data as JSON.    """    from random import choice, randint    return json.dumps(        {            "ticker": ticker.upper(),            "price_usd": round(100 + randint(0, 400) + randint(0, 99) / 100, 2),            "change_pct": round(choice([-1, 1]) * (randint(0, 300) / 100), 2),        }    )@tooldef roll_dice(sides: int = 6):    """    Roll a single die with the given number of sides.    When the user asks for a roll, consider rolling twice with different    numbers of sides so the reply can show a contrast (e.g. a d6 AND a d20).    Args:        sides (int): The number of sides on the die. Defaults to 6.    Returns:        str: Dice roll result as JSON.    """    from random import randint    return json.dumps({"sides": sides, "result": randint(1, max(2, sides))})@tooldef generate_a2ui(context: str):    """    Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    Args:        context (str): Conversation context to generate UI for.    Returns:        str: A2UI operations as JSON.    """    import openai    client = openai.OpenAI()    response = client.chat.completions.create(        model="gpt-5-mini",        messages=[            {"role": "system", "content": context or "Generate a useful dashboard UI."},            {                "role": "user",                "content": "Generate a dynamic A2UI dashboard based on the conversation.",            },        ],        tools=[            {                "type": "function",                "function": RENDER_A2UI_TOOL_SCHEMA,            }        ],        tool_choice={"type": "function", "function": {"name": "render_a2ui"}},    )    choice = response.choices[0]    if choice.message.tool_calls:        args = json.loads(choice.message.tool_calls[0].function.arguments)        result = build_a2ui_operations_from_tool_call(args)        return json.dumps(result)    return json.dumps({"error": "LLM did not call render_a2ui"})def _create_session_db():    # Keep this import outside the public weather-tool region above.    from agno.db.sqlite import SqliteDb    # The production container runs as an unprivileged user with a read-only    # application directory, so its SQLite file belongs in writable /tmp.    return SqliteDb(db_file="/tmp/agno.db")agent = Agent(    # Raise the HTTP timeout so requests routed through aimock don't time out    # under normal load.  The default httpx timeout is too short when aimock    # is proxying to the upstream LLM — observed "Request timed out" errors    # that crash the agent run and trigger watchdog restarts.    model=OpenAIChat(id="gpt-5-mini", timeout=120),    # Frontend and HITL tools pause the run before the browser responds.    # Keep the session in a writable location so Agno can resume that run.    db=_create_session_db(),    tools=[        get_weather,        query_data,        manage_sales_todos,        schedule_meeting,        change_background,        book_call,        generate_task_steps,        request_user_approval,        search_flights,        get_stock_price,        roll_dice,        generate_a2ui,    ],    # Prevent runaway tool-call loops — same guard as the ag2 package.    tool_call_limit=15,    description="You are a helpful sales assistant for the CopilotKit showcase demos.",    instructions="""        SALES PIPELINE:        When a user asks you to do anything regarding sales todos or the pipeline,        use the manage_sales_todos tool. Always pass the COMPLETE LIST of todos.        Be helpful in managing sales pipeline items.        After using the tool, provide a brief summary of what you created, removed, or changed.        WEATHER:        Only call the get_weather tool if the user asks about the weather.        If the user does not specify a location, use "Everywhere ever in the whole wide world".        QUERY DATA:        Use the query_data tool when the user asks for financial data, charts, or analytics.        SCHEDULE MEETING:        Use the schedule_meeting tool when the user wants to schedule a meeting.        BACKGROUND:        Only call change_background when the user explicitly asks to change colors/background.        BOOK CALL (HITL):        When the user asks to book a call / schedule an intro / 1:1, call        book_call with the topic and the person's name. The frontend renders a        time picker; the user's choice is returned as the tool result.        TASK STEPS (HITL):        When asked to plan something, use the generate_task_steps tool with a list of steps.        Each step should have a description and status of "enabled".        FLIGHT SEARCH:        Use search_flights when the user asks about flights. Generate 2 realistic flights.        STOCK PRICES:        Use get_stock_price when the user asks about a ticker. Consider        fetching a second related ticker for comparison when helpful.        DICE:        Use roll_dice when the user asks to roll a die. Consider rolling a        second time with a different number of sides for contrast.        DYNAMIC A2UI:        Use generate_a2ui when the user asks for a dashboard or dynamic UI.        USER APPROVAL (HITL):        When asked to take any action that affects a customer — for example        issuing a refund, updating a plan, cancelling a subscription,        escalating a ticket, or sending a credit — call request_user_approval        FIRST with a short summary and optional context. Follow the tool        result: if approved, confirm in one short sentence; if rejected,        acknowledge and do not retry.    """,)

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/agno/inspector).

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

When you need both reads _and_ writes, you want full **[shared state](https://docs.copilotkit.ai/agno/shared-state)** instead.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/agno/shared-state)** — bidirectional reads + writes.
  * **[State streaming](https://docs.copilotkit.ai/agno/shared-state/streaming)** — stream agent-written state back to the UI during a run.


