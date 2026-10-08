---
url: https://docs.copilotkit.ai/google-adk/threads/
title: AG-UI Streams
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:39.774409+00:00
---

# AG-UI Streams

> Source: https://docs.copilotkit.ai/google-adk/threads/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Overview](https://docs.copilotkit.ai/google-adk/threads)[Bring your own thread system](https://docs.copilotkit.ai/google-adk/intelligence/bring-your-own-thread-system)[Add to Existing Threads](https://docs.copilotkit.ai/google-adk/threads-import)[Thread & History Lifecycle](https://docs.copilotkit.ai/google-adk/threads-lifecycle)[Streams & Framework Threads](https://docs.copilotkit.ai/google-adk/intelligence/threads-explained)

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Overview

IntelligenceFeaturesAG-UI Streams

# AG-UI Streams

Let users reconnect, catch up on missed events, and resume conversations across devices with Intelligence’s AG-UI streams.

CopilotKit Intelligence’s AG-UI streams carry the full interaction between your agent and your users. That includes messages, thinking traces, tool calls, generative UI, uploaded files (such as images, PDFs, and Excel files), and application state.

They’re designed to complement your existing thread storage, whether you use LangGraph, Google ADK, Mastra, or a custom backend. You can also use CopilotKit Intelligence as your standalone thread store.

