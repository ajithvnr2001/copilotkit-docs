---
url: https://docs.copilotkit.ai/mastra/generative-ui/a2ui/
title: A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:26.603068+00:00
---

# A2UI

> Source: https://docs.copilotkit.ai/mastra/generative-ui/a2ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/mastra/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/mastra/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/mastra/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/mastra/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/mastra/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

A2UI

Generative UIDeclarativeA2UI

# A2UI

Render declarative UI components using the A2UI specification.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# A2UI - Google's Generative UI Spec

**A2UI** is Google's declarative, LLM-friendly Generative UI specification that enables agents to generate dynamic user interfaces.

![Generative UI Specs](https://docs.copilotkit.ai/images/gen-ui-specs-light.webp)![Generative UI Specs](https://docs.copilotkit.ai/images/gen-ui-specs-dark.webp)

## What is A2UI?#

A2UI is a declarative generative UI specification launched by Google. It's designed to be:

  * **JSONL-based** \- Uses JSON Lines format for streaming
  * **LLM-friendly** \- Easy for language models to generate
  * **Platform-agnostic** \- Can be rendered on any platform
  * **Streaming-first** \- Built for real-time, progressive rendering



## Why A2UI?#

### Declarative Approach#

A2UI allows agents to describe UI components declaratively, making it easier for LLMs to generate dynamic interfaces without needing to understand implementation details.

### Streaming Support#

Built with streaming in mind, A2UI enables progressive rendering as the agent generates responses, providing a better user experience.

### Platform Agnostic#

A2UI specifications can be rendered on web, mobile, or any other platform, making your agent's UI truly universal.

## Setup with CopilotKit#

### Backend#

Enable A2UI in `CopilotRuntime` by passing `a2ui: {}`:

app/api/copilotkit/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: {},
    });
    
    // Single-route: only POST needed, no catch-all [...path] required
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    export { handler as POST };

This automatically applies `A2UIMiddleware` to all registered agents. To scope it to specific agents, you can specify agents with the `agents` property: `a2ui: { agents: ["my-agent"] }`.

Both halves of this page are v2 entry points: `@copilotkit/runtime/v2` on the server, `@copilotkit/react-core/v2` in the browser. If you are on the legacy `@copilotkit/runtime` root import with `copilotRuntimeNextJSAppRouterEndpoint`, A2UI still works — that class forwards `a2ui` straight to the v2 runtime — but the v2 handler is the current API, and our own showcase integrations moved to it (#6618). See [Deploy to any runtime](https://docs.copilotkit.ai/mastra/runtime-server-adapter) for the other hosts.

Once configured, any A2UI output returned from your agent will automatically be rendered in the chat interface — no additional frontend code required.

### Frontend#

The A2UI renderer activates automatically — no extra configuration needed on the frontend. Optionally, pass a custom theme:
    
    
    import { CopilotKit, type A2UITheme } from "@copilotkit/react-core/v2";
    
    // Your own theme object — the renderer reads the keys it understands.
    // Leave the `a2ui` prop off entirely to keep the built-in theme.
    const myCustomTheme: A2UITheme = {
      // ...your theme keys
    };
    
    <CopilotKit runtimeUrl="/api/copilotkit" a2ui={{ theme: myCustomTheme }}>
      {children}
    </CopilotKit>;

The `a2ui` prop on `<CopilotKit>` is only needed if you want to override the default theme provided.

## Using A2UI with CopilotKit#

[Get started with A2UI](https://docs.copilotkit.ai/docs/integrations/a2a/generative-ui/declarative-a2ui) and A2A with CopilotKit

Check out the [A2UI Composer](https://a2ui-editor.ag-ui.com/gallery) to create and find widgets

## Learn More#

  * [Generative UI Specs Overview](https://docs.copilotkit.ai/mastra/concepts/generative-ui-overview) \- Compare all supported specifications
  * [Generative UI Guide](https://docs.copilotkit.ai/mastra/generative-ui/tool-based) \- Build with Generative UI in CopilotKit
  * [A2UI Site](https://a2ui.org/) \- Visit the A2UI site
  * [AG-UI Protocol](https://docs.copilotkit.ai/mastra/agentic-protocols/ag-ui) \- Learn about the protocol that supports A2UI
  * [MCP Apps](https://docs.copilotkit.ai/mastra/generative-ui/mcp-apps) \- Iframe-based Generative UI extending MCP



### On this page

What is A2UI?Why A2UI?Declarative ApproachStreaming SupportPlatform AgnosticSetup with CopilotKitBackendFrontendUsing A2UI with CopilotKitLearn More
