---
url: https://docs.copilotkit.ai/strands-typescript/vs-code-extension/
title: VS Code Extension
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:35.236232+00:00
---

# VS Code Extension

> Source: https://docs.copilotkit.ai/strands-typescript/vs-code-extension/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands-typescript/webmcp)

Agent capabilities

AWS Strands (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands-typescript/learning)

[User Memories](https://docs.copilotkit.ai/strands-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands-typescript/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

[Inspector](https://docs.copilotkit.ai/strands-typescript/inspector)[VS Code Extension](https://docs.copilotkit.ai/strands-typescript/vs-code-extension)

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/strands-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

VS Code Extension

BackendDebugging

# VS Code Extension

Preview supported CopilotKit UI sources, A2UI catalog components, and the AG-UI event stream without leaving VS Code.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The CopilotKit VS Code extension is a three-in-one workbench for iterating on CopilotKit features inside your editor. Install it once and you get three sidebars under the CopilotKit activity-bar icon:

  * **CopilotKit Hooks** — discover every `useCopilotAction`, `useRenderTool`, `useCoAgentStateRender`, etc. in your workspace, and live-preview their `render` components with auto-generated form controls.


  * **A2UI Catalog** — live preview of your A2UI catalog components with fixture-driven scenarios and hot-reload on save.
  * **AG-UI Inspector** — a real-time, color-coded, filterable stream of every AG-UI event your runtime emits.



The A2UI catalog preview runs without a localhost server, browser tab, or agent run. The AG-UI Inspector connects to a running development runtime.

## Install#

### Install the extension#

Open VS Code, go to Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`), search for **CopilotKit** , and click Install. Or from a terminal:
    
    
    code --install-extension copilotkit.copilotkit

### Open the CopilotKit activity bar#

Click the **CopilotKit icon** in the Activity Bar on the left edge of VS Code. Three sidebar views expand underneath it, in this order:

  1. **CopilotKit Hooks**
  2. **A2UI Catalog**
  3. **AG-UI Inspector**



Each is a self-contained tool — pick the one that matches what you're working on.

## Hook Explorer#

You have a file that calls `useCopilotAction`, `useRenderTool`, or any other render-capable CopilotKit hook, and you want to iterate on the `render` prop. The **CopilotKit Hooks** sidebar lists every call-site in your workspace; clicking one opens a live preview panel where the `render` output is driven by a form built from your hook's declared parameters.

Extra niceties:

  * A `▶️ Preview Component` CodeLens sits directly above every render-hook call in your editor — one click opens the preview for exactly that site.
  * A `</>` button on each sidebar row jumps to the source file.
  * Cross-file hook switches auto-recover — a forced render-prop crash in one hook doesn't strand the whole webview.



Full walkthrough, hook coverage table, and limitations: [Hook Explorer](https://docs.copilotkit.ai/strands-typescript/troubleshooting/hook-explorer).

## A2UI Catalog#

You have a file that exports an A2UI catalog via `createCatalog` (or imports `@copilotkit/a2ui-renderer`). The **A2UI Catalog** sidebar lists every catalog file in your workspace, plus any named fixtures you've defined alongside them. Clicking a component opens a live preview; edit the file and the preview updates on save while preserving interaction state.

### Find your catalog files#

Open the **A2UI Catalog** sidebar. Each row is a catalog file (discovered by scanning for `@copilotkit/a2ui-renderer` imports). Rows with fixture files expand to show named scenarios; rows without one get an `auto` badge and render with a default empty surface.

Hover any row to reveal a `</>` button that jumps to the source — on fixture rows, it jumps to the named fixture key inside the fixture file.

### Preview a component#

Click a component row to open the preview. If the component has fixtures, click the row to expand and pick a fixture — otherwise the click previews directly. Edit the file and save — the preview rebundles and re-renders automatically.

### Add fixtures#

Fixtures are named test-data scenarios. Create a fixture file next to your component:

JSONTypeScript

`MyComponent.fixture.json`:
    
    
    {
      "default": {
        "surfaceId": "preview",
        "messages": [
          { "beginRendering": { "surfaceId": "preview", "root": "root" } },
          { "surfaceUpdate": { "surfaceId": "preview", "components": [] } }
        ]
      },
      "empty state": {
        "surfaceId": "preview",
        "messages": []
      }
    }

`MyComponent.fixture.ts`:
    
    
    export default {
      "default": {
        surfaceId: "preview",
        messages: [
          { beginRendering: { surfaceId: "preview", root: "root" } },
          { surfaceUpdate: { surfaceId: "preview", components: [] } },
        ],
      },
      "empty state": {
        surfaceId: "preview",
        messages: [],
      },
    };

Each top-level key is a named fixture. Switch between them from the fixture dropdown inside the preview panel.

The extension validates fixture files on save and surfaces structural warnings (missing `surfaceId`, invalid `messages`, unknown component types) as in-editor diagnostics.

## AG-UI Inspector#

You're running a CopilotKit runtime and something in an agent interaction is off — a tool call isn't firing, a state delta is wrong, or the run ends before the UI settles. The **AG-UI Inspector** sidebar opens a dedicated SSE connection to `{runtimeUrl}/cpk-debug-events` and renders every event in a filterable, color-coded stream. Click any event row to expand the full JSON payload. That path is relative to the base path the runtime is mounted at, so give the panel the full runtime URL rather than just the origin.

Full walkthrough, event-type color reference, and production guard details: [AG-UI Event Inspector](https://docs.copilotkit.ai/strands-typescript/troubleshooting/event-inspector).

### On this page

InstallInstall the extensionOpen the CopilotKit activity barHook ExplorerA2UI CatalogFind your catalog filesPreview a componentAdd fixturesAG-UI Inspector
