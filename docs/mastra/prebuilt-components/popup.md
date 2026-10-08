---
url: https://docs.copilotkit.ai/mastra/prebuilt-components/popup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:54.495822+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/mastra/prebuilt-components/popup/

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

On this page

[Mastra](https://docs.copilotkit.ai/mastra)[Prebuilt Components](https://docs.copilotkit.ai/mastra/prebuilt-components)

# CopilotPopup

Floating chat bubble that toggles open an overlay chat window.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

route.ts
    
    
    "use client";import React from "react";import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";import { MainContent } from "./main-content";import { Suggestions } from "./suggestions-mount";export default function PrebuiltPopupDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-popup">      <MainContent />      <CopilotPopup        agentId="prebuilt-popup"        defaultOpen={true}        labels={{          chatInputPlaceholder: "Ask the popup anything...",        }}      />      <Suggestions />    </CopilotKit>  );}

## What is this?#

`<CopilotPopup>` is a prebuilt floating launcher that opens an overlay chat window on top of your page content. It's the lightest-weight way to add a copilot to an existing app. Drop it in once and a bubble appears in the corner ready to chat.

## When should I use this?#

Use the popup when you want:

  * A minimal-footprint copilot that overlays existing content on demand
  * A launcher you can place on top of any page without reflowing the layout
  * A quick assistant bubble that users open for short, task-focused chats



If you need chat to live alongside your content rather than on top of it, use [CopilotSidebar](https://docs.copilotkit.ai/mastra/prebuilt-components/sidebar). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/mastra/prebuilt-components/chat) directly.

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotPopup>` as a sibling of your main content. The example below opens the popup by default and customizes the input placeholder via `labels`:
    
    
    import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotPopup`. That one is the [deprecated v1 popup](https://docs.copilotkit.ai/mastra/migrate/v2). This page documents the v2 popup, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-popup">      <MainContent />      <CopilotPopup        agentId="prebuilt-popup"        defaultOpen={true}        labels={{          chatInputPlaceholder: "Ask the popup anything...",        }}      />      <Suggestions />    </CopilotKit>

## Configuring the popup#

`<CopilotPopup>` accepts the same props as `<CopilotChat>` plus a few of its own. Commonly used options:

Prop| Description  
---|---  
`defaultOpen`| Whether the popup starts open on first render.  
`agentId`| Agent slug the popup should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the popup header bar — see the [slot system](https://docs.copilotkit.ai/mastra/custom-look-and-feel/slots).  
`toggleButton`| Slot for the floating launcher button.  
  
## Styling#

`CopilotPopup` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/mastra/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the popupStyling
