---
url: https://docs.copilotkit.ai/langgraph-fastapi/migrate/ag-ui-1.0
title: Upgrade to AG-UI 1.0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:39.634114+00:00
---

# Upgrade to AG-UI 1.0

> Source: https://docs.copilotkit.ai/langgraph-fastapi/migrate/ag-ui-1.0

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)Migrate

# Upgrade to AG-UI 1.0

What changes for your app when CopilotKit moves to AG-UI 1.0

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit now uses AG-UI 1.0 (`@ag-ui/core`, `@ag-ui/client`, `@ag-ui/encoder` and `@ag-ui/proto` 1.0.0). Most apps need no change. This page lists what keeps working and what you can need to update.

For the protocol-level changes, read the AG-UI guide [Migrating to 1.0](https://docs.ag-ui.com/migrating-to-1-0).

## What keeps working#

  * **Agents built on AG-UI 0.x.** The 1.0 client translates the old event shapes. For example, `THINKING_*` events become `REASONING_*` events.
  * **Older CopilotKit frontends.** The runtime accepts requests from 0.x clients. This includes legacy `binary` attachment parts and the `null` values that 0.x sent for optional fields.
  * **Stored threads.** When a thread replays, CopilotKit translates 0.x history before it shows the messages.
  * **Validators.** `@copilotkit/react-core/v2` and `@copilotkit/vue` still export `EventSchemas`, `RunAgentInputSchema` and the other `*Schema` validators.
  * **An`HttpAgent` from your own `@ag-ui/client` copy.** CopilotKit still applies its headers to it.



## What you can need to change#

### If your app depends on `@ag-ui/*` packages directly#

Upgrade them to 1.0 at the same time as CopilotKit. If you keep 0.x types in your code, TypeScript can report that two `AbstractAgent` or `Message` types do not match.

### Tool results can be content parts#

`ToolMessage.content` and `TOOL_CALL_RESULT.content` are now `string | ContentPart[]`. If your code reads a tool result as a string, convert it first:
    
    
    import { contentToText } from "@ag-ui/client";
    
    const text = contentToText(toolMessage.content);

The `result` prop of a tool renderer is still a string. CopilotKit converts it for you.

### The finish reason moved into metadata#

`RUN_FINISHED` has no `finishReason` field in AG-UI 1.0. CopilotKit now sends it in `metadata`:
    
    
    agent.subscribe({
      onRunFinishedEvent: ({ event }) => {
        const finishReason = event.metadata?.finishReason;
      },
    });

### A stopped run finishes as cancelled#

When the user stops a run, a 1.0 client receives `RUN_FINISHED` with `outcome: { type: "cancelled" }`. Before, the event had no outcome, which means success. Do not show a cancelled run as a failure.

### Removed names#

AG-UI 1.0 removed these names, so CopilotKit no longer exports them:

Removed| Use instead  
---|---  
`THINKING_*` event types and their `Thinking*Event` types| `REASONING_*` events  
`BinaryInputContent`| `image`, `audio`, `video` and `document` parts with a `source`  
`SubAgentInfo`| `SubagentInfo`  
`BackwardCompatibility_0_0_47`| Not needed. The client translates old shapes by default.  
  
### Validators moved in `@ag-ui/client`#

`@ag-ui/client` no longer exports the zod validators. If you import them from `@ag-ui/client` directly, import them from `@ag-ui/core/schemas` instead. That subpath needs `zod` 3.25.18 or later, or `zod` 4.

### `RunAgentInput.tools` and `context` are required in TypeScript#

If you build a `RunAgentInput` in your own code, set `tools: []` and `context: []` when you have none. On the wire, a missing field still means an empty list.

### On this page

What keeps workingWhat you can need to changeIf your app depends on @ag-ui/* packages directlyTool results can be content partsThe finish reason moved into metadataA stopped run finishes as cancelledRemoved namesValidators moved in @ag-ui/clientRunAgentInput.tools and context are required in TypeScript
