---
url: https://docs.copilotkit.ai/llamaindex/prebuilt-components/chat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:20.326610+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/llamaindex/prebuilt-components/chat/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)[Prebuilt Components](https://docs.copilotkit.ai/llamaindex/prebuilt-components)

# CopilotChat

Inline chat component you can place anywhere and size as needed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

route.ts
    
    
    """LlamaIndex AG-UI AgentUses llama-index-protocols-ag-ui to expose a LlamaIndex workflow as anAG-UI compatible FastAPI router. The router handles all four demoscenarios (agentic-chat, tool-rendering, hitl, gen-ui-tool-based) througha single endpoint since LlamaIndex's get_ag_ui_workflow_router buildsthe full AG-UI protocol surface automatically.NOTE: Uses FixedAGUIChatWorkflow from hitl_in_chat_agent to fix threeupstream library bugs (duplicate tool-call rendering, missingparent_message_id, and incorrect tool-result message roles). Seehitl_in_chat_agent.py module docstring for details."""import asyncioimport jsonimport osfrom typing import Annotatedfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.router import get_ag_ui_workflow_routerfrom agents.hitl_in_chat_agent import FixedAGUIChatWorkflow# Import shared tool implementationsfrom tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)# --- Frontend tools (executed client-side, agent just returns a confirmation) ---def change_background(    background: Annotated[str, "CSS background value. Prefer gradients."],) -> str:    """Change the background color/gradient of the chat area."""    return f"Background changed to {background}"def generate_haiku(    japanese: Annotated[list[str], "3 lines of haiku in Japanese"],    english: Annotated[list[str], "3 lines of haiku translated to English"],    image_name: Annotated[str, "One relevant image name from the valid set"],    gradient: Annotated[str, "CSS Gradient color for the background"],) -> str:    """Generate a haiku with Japanese text, English translation, and a background image."""    return "Haiku generated!"def generate_task_steps(    steps: Annotated[        list[dict],        "Array of step objects with 'description' (string) and 'status' ('enabled' or 'disabled')",    ],) -> str:    """Generate a list of task steps for the user to review and approve."""    return f"Generated {len(steps)} steps for review"def book_call(    topic: Annotated[str, "What the call is about (e.g. 'Intro with sales')"],    attendee: Annotated[str, "Who the call is with (e.g. 'Alice from Sales')"],) -> str:    """Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent."""    return f"Booking call about {topic} with {attendee}"def show_card(    title: Annotated[str, "Short heading for the card."],    body: Annotated[str, "Body text for the card."],) -> str:    """Display a titled card with a short body of text. Rendered on the frontend via useComponent."""    return f"Displayed card: {title}"# --- Backend tools (executed server-side, using shared implementations) ---async def get_weather(    location: Annotated[str, "The location to get the weather for."],) -> str:    """Get the weather for a given location. Returns temperature, conditions, humidity, wind speed, and feels-like temperature."""    return json.dumps(get_weather_impl(location))async def query_data(    query: Annotated[str, "Natural language query for financial data."],) -> str:    """Query financial database for chart data. Always call before showing a chart or graph."""    return json.dumps(query_data_impl(query))async def manage_sales_todos(    todos: Annotated[        list[dict], "Complete list of sales todos to replace the current list."    ],) -> str:    """Manage the sales pipeline by replacing the entire list of todos."""    result = manage_sales_todos_impl(todos)    return json.dumps(        {"status": "updated", "count": len(result), "todos": [dict(t) for t in result]}    )async def get_sales_todos_tool() -> str:    """Get the current sales pipeline todos."""    return json.dumps(get_sales_todos_impl(None))async def schedule_meeting(    reason: Annotated[str, "Reason for the meeting."],) -> str:    """Schedule a meeting with the user. Requires human approval."""    return json.dumps(schedule_meeting_impl(reason))async def search_flights(    flights: Annotated[        list[dict],        "List of flight objects to search and display as rich cards. Return exactly 2 flights.",    ],) -> str:    """Search for flights and display the results as rich A2UI cards.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date, departureTime, arrivalTime, duration, status, statusColor, price, currency.    """    result = search_flights_impl(flights)    return json.dumps(result)def _generate_a2ui(context: str) -> str:    """Blocking secondary-LLM round-trip for `generate_a2ui`.    Kept synchronous and offloaded via ``asyncio.to_thread`` from the async    tool wrapper below: the synchronous ``openai.OpenAI().chat.completions``    call would otherwise block the uvicorn asyncio event loop for the full    LLM round-trip, wedging the ``:8000`` ``/health`` endpoint under load.    """    from openai import OpenAI    client = OpenAI()    tool_schema = {        "type": "function",        "function": {            "name": "render_a2ui",            "description": "Render a dynamic A2UI v0.9 surface.",            "parameters": {                "type": "object",                "properties": {                    "surfaceId": {"type": "string"},                    "catalogId": {"type": "string"},                    "components": {"type": "array", "items": {"type": "object"}},                    "data": {"type": "object"},                },                "required": ["surfaceId", "catalogId", "components"],            },        },    }    response = client.chat.completions.create(        model="gpt-5-mini",        messages=[            {"role": "system", "content": context or "Generate a useful dashboard UI."},            {                "role": "user",                "content": "Generate a dynamic A2UI dashboard based on the conversation.",            },        ],        tools=[tool_schema],        tool_choice={"type": "function", "function": {"name": "render_a2ui"}},    )    if not response.choices[0].message.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    tool_call = response.choices[0].message.tool_calls[0]    args = json.loads(tool_call.function.arguments)    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)async def generate_a2ui(    context: Annotated[str, "Conversation context to generate UI from."],) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    The blocking LLM round-trip runs in ``_generate_a2ui`` and is offloaded    via ``asyncio.to_thread`` so it never blocks the event loop.    """    return await asyncio.to_thread(_generate_a2ui, context)_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]_AGENT_SYSTEM_PROMPT = (    "You are a polished, professional demo assistant for CopilotKit. "    "Keep responses brief and clear -- 1 to 2 sentences max.\n\n"    "You can:\n"    "- Chat naturally with the user\n"    "- Change the UI background when asked (via frontend tool)\n"    "- Query data and render charts (via query_data tool)\n"    "- Get weather information (via get_weather tool)\n"    "- Schedule meetings with the user (via schedule_meeting tool)\n"    "- Manage sales pipeline todos (via manage_sales_todos / get_sales_todos tools)\n"    "- Search flights and display rich A2UI cards (via search_flights tool)\n"    "- Generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool)\n"    "- Generate step-by-step plans for user review (human-in-the-loop)\n"    "- Book calls with people (via book_call frontend tool)\n"    "- Show titled cards with a body of text (via show_card frontend tool)\n"    "When asked about weather, always use the get_weather tool. "    "When asked about financial data or charts, use query_data first. "    "When asked to book a call, use the book_call tool with topic and name.")async def _agent_workflow_factory():    wf = FixedAGUIChatWorkflow(        llm=OpenAI(model="gpt-5-mini", **_openai_kwargs),        frontend_tools=[            change_background,            generate_haiku,            generate_task_steps,            book_call,            show_card,            get_weather,        ],        backend_tools=[            query_data,            manage_sales_todos,            get_sales_todos_tool,            schedule_meeting,            search_flights,            generate_a2ui,        ],        system_prompt=_AGENT_SYSTEM_PROMPT,        initial_state={            "todos": [],        },    )    # Tools that use useRenderTool on the frontend — emit    # TOOL_CALL_RESULT so the render transitions to "complete".    wf.render_only_tool_names = {"get_weather"}    return wfagent_router = get_ag_ui_workflow_router(    workflow_factory=_agent_workflow_factory,)