![A support desk application with a Threads Drawer listing customer conversations beside CopilotChat case details for Northstar Analytics](https://docs.copilotkit.ai/images/threads/support-desk-threads.png)

Starting fresh?

Intelligence stores your conversation history and restores messages, generative UI, tool interactions, and multimodal inputs when users return.

Already have your own threading system?

Keep it. Intelligence records its own copy of your supported AG-UI interactions while your framework manages the original conversation and agent state. [Read more](https://docs.copilotkit.ai/google-adk/intelligence/bring-your-own-thread-system).

## Add AG-UI Streams to existing threads#

Already have threads in LangGraph, Google ADK, Mastra, or a custom backend and want them to work with CopilotKit? Keep your existing storage. Your framework manages the agent’s conversation, model context, and execution state; Intelligence adds the event history and delivery needed to restore the interactive conversation for your users.

Connect your existing CopilotKit app through the [Intelligence quickstart](https://docs.copilotkit.ai/google-adk/intelligence/quickstart) to add AG-UI delivery to future runs while your framework continues managing agent context and persistence. To include earlier conversations too, follow [Add AG-UI Streams to Existing Threads](https://docs.copilotkit.ai/threads-import) for the optional historical steps supported for ADK, LangGraph, and Mastra. Import is a one-time adoption step, not ongoing replication between databases.

CopilotKit Threads are separate from native framework session or checkpoint stores. Your backend can keep a stable mapping when the agent framework also needs its own conversation identifier.

ADK sessions

CopilotKit passes the active `threadId` to your ADK backend through AG-UI. Keep a stable mapping when you also use a durable ADK session service; CopilotKit thread lifecycle actions do not mutate the native ADK session store.

## Why use CopilotKit AG-UI Streams?#

Intelligence’s AG-UI streams add delivery capabilities around your existing agent and framework threads:

  * **Reconnect and catch up.** Reopen a conversation to replay recorded events and reconnect to an active run.
  * **Continue in the background.** An agent run can continue after the browser disconnects while your Runtime and agent remain running. This is not execution recovery after a server failure.
  * **Deliver across devices.** Users can reopen the same conversation on another device. Intelligence synchronizes thread metadata for connected clients; your application supplies a stable user identity.
  * **Separate user history from model context.** Intelligence records the AG-UI events delivered through it. Your framework’s model-context compaction and Intelligence’s event replay serve different purposes.
  * **Restore the interactive conversation.** Replay includes supported messages, generative UI, tool interactions, state, and multimodal inputs.



These are capabilities of CopilotKit Intelligence, not guarantees provided by the AG-UI protocol alone. Reopening or switching back to a conversation triggers replay and reconnection; see [connection behavior](https://docs.copilotkit.ai/google-adk/intelligence/threads-explained#websocket-disconnection).

## Start with your coding agent#

Copy this prompt into your coding agent to inspect your existing CopilotKit app and configure AG-UI Streams with CopilotKit Intelligence. Prefer to work through the setup yourself? Follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Set up AG-UI Streams manually#

Create a new CopilotKit app connected to cloud-hosted CopilotKit Intelligence. Your application and CopilotKit Runtime run locally while CopilotKit Intelligence records AG-UI events and delivers them to connected clients. If you already have a working app, follow the [Intelligence quickstart](https://docs.copilotkit.ai/google-adk/intelligence/quickstart#set-it-up-manually) to connect it instead.

### Create your app#

Run the interactive starter command:

Terminal
    
    
    npx copilotkit@latest init

### Connect CopilotKit Intelligence#

Complete browser sign-in, then create or select a CopilotKit Intelligence project when the CLI asks.

### Start your app and Runtime#

Start the generated application and Runtime with the command printed by the CLI. For the standard npm setup:

Terminal
    
    
    cd <project-directory>
    npm run dev

### Verify your first thread#

Use the included Threads Drawer to create a conversation. Reload the page or reopen the conversation and confirm that its complete history returns.

### See it in Inspector#

Open Inspector on localhost and inspect your conversation under the **Rich Threads** pane. Real threads appear when Intelligence is on. Enable Intelligence appears when it is off. Open a real thread and use **Try from here** to copy it into a Playground scratch session. The stored thread does not change.

More detail: [Inspector](https://docs.copilotkit.ai/google-adk/inspector).

Threads-capable CLI starters already include [Threads Drawer](https://docs.copilotkit.ai/google-adk/prebuilt-components/copilot-threads-drawer). Use its guide when you are ready to customize the drawer. Choose [Headless Threads](https://docs.copilotkit.ai/google-adk/headless-threads) later if your product needs a fully custom thread UI.

### Production self-hosting: Run CopilotKit Intelligence in your own infrastructure#

Production self-hosting keeps AG-UI Streams, durable event history, identity, storage, and operations inside your network, giving your organization control over data residency, security, and infrastructure. CopilotKit Engineering helps your team deploy CopilotKit Intelligence in your Kubernetes environment. [Book time with a CopilotKit engineer](https://copilotkit.ai/talk-to-an-engineer) to get started.

## How AG-UI Streams work#

Both UI paths use Intelligence’s AG-UI streams. A stable `threadId` connects the visible conversation to the runtime and its durable event history.

![A user starts a conversation on a laptop, leaves or switches devices, and returns to the same conversation on a phone.](https://docs.copilotkit.ai/images/threads/threads-diagram-light.png)![A user starts a conversation on a laptop, leaves or switches devices, and returns to the same conversation on a phone.](https://docs.copilotkit.ai/images/threads/threads-diagram-dark.png)

  1. Your UI opens a conversation with a stable `threadId`.
  2. `CopilotRuntime` runs your agent and sends conversation events to CopilotKit Intelligence.
  3. When users return, CopilotKit Intelligence replays the stored history, reconnects any live run, and synchronizes thread metadata.



How are threads scoped to each user?

Your application authenticates its users, and `CopilotRuntime` resolves that verified identity on the server with `identifyUser`. CopilotKit Intelligence uses the stable user ID to scope thread lists and lifecycle actions. See [Scope AG-UI Streams to the signed-in user](https://docs.copilotkit.ai/google-adk/threads-lifecycle#scope-rich-threads-to-the-signed-in-user) for the Runtime contract and an implementation pattern.

### What CopilotKit handles#

CopilotKit handles| You control  
---|---  
Durable event storage and replay| Your agent's behavior and tools  
Replay-to-live stream reconnection| The conversation experience and layout  
Realtime thread metadata synchronization| Which thread actions your users can access  
Naming, pagination, archive, and delete semantics| Application authorization and permissions  
Runtime-to-platform event plumbing and thread locks| Mapping to native framework sessions when needed  
Cloud-hosted or self-hosted platform infrastructure| The deployment model that fits your organization  
  
Headless means custom UI, not custom infrastructure

Threads Drawer and Headless Threads use the same persistence, replay, synchronization, and locking infrastructure. Choose Headless Threads when you want to build the interface yourself, not when you want to rebuild the Threads backend.

## Choose how to build the UI#

Use Threads Drawer for a ready-made conversation list, or build your own with `useThreads`. Pass the selected `threadId` to your chat to load its history and receive new events.

### [Threads DrawerShip a mobile-friendly conversation sidebar with switching, new conversations, archive, delete, and pagination already wired to your chat.](https://docs.copilotkit.ai/google-adk/prebuilt-components/copilot-threads-drawer)### [Headless ThreadsBuild a custom layout, workflow, permission model, or thread action UI while CopilotKit continues to handle the backend.](https://docs.copilotkit.ai/google-adk/headless-threads)

For how Intelligence and framework persistence work together, see [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/google-adk/intelligence/threads-explained#how-threads-work-with-framework-storage).

## Next steps#

  * [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/google-adk/intelligence/threads-explained) — event replay, live reconnection, synchronization, locking, and lifecycle behavior.
  * [Cloud-hosted CopilotKit Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/managed-intelligence-platform) — create the project that stores your app's threads and runtime credentials.
  * [Self-host CopilotKit Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/self-hosting) — run the Threads platform in your Kubernetes environment with CopilotKit Engineering.
  * [useThreads reference](https://docs.copilotkit.ai/reference/hooks/useThreads) — parameters, lifecycle methods, pagination, and return types.



### On this page

Add AG-UI Streams to existing threadsWhy use CopilotKit AG-UI Streams?Start with your coding agentSet up AG-UI Streams manuallyProduction self-hosting: Run CopilotKit Intelligence in your own infrastructureHow AG-UI Streams workWhat CopilotKit handlesChoose how to build the UINext steps
