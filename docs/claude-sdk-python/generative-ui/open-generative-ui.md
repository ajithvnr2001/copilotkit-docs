---
url: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/open-generative-ui/
title: Open Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:23.177377+00:00
---

# Open Generative UI

> Source: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/open-generative-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/open-generative-ui)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

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

open_gen_ui_agent.py

page.tsx

route.ts
    
    
    """Claude Agent SDK backing the Open-Ended Generative UI (minimal) demo.The simplest possible example that exercises the open-ended generative UIpipeline. All the interesting work happens outside the agent:- CopilotKit merges the frontend-registered `generateSandboxedUi` tool  (auto-registered by `CopilotKitProvider` when the runtime has  `openGenerativeUI` enabled) into the agent's tool list. The LLM then  sees the tool via the normal AG-UI flow.- When the LLM calls `generateSandboxedUi`, the runtime's  `OpenGenerativeUIMiddleware` (enabled via `openGenerativeUI` on the  runtime — see `src/app/api/copilotkit-ogui/route.ts`) converts that  streaming tool call into `open-generative-ui` activity events that the  built-in renderer mounts inside a sandboxed iframe.This is the minimal variant: no sandbox functions, no app-side tools.The shared Claude backend in `src/agents/agent.py` handles this demovia the `open-gen-ui` agent name registered in the ogui route. Thismodule exists so the manifest's `highlight` path references a per-demoPython reference, mirroring the langgraph-python layout."""SYSTEM_PROMPT_HINT = (    "You are a UI-generating assistant for an Open Generative UI demo "    "focused on intricate, educational visualisations. On every user "    "turn you MUST call the `generateSandboxedUi` frontend tool exactly "    "once. Design a visually polished, self-contained HTML + CSS + SVG "    "widget that teaches the requested concept. Use inline SVG (or "    "<canvas>) for geometric content — no stacks of <div>s. Keep your "    "own chat message brief (1 sentence); the rendered visualisation is "    "the real output.")

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
    
    
          // Server-side config is identical for minimal and advanced cells —      // the advanced behaviour (sandbox -> host function calls) is wired      // entirely on the frontend via `openGenerativeUI.sandboxFunctions` on      // the provider. The single `openGenerativeUI` flag below turns on      // Open Generative UI for the listed agent(s); the runtime middleware      // converts each agent's streamed `generateSandboxedUi` tool call into      // `open-generative-ui` activity events.      runtime: new CopilotRuntime({        // @ts-ignore -- see main route.ts        agents,        openGenerativeUI: {          agents: ["open-gen-ui", "open-gen-ui-advanced"],        },      }),

The `OpenGenerativeUIMiddleware` then converts the agent's streamed `generateSandboxedUi` tool call into `open-generative-ui` activity events, which the built-in `OpenGenerativeUIActivityRenderer` mounts inside a sandboxed iframe.

### Drop `<CopilotChat />` into the page#

Wrap your app in `CopilotKit` and render `<CopilotChat>` — no extra props needed:

page.tsx
    
    
      // Minimal Open Generative UI frontend: the built-in activity renderer is  // registered by CopilotKitProvider, so a plain <CopilotChat /> is enough —  // no custom tool renderers, no activity-renderer registration.  // We DO pass `openGenerativeUI.designSkill` to swap in visualisation-tuned  // guidance in place of the default shadcn design skill.  return (    <CopilotKit      runtimeUrl="/api/copilotkit-ogui"      agent="open-gen-ui"      openGenerativeUI={{ designSkill: VISUALIZATION_DESIGN_SKILL }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl flex flex-col p-3">          <Chat />        </div>      </div>    </CopilotKit>  );

That's it. Ask the agent "build me a simple greeting card" to see HTML stream into a sandboxed preview live.

## Advanced: With app tool calling#

Sandbox functions let the generated UI call back into your host application — a generated settings panel can toggle your app's theme, a product card can push items into your cart, or a data view can ask the host to fetch data the iframe can't reach directly.

DemoCode

open_gen_ui_advanced_agent.py

page.tsx

sandbox-functions.ts

suggestions.ts

route.ts
    
    
    """Claude Agent SDK backing the Open-Ended Generative UI (Advanced) demo.This is the "advanced" variant of the Open Generative UI demo. The keydistinguishing feature: the agent-authored, sandboxed UI can invokefrontend-registered **sandbox functions** — functions the app defineson the host page (see `src/app/demos/open-gen-ui-advanced/sandbox-functions.ts`)and makes callable from inside the iframe via`await Websandbox.connection.remote.<name>(args)`.The shared Claude backend in `src/agents/agent.py` handles this demovia the `open-gen-ui-advanced` agent name registered in the ogui route.This module exists so the manifest's `highlight` path references aper-demo Python reference, mirroring the langgraph-python layout."""SYSTEM_PROMPT_HINT = (    "You are a UI-generating assistant for the Open Generative UI "    "(Advanced) demo. On every user turn you MUST call the "    "`generateSandboxedUi` frontend tool exactly once. The generated UI "    "must be INTERACTIVE and must invoke the available host-side sandbox "    "functions described in your agent context in response to user "    "interactions. Call host functions with "    "`await Websandbox.connection.remote.<functionName>(args)`. Do NOT "    "use <form> or type='submit' — the sandbox blocks form submissions; "    "use <button type='button'> wired with addEventListener('click').")

### Runtime is unchanged#

The server-side flag is identical to the minimal cell; the advanced behaviour is a pure frontend addition.

route.ts
    
    
          // Server-side config is identical for minimal and advanced cells —      // the advanced behaviour (sandbox -> host function calls) is wired      // entirely on the frontend via `openGenerativeUI.sandboxFunctions` on      // the provider. The single `openGenerativeUI` flag below turns on      // Open Generative UI for the listed agent(s); the runtime middleware      // converts each agent's streamed `generateSandboxedUi` tool call into      // `open-generative-ui` activity events.      runtime: new CopilotRuntime({        // @ts-ignore -- see main route.ts        agents,        openGenerativeUI: {          agents: ["open-gen-ui", "open-gen-ui-advanced"],        },      }),

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
