---
url: https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:55.177070+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/css/

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

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)Custom Look and Feel

# CSS Customization

Theme CopilotKit components via CSS variables and class overrides.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

theme.css

route.ts
    
    
    """MS Agent Framework agent with sales todos state, weather tool, query data,and HITL schedule meeting tool.Adapted from examples/integrations/ms-agent-framework-python/agent/src/agent.py"""from __future__ import annotationsimport jsonfrom textwrap import dedentfrom typing import Annotatedfrom agent_framework import Agent, BaseChatClient, toolfrom agent_framework_ag_ui import AgentFrameworkAgentfrom pydantic import Field# =====================================================================# Shared tool implementations# =====================================================================from tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,)STATE_SCHEMA: dict[str, object] = {    "salesTodos": {        "type": "array",        "items": {            "type": "object",            "properties": {                "id": {"type": "string"},                "title": {"type": "string"},                "stage": {"type": "string"},                "value": {"type": "number"},                "dueDate": {"type": "string"},                "assignee": {"type": "string"},                "completed": {"type": "boolean"},            },        },        "description": "Ordered list of the user's sales pipeline todos.",    }}PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {    "salesTodos": {        "tool": "manage_sales_todos",        "tool_argument": "todos",    }}@tool(    name="manage_sales_todos",    description=(        "Replace the entire list of sales todos with the provided values. "        "Always include every todo you want to keep."    ),)def manage_sales_todos(    todos: Annotated[        list[dict],        Field(            description=(                "The complete source of truth for the user's sales todos. "                "Maintain ordering and include the full list on each call."            )        ),    ],) -> str:    """Persist the provided set of sales todos."""    result = manage_sales_todos_impl(todos)    return f"Sales todos updated. Tracking {len(result)} item(s)."@tool(    name="get_sales_todos",    description="Get the current list of sales todos.",)def get_sales_todos() -> str:    """Return the current sales todos or defaults."""    result = get_sales_todos_impl()    return json.dumps(result)@tool(    name="get_weather",    description="Get the current weather for a location. Use this to render the frontend weather card.",)def get_weather(    location: Annotated[        str,        Field(            description="The city or region to describe. Use fully spelled out names."        ),    ],) -> str:    """Return weather data as JSON for UI rendering."""    result = get_weather_impl(location)    return json.dumps(result)@tool(    name="query_data",    description="Query the database. Takes natural language. Always call before showing a chart or graph.",)def query_data(    query: Annotated[        str, Field(description="Natural language query to run against the database.")    ],) -> str:    """Query the database and return results as JSON."""    result = query_data_impl(query)    return json.dumps(result)@tool(    name="schedule_meeting",    description="Schedule a meeting. The user will be asked to pick a time via the meeting time picker UI.",    approval_mode="always_require",)def schedule_meeting(    reason: Annotated[str, Field(description="Reason for scheduling the meeting.")],    duration_minutes: Annotated[        int, Field(description="Duration of the meeting in minutes.")    ] = 30,) -> str:    """Request human approval to schedule a meeting."""    result = schedule_meeting_impl(reason, duration_minutes)    return json.dumps(result)@tool(    name="search_flights",    description=(        "Search for flights and display the results as rich A2UI cards. Return exactly 2 flights. "        "Each flight must have: airline, airlineLogo, flightNumber, origin, destination, "        "date, departureTime, arrivalTime, duration, status, statusColor, price, currency."    ),)def search_flights(    flights: Annotated[        list[dict],        Field(description="List of flight objects to search and display."),    ],) -> str:    """Search for flights and display as rich cards."""    result = search_flights_impl(flights)    return json.dumps(result)def create_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:    """Instantiate the CopilotKit demo agent backed by Microsoft Agent Framework."""    base_agent = Agent(        client=chat_client,        name="sales_agent",        instructions=dedent(            """            You help users manage their sales pipeline, check weather, query data, and schedule meetings.            State sync:            - The current list of sales todos is provided in the conversation context.            - When you add, remove, or reorder todos, call `manage_sales_todos` with the full list.              Never send partial updates--always include every todo that should exist.            - CRITICAL: When asked to "add" a todo, you must:              1. First, identify ALL existing todos from the conversation history              2. Create EXACTLY ONE new todo (never more than one unless explicitly requested)              3. Call manage_sales_todos with: [all existing todos] + [the one new todo]            - When asked to "remove" a todo, remove exactly ONE item unless user specifies otherwise.            Tool usage rules:            - When user asks to schedule a meeting, you MUST call the `schedule_meeting` tool immediately.              Do NOT ask for approval yourself--the tool's approval workflow and the client UI will handle it.            Frontend integrations:            - `get_weather` renders a weather card in the UI. Only call this tool when the user explicitly              asks for weather. Do NOT call it after unrelated tasks or approvals.            - `query_data` fetches database records. Always call before showing charts or graphs.            - `schedule_meeting` requires explicit user approval before you proceed. Only use it when a              user asks to schedule or set up a meeting. Always call the tool instead of asking manually.            Conversation tips:            - Reference the latest todo list before suggesting changes.            - Keep responses concise and friendly unless the user requests otherwise.            - After you finish executing tools for the user's request, provide a brief, final assistant              message summarizing exactly what changed. Do NOT call additional tools or switch topics              after that summary unless the user asks. ALWAYS send this conversational summary so the message persists.            """.strip()        ),        tools=[            manage_sales_todos,            get_sales_todos,            get_weather,            query_data,            schedule_meeting,            search_flights,        ],    )    return AgentFrameworkAgent(        agent=base_agent,        name="CopilotKitMicrosoftAgentFrameworkAgent",        description="Manages sales pipeline todos, weather, data queries, and meeting scheduling.",        predict_state_config=PREDICT_STATE_CONFIG,        require_confirmation=False,    )

