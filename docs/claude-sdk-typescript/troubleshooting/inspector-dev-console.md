---
url: https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/inspector-dev-console/
title: Inspector and dev console
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:55:33.869061+00:00
---

# Inspector and dev console

> Source: https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/inspector-dev-console/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-typescript)[Quickstart](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-typescript/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-typescript/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/channels)

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

[Common Copilot Issues](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/common-issues)[Error message reference](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/error-reference)[Error Debugging & Observability](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/error-debugging)[Inspector and dev console](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/inspector-dev-console)[Debug Mode](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/debug-mode)[AG-UI Event Inspector](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/event-inspector)[Hook Explorer](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/hook-explorer)

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Inspector and dev console

OtherTroubleshooting

# Inspector and dev console

Configure the CopilotKit Inspector in React, Vue, and Angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`enableInspector` controls the built-in Inspector in browser applications:

  * `true` or omitted: show it in development builds.
  * `false`: hide it in development builds.



The Inspector is never loaded or rendered in production builds or during server-side rendering. This safety guard cannot be overridden by an explicit `true`, and development hostnames are unrestricted.

## React v2#
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="/api/copilotkit" enableInspector={false}>
      {children}
    </CopilotKit>;

Legacy `showDevConsole` values no longer control the Inspector. Use `enableInspector` for Inspector visibility.

## Vue#
    
    
    <CopilotKitProvider runtime-url="/api/copilotkit" :enable-inspector="false">
      <App />
    </CopilotKitProvider>

Vue's deprecated `showDevConsole` prop no longer controls the Inspector.

## Angular#
    
    
    provideCopilotKit({
      runtimeUrl: "/api/copilotkit",
      enableInspector: false,
    });

Angular has no `showDevConsole` alias. Configure the Inspector through `enableInspector` on `CopilotKitConfig`.

## React v1#

The v1 compatibility component follows the same development-only `enableInspector` behavior. Its deprecated `showDevConsole?: boolean` prop controls error toasts and banners, not the Inspector.

The Inspector cannot be enabled in a production build. Use a development build when debugging a deployed or remote environment.

## React Native#

Native iOS and Android applications do not have a built-in Inspector yet. The current Inspector is a DOM web component and is not included in the React Native dependency graph.

## Related#

  * [Inspector](https://docs.copilotkit.ai/claude-sdk-typescript/inspector): what the Inspector shows and how to use it.
  * [Error Debugging](https://docs.copilotkit.ai/claude-sdk-typescript/troubleshooting/error-debugging): the error console and the programmatic `onError` callback.
  * [Migrate to v2](https://docs.copilotkit.ai/claude-sdk-typescript/migrate/v2): the full React v1 to v2 migration guide.



### On this page

React v2VueAngularReact v1React NativeRelated
