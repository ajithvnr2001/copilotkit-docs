---
url: https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:38.309146+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/css/

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

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)Custom Look and Feel

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
    
    
    """PydanticAI agent with sales todos state, weather/query tools, and HITL scheduling.Upgraded from proverbs demo to full feature parity with shared tool implementations."""import jsonfrom textwrap import dedentfrom typing import Anyfrom pydantic import BaseModel, Fieldfrom pydantic_ai import Agent, RunContextfrom pydantic_ai.ui import StateDepsfrom ag_ui.core import EventType, StateSnapshotEventfrom pydantic_ai.models.openai import OpenAIResponsesModelfrom dotenv import load_dotenvfrom tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)from tools.types import Flightload_dotenv()# =====# State# =====class SalesTodosState(BaseModel):    """Sales pipeline todos managed by the agent."""    todos: list[dict[str, Any]] = Field(        default_factory=list,        description="The list of sales pipeline todos",    )# =====# Agent# =====agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    deps_type=StateDeps[SalesTodosState],    system_prompt=dedent("""        You are a helpful sales assistant that helps manage a sales pipeline.        The user has a list of sales todos that you can help them manage.        You have tools available to add, update, or retrieve todos from the pipeline.        You can also look up weather and query financial data.        You can search flights and display rich A2UI cards (via search_flights tool).        You can generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool).        When discussing sales todos, ALWAYS use the get_sales_todos tool to see the current list        before mentioning, updating, or discussing todos with the user.    """).strip(),)# =====# Tools# =====@agent.tooldef get_weather(ctx: RunContext[StateDeps[SalesTodosState]], location: str) -> str:    """Get the weather for a given location. Ensure location is fully spelled out.    Useful on its own for weather questions, and a great companion to    `search_flights` — always consider checking the weather at a    destination the user is flying to, and checking flights to any    city whose weather the user has just asked about.    """    return json.dumps(get_weather_impl(location))@agent.tooldef query_data(ctx: RunContext[StateDeps[SalesTodosState]], query: str) -> str:    """Query financial database for chart data. Returns data suitable for pie or bar charts."""    return json.dumps(query_data_impl(query))@agent.toolasync def manage_sales_todos(    ctx: RunContext[StateDeps[SalesTodosState]], todos: list[dict[str, Any]]) -> StateSnapshotEvent:    """Manage the sales pipeline. Pass the complete list of sales todos."""    result = manage_sales_todos_impl(todos)    ctx.deps.state.todos = result    return StateSnapshotEvent(        type=EventType.STATE_SNAPSHOT,        snapshot=ctx.deps.state,    )@agent.tooldef get_sales_todos(ctx: RunContext[StateDeps[SalesTodosState]]) -> str:    """Get the current list of sales pipeline todos."""    return json.dumps(get_sales_todos_impl(ctx.deps.state.todos or None))@agent.tooldef schedule_meeting(    ctx: RunContext[StateDeps[SalesTodosState]], reason: str, duration_minutes: int = 30) -> str:    """Schedule a meeting. The user will be asked to pick a time via the UI."""    return json.dumps(schedule_meeting_impl(reason, duration_minutes))@agent.tooldef search_flights(    ctx: RunContext[StateDeps[SalesTodosState]], flights: list[dict[str, Any]]) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    result = search_flights_impl(flights)    return json.dumps(result)@agent.tooldef generate_a2ui(ctx: RunContext[StateDeps[SalesTodosState]]) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    """    from openai import OpenAI    # Extract conversation messages from deps    copilotkit_state = getattr(ctx.deps, "copilotkit", None)    conversation_messages: list[dict] = []    context_entries: list[dict] = []    if copilotkit_state:        if hasattr(copilotkit_state, "messages"):            for msg in copilotkit_state.messages or []:                role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)                if role in ("user", "assistant"):                    content = ""                    if hasattr(msg, "content"):                        if isinstance(msg.content, str):                            content = msg.content                        elif isinstance(msg.content, list):                            parts = []                            for part in msg.content:                                if hasattr(part, "text"):                                    parts.append(part.text)                                elif isinstance(part, dict) and "text" in part:                                    parts.append(part["text"])                            content = "".join(parts)                    if content:                        conversation_messages.append({"role": role, "content": content})        if hasattr(copilotkit_state, "context"):            context_entries = copilotkit_state.context or []    context_text = "\n\n".join(        entry.get("value", "")        for entry in context_entries        if isinstance(entry, dict) and entry.get("value")    )    client = OpenAI()    tool_schema = {        "type": "function",        "function": {            "name": "render_a2ui",            "description": "Render a dynamic A2UI v0.9 surface.",            "parameters": {                "type": "object",                "properties": {                    "surfaceId": {"type": "string"},                    "catalogId": {"type": "string"},                    "components": {"type": "array", "items": {"type": "object"}},                    "data": {"type": "object"},                },                "required": ["surfaceId", "catalogId", "components"],            },        },    }    llm_messages: list[dict] = [        {            "role": "system",            "content": context_text or "Generate a useful dashboard UI.",        },    ]    llm_messages.extend(conversation_messages)    response = client.chat.completions.create(        model="gpt-5-mini",        messages=llm_messages,        tools=[tool_schema],        tool_choice={"type": "function", "function": {"name": "render_a2ui"}},    )    if not response.choices[0].message.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    tool_call = response.choices[0].message.tool_calls[0]    args = json.loads(tool_call.function.arguments)    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)

## What is this?#

CopilotKit has a variety of ways to customize the colors and structure of the Copilot UI components via plain CSS. You can:

  * Override CopilotKit CSS variables to re-tint the whole UI
  * Target the built-in class names (`.copilotKit...`) for structural tweaks
  * Swap fonts per surface (messages, input, bubbles)
  * Replace icons and labels via component props



If you need to change behavior, not just look, see [slots](https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/slots) or [fully headless UI](https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/headless-ui).

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
