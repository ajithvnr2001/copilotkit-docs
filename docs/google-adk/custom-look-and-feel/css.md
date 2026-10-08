---
url: https://docs.copilotkit.ai/google-adk/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:48.352351+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/google-adk/custom-look-and-feel/css/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/google-adk/multimodal-attachments)[Voice](https://docs.copilotkit.ai/google-adk/voice)[Reasoning](https://docs.copilotkit.ai/google-adk/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CSS Customization

BasicsChatCustom Look and Feel

# CSS Customization

Theme CopilotKit components via CSS variables and class overrides.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

shared_chat.py

page.tsx

theme.css

route.ts
    
    
    """Shared LlmAgent factories used across multiple demos.`build_simple_chat_agent` produces a plain Gemini chat agent with no backendtools — appropriate for any demo whose only customisation is on the frontend(prebuilt-sidebar, prebuilt-popup, chat-slots, chat-customization-css,headless-simple, headless-complete, voice, frontend-tools, agentic-chat).`build_thinking_chat_agent` uses Gemini 3.1 Flash-Lite with the thinking_configexposed so reasoning is streamed back as `thought` parts; the v2 React corerenders these via CopilotChatReasoningMessage.`get_model` returns a `Gemini` instance configured with the aimock proxyendpoint when `GOOGLE_GEMINI_BASE_URL` is set, or the default model stringotherwise. All agent modules should call `get_model()` instead ofhard-coding `"gemini-3.1-flash-lite"` so Railway deployments route throughaimock.`stop_on_terminal_text` is the canonical after_model_callback shared by everyregistered LlmAgent. Gemini 3.1 Flash-Lite does not naturally end its agenticloop after a successful tool call — it keeps re-issuing the same tool. Thecallback inspects each non-partial model response and, when it containstext with no pending function_call, sets `_invocation_context.end_invocation= True` so ADK terminates the loop. Without this guard every backend orfrontend tool in this package fires infinitely."""from __future__ import annotationsimport loggingimport osfrom typing import Optional, Unionfrom google.adk.agents import LlmAgentfrom google.adk.agents.callback_context import CallbackContextfrom google.adk.models.google_llm import Geminifrom google.adk.models.llm_response import LlmResponsefrom google.genai import typesfrom ag_ui_adk import AGUIToolsetfrom agents._header_forwarding import install_httpx_hooklogger = logging.getLogger(__name__)DEFAULT_MODEL = "gemini-3.1-flash-lite"def stop_on_terminal_text(    callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:    """Terminate the ADK agentic loop on a final text-only model turn.    Lifted from the (orphaned) `simple_after_model_modifier` in    `agents/main.py`, with the SalesPipelineAgent name-gate removed so it    applies to every registered agent. Guards:    1. Skip partial streaming events — never end on a mid-stream chunk       (belt-and-suspenders with `ADK_DISABLE_PROGRESSIVE_SSE_STREAMING=1`       in `entrypoint.sh`).    2. Only terminate when the final non-partial response contains TEXT       and NO pending function_call — mixed text+function_call responses       (a known Gemini Flash quirk) must NOT terminate.    3. `_invocation_context` is an ADK private attribute; if it disappears       in a future ADK release, log-and-degrade rather than crash the       callback (which would stall the request).    Without this guard, Gemini calls the same tool indefinitely after a    successful tool result because no native termination condition fires.    """    content = llm_response.content    if not content or not content.parts:        if llm_response.error_message:            logger.warning(                "stop_on_terminal_text: Gemini returned error_message for agent=%s: %s",                callback_context.agent_name,                llm_response.error_message,            )        return None    if getattr(llm_response, "partial", False):        return None    # Under thinking mode (`include_thoughts=True`), Gemini emits a turn    # as TWO separate non-partial chunks:    #   1. text-only chunk: thought + reply text, `finish_reason=None`    #   2. function_call-only chunk: `finish_reason=FUNCTION_CALL`    # The callback fires on both. Without the finish_reason guard below,    # chunk 1's text-without-function-call shape causes premature    # termination — the function call in chunk 2 still streams but the    # agentic loop is already marked `end_invocation=True`, so the    # post-tool-result re-invocation that would chain to the next tool    # never happens (tool-rendering-reasoning-chain AAPL→MSFT regression).    # Only terminate when Gemini signals the turn is genuinely done with    # `finish_reason=STOP` (no further chunks coming). FUNCTION_CALL and    # None mean "more chunks are inbound" — defer.    finish_reason = getattr(llm_response, "finish_reason", None)    finish_reason_name = (        getattr(finish_reason, "name", None) if finish_reason is not None else None    )    if finish_reason_name != "STOP" and finish_reason != "STOP":        return None    has_text = any(getattr(part, "text", None) for part in content.parts)    has_function_call = any(        getattr(part, "function_call", None) for part in content.parts    )    if content.role != "model" or not has_text or has_function_call:        return None    invocation_context = getattr(callback_context, "_invocation_context", None)    if invocation_context is None:        logger.debug(            "stop_on_terminal_text: callback_context has no "            "_invocation_context attribute; skipping end_invocation."        )        return None    try:        invocation_context.end_invocation = True    except AttributeError:        logger.debug(            "stop_on_terminal_text: _invocation_context lacks "            "end_invocation; ADK private-API shape may have drifted."        )    return Nonedef get_model(model: str = DEFAULT_MODEL) -> Union[str, Gemini]:    """Return a model suitable for LlmAgent's `model=` parameter.    When `GOOGLE_GEMINI_BASE_URL` is set (Railway aimock proxy), returns a    `Gemini` instance with its `base_url` pointed at the proxy. Otherwise    returns the plain model string so the ADK resolves the default endpoint.    """    base_url = os.environ.get("GOOGLE_GEMINI_BASE_URL")    if base_url:        gemini = Gemini(model=model, base_url=base_url)        # Walk Gemini's ``._client`` chain and attach the request hook so        # inbound x-* headers (e.g. ``x-aimock-context``) ride along on        # outbound calls to the aimock proxy.        install_httpx_hook(gemini)        return gemini    return modeldef get_a2ui_model(model: str = DEFAULT_MODEL) -> Gemini:    """Return a concrete ``Gemini`` BaseLlm for the A2UI sub-agent.    The middleware's ``get_a2ui_tool({"model": ...})`` invokes the model    directly (forced ``render_a2ui`` call), so it needs a model *object*, not    the bare string ``get_model`` may return for ``LlmAgent.model=``. This    mirrors ``get_model``'s aimock-proxy wiring (base_url + x-header hook) so    the sub-agent's Gemini calls route through the same proxy as the primary    agent and match the same aimock fixtures. (The auto-inject path got this    object for free from the agent's ``canonical_model``; backend-owned wiring    must resolve it explicitly.)    """    resolved = get_model(model)    if isinstance(resolved, Gemini):        return resolved    # No proxy: build a plain Gemini against the default endpoint.    return Gemini(model=model)def build_simple_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        after_model_callback=stop_on_terminal_text,    )def build_thinking_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    """LlmAgent with Gemini thinking enabled.    `include_thoughts=True` makes Gemini emit `thought=True` parts alongside    final answer parts; ADK forwards these through ag-ui as reasoning chunks    so v2's CopilotChatReasoningMessage / useRenderReasoning can show them.    `thinking_budget=-1` lets the model decide how much to think.    """    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        generate_content_config=types.GenerateContentConfig(            thinking_config=types.ThinkingConfig(                include_thoughts=True,                thinking_budget=-1,            ),        ),        after_model_callback=stop_on_terminal_text,    )

## What is this?#

CopilotKit has a variety of ways to customize the colors and structure of the Copilot UI components via plain CSS. You can:

  * Override CopilotKit CSS variables to re-tint the whole UI
  * Target the built-in class names (`.copilotKit...`) for structural tweaks
  * Swap fonts per surface (messages, input, bubbles)
  * Replace icons and labels via component props



If you need to change behavior, not just look, see [slots](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/slots) or [fully headless UI](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/headless-ui).

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
