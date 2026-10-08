---
url: https://docs.copilotkit.ai/agno/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:46:45.883046+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/agno/custom-look-and-feel/reasoning-messages/

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

# Reasoning Messages

Customize how reasoning (thinking) tokens from models like o1, o3, and o4-mini are displayed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning_agent.py

page.tsx

route.ts
    
    
    """Reasoning-capable Agno agent for the reasoning family of demos.Backs three showcase cells:    - reasoning-custom             (custom amber ReasoningBlock slot)    - reasoning-default            (CopilotKit's built-in reasoning card)    - tool-rendering-reasoning-chain (reasoning + sequential tool calls)Mirrors `showcase/integrations/langgraph-python/src/agents/reasoning_agent.py`(shared across the three reasoning demos there).Uses reasoning=False with a custom AGUI handler in agent_server.py thatemits REASONING_MESSAGE_* AG-UI events. The primary channel is Agno'snative `reasoning_content` (chat-completions stream a `delta.reasoning_content`field surfaced on each `RunContentEvent.reasoning_content`), tee'd into theAG-UI reasoning stream; parsing of <reasoning>...</reasoning> XML tags in themodel output remains as a defensive fallback when the native channel is empty.Running with reasoning=False avoids Agno's multi-call CoT loop (which breaksaimock fixtures) while still producing the proper AG-UI events thatCopilotKit's frontend renders via the reasoningMessage slot.For the reasoning-chain demo we also expose the same shared backend tools(`get_weather`, `search_flights`, `get_stock_price`, `roll_dice`) as theprimary agent so the catch-all tool renderer can observe a fullreasoning -> tool call -> reasoning -> tool call chain."""from __future__ import annotationsimport jsonfrom agno.agent.agent import Agentfrom agno.models.openai import OpenAIChatfrom agno.tools import toolfrom dotenv import load_dotenvfrom tools import (    get_weather_impl,    search_flights_impl,)from tools.types import Flightload_dotenv()@tooldef get_weather(location: str):    """    Get the weather for a given location. Ensure location is fully spelled out.    Args:        location (str): The location to get the weather for.    Returns:        str: Weather data as JSON.    """    return json.dumps(get_weather_impl(location))@tooldef search_flights(flights: list[dict]):    """    Search for flights and display the results as rich A2UI cards.    Return exactly 2 flights.    Args:        flights (list[dict]): List of flight objects to display.    Returns:        str: A2UI operations as JSON.    """    typed_flights = [Flight(**f) for f in flights]    result = search_flights_impl(typed_flights)    return json.dumps(result)@tooldef get_stock_price(ticker: str):    """    Get a mock current price for a stock ticker.    Args:        ticker (str): The ticker symbol to look up.    Returns:        str: Mock price data as JSON.    """    from random import choice, randint    return json.dumps(        {            "ticker": ticker.upper(),            "price_usd": round(100 + randint(0, 400) + randint(0, 99) / 100, 2),            "change_pct": round(choice([-1, 1]) * (randint(0, 300) / 100), 2),        }    )@tooldef roll_dice(sides: int = 6):    """    Roll a single die with the given number of sides.    Args:        sides (int): The number of sides on the die. Defaults to 6.    Returns:        str: Dice roll result as JSON.    """    from random import randint    return json.dumps({"sides": sides, "result": randint(1, max(2, sides))})# NOTE: reasoning=False (the default) is used here intentionally.## Agno's reasoning=True triggers a multi-call Chain-of-Thought loop that# makes up to `reasoning_max_steps` sequential LLM calls. This breaks in# proxy/fixture environments (aimock, D5 probes) where only the first# call matches a fixture — subsequent calls don't match and either fall# through to the real API (slow, non-deterministic) or fail entirely.## Instead, the custom AGUI handler in agent_server.py synthesizes# REASONING_MESSAGE_* AG-UI events from the agent's response text. The# system prompt instructs the model to prefix its answer with a reasoning# block delimited by <reasoning>...</reasoning> tags. The custom handler# parses those tags and emits proper AG-UI reasoning events that# CopilotKit's frontend renders via the reasoningMessage slot.## This approach:#   - Works with aimock (single LLM call)#   - Emits proper AG-UI REASONING_MESSAGE_* events (unlike Agno's stock#     AGUI handler which only emits STEP_STARTED/STEP_FINISHED)#   - Keeps the demo visually identical to native reasoning modelsagent = Agent(    model=OpenAIChat(id="gpt-4o-mini", timeout=120),    tools=[get_weather, search_flights, get_stock_price, roll_dice],    reasoning=False,    tool_call_limit=10,    description=(        "You are a helpful assistant. For each user question, first think "        "step-by-step about the approach, then answer concisely. When the "        "question calls for a tool, call it explicitly rather than guessing."    ),    instructions="""        REASONING STYLE:        Always begin your response with a reasoning block wrapped in        <reasoning>...</reasoning> XML tags. Inside the tags, think        step-by-step (two to four short steps is plenty). After the closing        tag, give your concise final answer. Example:        <reasoning>        Step 1: Identify what the user is asking.        Step 2: Consider which tool to use.        Step 3: Formulate the answer.        </reasoning>        Here is my answer...        TOOLS (reasoning-chain cell):        - get_weather: use when the user asks about weather.        - search_flights: use when the user asks about flights. Generate 2          realistic flights. Flight shape: airline, airlineLogo (Google          favicon URL), flightNumber, origin, destination, date          ("Tue, Mar 18"), departureTime, arrivalTime, duration ("4h 25m"),          status ("On Time"|"Delayed"), statusColor (hex), price ("$289"),          currency ("USD").        - get_stock_price: use when the user asks about a ticker. Consider          fetching a second related ticker for comparison.        - roll_dice: use when the user asks to roll a die. Consider rolling          twice with different numbers of sides.    """,)

