---
url: https://docs.copilotkit.ai/angular/inspector/
title: Inspector
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:37.444062+00:00
---

# Inspector

> Source: https://docs.copilotkit.ai/angular/inspector/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Runtime

Deployment

Debugging

[Inspector](https://docs.copilotkit.ai/angular/inspector)

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Inspector

BackendRuntimeDebugging

# Inspector

The Inspector mounts itself in Angular applications. What changed, and what to remove if you mounted it by hand.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`@copilotkit/angular` mounts the Inspector for you. It depends on `@copilotkit/web-inspector` directly, so there is nothing to install and no version to pin — the `CopilotKit` service creates `cpk-web-inspector`, supplies your application's core, and appends it to `document.body` after the first browser render.

**[Inspector](https://docs.copilotkit.ai/angular/inspector)** is the page to read for what the panes show and how `enableInspector` controls visibility. Angular sets it through `provideCopilotKit`:

src/app/app.config.ts
    
    
    provideCopilotKit({
      runtimeUrl: "http://localhost:8200/api/copilotkit",
      enableInspector: false, // hide it during development
    });

Remove a hand-written mount before upgrading

`@copilotkit/angular` did not mount the Inspector before **0.4.0** , and this page previously described a `WebInspector` component that created the element by hand. If your application still has that component, delete it — along with its `<app-web-inspector />` usage and any direct `@copilotkit/web-inspector` dependency in `package.json`.

Leaving it in place is worse than redundant. The framework reuses an existing `cpk-web-inspector` rather than creating a second one, but the hand-written component's `DestroyRef.onDestroy` removes that element unconditionally — so a route change that destroys the component tears out the Inspector the framework is now driving, and it does not come back without a full reload.

## Production and server rendering#

Nothing to do for either.

The `@copilotkit/web-inspector` import is a dynamic `import()` inside the service, so the bundler splits it into its own chunk and a production build never requests it. Mounting runs in `afterNextRender` behind an `isPlatformBrowser` check, so the element is never created during a server render. Both matter, because the web component registers itself against `customElements`, which does not exist on the server.

## Position the launcher#

The launcher defaults to the top-right corner, and the element positions itself with an inline transform. Override both from your global stylesheet. A bottom-left corner keeps the launcher clear of the close button on a chat panel or sidebar:

src/styles.css
    
    
    cpk-web-inspector {
      /* The panel is draggable and sets an inline transform. Neutralize it before
         choosing a corner. */
      transform: none !important;
      top: auto !important;
      bottom: 1rem !important;
      left: 1rem !important;
      right: auto !important;
    }

## Next steps#

  * [Inspector](https://docs.copilotkit.ai/angular/inspector)
  * [Troubleshooting Angular apps](https://docs.copilotkit.ai/angular/guides/troubleshooting)
  * [AG-UI Event Inspector](https://docs.copilotkit.ai/angular/troubleshooting/event-inspector)
  * [Angular API: CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)



### On this page

Production and server renderingPosition the launcherNext steps