## What is this?#

CopilotKit has a variety of ways to customize the colors and structure of the Copilot UI components via plain CSS. You can:

  * Override CopilotKit CSS variables to re-tint the whole UI
  * Target the built-in class names (`.copilotKit...`) for structural tweaks
  * Swap fonts per surface (messages, input, bubbles)
  * Replace icons and labels via component props



If you need to change behavior, not just look, see [slots](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/slots) or [fully headless UI](https://docs.copilotkit.ai/ms-agent-python/custom-look-and-feel/headless-ui).

## Scoping the theme#

The demo keeps all of its styling in a sibling `theme.css` file and applies it only to the wrapper div holding `<CopilotChat>`. Importing the stylesheet from the page module is enough; Next.js bundles it with the route:

page.tsx
    
    
    import "./theme.css";

Scoping every selector under a wrapper class keeps the overrides from leaking into the rest of the app.

## CSS Variables (Easiest)#

The easiest way to change the colors used in the Copilot UI components is to override CopilotKit CSS variables. The demo sets them on the scope wrapper so they cascade into every nested chat component:

theme.css
    
    
    /* HALCYON palette — a private library at golden hour. The whole theme is * one warm parchment hue, one warm ink, and a deep copper ember used * sparingly so it actually reads as a signal. */.chat-css-demo-scope {  --halcyon-paper: #f4efe6;  --halcyon-paper-soft: #ece6d9;  --halcyon-paper-elevated: #fbf8f2;  --halcyon-card: #ffffff;  --halcyon-rule: #d6cfbe;  --halcyon-rule-strong: #aea48a;  --halcyon-ink: #1a1714;  --halcyon-ink-soft: #3d362e;  --halcyon-ink-mute: #7a7468;  --halcyon-ember: #c44a1f;  --halcyon-ember-bright: #e45f2b;  --halcyon-ember-soft: #f3d7c5;  --halcyon-champagne: #98794a;  --halcyon-display:    "Instrument Serif", ui-serif, "Iowan Old Style", Georgia, serif;  --halcyon-serif:    "Fraunces", "Source Serif Pro", ui-serif, Georgia, "Times New Roman", serif;  --halcyon-sans:    "Inter Tight", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI",    sans-serif;  --halcyon-mono:    "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;  --halcyon-shadow-soft:    0 1px 0 rgba(26, 23, 20, 0.04), 0 12px 32px -18px rgba(26, 23, 20, 0.18);  --halcyon-shadow-ember:    0 1px 0 rgba(196, 74, 31, 0.18), 0 14px 36px -16px rgba(196, 74, 31, 0.42);}

Once you've found the right variable, you can also apply the overrides inline via the `CopilotKitCSSProperties` helper:
    
    
    import { CopilotKitCSSProperties } from "@copilotkit/react-ui";
    
    <div
      style={
        {
          "--copilot-kit-primary-color": "#222222",
        } as CopilotKitCSSProperties
      }
    >
      <CopilotSidebar />
    </div>

### Reference#

CSS Variable| Description  
---|---  
`--copilot-kit-primary-color`| Main brand/action color for buttons and interactive elements  
`--copilot-kit-contrast-color`| Color that contrasts with primary, used for text on primary elements  
`--copilot-kit-background-color`| Main page/container background color  
`--copilot-kit-secondary-color`| Secondary background for cards, panels, and elevated surfaces  
`--copilot-kit-secondary-contrast-color`| Primary text color for main content  
`--copilot-kit-separator-color`| Border color for dividers and containers  
`--copilot-kit-muted-color`| Muted color for disabled/inactive states  
`--copilot-kit-shadow-sm` / `-md` / `-lg`| Elevation shadows for subtle surfaces, cards, and modals  
  
Two token systems

The `--copilot-kit-*` variables above style the **v1** component CSS (`@copilotkit/react-ui`). The newer **v2** components (`@copilotkit/react-core/v2`) are Tailwind + shadcn-based and use a separate set of design tokens. See v2 design tokens below.

## v2 Design Tokens (shadcn)#

The v2 components (`@copilotkit/react-core/v2`) ship a Tailwind v4 theme built on the standard shadcn/ui token set. Instead of the `--copilot-kit-*` variables, they read [oklch](https://oklch.com) color tokens that are scoped to the `[data-copilotkit]` root and wired into Tailwind utilities through an `@theme inline` block. This means you can re-skin the entire v2 UI by overriding a handful of CSS custom properties. Every component picks the change up automatically.

Override them on the `[data-copilotkit]` element (or any ancestor) the same way you would in a shadcn project:

globals.css
    
    
    [data-copilotkit] {
      --primary: oklch(0.55 0.22 264); /* accent / action color */
      --primary-foreground: oklch(0.99 0 0); /* text on primary */
      --background: oklch(1 0 0); /* surface background */
      --foreground: oklch(0.145 0 0); /* primary text */
      --muted: oklch(0.97 0 0); /* subtle backgrounds */
      --border: oklch(0.922 0 0); /* dividers, outlines */
      --radius: 0.625rem; /* global corner radius */
    }
    
    /* Dark mode is keyed off a `.dark` ancestor */
    .dark [data-copilotkit] {
      --background: oklch(0.145 0 0);
      --foreground: oklch(0.985 0 0);
      --border: oklch(0.269 0 0);
    }

### Reference#

These are the most commonly overridden v2 tokens. Each light value has a matching dark-mode value under `.dark [data-copilotkit]`. The full set (popover, accent, destructive, chart, and sidebar variants) lives in `@copilotkit/react-core/v2/styles.css`.

Token| Description  
---|---  
`--background` / `--foreground`| Base surface background and primary text color  
`--primary` / `--primary-foreground`| Accent/action color and the text rendered on top of it  
`--secondary` / `--secondary-foreground`| Secondary surfaces (cards, panels) and their text  
`--muted` / `--muted-foreground`| Subtle backgrounds and de-emphasized text  
`--accent` / `--accent-foreground`| Hover/active states and their text  
`--border` / `--input` / `--ring`| Divider/outline color, input borders, focus ring  
`--destructive` / `--destructive-foreground`| Error/danger color and its text  
`--card` / `--popover` (+ `-foreground`)| Elevated surface backgrounds and their text  
`--sidebar-*`| The sidebar's own background/foreground/border/ring set  
`--radius`| Base corner radius; `--radius-sm/md/lg/xl` derive from it  
  
oklch values

v2 tokens use the `oklch()` color space, which keeps perceived lightness consistent across hues. You can still pass `hsl()`, `rgb()`, or hex; any valid CSS color works.

## Custom CSS#

The CopilotKit CSS is structured to allow customization via CSS classes. You can target specific pieces of the UI from your own stylesheet:

globals.css
    
    
    .copilotKitButton {
      border-radius: 0;
    }
    
    .copilotKitMessages {
      padding: 2rem;
    }
    
    .copilotKitUserMessage {
      background: #007AFF;
    }

The demo's `theme.css` wraps every selector under `.chat-css-demo-scope` so the overrides don't leak out. Here's the user message bubble block from that file:

theme.css
    
    
    /* User message — a "transmission" in JetBrains Mono on a paper card. The * outer wrapper is the right-aligning flex column; we leave it transparent * and style the inner bubble (which uses cpk:bg-muted, hence we also * target the substring class as a stable hook). */.chat-css-demo-scope .copilotKitMessage.copilotKitUserMessage {  background: transparent;  padding: 0;  border: none;  box-shadow: none;}.chat-css-demo-scope  .copilotKitMessage.copilotKitUserMessage  > [class*="bg-muted"] {  font-family: var(--halcyon-mono);  font-size: 0.875rem;  font-weight: 400;  color: var(--halcyon-ink);  background: var(--halcyon-paper-elevated);  border: 1px solid var(--halcyon-rule);  border-left: 2px solid var(--halcyon-ember);  border-radius: 0;  padding: 12px 16px 12px 18px;  letter-spacing: -0.005em;  line-height: 1.55;  box-shadow: 0 1px 0 rgba(26, 23, 20, 0.03);  position: relative;}/* A mono "→" marker before the user's text to read like a CLI prompt. */.chat-css-demo-scope  .copilotKitMessage.copilotKitUserMessage  > [class*="bg-muted"]::before {  content: "→";  display: inline-block;  margin-right: 10px;  color: var(--halcyon-ember);  font-weight: 500;}

### Reference#

CSS Class| Description  
---|---  
`.copilotKitMessages`| Main container for all chat messages  
`.copilotKitMessage`| Base class applied to every message bubble (user and assistant)  
`.copilotKitInput`| Text input container with typing area and send button  
`.copilotKitUserMessage`| Styling for user messages  
`.copilotKitAssistantMessage`| Styling for AI responses  
`.copilotKitHeader`| Top bar of chat window containing title and controls  
`.copilotKitButton`| Primary chat toggle button  
`.copilotKitWindow`| Root container defining overall chat window dimensions  
`.copilotKitMarkdown`| Styles for rendered markdown content  
`.copilotKitCodeBlock`| Code snippet container with syntax highlighting  
`.copilotKitSidebar`| Styles for sidebar chat mode  
`.copilotKitPopup`| Styles for popup chat mode  
  
## Custom Fonts#

You can customize the fonts by updating the `fontFamily` property on the relevant CopilotKit classes:

globals.css
    
    
    .copilotKitMessages {
      font-family: "Arial, sans-serif";
    }
    
    .copilotKitInput {
      font-family: "Arial, sans-serif";
    }

## Custom Icons#

Customize icons by passing the `icons` prop to `CopilotSidebar`, `CopilotPopup`, or `CopilotChat`:
    
    
    <CopilotChat
      icons={{
        openIcon: <YourOpenIconComponent />,
        closeIcon: <YourCloseIconComponent />,
      }}
    />

## Custom Labels#

Customize all user-facing copy via the `labels` prop:
    
    
    <CopilotChat
      labels={{
        welcomeMessageText: "Hello! How can I help you today?",
        modalHeaderTitle: "My Copilot",
        chatInputPlaceholder: "Ask me anything!",
      }}
    />

### On this page

What is this?Scoping the themeCSS Variables (Easiest)Referencev2 Design Tokens (shadcn)ReferenceCustom CSSReferenceCustom FontsCustom IconsCustom Labels
