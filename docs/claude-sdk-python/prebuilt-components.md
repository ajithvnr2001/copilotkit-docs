---
url: https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:44.375803+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/

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

[Claude Agent SDK (Python)](https://docs.copilotkit.ai/claude-sdk-python)

# Prebuilt Components

Drop-in chat components with a full customization ladder, from pure CSS to fully headless.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

chat-component.snippet.tsx

suggestions.ts
    
    
    "use client";import React from "react";import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";import { useAgenticChatSuggestions } from "./suggestions";export default function AgenticChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>  );}function Chat() {  useAgenticChatSuggestions();  return <CopilotChat agentId="agentic_chat" />;}

[Want users to resume conversations across sessions?Persistent threads ship with CopilotKit Intelligence. Try it for free.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_prebuilt_components&utm_frontend=react&utm_backend=claude-sdk-python)

## Pre-built components for agentic chat#

CopilotKit ships three prebuilt chat surfaces that connect directly to your agent: [**CopilotChat**](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/chat), [**CopilotSidebar**](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/sidebar), and [**CopilotPopup**](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/popup). Each is a wrapper around the same primitives with a different layout. Pick the one that fits your app; they all handle streaming, generative UI, and deep customization.

If your chat surface needs saved conversations, history, or thread switching, drop in the [**Threads Drawer**](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/copilot-threads-drawer) next to any of them — or build your own switcher with [Headless Threads](https://docs.copilotkit.ai/claude-sdk-python/headless-threads).

## The customization ladder#

One of CopilotKit's design principles is that **you should never have to throw the prebuilt UI away** to get the look you want. Start at the top of this ladder and step down only when you need more control.

[Level 1 · EasiestDrop in as-isRender `<CopilotChat>`, `<CopilotSidebar>`, or `<CopilotPopup>` and ship. Streaming, tool calls, generative UI, and suggestions, all wired up.](https://docs.copilotkit.ai/prebuilt-components/chat)[Level 2 · Re-skinCustomize with CSSOverride theme tokens (`--copilot-kit-primary-color`, etc.) or target `.copilotKit...` classes. Keep every feature, change every color.](https://docs.copilotkit.ai/custom-look-and-feel/css)[Level 3 · RecomposeCustomize via slots (subcomponents)Swap the welcome screen, message bubble, composer, disclaimer, header, or toggle button with your own React component. Recursive; drill down as deep as you want.](https://docs.copilotkit.ai/custom-look-and-feel/slots)[Level 4 · Full controlGo fully headlessCompose your own chat from the low-level hooks (`useAgent`, `useCopilotKit`, `useRenderToolCall`). Any layout, any design system, or even non-chat surfaces.](https://docs.copilotkit.ai/custom-look-and-feel/headless-ui)

Everything below Level 1 is incremental: you can freely mix CSS variables, a custom welcome slot, and headless tool-call renderers in the same app. Nothing forces you to throw work away as your needs grow.

## Drop-in chat in a few lines#

Wrap your app in `<CopilotKit>` and drop `<CopilotChat>` where the chat should live. The provider wires the runtime, the session, and the agent registry. Everything else is optional configuration:

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

## Starter suggestions#

`useConfigureSuggestions` lets you seed the chat with contextual prompts the moment a user arrives. The example below uses a single "Write a sonnet" suggestion:

suggestions.ts
    
    
    export function useAgenticChatSuggestions() {  useConfigureSuggestions({    suggestions: [      { title: "Write a sonnet", message: "Write a short sonnet about AI." },      {        title: "Tell me a joke",        message: "Tell me a one-line joke.",      },      {        title: "Is 17 prime?",        message: "Walk me through whether 17 is prime.",      },    ],    available: "always",  });}

## Pick a surface#

Each surface is a drop-in component with the same underlying primitives, differing only in layout.

  * [`<CopilotChat>`](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/chat): inline chat pane you can place anywhere and size to fit.
  * [`<CopilotSidebar>`](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/sidebar): collapsible sidebar docked to the edge of your app.
  * [`<CopilotPopup>`](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/popup): floating bubble that overlays your page content.



Add a conversation-history sidebar next to any of these with [Threads Drawer](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/copilot-threads-drawer) — a drop-in thread switcher with no active-thread wiring.

Need to open/close the chat from your own button, or capture thumbs-up/down feedback? See [Open, close, and feedback](https://docs.copilotkit.ai/claude-sdk-python/prebuilt-components/chat-controls).