Some models (like OpenAI's o1, o3, and o4-mini) emit **reasoning tokens** : internal "thinking" traces that show the model's chain-of-thought before it produces a final answer. CopilotKit surfaces these tokens automatically with a collapsible **Reasoning Message** card.

## Default Behavior#

When reasoning events arrive from the agent, CopilotKit renders them inside a built-in card that:

  * Shows a **"Thinking…"** label with a pulsating indicator while the model is reasoning.
  * Expands automatically so you can follow the model's thought process in real-time.
  * Collapses and switches to **"Thought for X seconds"** once reasoning finishes.
  * Renders the reasoning content as **Markdown**.
  * Includes a chevron toggle so users can re-expand and review the reasoning at any time.



No extra configuration is needed; if your model emits reasoning tokens, the card appears automatically.

The only requirement is connecting your agent to CopilotKit; no extra props or configuration needed:

page.tsx
    
    
    const AGENT_ID = "reasoning-default";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

## Customizing the Reasoning Message#

The reasoning message is composed of three sub-components that can each be replaced independently via **slot props** :

Sub-component| Slot prop| Description  
---|---|---  
`Header`| `header`| The clickable bar with the brain icon, label, and chevron  
`Content`| `contentView`| The reasoning text area (Markdown)  
`Toggle`| `toggle`| The expand/collapse animation wrapper  
  
You pass custom sub-components through the `messageView` prop on `CopilotChat`, `CopilotPopup`, or `CopilotSidebar`:
    
    
    <CopilotChat
      messageView={{
        reasoningMessage: {
          header: CustomHeader,
          contentView: CustomContent,
        },
      }}
    />

### Custom Header#

Replace the header to change the icon, label text, or styling. The header receives these props:

Prop| Type| Description  
---|---|---  
`isOpen`| `boolean`| Whether the content panel is currently expanded  
`label`| `string`| `"Thinking…"` while streaming, `"Thought for X seconds"` after  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`isStreaming`| `boolean`| Whether reasoning is actively streaming  
`onClick`| `() => void`| Toggle handler (only present when `hasContent` is `true`)  
      
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function CustomHeader({
      isOpen,
      label,
      hasContent,
      isStreaming,
      ...props
    }: React.ButtonHTMLAttributes<HTMLButtonElement> & {
      isOpen?: boolean;
      label?: string;
      hasContent?: boolean;
      isStreaming?: boolean;
    }) {
      return (
        <button
          className="flex w-full items-center gap-2 px-3 py-2 text-sm font-medium"
          {...props}
        >
          {isStreaming ? "🧠" : "💡"}
          <span>{label}</span>
          {hasContent && (
            <span className="ml-auto text-xs">{isOpen ? "Hide" : "Show"}</span>
          )}
        </button>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { header: CustomHeader },
      }}
    />

### Custom Content#

Replace the content area to change how reasoning text is displayed:

Prop| Type| Description  
---|---|---  
`isStreaming`| `boolean`| Whether reasoning tokens are still arriving  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`children`| `string`| The raw reasoning text  
      
    
    function CustomContent({
      isStreaming,
      hasContent,
      children,
      ...props
    }: React.HTMLAttributes<HTMLDivElement> & {
      isStreaming?: boolean;
      hasContent?: boolean;
    }) {
      if (!hasContent && !isStreaming) return null;
    
      return (
        <div className="px-4 pb-3 text-sm text-gray-500 font-mono" {...props}>
          {children}
          {isStreaming && <span className="animate-pulse ml-1">▊</span>}
        </div>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { contentView: CustomContent },
      }}
    />

## Fully Custom Reasoning Message#

For complete control over the entire reasoning card, pass a **component** instead of slot props. Your component receives the same top-level props as the built-in one:

Prop| Type| Description  
---|---|---  
`message`| `ReasoningMessage`| The reasoning message object (`.content` holds the text)  
`messages`| `Message[]`| All messages in the conversation  
`isRunning`| `boolean`| Whether the agent is currently running  
  
DemoCode

reasoning_agent.py

page.tsx

reasoning-block.tsx

route.ts
    
    
    """Reasoning-capable Agno agent for the reasoning family of demos.Backs three showcase cells:    - reasoning-custom             (custom amber ReasoningBlock slot)    - reasoning-default            (CopilotKit's built-in reasoning card)    - tool-rendering-reasoning-chain (reasoning + sequential tool calls)Mirrors `showcase/integrations/langgraph-python/src/agents/reasoning_agent.py`(shared across the three reasoning demos there).Uses reasoning=False with a custom AGUI handler in agent_server.py thatemits REASONING_MESSAGE_* AG-UI events. The primary channel is Agno'snative `reasoning_content` (chat-completions stream a `delta.reasoning_content`field surfaced on each `RunContentEvent.reasoning_content`), tee'd into theAG-UI reasoning stream; parsing of <reasoning>...</reasoning> XML tags in themodel output remains as a defensive fallback when the native channel is empty.Running with reasoning=False avoids Agno's multi-call CoT loop (which breaksaimock fixtures) while still producing the proper AG-UI events thatCopilotKit's frontend renders via the reasoningMessage slot.For the reasoning-chain demo we also expose the same shared backend tools(`get_weather`, `search_flights`, `get_stock_price`, `roll_dice`) as theprimary agent so the catch-all tool renderer can observe a fullreasoning -> tool call -> reasoning -> tool call chain."""from __future__ import annotationsimport jsonfrom agno.agent.agent import Agentfrom agno.models.openai import OpenAIChatfrom agno.tools import toolfrom dotenv import load_dotenvfrom tools import (    get_weather_impl,    search_flights_impl,)from tools.types import Flightload_dotenv()@tooldef get_weather(location: str):    """    Get the weather for a given location. Ensure location is fully spelled out.    Args:        location (str): The location to get the weather for.    Returns:        str: Weather data as JSON.    """    return json.dumps(get_weather_impl(location))@tooldef search_flights(flights: list[dict]):    """    Search for flights and display the results as rich A2UI cards.    Return exactly 2 flights.    Args:        flights (list[dict]): List of flight objects to display.    Returns:        str: A2UI operations as JSON.    """    typed_flights = [Flight(**f) for f in flights]    result = search_flights_impl(typed_flights)    return json.dumps(result)@tooldef get_stock_price(ticker: str):    """    Get a mock current price for a stock ticker.    Args:        ticker (str): The ticker symbol to look up.    Returns:        str: Mock price data as JSON.    """    from random import choice, randint    return json.dumps(        {            "ticker": ticker.upper(),            "price_usd": round(100 + randint(0, 400) + randint(0, 99) / 100, 2),            "change_pct": round(choice([-1, 1]) * (randint(0, 300) / 100), 2),        }    )@tooldef roll_dice(sides: int = 6):    """    Roll a single die with the given number of sides.    Args:        sides (int): The number of sides on the die. Defaults to 6.    Returns:        str: Dice roll result as JSON.    """    from random import randint    return json.dumps({"sides": sides, "result": randint(1, max(2, sides))})# NOTE: reasoning=False (the default) is used here intentionally.## Agno's reasoning=True triggers a multi-call Chain-of-Thought loop that# makes up to `reasoning_max_steps` sequential LLM calls. This breaks in# proxy/fixture environments (aimock, D5 probes) where only the first# call matches a fixture — subsequent calls don't match and either fall# through to the real API (slow, non-deterministic) or fail entirely.## Instead, the custom AGUI handler in agent_server.py synthesizes# REASONING_MESSAGE_* AG-UI events from the agent's response text. The# system prompt instructs the model to prefix its answer with a reasoning# block delimited by <reasoning>...</reasoning> tags. The custom handler# parses those tags and emits proper AG-UI reasoning events that# CopilotKit's frontend renders via the reasoningMessage slot.## This approach:#   - Works with aimock (single LLM call)#   - Emits proper AG-UI REASONING_MESSAGE_* events (unlike Agno's stock#     AGUI handler which only emits STEP_STARTED/STEP_FINISHED)#   - Keeps the demo visually identical to native reasoning modelsagent = Agent(    model=OpenAIChat(id="gpt-4o-mini", timeout=120),    tools=[get_weather, search_flights, get_stock_price, roll_dice],    reasoning=False,    tool_call_limit=10,    description=(        "You are a helpful assistant. For each user question, first think "        "step-by-step about the approach, then answer concisely. When the "        "question calls for a tool, call it explicitly rather than guessing."    ),    instructions="""        REASONING STYLE:        Always begin your response with a reasoning block wrapped in        <reasoning>...</reasoning> XML tags. Inside the tags, think        step-by-step (two to four short steps is plenty). After the closing        tag, give your concise final answer. Example:        <reasoning>        Step 1: Identify what the user is asking.        Step 2: Consider which tool to use.        Step 3: Formulate the answer.        </reasoning>        Here is my answer...        TOOLS (reasoning-chain cell):        - get_weather: use when the user asks about weather.        - search_flights: use when the user asks about flights. Generate 2          realistic flights. Flight shape: airline, airlineLogo (Google          favicon URL), flightNumber, origin, destination, date          ("Tue, Mar 18"), departureTime, arrivalTime, duration ("4h 25m"),          status ("On Time"|"Delayed"), statusColor (hex), price ("$289"),          currency ("USD").        - get_stock_price: use when the user asks about a ticker. Consider          fetching a second related ticker for comparison.        - roll_dice: use when the user asks to roll a die. Consider rolling          twice with different numbers of sides.    """,)

The `ReasoningBlock` used above renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone:

page.tsx
    
    
    const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}

## Render-Prop Children#

The built-in `CopilotChatReasoningMessage` also supports a **render-prop** pattern for cases where you want to rearrange the built-in sub-components without reimplementing them:
    
    
    import {
      CopilotChatReasoningMessage,
    } from "@copilotkit/react-core/v2";
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function MyReasoningLayout(props: React.ComponentProps<typeof CopilotChatReasoningMessage>) {
      return (
        <CopilotChatReasoningMessage {...props}>
          {({ header, toggle }) => (
            <div className="rounded-lg border bg-yellow-50 my-2">
              {header}
              {toggle}
            </div>
          )}
        </CopilotChatReasoningMessage>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: MyReasoningLayout,
      }}
    />

The render-prop callback receives:

Property| Description  
---|---  
`header`| Pre-rendered header element  
`contentView`| Pre-rendered content element  
`toggle`| Pre-rendered expand/collapse wrapper (contains `contentView`)  
`message`| The reasoning message object  
`messages`| All messages  
`isRunning`| Whether the agent is running  
  
### On this page

Default BehaviorCustomizing the Reasoning MessageCustom HeaderCustom ContentFully Custom Reasoning MessageRender-Prop Children
