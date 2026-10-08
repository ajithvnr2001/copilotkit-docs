---
url: https://docs.copilotkit.ai/deepagents/generative-ui/open-generative-ui/
title: Open Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:04.642933+00:00
---

# Open Generative UI

> Source: https://docs.copilotkit.ai/deepagents/generative-ui/open-generative-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/deepagents/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/deepagents/generative-ui/open-generative-ui)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Open Generative UI

Generative UIOpen-ended

# Open Generative UI

Let agents generate fully interactive HTML/CSS/JS UIs that stream live into the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`open-gen-ui`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/generative-ui/open-generative-ui), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/open-generative-ui), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/open-generative-ui).

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

Missing snippet

No demo found for `deepagents::open-gen-ui`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

The `OpenGenerativeUIMiddleware` then converts the agent's streamed `generateSandboxedUi` tool call into `open-generative-ui` activity events, which the built-in `OpenGenerativeUIActivityRenderer` mounts inside a sandboxed iframe.

### Drop `<CopilotChat />` into the page#

Wrap your app in `CopilotKit` and render `<CopilotChat>` — no extra props needed:

Missing snippet

No demo found for `deepagents::open-gen-ui`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

That's it. Ask the agent "build me a simple greeting card" to see HTML stream into a sandboxed preview live.

## Advanced: With app tool calling#

Sandbox functions let the generated UI call back into your host application — a generated settings panel can toggle your app's theme, a product card can push items into your cart, or a data view can ask the host to fetch data the iframe can't reach directly.

### Runtime is unchanged#

The server-side flag is identical to the minimal cell; the advanced behaviour is a pure frontend addition.

Missing snippet

No demo found for `deepagents::open-gen-ui-advanced`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

### Register sandbox functions on the provider#

Each sandbox function is a Zod-validated, host-side bridge the agent can invoke from inside the generated iframe via `Websandbox.connection.remote.<name>(args)`. The handler runs in the host page and its description is appended to the agent's context, so the agent knows which bridges are available when generating HTML/JS.

Missing snippet

No demo found for `deepagents::open-gen-ui-advanced`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

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
