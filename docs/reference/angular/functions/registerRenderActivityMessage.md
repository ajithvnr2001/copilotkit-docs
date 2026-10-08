---
url: https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage/
title: registerRenderActivityMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:10.212931+00:00
---

# registerRenderActivityMessage

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Functions

# registerRenderActivityMessage

Register a typed Angular renderer for AG-UI activity messages.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`registerRenderActivityMessage` registers a standalone component for one AG-UI activity type for the lifetime of the current injector.
    
    
    function registerRenderActivityMessage<TContent>(
      config: RenderActivityMessageConfig<TContent>,
    ): void;
    
    interface RenderActivityMessageConfig<TContent> {
      activityType: string;
      agentId?: string;
      content: AngularActivityContentSchema<TContent>;
      component: Type<ActivityRenderer<TContent>>;
    }
    
    
    import { Component, input } from "@angular/core";
    import type { AbstractAgent, ActivityMessage } from "@ag-ui/client";
    import {
      ActivityRenderer,
      registerRenderActivityMessage,
    } from "@copilotkit/angular";
    import { z } from "zod";
    
    const progressSchema = z.object({ label: z.string(), percent: z.number() });
    
    @Component({
      template: `<progress [value]="content().percent" max="100"></progress>`,
    })
    export class ProgressActivity implements ActivityRenderer<
      z.infer<typeof progressSchema>
    > {
      readonly activityType = input.required<string>();
      readonly content = input.required<z.infer<typeof progressSchema>>();
      readonly message = input.required<ActivityMessage>();
      readonly agent = input<AbstractAgent>();
    }
    
    @Component({ template: `` })
    export class ActivityRegistration {
      constructor() {
        registerRenderActivityMessage({
          activityType: "job-progress",
          content: progressSchema,
          component: ProgressActivity,
        });
      }
    }

Content must pass `safeParse` before the component renders. `agentId` scopes a renderer to one agent. Application registrations take precedence over CopilotKit built-ins such as A2UI, Open Generative UI, and MCP Apps. The helper must run in an injection context and removes the exact registration on destroy. Renderer components should be standalone, OnPush- or zoneless-compatible, and must guard their own browser-only work for SSR and hydration.
