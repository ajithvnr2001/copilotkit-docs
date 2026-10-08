---
url: https://docs.copilotkit.ai/ag2/intelligence/bring-your-own-thread-system/
title: Bring your own thread system
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:17.855450+00:00
---

# Bring your own thread system

> Source: https://docs.copilotkit.ai/ag2/intelligence/bring-your-own-thread-system/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Overview](https://docs.copilotkit.ai/ag2/threads)[Bring your own thread system](https://docs.copilotkit.ai/ag2/intelligence/bring-your-own-thread-system)[Add to Existing Threads](https://docs.copilotkit.ai/ag2/threads-import)[Thread & History Lifecycle](https://docs.copilotkit.ai/ag2/threads-lifecycle)[Streams & Framework Threads](https://docs.copilotkit.ai/ag2/intelligence/threads-explained)

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Bring your own thread system

IntelligenceFeaturesAG-UI Streams

# Bring your own thread system

Keep your existing thread storage while Intelligence records a separate copy of your AG-UI interactions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Keep your existing thread system when you connect CopilotKit Intelligence. You do not need to replace your thread storage or move your agent state.

Your framework continues managing the original conversation and agent state. Intelligence automatically records its own copy of the supported AG-UI interaction history that passes through your connected CopilotKit runtime.

## How recording works#

Sending a message that starts an agent run through the connected runtime creates the Intelligence thread record if it does not exist. Intelligence then records the interaction under that thread ID. Selecting a thread ID or opening the chat alone does not record a conversation.

Recording covers traffic through that runtime after you connect Intelligence. Runs that bypass it do not appear automatically. Connecting Intelligence does not scan your framework database or copy all its older conversations. If the agent sends earlier messages during a new run, Intelligence can record those messages too.

## What Intelligence records#

Intelligence records the supported interaction data sent through the connected runtime:

  * Messages sent by the user and agent.
  * Tool calls, their arguments, and tool results.
  * Application state sent as AG-UI state events.
  * Supported UI content, such as generative UI and activity messages, sent as part of the interaction.



The copy contains what the integration sends through AG-UI. It is not a copy of your framework database, internal checkpoints, or arbitrary browser state. Restoring UI content also requires the matching renderers in your app.

## Older history and lifecycle actions#

To include older history, use the optional [supported import flow](https://docs.copilotkit.ai/ag2/threads-import) for LangGraph, ADK, or Mastra. Import copies the supported content that the source still exposes. Future runs record automatically without an import. Import does not keep the two databases in sync.

Intelligence rename, archive, and delete actions affect only Intelligence records. They do not rename, archive, or delete the original conversation in your native framework store. Neither automatic recording nor historical import keeps the two databases in sync.

## Example: keep an existing LangGraph conversation#

This example uses a React app with a LangGraph agent registered as `support` in the CopilotKit runtime. Its durable checkpointer or LangGraph deployment already stores a conversation. [Connect the runtime to Intelligence](https://docs.copilotkit.ai/ag2/intelligence/quickstart), then continue that conversation.

If you want to copy its earlier history, [import it first](https://docs.copilotkit.ai/langgraph-python/threads-import). Import cannot merge that history into a record already created by live recording. Otherwise, continue without importing:

  1. Keep the agent's native persistence configured. Intelligence records AG-UI interaction history while LangGraph continues saving its own conversation and graph state.

  2. Copy the native conversation's thread ID from your app. Pass that value to `CopilotChat` under your existing `CopilotKitProvider`.

For example, if the native thread ID is `550e8400-e29b-41d4-a716-446655440000`, render this component in your app:

SupportConversation.tsx
         
         "use client";
         
         import { CopilotChat } from "@copilotkit/react-core/v2";
         
         export function SupportConversation() {
           return (
             <CopilotChat
               agentId="support"
               threadId="550e8400-e29b-41d4-a716-446655440000"
             />
           );
         }

Use your runtime's registered agent ID and your conversation's actual thread ID. This example uses the same UUID in both systems. If your backend maps IDs instead, reuse the saved mapping on every run. LangGraph Platform requires UUID thread IDs. Do not generate a new ID or mapping when you reopen the conversation.

  3. Send a message through your app to run the agent. That run creates the Intelligence record if needed and records the supported interaction data. Opening the chat alone does not create the record or import old history.

  4. Open your runtime's project in [CopilotKit Intelligence](https://dashboard.operations.copilotkit.ai/) and find the thread by its ID. Make sure that it contains your new message and the agent's reply. On localhost, you can also find it in Inspector's Rich Threads pane.

  5. Reopen the chat with the same thread ID and send another message as the same application user. Make sure that Intelligence adds it to the same thread and LangGraph updates the same native conversation.




### On this page

How recording worksWhat Intelligence recordsOlder history and lifecycle actionsExample: keep an existing LangGraph conversation
