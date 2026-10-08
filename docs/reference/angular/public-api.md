---
url: https://docs.copilotkit.ai/reference/angular/public-api/
title: Public API inventory
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:13.286724+00:00
---

# Public API inventory

> Source: https://docs.copilotkit.ai/reference/angular/public-api/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁AngularSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Guides

[Public API inventory](https://docs.copilotkit.ai/reference/angular/public-api)[Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle)

Components

[CopilotActivity](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity)[CopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)[CopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)

Functions

[connectAgentContext](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)[injectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)[injectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)[injectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)[injectCopilotKitConfig](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)[injectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)[injectThreads](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)[provideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)[provideCopilotKit](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)[provideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)[registerComponent](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)[registerFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)[registerHumanInTheLoop](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)[registerRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)[registerRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)

Services

[CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)

Directives

[CopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Public-api

# Public API inventory

Supported entry points and API families for @copilotkit/angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The supported entry points are `@copilotkit/angular`, `@copilotkit/angular/mcp-apps`, and `@copilotkit/angular/styles.css`. The published package includes `API.md`, an alphabetized, machine-validated list of every exported value and type. A test resolves both TypeScript entry points and requires every export to appear exactly once in that inventory.

## Root API families

  * **Setup and runtime:** `provideCopilotKit`, `CopilotKit`, `CopilotKitConfig`, configuration and label providers, and injection tokens.
  * **Complete UI:** `CopilotChat`, `CopilotPopup`, `CopilotSidebar`, `CopilotThreadsDrawer`, and their input/model types.
  * **Composable chat UI:** `CopilotChatView`, message, input, textarea, suggestion, toolbar, button, attachment, audio, scroll, cursor, disclaimer, feather, tools-menu, and renderer components plus their slot/context types.
  * **Agents and application state:** `injectAgentStore`, `injectCapabilities`, `AgentStore`, `connectAgentContext`, `CopilotKitAgentContext`, `injectChatState`, `injectThreads`, `injectMemories`, and their stores, controllers, and types.
  * **Tools and activities:** `registerComponent`, `registerFrontendTool`, `registerRenderToolCall`, `registerHumanInTheLoop`, `registerRenderActivityMessage`, `RenderToolCalls`, `CopilotDefaultToolRenderer`, schemas, configurations, renderer interfaces, and safe parsing/serialization utilities.
  * **Interrupts:** `injectInterrupt`, `InterruptController`, `InterruptExpiredError`, and the event, view, runner, handler, and options types.
  * **Generative UI:** A2UI configuration, activity/tool/progress/recovery components and lifecycle schemas; Open Generative UI configuration, sandboxes, activity/tool renderers, content schemas, and constants.
  * **Attachments and transcription:** attachment types, queue and renderer components, attachment directive, audio recorder controls, transcription function, errors, and result/state types.
  * **Slots, directives, and utilities:** slot registry and render helpers, stick-to-bottom, tooltip, resize/scroll services and state, class-name and tool-call utilities.
  * **Protocol types:** selected AG-UI messages and CopilotKit suggestion and memory types are re-exported so application signatures use the same types as the SDK.



The exported `ɵCOPILOTKIT_BUILT_IN_ACTIVITY_RENDERERS` token is explicitly internal. It exists only for CopilotKit-maintained secondary entry points and applications must not depend on it.

## MCP Apps API family

The secondary entry point exports `provideMCPApps`, its configuration and DI tokens, the snapshot schema and type, the ready-made activity renderer config, and `CopilotMCPAppsActivityRenderer`/`CopilotMCPAppsWidget` for advanced hosts.

Use the task-specific reference pages for signatures and behavior. Consult the `API.md` included beside the package README when reviewing the exact symbol inventory for an installed version; that file is the normative export list.
