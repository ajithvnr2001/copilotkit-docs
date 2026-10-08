---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotActivity/
title: CopilotActivity
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:53.158933+00:00
---

# CopilotActivity

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotActivity/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Components

# CopilotActivity

Angular component that renders a single activity message through the activity renderer registered for its activity type.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotActivity` renders one activity message. It looks up the renderer registered for the message's `activityType` — via `provideCopilotKit({ renderActivityMessages })` or [`registerRenderActivityMessage`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage) — validates the message content against the renderer's schema, and mounts the renderer component with the `activityType`, `content`, `message`, and `agent` inputs.

It is the activity counterpart of `RenderToolCalls` and the Angular equivalent of React's `useRenderActivityMessage()`. [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView) uses it for every message with `role: "activity"`, so the built-in chat and your own templates share one implementation.

Use it directly when you build a custom chat shell without `CopilotChatMessageView`, or when you host activities outside of a chat entirely — a dashboard, a side panel, an output area.

The component is standalone. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## Usage

src/app/activity-panel.component.ts
    
    
    import { Component, computed, input } from "@angular/core";
    import { CopilotActivity } from "@copilotkit/angular";
    import type { ActivityMessage, Message } from "@ag-ui/core";
    
    @Component({
      selector: "app-activity-panel",
      standalone: true,
      imports: [CopilotActivity],
      template: `
        @for (activity of activities(); track activity.id) {
          <copilot-activity [message]="activity" [agentId]="agentId()" />
        }
      `,
    })
    export class ActivityPanelComponent {
      messages = input.required<Message[]>();
      agentId = input<string>();
    
      activities = computed(() =>
        this.messages().filter(
          (message): message is ActivityMessage => message.role === "activity",
        ),
      );
    }

## Renderer resolution

For a given `activityType`, the first matching renderer wins in this order:

  1. a renderer for that type registered with the same `agentId`
  2. a renderer for that type without an `agentId` (global)
  3. the `"*"` wildcard renderer



Within a tier, registration order decides: renderers passed to `provideCopilotKit` or registered at runtime come before the built-in ones (A2UI, Open Generative UI, MCP Apps), so an application renderer can override a built-in for the same activity type.

If no renderer matches, nothing is rendered. If the renderer's content schema rejects the message content, nothing is rendered and a warning is logged.

## Inputs

Input| Type| Default| Description  
---|---|---|---  
`message`| `ActivityMessage`| — (required)| The activity message to render.  
`agentId`| `string | undefined`| `undefined`| Agent scope for renderer resolution. Also used to look up the `AbstractAgent` handed to the renderer's `agent` input.  
  
## See also

  * [`registerRenderActivityMessage`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage) — register a renderer for the lifetime of the current injector.
  * [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView) — the message list that uses this component for activity messages.


