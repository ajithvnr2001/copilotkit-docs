---
url: https://docs.copilotkit.ai/deepagents/prebuilt-components/sidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:54.538782+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/deepagents/prebuilt-components/sidebar/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Prebuilt Components

[CopilotChat](https://docs.copilotkit.ai/deepagents/prebuilt-components/chat)[CopilotSidebar](https://docs.copilotkit.ai/deepagents/prebuilt-components/sidebar)[CopilotPopup](https://docs.copilotkit.ai/deepagents/prebuilt-components/popup)[Open, close, and feedback](https://docs.copilotkit.ai/deepagents/prebuilt-components/chat-controls)

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/deepagents/multimodal-attachments)[Voice](https://docs.copilotkit.ai/deepagents/voice)[Reasoning](https://docs.copilotkit.ai/deepagents/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

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

CopilotSidebar

BasicsChatPrebuilt Components

# CopilotSidebar

Drop-in collapsible sidebar chat that wraps your main content.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`prebuilt-sidebar`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/prebuilt-components/sidebar), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/prebuilt-components/sidebar), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/sidebar).

## What is this?#

`<CopilotSidebar>` is a prebuilt chat surface that docks to the side of your app. It wraps your main content so the chat can slide out on demand, making it a good fit for in-app copilots that need to stay accessible without taking over the entire viewport.

## When should I use this?#

Use the sidebar when you want:

  * A persistent, collapsible chat attached to your app shell
  * Chat to live alongside your main content rather than on top of it
  * A launcher the user can toggle without losing their place



For a floating bubble that overlays content, see [CopilotPopup](https://docs.copilotkit.ai/deepagents/prebuilt-components/popup). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/deepagents/prebuilt-components/chat) directly. For saved conversations and switching between them, the sidebar hosts the [Threads Drawer](https://docs.copilotkit.ai/deepagents/prebuilt-components/copilot-threads-drawer).

## Basic setup#

Wrap your app in `<CopilotKit>` once (it wires the runtime, session, and agent registry) and drop `<CopilotSidebar>` alongside your main content. The sidebar renders as a sibling so it can slide out without reflowing your page:
    
    
    import { CopilotKit, CopilotSidebar } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotSidebar`. That one is the [deprecated v1 sidebar](https://docs.copilotkit.ai/deepagents/migrate/v2). This page documents the v2 sidebar, which you import from `@copilotkit/react-core/v2`.

Missing snippet

No demo found for `deepagents::prebuilt-sidebar`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

## Configuring the sidebar#

`<CopilotSidebar>` accepts the same props as `<CopilotChat>` plus a few of its own. The example below opens the sidebar by default and targets a named agent:

Missing snippet

No demo found for `deepagents::prebuilt-sidebar`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

Common sidebar-specific props:

Prop| Description  
---|---  
`defaultOpen`| Whether the sidebar starts open on first render.  
`agentId`| Agent slug the sidebar should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the sidebar header bar — see the [slot system](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots).  
`toggleButton`| Slot for the open/close launcher button.  
  
## Styling#

`CopilotSidebar` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the sidebarStyling
