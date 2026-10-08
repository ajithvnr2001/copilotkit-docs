---
url: https://docs.copilotkit.ai/ag2/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:43:53.027666+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/ag2/custom-look-and-feel/css/

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

On this page

[AG2](https://docs.copilotkit.ai/ag2)Custom Look and Feel

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
    
    
    """AG2 agent with weather and sales tools for CopilotKit showcase.Uses AG2's ConversableAgent with AGUIStream to exposethe agent via the AG-UI protocol."""from __future__ import annotationsimport jsonimport loggingfrom typing import Annotated, Anyimport openaifrom autogen import ConversableAgent, LLMConfigfrom autogen.ag_ui import AGUIStreamfrom dotenv import load_dotenvfrom pydantic import ValidationErrorload_dotenv()# Import shared tool implementationsfrom tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,    RENDER_A2UI_TOOL_SCHEMA,)from tools.types import Flightfrom ._header_forwarding import get_forwarded_headersfrom ._request_context import get_latest_user_messagelogger = logging.getLogger(__name__)# Module-level async client: re-used across requests (httpx connection pool is# thread-safe). Using AsyncOpenAI inside an `async def` avoids blocking the# ASGI event loop on the secondary LLM call._async_openai_client = openai.AsyncOpenAI()# =====# Tools# =====async def get_weather(    location: Annotated[str, "City name to get weather for"],) -> str:    """Get current weather for a location."""    result = get_weather_impl(location)    # Return a JSON string (not a dict): autogen serializes dict returns with    # str(), producing a Python repr (single quotes) that the frontend's    # parseJsonResult/JSON.parse cannot parse — the weather card then renders    # "--" placeholders. Same pattern as search_flights below.    return json.dumps(        {            "city": result["city"],            "temperature": result["temperature"],            "feels_like": result["feels_like"],            "humidity": result["humidity"],            "wind_speed": result["wind_speed"],            "conditions": result["conditions"],        }    )async def query_data(    query: Annotated[str, "Natural language query for financial data"],) -> str:    """Query financial database for chart data."""    # Return a JSON string (not a list): autogen serializes non-str returns    # with str(), producing a Python repr (single quotes) that the frontend's    # parseJsonResult/JSON.parse cannot parse. Same pattern as get_weather.    return json.dumps(query_data_impl(query))async def manage_sales_todos(    todos: Annotated[list, "Complete list of sales todos"],) -> str:    """Manage the sales pipeline."""    # See contract comment on query_data above — return JSON, not dict.    # SalesTodo is a Pydantic model; coerce via model_dump for serialisability.    result = [t.model_dump() for t in manage_sales_todos_impl(todos)]    return json.dumps({"todos": result})async def get_sales_todos() -> str:    """Get the current sales pipeline."""    # See contract comment on query_data above — return JSON, not list.    # SalesTodo is a Pydantic model; coerce via model_dump for serialisability.    return json.dumps([t.model_dump() for t in get_sales_todos_impl(None)])async def schedule_meeting(    reason: Annotated[str, "Reason for the meeting"],) -> str:    """Schedule a meeting with user approval."""    # See contract comment on query_data above — return JSON, not dict.    return json.dumps(schedule_meeting_impl(reason))async def search_flights(    flights: Annotated[        list[dict[str, Any]], "List of flight objects to display as rich A2UI cards"    ],) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    try:        typed_flights: list[Flight] = [Flight(**f) for f in flights]    except ValidationError as exc:        logger.warning(            "search_flights: invalid flight shape type=%s err=%s",            type(exc).__name__,            exc,            exc_info=True,        )        return json.dumps({"error": f"invalid flight shape: {exc}"})    result = search_flights_impl(typed_flights)    return json.dumps(result)async def generate_a2ui(    context: Annotated[str, "Conversation context to generate UI for"],) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    """    # A13: AsyncOpenAI inside async def (was sync openai.OpenAI which blocks    # the ASGI event loop). Forward x-* headers via extra_headers in addition    # to the global httpx hook so aimock context routing is explicit at the    # call site.    #    # R2-A1 / A4: thread the latest user prompt from the inbound    # RunAgentInput.messages payload (captured into a per-request ContextVar    # by RequestUserMessageMiddleware — see agents/_request_context.py) into    # the inner LLM call so each pill's request body is byte-distinct.    # Without this, every pill landing on the omnibus agent (agentic-chat /    # tool-rendering / chat-customization-css / hitl) produces an IDENTICAL    # inner-LLM body and the aimock fixture cannot disambiguate. Falls back    # to the original hardcoded prompt when the middleware captured nothing    # (parse failure already logged at WARNING).    user_prompt = get_latest_user_message() or (        "Generate a dynamic A2UI dashboard based on the conversation."    )    forwarded = get_forwarded_headers()    try:        response = await _async_openai_client.chat.completions.create(            model="gpt-5-mini",            messages=[                {                    "role": "system",                    "content": context or "Generate a useful dashboard UI.",                },                {                    "role": "user",                    "content": user_prompt,                },            ],            tools=[                {                    "type": "function",                    "function": RENDER_A2UI_TOOL_SCHEMA,                }            ],            tool_choice={"type": "function", "function": {"name": "render_a2ui"}},            extra_headers=forwarded or None,        )    except Exception as exc:        logger.error(            "generate_a2ui: inner LLM call failed type=%s err=%s",            type(exc).__name__,            exc,            exc_info=True,        )        return json.dumps({"error": f"inner LLM call failed: {type(exc).__name__}"})    if not response.choices:        logger.warning("generate_a2ui: LLM returned no choices")        return json.dumps({"error": "LLM returned no choices"})    choice = response.choices[0]    if not choice.message.tool_calls:        logger.warning("generate_a2ui: secondary LLM produced no render_a2ui tool call")        return json.dumps({"error": "LLM did not call render_a2ui"})    try:        args = json.loads(choice.message.tool_calls[0].function.arguments)        result = build_a2ui_operations_from_tool_call(args)        return json.dumps(result)    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:        logger.error(            "generate_a2ui: failed to parse render_a2ui args type=%s err=%s",            type(exc).__name__,            exc,            exc_info=True,        )        return json.dumps(            {"error": f"failed to parse render_a2ui args: {type(exc).__name__}"}        )# =====# Agent# =====agent = ConversableAgent(    name="assistant",    system_message=(        "You are a helpful sales assistant. You can look up current weather "        "for any city using the get_weather tool, query financial data with "        "query_data, manage the sales pipeline with manage_sales_todos and "        "get_sales_todos, schedule meetings with schedule_meeting, search "        "flights and display rich A2UI cards with search_flights, and "        "generate dynamic A2UI dashboards with generate_a2ui. "        "When asked about the weather, always use the tool rather than guessing. "        "Be concise and friendly in your responses."    ),    llm_config=LLMConfig({"model": "gpt-5-mini", "stream": True}),    human_input_mode="NEVER",    # Guard against infinite tool-call loops: AG2's ConversableAgent with    # human_input_mode="NEVER" will keep executing tool calls indefinitely    # if the LLM keeps requesting them.  Without this limit the agent floods    # Railway's log stream (500 logs/sec rate-limit), becomes unresponsive    # to health probes, and gets killed by the watchdog.    max_consecutive_auto_reply=15,    functions=[        get_weather,        query_data,        manage_sales_todos,        get_sales_todos,        schedule_meeting,        search_flights,        generate_a2ui,    ],)# AG-UI stream wrapperstream = AGUIStream(agent)

## What is this?#

CopilotKit has a variety of ways to customize the colors and structure of the Copilot UI components via plain CSS. You can:

  * Override CopilotKit CSS variables to re-tint the whole UI
  * Target the built-in class names (`.copilotKit...`) for structural tweaks
  * Swap fonts per surface (messages, input, bubbles)
  * Replace icons and labels via component props



If you need to change behavior, not just look, see [slots](https://docs.copilotkit.ai/ag2/custom-look-and-feel/slots) or [fully headless UI](https://docs.copilotkit.ai/ag2/custom-look-and-feel/headless-ui).

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
