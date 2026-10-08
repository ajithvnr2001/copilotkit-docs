---
url: https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt/
title: injectInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:59.002524+00:00
---

# injectInterrupt

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt/

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

# injectInterrupt

Signal-based standard and legacy AG-UI interrupt handling for Angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`injectInterrupt` creates an injector-scoped controller for AG-UI interrupts. It supports standard interrupt arrays and the legacy `on_interrupt` custom event, including multiple simultaneous decisions.
    
    
    function injectInterrupt<TValue = unknown, TResult = never>(
      agentId?: string | Signal<string | undefined>,
      options?: Omit<InjectInterruptOptions<TValue, TResult>, "agentId">,
    ): InterruptController<TValue, TResult>;
    
    
    import { Component } from "@angular/core";
    import { injectInterrupt } from "@copilotkit/angular";
    
    @Component({
      template: `
        @if (interrupt.view(); as decision) {
          <p>{{ decision.event.name }}</p>
          <button type="button" (click)="decision.cancel()">Cancel</button>
          <button type="button" (click)="decision.resolve({ approved: true })">
            Approve
          </button>
        }
      `,
    })
    export class ApprovalView {
      readonly interrupt = injectInterrupt<{ reason: string }>();
    }

## Parameters

  * `agentId`: string or signal; defaults to the ambient chat agent.
  * `enabled(event)`: synchronous or asynchronous filter. `false` leaves the event available for another controller.
  * `handler(props)`: synchronous or asynchronous preprocessing whose result is exposed through the controller's `result` signal.



The previous `injectInterrupt({ agentId, enabled, handler })` form remains supported.

The controller exposes `event`, `interrupt`, `interrupts`, `result`, `error`, `hasInterrupt`, and `view` signals plus `resolve(payload?, interruptId?)` and `cancel(interruptId?)`. When several standard interrupts are pending, resolve or cancel every ID before the agent resumes. Tool-backed decisions persist a tool-result message before resumption.

Every store already exposes an unfiltered controller as [`AgentStore.interruptController`](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore). Reach for `injectInterrupt` when a decision needs a typed value, an `enabled` filter, or a `handler`.

Controllers do not claim interrupts from one another. A store controller and a filtered controller for the same agent can both expose the same decision. If both UIs call `resolve` before the next run starts, both can attempt to resume it. Render only one controller for a given decision.

For example, a matching refund interrupt is visible through both properties in this component:
    
    
    type RefundRequest = { type: "refund"; amount: number };
    
    export class RefundPage {
      readonly store = injectAgentStore("ticketing");
      readonly refunds = injectInterrupt<RefundRequest>("ticketing", {
        enabled: event => event.value.type === "refund",
      });
    
      // For a matching interrupt, both expressions are true:
      // this.store().interruptController.hasInterrupt()
      // this.refunds.hasInterrupt()
    }

Render `refunds` for this decision and do not also render `store().interruptController`. The unrendered store controller only observes the interrupt; it cannot resume anything unless application code calls its `resolve` or `cancel` method.

The agent subscription is disconnected when the owning injector is destroyed. Thread changes and new or failed runs clear stale decisions. Predicate and handler failures are captured by `error`; expired decisions use `InterruptExpiredError`. A resume failure clears pending state and rejects—it is never retried automatically. The controller performs no DOM work and is SSR safe, but applications should not resume an agent during server rendering.
