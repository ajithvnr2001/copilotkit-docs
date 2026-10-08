---
url: https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop/
title: registerHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:10.053897+00:00
---

# registerHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop/

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

# registerHumanInTheLoop

Angular function for registering a human-in-the-loop tool with CopilotKit that pauses the agent and resumes it when the user responds from a rendered component

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`registerHumanInTheLoop` registers a tool that pauses the agent and waits for human input. When the agent calls the tool, CopilotKit renders the `component` you provide and suspends the agent run. The component collects a decision from the user (for example a confirm or reject choice) and calls `respond(result)`. That call resolves the tool with the value you passed to `respond`, serialized as described below, and lets the run continue.

You call `registerHumanInTheLoop` inside an Angular injection context (a component or service constructor, or a field initializer). The tool registers immediately. When the owning injector is destroyed, CopilotKit removes tool and renderer registrations with the same name and optional agent id.

Unlike [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool), you do not write a `handler`. CopilotKit supplies one that waits for the user's `respond` call, so the rendered component controls when the agent resumes.

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerHumanInTheLoop` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## Signature
    
    
    import { registerHumanInTheLoop } from "@copilotkit/angular";
    
    function registerHumanInTheLoop<Args extends Record<string, unknown>>(
      humanInTheLoop: HumanInTheLoopConfig<Args>,
    ): void;

## Parameters

Prop

Type

`humanInTheLoop`HumanInTheLoopConfig<Args>

## Return Value

`registerHumanInTheLoop` returns `void`. It registers the tool as a side effect and wires up name-and-agent-id cleanup for the owning injector.

## The renderer component

Your `component` implements the `HumanInTheLoopToolRenderer<Args>` interface. It exposes a single `toolCall` signal input, so declare it with Angular's `input()`:
    
    
    import { Signal } from "@angular/core";
    
    interface HumanInTheLoopToolRenderer<Args extends Record<string, unknown>> {
      toolCall: Signal<HumanInTheLoopToolCall<Args>>;
    }

### HumanInTheLoopToolCall

`toolCall()` returns a discriminated union keyed on `status`. Every variant carries a `respond` callback:
    
    
    type HumanInTheLoopToolCall<Args extends Record<string, unknown>> =
      | {
          name?: string;
          args: Partial<Args>; // streaming, may be incomplete
          status: "in-progress";
          result: undefined;
          respond: (result: unknown) => void;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "executing";
          result: undefined;
          respond: (result: unknown) => void;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "complete";
          result: string; // stored tool-message content
          respond: (result: unknown) => void;
        };

The `respond(result)` callback is how your component resumes the agent. The value you pass to `respond` becomes the tool result directly: a string is stored as-is, and any other value is serialized to JSON by core. It is not wrapped in an envelope, so the agent sees the same shape it would from the React and Vue adapters. While the agent waits, `status` is `executing` (or `in-progress` while the arguments are still streaming). Once the tool message arrives, `status` becomes `complete` and `result` contains the stored tool-message string.

## Usage

### A confirmation dialog

This component renders a confirm and a reject button. Each records a different decision and resumes the agent.

src/app/confirm-dialog.component.ts
    
    
    import { Component, computed, input } from "@angular/core";
    import { HumanInTheLoopToolCall, HumanInTheLoopToolRenderer } from "@copilotkit/angular";
    
    type ConfirmArgs = { message: string };
    
    @Component({
      selector: "app-confirm-dialog",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "complete") {
          <pre class="text-sm opacity-70">{{ call.result }}</pre>
        } @else {
          <div class="rounded border p-4">
            <p>{{ message() }}</p>
            <div class="mt-3 flex gap-2">
              <button type="button" (click)="call.respond('confirmed')">Confirm</button>
              <button type="button" (click)="call.respond('rejected')">Reject</button>
            </div>
          </div>
        }
      `,
    })
    export class ConfirmDialogComponent implements HumanInTheLoopToolRenderer<ConfirmArgs> {
      readonly toolCall = input.required<HumanInTheLoopToolCall<ConfirmArgs>>();
      readonly message = computed(() => this.toolCall().args.message ?? "Are you sure?");
    }

Register the tool with that component:

src/app/chat.component.ts
    
    
    import { Component } from "@angular/core";
    import { z } from "zod";
    import { registerHumanInTheLoop } from "@copilotkit/angular";
    import { ConfirmDialogComponent } from "./confirm-dialog.component";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      template: ``,
    })
    export class ChatComponent {
      constructor() {
        registerHumanInTheLoop({
          name: "confirmAction",
          description: "Ask the user to confirm before performing a sensitive action",
          parameters: z.object({
            message: z.string().describe("The confirmation question to show the user"),
          }),
          component: ConfirmDialogComponent,
        });
      }
    }

When the agent calls `confirmAction`, the dialog appears in the chat and the run pauses. A button click sends `"confirmed"` or `"rejected"` as the tool result. The completed tool call exposes that stored string.

Cleanup uses the same shared name-and-agent-id removal path as the other tool registration helpers. Frontend tools, human-in-the-loop tools, and tool-call renderers that share that key are removed together.

## Related

### [registerFrontendToolRegister a client-side tool with an async handler and an optional renderer component.](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)### [registerRenderToolCallRegister a renderer for a tool call with access to streaming status and results, without a handler.](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)### [CopilotKit serviceThe central service that holds agents, tools, and the runtime connection.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
