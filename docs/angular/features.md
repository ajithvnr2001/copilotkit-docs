---
url: https://docs.copilotkit.ai/angular/features/
title: Angular feature examples
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:21.991308+00:00
---

# Angular feature examples

> Source: https://docs.copilotkit.ai/angular/features/

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

Debugging

Learn

Concepts

Angular guides

[Using the Angular docs](https://docs.copilotkit.ai/angular/using-these-docs)[Feature examples](https://docs.copilotkit.ai/angular/features)[Angular API reference](https://docs.copilotkit.ai/reference/angular)[Chat UI and customization](https://docs.copilotkit.ai/angular/guides/chat-ui)[Frontend tools and generative UI](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)[A2UI schemas, styling, and recovery](https://docs.copilotkit.ai/angular/guides/a2ui)[Voice and multimodal input](https://docs.copilotkit.ai/angular/guides/voice-multimodal)[Human-in-the-loop and interrupts](https://docs.copilotkit.ai/angular/guides/human-in-the-loop)[Shared state and agent context](https://docs.copilotkit.ai/angular/guides/shared-state)[Threads, memory, attachments, and headless UI](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless)[Troubleshooting Angular apps](https://docs.copilotkit.ai/angular/guides/troubleshooting)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

LearnAngular guides

# Angular feature examples

Browse examples, source, API docs, and support state for all 41 Angular features.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The catalog covers all 41 supported Angular features. Forty entries include a runnable example. Every entry links to its source and the closest API documentation.

## Shared setup#

Install `@copilotkit/angular` and the matching `@angular/cdk` major. Register the provider in your application config:

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [provideCopilotKit({ runtimeUrl: "/api/copilotkit" })],
    };

The source link opens the standalone Angular component used for that feature.

## A2UI Error Recovery

`a2ui-recovery`

Supported

Visible A2UI validate-retry recovery loop: an invalid render heals to a valid one, an always-invalid render shows a graceful recovery-exhausted fallback

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/a2ui-recovery)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/a2ui-recovery/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Agent Config Object

`agent-config`

Supported

Forwarded props / config objects

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/agent-config)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/agent-config/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Attachments

`multimodal`

Supported

File upload and agent processing

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/multimodal)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/multimodal/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Authentication

`auth`

Supported

Framework-native authentication

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/auth)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/auth/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Background Agents

`background-agents`

Supported

A long-running deep-research tool dispatched as a background task, surfaced inline as a live "working" activity card

[Run example](https://showcase.copilotkit.ai/angular/mastra/background-agents)[View source](https://showcase.copilotkit.ai/angular/mastra/background-agents/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Beautiful Chat

`beautiful-chat`

Supported

Canonical polished starter chat (same as /examples/integrations/langgraph-python)

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/beautiful-chat)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/beautiful-chat/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Browser Use

`browser-use`

Supported

The agent drives a real local headless browser to fetch pages and renders the results inline in chat

[Run example](https://showcase.copilotkit.ai/angular/mastra/browser-use)[View source](https://showcase.copilotkit.ai/angular/mastra/browser-use/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Chat Customization: CSS

`chat-customization-css`

Supported

Customizing chat components via CSS

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/chat-customization-css)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/chat-customization-css/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Chat Customization: Slots

`chat-slots`

Supported

Customizing chat components via the slot system

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/chat-slots)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/chat-slots/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Declarative UI: Dynamic A2UI

`declarative-gen-ui`

Supported

Canonical A2UI BYOC — custom catalog wired via a2ui.catalog

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/declarative-gen-ui)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/declarative-gen-ui/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Declarative UI: Fixed A2UI

`a2ui-fixed-schema`

Supported

A2UI rendering against a known, fixed client-side schema

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/a2ui-fixed-schema)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/a2ui-fixed-schema/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Frontend tools: async

`frontend-tools-async`

Supported

Register an async browser tool whose result returns to the agent.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/frontend-tools-async)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/frontend-tools-async/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)

## Frontend Tools: In-app Actions

`frontend-tools`

Supported

Frontend tool execution triggered by the agent

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/frontend-tools)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/frontend-tools/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)

## Generative UI: agent state

`gen-ui-agent`

Supported

Read live agent state with injectAgentStore and render it in the chat transcript.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/gen-ui-agent)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/gen-ui-agent/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Generative UI: component rendering

`gen-ui-tool-based`

Supported

Render typed tool results with registerFrontendTool and a standalone Angular component.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/gen-ui-tool-based)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/gen-ui-tool-based/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Generative UI: Rendering multiple tools

`tool-rendering-reasoning-chain`

Supported

Sequential tool calls with reasoning tokens rendered side-by-side

[Run example](https://showcase.copilotkit.ai/angular/langgraph-python/tool-rendering-reasoning-chain)[View source](https://showcase.copilotkit.ai/angular/langgraph-python/tool-rendering-reasoning-chain/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Generative UI: Tool Rendering (Custom default)

`tool-rendering-custom-catchall`

Supported

Single branded wildcard renderer that paints every tool call — one card handles them all

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/tool-rendering-custom-catchall)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/tool-rendering-custom-catchall/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Generative UI: Tool Rendering (Default)

