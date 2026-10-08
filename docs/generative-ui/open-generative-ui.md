---
url: https://docs.copilotkit.ai/generative-ui/open-generative-ui/
title: Open Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:07.849702+00:00
---

# Open Generative UI

> Source: https://docs.copilotkit.ai/generative-ui/open-generative-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/generative-ui/open-generative-ui)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

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

page.tsx

ogui-factory.ts

route.ts
    
    
    "use client";/** * Open-Ended Generative UI — minimal setup. * ----------------------------------------- * The simplest possible example. Enabling `openGenerativeUI` in the * runtime (see `src/app/api/copilotkit-ogui/route.ts`) is all that's * needed — the runtime middleware streams agent-authored HTML + CSS to * the built-in `OpenGenerativeUIActivityRenderer`, which mounts it * inside a sandboxed iframe. No custom sandbox functions, no custom * tools — just chat. * * This page customises the LLM's visual-authoring prompt via * `openGenerativeUI.designSkill` on the provider (see * `VISUALIZATION_DESIGN_SKILL` in `./design-skill.ts`) so the cell * showcases rich educational visualisations (3D axes, neural nets, * algorithms). * * Reference: https://docs.copilotkit.ai/generative-ui/open-generative-ui */import React from "react";import { CopilotKit } from "@copilotkit/react-core/v2";import { VISUALIZATION_DESIGN_SKILL } from "./design-skill";import { Chat } from "./chat";export default function OpenGenUiDemo() {  // Minimal Open Generative UI frontend: the built-in activity renderer is  // registered by CopilotKitProvider, so a plain <CopilotChat /> is enough —  // no custom tool renderers, no activity-renderer registration.  // We DO pass `openGenerativeUI.designSkill` to swap in visualisation-tuned  // guidance in place of the default shadcn design skill.  return (    <CopilotKit      runtimeUrl="/api/copilotkit-ogui"      agent="open-gen-ui"      openGenerativeUI={{ designSkill: VISUALIZATION_DESIGN_SKILL }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl flex flex-col p-3">          <Chat />        </div>      </div>    </CopilotKit>  );}

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
    
    
    const runtime = new CopilotRuntime({  agents: {    "open-gen-ui": createOguiAgent(),    "open-gen-ui-advanced": createOguiAgent(),  },  runner: new InMemoryAgentRunner(),  openGenerativeUI: {    agents: ["open-gen-ui", "open-gen-ui-advanced"],  },});

The `OpenGenerativeUIMiddleware` then converts the agent's streamed `generateSandboxedUi` tool call into `open-generative-ui` activity events, which the built-in `OpenGenerativeUIActivityRenderer` mounts inside a sandboxed iframe.

### Drop `<CopilotChat />` into the page#

Wrap your app in `CopilotKit` and render `<CopilotChat>` — no extra props needed:

page.tsx
    
    
      // Minimal Open Generative UI frontend: the built-in activity renderer is  // registered by CopilotKitProvider, so a plain <CopilotChat /> is enough —  // no custom tool renderers, no activity-renderer registration.  // We DO pass `openGenerativeUI.designSkill` to swap in visualisation-tuned  // guidance in place of the default shadcn design skill.  return (    <CopilotKit      runtimeUrl="/api/copilotkit-ogui"      agent="open-gen-ui"      openGenerativeUI={{ designSkill: VISUALIZATION_DESIGN_SKILL }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl flex flex-col p-3">          <Chat />        </div>      </div>    </CopilotKit>  );

That's it. Ask the agent "build me a simple greeting card" to see HTML stream into a sandboxed preview live.

## Advanced: With app tool calling#

Sandbox functions let the generated UI call back into your host application — a generated settings panel can toggle your app's theme, a product card can push items into your cart, or a data view can ask the host to fetch data the iframe can't reach directly.

DemoCode

page.tsx

sandbox-functions.ts

suggestions.ts

ogui-factory.ts

route.ts
    
    
    "use client";/** * Open-Ended Generative UI * ------------------------ * The agent streams ONE `generateSandboxedUi` tool call; the runtime's * `OpenGenerativeUIMiddleware` (enabled by `openGenerativeUI: { agents: [...] }` * in `api/copilotkit-ogui/route.ts`) converts that stream into * `open-generative-ui` activity events. Passing `openGenerativeUI` to * CopilotKit here activates the built-in `OpenGenerativeUIActivityRenderer`, * which mounts the agent-authored HTML + CSS inside a sandboxed iframe. * * Reference: https://docs.copilotkit.ai/generative-ui/open-generative-ui */import React from "react";import {  CopilotKit,  CopilotChat,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { openGenUiSandboxFunctions } from "./sandbox-functions";import { openGenUiSuggestions } from "./suggestions";export default function OpenGenUiAdvancedDemo() {  return (    // Pass the sandbox-function array on the `openGenerativeUI` provider prop.    // The built-in `OpenGenerativeUIActivityRenderer` wires these as callable    // remotes inside the agent-authored iframe.    <CopilotKit      runtimeUrl="/api/copilotkit-ogui"      agent="open-gen-ui-advanced"      openGenerativeUI={{ sandboxFunctions: openGenUiSandboxFunctions }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useConfigureSuggestions({    suggestions: openGenUiSuggestions,    available: "always",  });  return (    <div className="flex h-full w-full flex-col p-3">      <CopilotChat        agentId="open-gen-ui-advanced"        className="flex-1 rounded-2xl"      />    </div>  );}

### Runtime is unchanged#

The server-side flag is identical to the minimal cell; the advanced behaviour is a pure frontend addition.

route.ts
    
    
    const runtime = new CopilotRuntime({  agents: {    "open-gen-ui": createOguiAgent(),    "open-gen-ui-advanced": createOguiAgent(),  },  runner: new InMemoryAgentRunner(),  openGenerativeUI: {    agents: ["open-gen-ui", "open-gen-ui-advanced"],  },});

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

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/open-generative-ui).

### On this page

What is this?Minimal setupEnable it in the runtimeDrop <CopilotChat /> into the pageAdvanced: With app tool callingRuntime is unchangedRegister sandbox functions on the providerCommon use casesHow streaming worksUsing CDN libraries
