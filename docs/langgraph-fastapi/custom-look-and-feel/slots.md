---
url: https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/slots/
title: Slots (Subcomponents)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:52.557991+00:00
---

# Slots (Subcomponents)

> Source: https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/slots/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/langgraph-fastapi/multimodal-attachments)[Voice](https://docs.copilotkit.ai/langgraph-fastapi/voice)[Reasoning](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/reasoning)

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

Slots (Subcomponents)

BasicsChatCustom Look and Feel

# Slots (Subcomponents)

Customize any part of the chat UI by overriding individual sub-components via slots.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

slot-wrappers.tsx

route.ts
    
    
    """LangGraph agent for the CopilotKit Showcase (FastAPI variant).Uses copilotkit's create_agent (wrapping langgraph) with CopilotKitMiddlewareso frontend-registered tools (useHumanInTheLoop, useFrontendTool) are properlyinjected into the LLM's tool list and executed on the frontend rather thanlocally."""from tools import (    get_weather_impl,    query_data_impl,    schedule_meeting_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)from tools.types import SalesTodo, Flightimport jsonimport timefrom typing import Anyfrom langchain_openai import ChatOpenAIfrom langchain_core.tools import tool as lc_toolfrom langchain_core.messages import SystemMessagefrom langchain.agents import AgentState as BaseAgentState, create_agentfrom langchain.tools import ToolRuntime, toolfrom langchain.messages import ToolMessagefrom langgraph.types import Commandfrom copilotkit import CopilotKitMiddlewareclass AgentState(BaseAgentState):    todos: list[SalesTodo]@lc_tooldef get_weather(location: str):    """Get the current weather for a location."""    return get_weather_impl(location)@lc_tooldef query_data(query: str):    """Query the database. Takes natural language. Always call before showing a chart."""    return query_data_impl(query)@lc_tooldef schedule_meeting(reason: str, duration_minutes: int = 30):    """Schedule a meeting. The user will be asked to pick a time via the UI."""    return schedule_meeting_impl(reason, duration_minutes)@lc_tooldef search_flights(flights: list[Flight]) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    result = search_flights_impl(flights)    return json.dumps(result)@tooldef manage_sales_todos(todos: list[SalesTodo], runtime: ToolRuntime) -> Command:    """    Manage the current sales todos. Pass the full updated list.    """    updated = manage_sales_todos_impl(todos)    return Command(        update={            "todos": updated,            "messages": [                ToolMessage(                    content="Successfully updated sales todos",                    tool_call_id=runtime.tool_call_id,                )            ],        }    )@tooldef get_sales_todos(runtime: ToolRuntime):    """    Get the current sales todos.    """    current = runtime.state.get("todos", [])    return get_sales_todos_impl(current if current else None)@lc_tooldef render_a2ui(    surfaceId: str,    catalogId: str,    components: list[dict],    data: dict | None = None,) -> str:    """Render a dynamic A2UI v0.9 surface."""    return "rendered"@tool()def generate_a2ui(runtime: ToolRuntime[Any]) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data.    """    t0 = time.time()    messages = runtime.state["messages"][:-1]    context_entries = runtime.state.get("copilotkit", {}).get("context", [])    context_text = "\n\n".join(        entry.get("value", "")        for entry in context_entries        if isinstance(entry, dict) and entry.get("value")    )    model = ChatOpenAI(model="gpt-5-mini")    model_with_tool = model.bind_tools([render_a2ui], tool_choice="render_a2ui")    response = model_with_tool.invoke(        [SystemMessage(content=context_text), *messages],    )    if not response.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    args = response.tool_calls[0]["args"]    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)model = ChatOpenAI(model="gpt-5-mini")SYSTEM_PROMPT = """You are a polished, professional demo assistant for CopilotKit.Keep responses brief and clear -- 1 to 2 sentences max.You can:- Chat naturally with the user- Change the UI background when asked (via frontend tool)- Query data and render charts (via query_data tool)- Get weather information (via get_weather tool)- Schedule meetings with the user (via schedule_meeting tool -- the user picks a time in the UI)- Manage sales pipeline todos (via manage_sales_todos / get_sales_todos tools)- Search flights and display rich A2UI cards (via search_flights tool)- Generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool)- Generate step-by-step plans for user review (human-in-the-loop)"""graph = create_agent(    model=model,    tools=[        get_weather,        query_data,        schedule_meeting,        search_flights,        generate_a2ui,        manage_sales_todos,        get_sales_todos,    ],    middleware=[CopilotKitMiddleware()],    state_schema=AgentState,    system_prompt=SYSTEM_PROMPT,)

## What is this?#

Every CopilotKit chat component is built from composable **slots** , named sub-components you can override individually. The slot system gives you three levels of customization without needing to rebuild the entire UI:

  1. **Tailwind classes** — pass a string to add/override CSS classes
  2. **Props override** — pass an object to override specific props on the default component
  3. **Custom component** — pass your own React component to fully replace a slot



Slots are recursive: you can drill into nested sub-components at any depth.

## What it looks like in code#

The `chat-slots` cell above overrides three slots on a single `<CopilotChat>` — the welcome screen, the assistant message card, and the input's disclaimer. Each slot is just a prop; the demo extracts them into locals so the override points are easy to see.

### Welcome screen slot#

The `welcomeScreen` prop replaces the empty-state view shown before the first message is sent. The demo swaps in a gradient card that still renders the default input and suggestions:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;

### Assistant message slot#

Drill into `messageView={{ assistantMessage: ... }}` to wrap every assistant response. The cell wraps the default component with a tinted card and a small "slot" badge so you can see the override is active during the message flow:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };

### Disclaimer slot#

The `input={{ disclaimer: ... }}` sub-slot lets you replace the small text shown below the input. The demo uses it to display a visibly tagged disclaimer so reviewers can tell the override is still in effect once the welcome screen is gone:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };  const input = {    disclaimer:      CustomDisclaimer as unknown as typeof CopilotChatInput.Disclaimer,  };

## Tailwind Classes#

The simplest way to customize a slot. Pass a Tailwind class string and it will be merged with the default component's classes.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export function Chat() {
      return (
        <CopilotChat
          messageView="bg-gray-50 dark:bg-gray-900 p-4"
          input="border-2 border-blue-400 rounded-xl"
        />
      );
    }

## Props Override#

Pass an object to override specific props on the default component. This is useful for adding `className`, event handlers, data attributes, or any other prop the default component accepts.

page.tsx
    
    
    <CopilotChat
      messageView={{
        className: "my-custom-messages",
        "data-testid": "message-view",
      }}
      input={{ autoFocus: true }}
    />

## Custom Components#

For full control, pass your own React component. It receives all the same props as the default component.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    const CustomMessageView = ({ messages, isRunning }) => (
      <div className="space-y-4 p-6">
        {messages?.map((msg) => (
          <div key={msg.id} className={msg.role === "user" ? "text-right" : "text-left"}>
            {msg.content}
          </div>
        ))}
        {isRunning && <div className="animate-pulse">Thinking...</div>}
      </div>
    );
    
    export function Chat() {
      return <CopilotChat messageView={CustomMessageView} />;
    }

## Nested Slots (Drill-Down)#

Slots are recursive. You can customize sub-components at any depth by nesting objects.

### Two levels deep#

Override the assistant message's toolbar within the message view:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          toolbar: CustomToolbar,
          copyButton: CustomCopyButton,
        },
        userMessage: CustomUserMessage,
      }}
    />

### Three levels deep#

Override a specific button inside the assistant message toolbar:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          copyButton: ({ onClick }) => (
            <button onClick={onClick}>Copy</button>
          ),
        },
      }}
    />

The `assistantMessage` slot also holds `markdownRenderer`, which controls how assistant markdown is rendered. It has its own guide: [Markdown Rendering](https://docs.copilotkit.ai/langgraph-fastapi/custom-look-and-feel/markdown).

## Labels#

Customize any text string in the UI via the `labels` prop. This is a separate convenience prop on `CopilotChat`, `CopilotSidebar`, and `CopilotPopup`, not part of the slot system.

page.tsx
    
    
    <CopilotChat
      labels={{
        chatInputPlaceholder: "Ask your agent anything...",
        welcomeMessageText: "How can I help you today?",
        chatDisclaimerText: "AI responses may be inaccurate.",
      }}
    />

## Available Slots#

### `CopilotChat` / `CopilotSidebar` / `CopilotPopup`#

These are the root-level slot props available on all chat components:

Slot| Description  
---|---  
`messageView`| The message list container.  
`scrollView`| The scroll container with auto-scroll behavior.  
`input`| The text input area with send/transcribe controls.  
`suggestionView`| The suggestion pills shown below messages.  
`welcomeScreen`| The initial empty-state screen (pass `false` to disable).  
  
`CopilotSidebar` and `CopilotPopup` also have:

Slot| Description  
---|---  
`header`| The modal header bar.  
`toggleButton`| The open/close toggle button.  
  
### On this page

What is this?What it looks like in codeWelcome screen slotAssistant message slotDisclaimer slotTailwind ClassesProps OverrideCustom ComponentsNested Slots (Drill-Down)Two levels deepThree levels deepLabelsAvailable SlotsCopilotChat / CopilotSidebar / CopilotPopup