`tool-rendering-default-catchall`

Supported

Out-of-the-box rendering: backend tools surfaced via CopilotKit's built-in default catch-all renderer; no frontend customization

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/tool-rendering-default-catchall)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/tool-rendering-default-catchall/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Generative UI: Tool Rendering (Specific)

`tool-rendering`

Supported

Custom per-tool renderers for the tools you care about, plus a wildcard catch-all for the rest

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/tool-rendering)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/tool-rendering/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Headless UI: Complete

`headless-complete`

Supported

Full headless UI with messages, tools, gen UI

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/headless-complete)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/headless-complete/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Headless UI: Simple

`headless-simple`

Supported

Simple headless UI getting started

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/headless-simple)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/headless-simple/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Human in the loop: headless interrupts

`interrupt-headless`

Supported

Resolve an agent interrupt with injectInterrupt from application UI outside the chat.

[Run example](https://showcase.copilotkit.ai/angular/mastra/interrupt-headless)[View source](https://showcase.copilotkit.ai/angular/mastra/interrupt-headless/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)

## Human in the loop: in app

`hitl-in-app`

Supported

Render approval UI outside chat and resolve the pending tool with the user's decision.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/hitl-in-app)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/hitl-in-app/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)

## Human in the loop: in chat

`hitl-in-chat`

Supported

Pause a tool call for user input with registerHumanInTheLoop and render the decision inside chat.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/hitl-in-chat)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/hitl-in-chat/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)

## Human in the loop: interrupts

`gen-ui-interrupt`

Supported

Handle an agent interrupt with injectInterrupt and render the response controls inside chat.

[Run example](https://showcase.copilotkit.ai/angular/google-adk/gen-ui-interrupt)[View source](https://showcase.copilotkit.ai/angular/google-adk/gen-ui-interrupt/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)

## MCP Apps

`mcp-apps`

Supported

MCP server integration with UI display

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/mcp-apps)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/mcp-apps/code)[API reference](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)

## Observational Memory

`observational-memory`

Supported

Conversation context is compressed and activated out of band; the background work surfaces inline as activity cards

[Run example](https://showcase.copilotkit.ai/angular/mastra/observational-memory)[View source](https://showcase.copilotkit.ai/angular/mastra/observational-memory/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Open Generative UI: Custom

`open-gen-ui-advanced`

Supported

Agent-authored UI that can invoke frontend sandbox functions from inside the iframe

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/open-gen-ui-advanced)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/open-gen-ui-advanced/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Open Generative UI: Default

`open-gen-ui`

Supported

Agent-generated UI from arbitrary component libraries

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/open-gen-ui)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/open-gen-ui/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Prebuilt chat

`agentic-chat`

Supported

Add a full chat surface with the standalone CopilotChat component.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/agentic-chat)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/agentic-chat/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Prebuilt popup

`prebuilt-popup`

Supported

Add a floating, accessible chat dialog with CopilotPopup.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/prebuilt-popup)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/prebuilt-popup/code)[API reference](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)

## Prebuilt sidebar

`prebuilt-sidebar`

Supported

Add a responsive docked or overlay chat with CopilotSidebar.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/prebuilt-sidebar)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/prebuilt-sidebar/code)[API reference](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)

## Reasoning: custom

`reasoning-custom`

Supported

Replace the reasoning-message slot with a standalone Angular component.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/reasoning-custom)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/reasoning-custom/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Reasoning: Default

`reasoning-default`

Supported

Built-in CopilotChatReasoningMessage rendering with no slot override

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/reasoning-default)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/reasoning-default/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Shared state: agent context

`readonly-state-agent-context`

Supported

Share read-only application state with the agent through connectAgentContext.

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/readonly-state-agent-context)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/readonly-state-agent-context/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Shared State: Read + Write

`shared-state-read-write`

Supported

Bidirectional agent state — UI writes preferences, agent writes notes back

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/shared-state-read-write)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/shared-state-read-write/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Shared State: Read-only

`shared-state-read`

Supported

Frontend recipe form publishes shared state via agent.setState; agent reads but does not mutate the recipe (neutral default agent, no backend tool)

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/shared-state-read)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/shared-state-read/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Shared State: Streaming

`shared-state-streaming`

Supported

Per-token state delta streaming from agent to UI

[Run example](https://showcase.copilotkit.ai/angular/langgraph-python/shared-state-streaming)[View source](https://showcase.copilotkit.ai/angular/langgraph-python/shared-state-streaming/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Sub-Agents

`subagents`

Supported

Multiple agents with visible task delegation

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/subagents)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/subagents/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Thread ID: frontend tool round trip

`threadid-frontend-tool-roundtrip`

Supported

Keep an explicit thread ID across an async frontend-tool call and resumed agent run.

Backend demo pending[View source](https://showcase.copilotkit.ai/angular/built-in-agent/threadid-frontend-tool-roundtrip/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)

## Voice

`voice`

Supported

Real-time voice interaction

[Run example](https://showcase.copilotkit.ai/angular/built-in-agent/voice)[View source](https://showcase.copilotkit.ai/angular/built-in-agent/voice/code)[API inventory](https://docs.copilotkit.ai/reference/angular/public-api)
