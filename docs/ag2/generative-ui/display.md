---
url: https://docs.copilotkit.ai/ag2/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:07.792591+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/ag2/generative-ui/display/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[AG2](https://docs.copilotkit.ai/ag2)[Build Generative UI](https://docs.copilotkit.ai/ag2/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """AG2 agent with weather and sales tools for CopilotKit showcase.Uses AG2's ConversableAgent with AGUIStream to exposethe agent via the AG-UI protocol."""from __future__ import annotationsimport jsonimport loggingfrom typing import Annotated, Anyimport openaifrom autogen import ConversableAgent, LLMConfigfrom autogen.ag_ui import AGUIStreamfrom dotenv import load_dotenvfrom pydantic import ValidationErrorload_dotenv()# Import shared tool implementationsfrom tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,    RENDER_A2UI_TOOL_SCHEMA,)from tools.types import Flightfrom ._header_forwarding import get_forwarded_headersfrom ._request_context import get_latest_user_messagelogger = logging.getLogger(__name__)# Module-level async client: re-used across requests (httpx connection pool is# thread-safe). Using AsyncOpenAI inside an `async def` avoids blocking the# ASGI event loop on the secondary LLM call._async_openai_client = openai.AsyncOpenAI()# =====# Tools# =====async def get_weather(    location: Annotated[str, "City name to get weather for"],) -> str:    """Get current weather for a location."""    result = get_weather_impl(location)    # Return a JSON string (not a dict): autogen serializes dict returns with    # str(), producing a Python repr (single quotes) that the frontend's    # parseJsonResult/JSON.parse cannot parse — the weather card then renders    # "--" placeholders. Same pattern as search_flights below.    return json.dumps(        {            "city": result["city"],            "temperature": result["temperature"],            "feels_like": result["feels_like"],            "humidity": result["humidity"],            "wind_speed": result["wind_speed"],            "conditions": result["conditions"],        }    )async def query_data(    query: Annotated[str, "Natural language query for financial data"],) -> str:    """Query financial database for chart data."""    # Return a JSON string (not a list): autogen serializes non-str returns    # with str(), producing a Python repr (single quotes) that the frontend's    # parseJsonResult/JSON.parse cannot parse. Same pattern as get_weather.    return json.dumps(query_data_impl(query))async def manage_sales_todos(    todos: Annotated[list, "Complete list of sales todos"],) -> str:    """Manage the sales pipeline."""    # See contract comment on query_data above — return JSON, not dict.    # SalesTodo is a Pydantic model; coerce via model_dump for serialisability.    result = [t.model_dump() for t in manage_sales_todos_impl(todos)]    return json.dumps({"todos": result})async def get_sales_todos() -> str:    """Get the current sales pipeline."""    # See contract comment on query_data above — return JSON, not list.    # SalesTodo is a Pydantic model; coerce via model_dump for serialisability.    return json.dumps([t.model_dump() for t in get_sales_todos_impl(None)])async def schedule_meeting(    reason: Annotated[str, "Reason for the meeting"],) -> str:    """Schedule a meeting with user approval."""    # See contract comment on query_data above — return JSON, not dict.    return json.dumps(schedule_meeting_impl(reason))async def search_flights(    flights: Annotated[        list[dict[str, Any]], "List of flight objects to display as rich A2UI cards"    ],) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    try:        typed_flights: list[Flight] = [Flight(**f) for f in flights]    except ValidationError as exc:        logger.warning(            "search_flights: invalid flight shape type=%s err=%s",            type(exc).__name__,            exc,            exc_info=True,        )        return json.dumps({"error": f"invalid flight shape: {exc}"})    result = search_flights_impl(typed_flights)    return json.dumps(result)async def generate_a2ui(    context: Annotated[str, "Conversation context to generate UI for"],) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    """    # A13: AsyncOpenAI inside async def (was sync openai.OpenAI which blocks    # the ASGI event loop). Forward x-* headers via extra_headers in addition    # to the global httpx hook so aimock context routing is explicit at the    # call site.    #    # R2-A1 / A4: thread the latest user prompt from the inbound    # RunAgentInput.messages payload (captured into a per-request ContextVar    # by RequestUserMessageMiddleware — see agents/_request_context.py) into    # the inner LLM call so each pill's request body is byte-distinct.    # Without this, every pill landing on the omnibus agent (agentic-chat /    # tool-rendering / chat-customization-css / hitl) produces an IDENTICAL    # inner-LLM body and the aimock fixture cannot disambiguate. Falls back    # to the original hardcoded prompt when the middleware captured nothing    # (parse failure already logged at WARNING).    user_prompt = get_latest_user_message() or (        "Generate a dynamic A2UI dashboard based on the conversation."    )    forwarded = get_forwarded_headers()    try:        response = await _async_openai_client.chat.completions.create(            model="gpt-5-mini",            messages=[                {                    "role": "system",                    "content": context or "Generate a useful dashboard UI.",                },                {                    "role": "user",                    "content": user_prompt,                },            ],            tools=[                {                    "type": "function",                    "function": RENDER_A2UI_TOOL_SCHEMA,                }            ],            tool_choice={"type": "function", "function": {"name": "render_a2ui"}},            extra_headers=forwarded or None,        )    except Exception as exc:        logger.error(            "generate_a2ui: inner LLM call failed type=%s err=%s",            type(exc).__name__,            exc,            exc_info=True,        )        return json.dumps({"error": f"inner LLM call failed: {type(exc).__name__}"})    if not response.choices:        logger.warning("generate_a2ui: LLM returned no choices")        return json.dumps({"error": "LLM returned no choices"})    choice = response.choices[0]    if not choice.message.tool_calls:        logger.warning("generate_a2ui: secondary LLM produced no render_a2ui tool call")        return json.dumps({"error": "LLM did not call render_a2ui"})    try:        args = json.loads(choice.message.tool_calls[0].function.arguments)        result = build_a2ui_operations_from_tool_call(args)        return json.dumps(result)    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:        logger.error(            "generate_a2ui: failed to parse render_a2ui args type=%s err=%s",            type(exc).__name__,            exc,            exc_info=True,        )        return json.dumps(            {"error": f"failed to parse render_a2ui args: {type(exc).__name__}"}        )# =====# Agent# =====agent = ConversableAgent(    name="assistant",    system_message=(        "You are a helpful sales assistant. You can look up current weather "        "for any city using the get_weather tool, query financial data with "        "query_data, manage the sales pipeline with manage_sales_todos and "        "get_sales_todos, schedule meetings with schedule_meeting, search "        "flights and display rich A2UI cards with search_flights, and "        "generate dynamic A2UI dashboards with generate_a2ui. "        "When asked about the weather, always use the tool rather than guessing. "        "Be concise and friendly in your responses."    ),    llm_config=LLMConfig({"model": "gpt-5-mini", "stream": True}),    human_input_mode="NEVER",    # Guard against infinite tool-call loops: AG2's ConversableAgent with    # human_input_mode="NEVER" will keep executing tool calls indefinitely    # if the LLM keeps requesting them.  Without this limit the agent floods    # Railway's log stream (500 logs/sec rate-limit), becomes unresponsive    # to health probes, and gets killed by the watchdog.    max_consecutive_auto_reply=15,    functions=[        get_weather,        query_data,        manage_sales_todos,        get_sales_todos,        schedule_meeting,        search_flights,        generate_a2ui,    ],)# AG-UI stream wrapperstream = AGUIStream(agent)

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

AG2's AG-UI stream surfaces frontend-registered tools to the model on every run, so the agent declares none of its own. A component registered with `useComponent` reaches the model through the AG-UI request payload, and the model calls it by name. Leave `tools` empty when the only tools in play are frontend ones.

src/agents/chart_agent.py
    
    
    from ag2 import Agent
    from ag2.ag_ui import AGUIStream
    from ag2.config import OpenAIResponsesConfig
    
    chart_agent = Agent(
        name="chart_agent",
        prompt=SYSTEM_PROMPT,
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[],
    )
    
    chart_stream = AGUIStream(chart_agent)

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in `prompt` and say what it is for.

src/agents/chart_agent.py
    
    
    SYSTEM_PROMPT = (
        "You are a data visualization assistant. "
        "When the user asks for a chart, call `render_bar_chart` with a "
        "concise title and a `data` array of `{label, value}` items. "
        "Keep chat responses brief and let the chart do the talking."
    )

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