## What is this?#

`<CopilotChat>` is the base prebuilt chat surface. Drop it in wherever you want the chat to render and size it to fit your layout. `<CopilotSidebar>` and `<CopilotPopup>` are both thin wrappers over the same primitives; if you need a dedicated chat page or an inline pane alongside other content, this is the component you want.

## When should I use this?#

Use `<CopilotChat>` when you want:

  * A full-bleed chat that fills its container
  * An inline chat pane as part of a larger page
  * A dedicated `/chat` route
  * Maximum layout freedom (no docked chrome or launcher)



For a collapsible docked chat, use [CopilotSidebar](https://docs.copilotkit.ai/llamaindex/prebuilt-components/sidebar). For a floating bubble that overlays content, use [CopilotPopup](https://docs.copilotkit.ai/llamaindex/prebuilt-components/popup). For saved conversations and switching between prior conversations, drop in the [Threads Drawer](https://docs.copilotkit.ai/llamaindex/prebuilt-components/copilot-threads-drawer) (or go headless with [Headless Threads](https://docs.copilotkit.ai/llamaindex/headless-threads)).

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotChat>` inside the layout of your choosing:
    
    
    import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotChat`. That one is the [deprecated v1 chat](https://docs.copilotkit.ai/llamaindex/migrate/v2). This page documents the v2 chat, which you import from `@copilotkit/react-core/v2`.

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
`messageView`| Slot for the message list — see [slots](https://docs.copilotkit.ai/llamaindex/custom-look-and-feel/slots).  
`input`| Slot for the composer area (text area, send button, disclaimer).  
`scrollView`| Slot for the scroll container (e.g. custom feather/gradient).  
`suggestionView`| Slot for the suggestion pills shown below messages.  
`welcomeScreen`| Slot for the empty-state. Pass `false` to disable.  
  
## Styling#

`<CopilotChat>` is fully themable:

  * **CSS variables / class overrides** — see [CSS customization](https://docs.copilotkit.ai/llamaindex/custom-look-and-feel/css)
  * **Slots (subcomponents)** — see [slots](https://docs.copilotkit.ai/llamaindex/custom-look-and-feel/slots)
  * **Fully headless** — see [headless UI](https://docs.copilotkit.ai/llamaindex/custom-look-and-feel/headless-ui)



### On this page

What is this?When should I use this?Basic setupCode exampleCommon propsStyling
