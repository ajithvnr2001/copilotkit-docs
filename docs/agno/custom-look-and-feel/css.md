---
url: https://docs.copilotkit.ai/agno/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:46:44.074008+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/agno/custom-look-and-feel/css/

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

On this page

[Agno](https://docs.copilotkit.ai/agno)Custom Look and Feel

# CSS Customization

Theme CopilotKit components via CSS variables and class overrides.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

main.py

page.tsx

theme.css

route.ts
    
    
    """Agno Sales Pipeline Agent with shared tools for showcase demos."""import jsonfrom agno.agent.agent import Agentfrom agno.models.openai import OpenAIChatfrom agno.tools import toolfrom dotenv import load_dotenvfrom tools import (    RENDER_A2UI_TOOL_SCHEMA,    build_a2ui_operations_from_tool_call,    get_weather_impl,    query_data_impl,    schedule_meeting_impl,    search_flights_impl,)from tools.types import Flightload_dotenv()@tooldef get_weather(location: str):    """    Get the weather for a given location. Ensure location is fully spelled out.    Args:        location (str): The location to get the weather for.    Returns:        str: Weather data as JSON.    """    return json.dumps(get_weather_impl(location))@tooldef query_data(query: str):    """    Query financial database for chart data. Returns data suitable for pie or bar charts.    Args:        query (str): The query to run against the financial database.    Returns:        str: Query results as JSON.    """    return json.dumps(query_data_impl(query))@tool(external_execution=True)def manage_sales_todos(todos: list[dict]):    """    Manage the sales pipeline. Pass the complete list of sales todos.    Always pass the COMPLETE list of todos.    Args:        todos (list[dict]): The complete list of sales todos to maintain.    """@tooldef schedule_meeting(reason: str):    """    Schedule a meeting with user approval. Returns available time slots.    Args:        reason (str): Reason for scheduling the meeting.    Returns:        str: Meeting scheduling data as JSON.    """    return json.dumps(schedule_meeting_impl(reason))@tool(external_execution=True, external_execution_silent=True)def request_user_approval(message: str, context: str = ""):    """    Ask the operator to approve or reject an action before you take it.    The operator will respond via an in-app modal dialog that appears    OUTSIDE the chat surface. The tool returns an object of the shape    { approved: boolean, reason?: string }.    Args:        message (str): Short summary of the action needing approval (include concrete numbers / IDs).        context (str): Optional extra context — e.g. the ticket ID or policy rule.    """@tool(external_execution=True)def change_background(background: str):    """    Change the background color of the chat.    ONLY call this tool when the user explicitly asks to change the background.    Never call it proactively or as part of another response.    Can be anything that the CSS background attribute accepts. Prefer gradients.    Args:        background (str): The CSS background value. Prefer gradients.    """@tool(external_execution=True, external_execution_silent=True)def book_call(topic: str, name: str):    """    Ask the user to pick a time slot for a call. The picker UI presents    fixed candidate slots; the user's choice is returned to the agent.    Args:        topic (str): What the call is about (e.g. "Intro with sales").        name (str): Name of the attendee (e.g. "Alice").    """@tool(external_execution=True, external_execution_silent=True)def generate_task_steps(steps: list[dict]):    """    Generates a list of steps for the user to perform.    Each step should have a description and status.    Args:        steps (list[dict]): A list of step objects, each with 'description' (str)                            and 'status' ('enabled' or 'disabled').    """@tooldef search_flights(flights: list[dict]):    """    Search for flights and display the results as rich A2UI cards.    Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18"),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    Args:        flights (list[dict]): List of flight objects to display.    Returns:        str: A2UI operations as JSON.    """    typed_flights = [Flight(**f) for f in flights]    result = search_flights_impl(typed_flights)    return json.dumps(result)@tooldef get_stock_price(ticker: str):    """    Get a mock current price for a stock ticker.    When the user asks about a single ticker, also consider pulling a    related ticker for context (e.g. if they ask about 'AAPL', also    fetch 'MSFT' or 'GOOGL' so the reply can compare).    Args:        ticker (str): The ticker symbol to look up.    Returns:        str: Mock price data as JSON.    """    from random import choice, randint    return json.dumps(        {            "ticker": ticker.upper(),            "price_usd": round(100 + randint(0, 400) + randint(0, 99) / 100, 2),            "change_pct": round(choice([-1, 1]) * (randint(0, 300) / 100), 2),        }    )@tooldef roll_dice(sides: int = 6):    """    Roll a single die with the given number of sides.    When the user asks for a roll, consider rolling twice with different    numbers of sides so the reply can show a contrast (e.g. a d6 AND a d20).    Args:        sides (int): The number of sides on the die. Defaults to 6.    Returns:        str: Dice roll result as JSON.    """    from random import randint    return json.dumps({"sides": sides, "result": randint(1, max(2, sides))})@tooldef generate_a2ui(context: str):    """    Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    Args:        context (str): Conversation context to generate UI for.    Returns:        str: A2UI operations as JSON.    """    import openai    client = openai.OpenAI()    response = client.chat.completions.create(        model="gpt-5-mini",        messages=[            {"role": "system", "content": context or "Generate a useful dashboard UI."},            {                "role": "user",                "content": "Generate a dynamic A2UI dashboard based on the conversation.",            },        ],        tools=[            {                "type": "function",                "function": RENDER_A2UI_TOOL_SCHEMA,            }        ],        tool_choice={"type": "function", "function": {"name": "render_a2ui"}},    )    choice = response.choices[0]    if choice.message.tool_calls:        args = json.loads(choice.message.tool_calls[0].function.arguments)        result = build_a2ui_operations_from_tool_call(args)        return json.dumps(result)    return json.dumps({"error": "LLM did not call render_a2ui"})def _create_session_db():    # Keep this import outside the public weather-tool region above.    from agno.db.sqlite import SqliteDb    # The production container runs as an unprivileged user with a read-only    # application directory, so its SQLite file belongs in writable /tmp.    return SqliteDb(db_file="/tmp/agno.db")agent = Agent(    # Raise the HTTP timeout so requests routed through aimock don't time out    # under normal load.  The default httpx timeout is too short when aimock    # is proxying to the upstream LLM — observed "Request timed out" errors    # that crash the agent run and trigger watchdog restarts.    model=OpenAIChat(id="gpt-5-mini", timeout=120),    # Frontend and HITL tools pause the run before the browser responds.    # Keep the session in a writable location so Agno can resume that run.    db=_create_session_db(),    tools=[        get_weather,        query_data,        manage_sales_todos,        schedule_meeting,        change_background,        book_call,        generate_task_steps,        request_user_approval,        search_flights,        get_stock_price,        roll_dice,        generate_a2ui,    ],    # Prevent runaway tool-call loops — same guard as the ag2 package.    tool_call_limit=15,    description="You are a helpful sales assistant for the CopilotKit showcase demos.",    instructions="""        SALES PIPELINE:        When a user asks you to do anything regarding sales todos or the pipeline,        use the manage_sales_todos tool. Always pass the COMPLETE LIST of todos.        Be helpful in managing sales pipeline items.        After using the tool, provide a brief summary of what you created, removed, or changed.        WEATHER:        Only call the get_weather tool if the user asks about the weather.        If the user does not specify a location, use "Everywhere ever in the whole wide world".        QUERY DATA:        Use the query_data tool when the user asks for financial data, charts, or analytics.        SCHEDULE MEETING:        Use the schedule_meeting tool when the user wants to schedule a meeting.        BACKGROUND:        Only call change_background when the user explicitly asks to change colors/background.        BOOK CALL (HITL):        When the user asks to book a call / schedule an intro / 1:1, call        book_call with the topic and the person's name. The frontend renders a        time picker; the user's choice is returned as the tool result.        TASK STEPS (HITL):        When asked to plan something, use the generate_task_steps tool with a list of steps.        Each step should have a description and status of "enabled".        FLIGHT SEARCH:        Use search_flights when the user asks about flights. Generate 2 realistic flights.        STOCK PRICES:        Use get_stock_price when the user asks about a ticker. Consider        fetching a second related ticker for comparison when helpful.        DICE:        Use roll_dice when the user asks to roll a die. Consider rolling a        second time with a different number of sides for contrast.        DYNAMIC A2UI:        Use generate_a2ui when the user asks for a dashboard or dynamic UI.        USER APPROVAL (HITL):        When asked to take any action that affects a customer — for example        issuing a refund, updating a plan, cancelling a subscription,        escalating a ticket, or sending a credit — call request_user_approval        FIRST with a short summary and optional context. Follow the tool        result: if approved, confirm in one short sentence; if rejected,        acknowledge and do not retry.    """,)

## What is this?#

CopilotKit has a variety of ways to customize the colors and structure of the Copilot UI components via plain CSS. You can:

  * Override CopilotKit CSS variables to re-tint the whole UI
  * Target the built-in class names (`.copilotKit...`) for structural tweaks
  * Swap fonts per surface (messages, input, bubbles)
  * Replace icons and labels via component props



If you need to change behavior, not just look, see [slots](https://docs.copilotkit.ai/agno/custom-look-and-feel/slots) or [fully headless UI](https://docs.copilotkit.ai/agno/custom-look-and-feel/headless-ui).

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
