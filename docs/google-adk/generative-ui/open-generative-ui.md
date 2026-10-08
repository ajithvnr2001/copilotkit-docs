---
url: https://docs.copilotkit.ai/google-adk/generative-ui/open-generative-ui/
title: Open Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:04.500302+00:00
---

# Open Generative UI

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/open-generative-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/google-adk/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/google-adk/generative-ui/open-generative-ui)

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

Open Generative UI

Generative UIOpen-ended

# Open Generative UI

Let agents generate fully interactive HTML/CSS/JS UIs that stream live into the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

open_gen_ui_agents.py

page.tsx

route.ts
    
    
    """Agents backing the Open-Ended Generative UI demos.
    
    Both variants ship the same backend behaviour — the agent emits raw HTML
    or component-tree JSON inside an iframe-rendered surface. The frontend
    sandboxes the output. The "advanced" variant additionally lets the
    generated UI invoke frontend sandbox functions; that's purely a frontend
    concern, the agent's job is identical.
    
    System prompts are ported verbatim from
    showcase/integrations/langgraph-python/src/agents/{open_gen_ui_agent,
    open_gen_ui_advanced_agent}.py so the generated HTML respects the same
    design-skill output contract and (for the advanced variant) the same
    sandbox-iframe restrictions and `Websandbox.connection.remote.*` calling
    convention as the LP reference.
    """
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from google.adk.agents import LlmAgent
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    # Ported verbatim from
    # showcase/integrations/langgraph-python/src/agents/open_gen_ui_agent.py
    # (SYSTEM_PROMPT). The frontend provider injects a detailed
    # VISUALIZATION_DESIGN_SKILL via `openGenerativeUI.designSkill`; the
    # agent's job is to lean on that skill and obey the output-order contract.
    _OPEN_GEN_UI_INSTRUCTION = """You are a UI-generating assistant for an Open Generative UI demo
    focused on intricate, educational visualisations (3D axes / rotations,
    neural-network activations, sorting-algorithm walkthroughs, Fourier
    series, wave interference, planetary orbits, etc.).
    
    On every user turn you MUST call the `generateSandboxedUi` frontend tool
    exactly once. Design a visually polished, self-contained HTML + CSS +
    SVG widget that *teaches* the requested concept.
    
    The frontend injects a detailed "design skill" as agent context
    describing the palette, typography, labelling, and motion conventions
    expected — follow it closely. Key invariants:
    - Use inline SVG (or <canvas>) for geometric content, not stacks of <div>s.
    - Every axis is labelled; every colour-coded series has a legend.
    - Prefer CSS @keyframes / transitions over setInterval; loop cyclical
      concepts with animation-iteration-count: infinite.
    - Motion must teach — animate the actual step of the concept, not decoration.
    - No fetch / XHR / localStorage — the sandbox has no same-origin access.
    
    Output order:
    - `initialHeight` (typically 480-560 for visualisations) first.
    - A short `placeholderMessages` array (2-3 lines describing the build).
    - `css` (complete).
    - `html` (streams live — keep it tidy). CDN <script> tags for Chart.js /
      D3 / etc. go inside the html.
    
    Keep your own chat message brief (1 sentence) — the real output is the
    rendered visualisation.
    """
    
    
    # Ported verbatim from
    # showcase/integrations/langgraph-python/src/agents/open_gen_ui_advanced_agent.py
    # (SYSTEM_PROMPT). The frontend wires host-side handlers as
    # `Websandbox.connection.remote.<name>(args)` — calling `window.sandbox.*`
    # (the prior ADK string) would never route to the host because the
    # OpenGenerativeUIActivityRenderer mounts handlers on the Websandbox
    # bridge, not on a `window.sandbox` global. The iframe also runs with
    # `sandbox="allow-scripts"` only, so `<form>` / `type="submit"` are
    # silently blocked — the explicit prohibition in the prompt is what
    # steers the LLM toward `addEventListener('click', ...)` and keydown
    # handlers instead.
    _OPEN_GEN_UI_ADVANCED_INSTRUCTION = """You are a UI-generating assistant for the Open Generative UI (Advanced) demo.
    
    On every user turn you MUST call the `generateSandboxedUi` frontend tool
    exactly once. The generated UI must be INTERACTIVE and must invoke the
    available host-side sandbox functions described in your agent context
    (delivered via `copilotkit.context`) in response to user interactions.
    
    Sandbox-function calling contract (inside the generated iframe):
    - Call a host function with:
          await Websandbox.connection.remote.<functionName>(args)
      The call returns a Promise; await it.
    - Each handler returns a plain object. Read the return shape from the
      function's description in your context and use the EXACT field names
      it returns (e.g. if the description says the handler returns
      `{ ok, value }`, read `res.value` — not `res.result`).
    - Descriptions, names, and JSON-schema parameter shapes for every
      available sandbox function are listed in your context. Read them
      carefully and wire at least one interactive UI element to call one.
    
    Sandbox iframe restrictions (CRITICAL):
    - The iframe runs with `sandbox="allow-scripts"` ONLY. Forms are NOT
      allowed. You MUST NOT use `<form>` elements or `<button type="submit">`.
      Clicking a submit button inside a sandboxed form is blocked by the
      browser BEFORE any onsubmit handler runs, so the sandbox-function call
      never fires.
    - Use plain `<button type="button">` elements and wire them with
      `addEventListener('click', ...)` or an inline click handler. Do the same
      for "Enter" keypresses on inputs: attach a `keydown` listener that
      checks `e.key === 'Enter'` and calls your handler directly — do NOT
      wrap inputs in a `<form>`.
    
    Generation guidance:
    - Emit `initialHeight` and `placeholderMessages` first, then CSS, then
      HTML, then `jsFunctions` / `jsExpressions` if helpful.
    - Always include a visible result element (e.g. an output div) that you
      UPDATE after the sandbox function resolves, so the user can *see* the
      round-trip: "Button clicked -> remote call -> visible result".
    - Use CDN scripts (Chart.js, D3, etc.) via <script> tags in the HTML head
      when you need libraries.
    - Do NOT use fetch/XHR, localStorage, or document.cookie — the sandbox has
      no same-origin access. ONLY use `Websandbox.connection.remote.*` for
      host-page interactions.
    - Keep your own chat message brief (1 sentence max); the rendered UI is
      the real output.
    """
    
    
    open_gen_ui_agent = LlmAgent(
        name="OpenGenUiAgent",
        model=get_model(),
        instruction=_OPEN_GEN_UI_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    open_gen_ui_advanced_agent = LlmAgent(
        name="OpenGenUiAdvancedAgent",
        model=get_model(),
        instruction=_OPEN_GEN_UI_ADVANCED_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    

## What is this?#

Open Generative UI lets the agent generate complete, sandboxed UI on the fly (HTML, CSS, and JavaScript) and stream it live into the chat. The user sees the interface build in real time: styles apply first, then HTML streams in progressively, and finally JavaScript expressions execute one by one.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

Key benefits:

  * **No predefined components** — the agent creates any UI it needs, on demand
  * **Live streaming** — HTML streams into a preview as it's generated
  * **CDN libraries** — the generated UI can load Chart.js, D3, Three.js, etc. via `<script>` tags
  * **Secure sandboxing** — content runs in an isolated iframe without same-origin access
  * **Sandbox functions** — optionally expose host functions to the generated UI for two-way communication



## Minimal setup#

Turning on Open Generative UI takes one flag in the runtime plus a plain `<CopilotChat />` on the frontend; the built-in activity renderer is auto-registered by `CopilotKit`, so no extra wiring is needed.

### Enable it in the runtime#

Add `OpenGenerativeUIMiddleware` to your runtime configuration:

route.ts
    
    
        const runtime = new CopilotRuntime({      agents: {        "open-gen-ui": new HttpAgent({          url: `${AGENT_URL}/open_gen_ui`,          headers,        }),        "open-gen-ui-advanced": new HttpAgent({          url: `${AGENT_URL}/open_gen_ui_advanced`,          headers,        }),      },      // The runtime's OpenGenerativeUIMiddleware turns each agent's streamed      // `generateSandboxedUi` tool call into `open-generative-ui` activity      // events that the provider's <CopilotKit openGenerativeUI={...}>      // renderer mounts in a sandboxed iframe. Without this list, the      // middleware never engages and the demo's iframe stays empty.      openGenerativeUI: {        agents: ["open-gen-ui", "open-gen-ui-advanced"],      },    });

The `OpenGenerativeUIMiddleware` then converts the agent's streamed `generateSandboxedUi` tool call into `open-generative-ui` activity events, which the built-in `OpenGenerativeUIActivityRenderer` mounts inside a sandboxed iframe.

### Drop `<CopilotChat />` into the page#

Wrap your app in `CopilotKit` and render `<CopilotChat>` — no extra props needed:

page.tsx
    
    
      // Minimal Open Generative UI frontend: the built-in activity renderer is  // registered by CopilotKitProvider, so a plain <CopilotChat /> is enough —  // no custom tool renderers, no activity-renderer registration.  // We DO pass `openGenerativeUI.designSkill` to swap in visualisation-tuned  // guidance in place of the default shadcn design skill.  return (    <CopilotKit      runtimeUrl="/api/copilotkit-ogui"      agent="open-gen-ui"      openGenerativeUI={{ designSkill: VISUALIZATION_DESIGN_SKILL }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl flex flex-col p-3">          <Chat />        </div>      </div>    </CopilotKit>  );

That's it. Ask the agent "build me a simple greeting card" to see HTML stream into a sandboxed preview live.

## Advanced: With app tool calling#

Sandbox functions let the generated UI call back into your host application — a generated settings panel can toggle your app's theme, a product card can push items into your cart, or a data view can ask the host to fetch data the iframe can't reach directly.

DemoCode

open_gen_ui_agents.py

page.tsx

route.ts
    
    
    """Agents backing the Open-Ended Generative UI demos.
    
    Both variants ship the same backend behaviour — the agent emits raw HTML
    or component-tree JSON inside an iframe-rendered surface. The frontend
    sandboxes the output. The "advanced" variant additionally lets the
    generated UI invoke frontend sandbox functions; that's purely a frontend
    concern, the agent's job is identical.
    
    System prompts are ported verbatim from
    showcase/integrations/langgraph-python/src/agents/{open_gen_ui_agent,
    open_gen_ui_advanced_agent}.py so the generated HTML respects the same
    design-skill output contract and (for the advanced variant) the same
    sandbox-iframe restrictions and `Websandbox.connection.remote.*` calling
    convention as the LP reference.
    """
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from google.adk.agents import LlmAgent
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    # Ported verbatim from
    # showcase/integrations/langgraph-python/src/agents/open_gen_ui_agent.py
    # (SYSTEM_PROMPT). The frontend provider injects a detailed
    # VISUALIZATION_DESIGN_SKILL via `openGenerativeUI.designSkill`; the
    # agent's job is to lean on that skill and obey the output-order contract.
    _OPEN_GEN_UI_INSTRUCTION = """You are a UI-generating assistant for an Open Generative UI demo
    focused on intricate, educational visualisations (3D axes / rotations,
    neural-network activations, sorting-algorithm walkthroughs, Fourier
    series, wave interference, planetary orbits, etc.).
    
    On every user turn you MUST call the `generateSandboxedUi` frontend tool
    exactly once. Design a visually polished, self-contained HTML + CSS +
    SVG widget that *teaches* the requested concept.
    
    The frontend injects a detailed "design skill" as agent context
    describing the palette, typography, labelling, and motion conventions
    expected — follow it closely. Key invariants:
    - Use inline SVG (or <canvas>) for geometric content, not stacks of <div>s.
    - Every axis is labelled; every colour-coded series has a legend.
    - Prefer CSS @keyframes / transitions over setInterval; loop cyclical
      concepts with animation-iteration-count: infinite.
    - Motion must teach — animate the actual step of the concept, not decoration.
    - No fetch / XHR / localStorage — the sandbox has no same-origin access.
    
    Output order:
    - `initialHeight` (typically 480-560 for visualisations) first.
    - A short `placeholderMessages` array (2-3 lines describing the build).
    - `css` (complete).
    - `html` (streams live — keep it tidy). CDN <script> tags for Chart.js /
      D3 / etc. go inside the html.
    
    Keep your own chat message brief (1 sentence) — the real output is the
    rendered visualisation.
    """
    
    
    # Ported verbatim from
    # showcase/integrations/langgraph-python/src/agents/open_gen_ui_advanced_agent.py
    # (SYSTEM_PROMPT). The frontend wires host-side handlers as
    # `Websandbox.connection.remote.<name>(args)` — calling `window.sandbox.*`
    # (the prior ADK string) would never route to the host because the
    # OpenGenerativeUIActivityRenderer mounts handlers on the Websandbox
    # bridge, not on a `window.sandbox` global. The iframe also runs with
    # `sandbox="allow-scripts"` only, so `<form>` / `type="submit"` are
    # silently blocked — the explicit prohibition in the prompt is what
    # steers the LLM toward `addEventListener('click', ...)` and keydown
    # handlers instead.
    _OPEN_GEN_UI_ADVANCED_INSTRUCTION = """You are a UI-generating assistant for the Open Generative UI (Advanced) demo.
    
    On every user turn you MUST call the `generateSandboxedUi` frontend tool
    exactly once. The generated UI must be INTERACTIVE and must invoke the
    available host-side sandbox functions described in your agent context
    (delivered via `copilotkit.context`) in response to user interactions.
    
    Sandbox-function calling contract (inside the generated iframe):
    - Call a host function with:
          await Websandbox.connection.remote.<functionName>(args)
      The call returns a Promise; await it.
    - Each handler returns a plain object. Read the return shape from the
      function's description in your context and use the EXACT field names
      it returns (e.g. if the description says the handler returns
      `{ ok, value }`, read `res.value` — not `res.result`).
    - Descriptions, names, and JSON-schema parameter shapes for every
      available sandbox function are listed in your context. Read them
      carefully and wire at least one interactive UI element to call one.
    
    Sandbox iframe restrictions (CRITICAL):
    - The iframe runs with `sandbox="allow-scripts"` ONLY. Forms are NOT
      allowed. You MUST NOT use `<form>` elements or `<button type="submit">`.
      Clicking a submit button inside a sandboxed form is blocked by the
      browser BEFORE any onsubmit handler runs, so the sandbox-function call
      never fires.
    - Use plain `<button type="button">` elements and wire them with
      `addEventListener('click', ...)` or an inline click handler. Do the same
      for "Enter" keypresses on inputs: attach a `keydown` listener that
      checks `e.key === 'Enter'` and calls your handler directly — do NOT
      wrap inputs in a `<form>`.
    
    Generation guidance:
    - Emit `initialHeight` and `placeholderMessages` first, then CSS, then
      HTML, then `jsFunctions` / `jsExpressions` if helpful.
    - Always include a visible result element (e.g. an output div) that you
      UPDATE after the sandbox function resolves, so the user can *see* the
      round-trip: "Button clicked -> remote call -> visible result".
    - Use CDN scripts (Chart.js, D3, etc.) via <script> tags in the HTML head
      when you need libraries.
    - Do NOT use fetch/XHR, localStorage, or document.cookie — the sandbox has
      no same-origin access. ONLY use `Websandbox.connection.remote.*` for
      host-page interactions.
    - Keep your own chat message brief (1 sentence max); the rendered UI is
      the real output.
    """
    
    
    open_gen_ui_agent = LlmAgent(
        name="OpenGenUiAgent",
        model=get_model(),
        instruction=_OPEN_GEN_UI_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    open_gen_ui_advanced_agent = LlmAgent(
        name="OpenGenUiAdvancedAgent",
        model=get_model(),
        instruction=_OPEN_GEN_UI_ADVANCED_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    

### Runtime is unchanged#

The server-side flag is identical to the minimal cell; the advanced behaviour is a pure frontend addition.

route.ts
    
    
        const runtime = new CopilotRuntime({      agents: {        "open-gen-ui": new HttpAgent({          url: `${AGENT_URL}/open_gen_ui`,          headers,        }),        "open-gen-ui-advanced": new HttpAgent({          url: `${AGENT_URL}/open_gen_ui_advanced`,          headers,        }),      },      // The runtime's OpenGenerativeUIMiddleware turns each agent's streamed      // `generateSandboxedUi` tool call into `open-generative-ui` activity      // events that the provider's <CopilotKit openGenerativeUI={...}>      // renderer mounts in a sandboxed iframe. Without this list, the      // middleware never engages and the demo's iframe stays empty.      openGenerativeUI: {        agents: ["open-gen-ui", "open-gen-ui-advanced"],      },    });

### Register sandbox functions on the provider#

Each sandbox function is a Zod-validated, host-side bridge the agent can invoke from inside the generated iframe via `Websandbox.connection.remote.<name>(args)`. The handler runs in the host page and its description is appended to the agent's context, so the agent knows which bridges are available when generating HTML/JS.

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { openGenUiSandboxFunctions } from "./sandbox-functions";import { openGenUiSuggestions } from "./suggestions";export default function OpenGenUiAdvancedDemo() {  return (    // Pass the sandbox-function array on the `openGenerativeUI` provider prop.    // The built-in `OpenGenerativeUIActivityRenderer` wires these as callable    // remotes inside the agent-authored iframe.    <CopilotKit      runtimeUrl="/api/copilotkit-ogui"      agent="open-gen-ui-advanced"      openGenerativeUI={{ sandboxFunctions: openGenUiSandboxFunctions }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>import { z } from "zod";/** * Host-side functions that agent-authored, sandboxed UIs can invoke from * inside the iframe via `Websandbox.connection.remote.<name>(args)`. * * The names, descriptions, and Zod-derived JSON schemas below are injected * into the agent's context so the LLM knows which bridges exist when it * generates HTML/JS. Each handler runs on the HOST page and its return * value is awaited by the in-iframe caller. * * Keep the surface small and obvious — these are the demo's "app-side * tools" that the sandbox-generated UI can call. */export const openGenUiSandboxFunctions = [  {    name: "evaluateExpression",    description:      "Safely evaluate a basic arithmetic expression on the host page and return the numeric result. " +      "Supports +, -, *, /, parentheses, and decimal numbers. " +      "Use this from inside a calculator or spreadsheet UI.",    parameters: z.object({      expression: z        .string()        .describe("An arithmetic expression, e.g. '12 * (3 + 4.5)'"),    }),    handler: async ({ expression }: { expression: string }) => {      // Evaluate only arithmetic-safe expressions. Reject anything with      // identifiers or suspicious characters so we never exec arbitrary JS.      if (!/^[\d+\-*/().\s]+$/.test(expression)) {        return { ok: false, error: "Unsupported characters in expression." };      }      try {        // eslint-disable-next-line no-new-func        const value = Function(`"use strict"; return (${expression});`)();        if (typeof value !== "number" || !Number.isFinite(value)) {          return { ok: false, error: "Not a finite number." };        }        // eslint-disable-next-line no-console        console.log(          "[open-gen-ui/advanced] evaluateExpression",          expression,          "=",          value,        );        return { ok: true, value };      } catch (err) {        return {          ok: false,          error: err instanceof Error ? err.message : String(err),        };      }    },  },  {    name: "notifyHost",    description:      "Send a short notification message from the sandboxed UI to the host page. " +      "The host logs the message and returns a confirmation object.",    parameters: z.object({      message: z.string().describe("A short status message."),    }),    handler: async ({ message }: { message: string }) => {      // eslint-disable-next-line no-console      console.log("[open-gen-ui/advanced] notifyHost:", message);      return { ok: true, receivedAt: new Date().toISOString(), message };    },  },];

How the sandbox calls you back

Inside the generated UI, the agent writes JS that calls `await Websandbox.connection.remote.notifyHost({ message: "hi" })`. The call is proxied back to the host page, where your `handler` runs with the validated args.

### Common use cases#

  * **Theme toggling** — generated UI controls your app's appearance
  * **Cart / state management** — product cards push items into host state
  * **Navigation** — generated UI triggers route changes in the host app
  * **Data fetching** — sandbox asks the host to fetch data the iframe can't reach directly



## How streaming works#

The agent generates the tool call's parameters in an order optimized for the user experience:

  1. **`placeholderMessages`** — shown immediately while generating
  2. **`css`** — all styles first; the preview starts once CSS is complete
  3. **`html`** — streams live into the preview as it's generated
  4. **`jsFunctions`** — reusable helpers injected before expressions
  5. **`jsExpressions`** — executed one by one; the user sees each take effect



The middleware parses the tool-call arguments incrementally and emits activity events as each parameter completes, so the preview updates progressively.

## Using CDN libraries#

The sandboxed iframe can load external libraries from CDNs; just include `<script>` or `<link>` tags in the generated HTML `<head>`. Chart.js, D3, Three.js, and any other CDN-hosted library work out of the box.
    
    
    <head>
      <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
      <canvas id="myChart"></canvas>
    </body>

### On this page

What is this?Minimal setupEnable it in the runtimeDrop <CopilotChat /> into the pageAdvanced: With app tool callingRuntime is unchangedRegister sandbox functions on the providerCommon use casesHow streaming worksUsing CDN libraries
