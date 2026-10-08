---
url: https://docs.copilotkit.ai/angular/guides/human-in-the-loop/
title: Human-in-the-loop and interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:34.440740+00:00
---

# Human-in-the-loop and interrupts

> Source: https://docs.copilotkit.ai/angular/guides/human-in-the-loop/

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

Human-in-the-loop and interrupts

LearnAngular guides

# Human-in-the-loop and interrupts

Pause an Angular agent flow for a user decision, then resume it from a typed component or interrupt controller.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Human-in-the-loop flows pause agent work until a person supplies a decision. Angular has two paths with different owners.

Pattern| Who chooses the pause?| Angular API  
---|---|---  
Human-in-the-loop tool| The agent calls a registered browser tool| `registerHumanInTheLoop`  
Interrupt| The backend agent emits an AG-UI interrupt| `AgentStore.interruptController`, `injectInterrupt`  
  
Use a tool when the model should decide whether to ask. Use an interrupt when the backend workflow must stop at a fixed checkpoint.

## Register a decision tool#

The renderer receives a `toolCall` signal. Call `respond(result)` once the user has made a choice.

src/app/approval-card.component.ts
    
    
    import { Component, input } from "@angular/core";
    import {
      type HumanInTheLoopToolCall,
      type HumanInTheLoopToolRenderer,
    } from "@copilotkit/angular";
    
    type ApprovalArgs = {
      action: string;
      reason: string;
    };
    
    @Component({
      selector: "app-approval-card",
      template: `
        @let call = toolCall();
        <article>
          <h3>Approve {{ call.args.action ?? "this action" }}?</h3>
          <p>{{ call.args.reason }}</p>
    
          @if (call.status !== "complete") {
            <button type="button" (click)="call.respond({ approved: true })">
              Approve
            </button>
            <button type="button" (click)="call.respond({ approved: false })">
              Reject
            </button>
          }
        </article>
      `,
    })
    export class ApprovalCardComponent
      implements HumanInTheLoopToolRenderer<ApprovalArgs>
    {
      readonly toolCall =
        input.required<HumanInTheLoopToolCall<ApprovalArgs>>();
    }

Register the tool from the component or service that owns the decision UI:

src/app/approval-tools.service.ts
    
    
    import { Injectable } from "@angular/core";
    import { registerHumanInTheLoop } from "@copilotkit/angular";
    import { z } from "zod";
    import { ApprovalCardComponent } from "./approval-card.component";
    
    @Injectable()
    export class ApprovalToolsService {
      constructor() {
        registerHumanInTheLoop({
          name: "requestApproval",
          description: "Ask the user before a consequential action",
          parameters: z.object({
            action: z.string(),
            reason: z.string(),
          }),
          component: ApprovalCardComponent,
        });
      }
    }

There is no handler. CopilotKit supplies one that waits for `respond`, returns the decision to the agent, and continues the run. The registration is removed when the owning injector is destroyed.

## Handle an interrupt from the store#

An interrupt is a state of one conversation: this agent, this thread, this run is waiting for a decision. The store that already exposes that conversation's messages and state exposes its pending interrupt too, so a component that holds a store needs nothing else:

src/app/ticket-approval.component.ts
    
    
    import { Component } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-ticket-approval",
      template: `
        @let interrupts = store().interruptController;
    
        @if (interrupts.hasInterrupt()) {
          <section>
            <p>{{ interrupts.interrupt()?.message }}</p>
            <button type="button" (click)="interrupts.resolve({ approved: true })">
              Approve
            </button>
            <button type="button" (click)="interrupts.cancel()">Reject</button>
          </section>
        }
      `,
    })
    export class TicketApprovalComponent {
      protected readonly store = injectAgentStore("ticketing");
    }

The controller is created and connected with the store, then destroyed when the store is torn down or replaced. Standard AG-UI interrupts already retained by the agent are visible immediately, and legacy `on_interrupt` events are observed for the store's full lifetime.

## Handle an interrupt with a typed controller#

`injectInterrupt` subscribes to one agent and exposes the pending decision as signals. It supports standard AG-UI interrupts and the legacy `on_interrupt` custom event. Use it when the store default is not enough — a typed payload, an `enabled` filter, or a `handler` that prepares data for the view.

Do not render an `injectInterrupt` controller and `store().interruptController` for the same decision. Both independently observe the agent, so the same interrupt becomes visible in both and two UI actions could attempt to resume it. Render only the specialized controller when you need filtering or typed handling.

src/app/interrupt-panel.component.ts
    
    
    import { Component } from "@angular/core";
    import { injectInterrupt } from "@copilotkit/angular";
    
    type ReviewRequest = {
      title?: string;
      choices?: Array<{ id: string; label: string }>;
    };
    
    @Component({
      selector: "app-interrupt-panel",
      template: `
        @if (controller.event(); as event) {
          @let request = asReviewRequest(event.value);
          <section aria-labelledby="review-title">
            <h2 id="review-title">{{ request.title ?? "Review required" }}</h2>
    
            @for (choice of request.choices ?? []; track choice.id) {
              <button type="button" (click)="resolve(choice.id)">
                {{ choice.label }}
              </button>
            }
    
            <button type="button" (click)="cancel()">Cancel</button>
          </section>
        }
    
        @if (controller.error()) {
          <p role="alert">The decision could not be submitted.</p>
        }
      `,
    })
    export class InterruptPanelComponent {
      protected readonly controller =
        injectInterrupt<ReviewRequest>("default");
    
      protected asReviewRequest(value: unknown): ReviewRequest {
        return typeof value === "object" && value !== null
          ? (value as ReviewRequest)
          : {};
      }
    
      protected resolve(choiceId: string): void {
        this.controller.resolve({ choiceId }).catch(() => undefined);
      }
    
      protected cancel(): void {
        this.controller.cancel().catch(() => undefined);
      }
    }

The controller clears stale decisions when the thread changes. Calls to `resolve` or `cancel` share one in-flight resume promise, so a double click does not start two resume runs.

The runnable Showcase uses the same controller API in its route-aware feature:

interrupt-feature.component.ts
    
    
    export class InterruptFeatureComponent {  private readonly route = inject(ActivatedRoute);  protected readonly feature =    (this.route.snapshot.data["feature"] as string | undefined) ??    "gen-ui-interrupt";  protected readonly isHeadless = this.feature === "interrupt-headless";  private readonly agentId = agentIdForCurrentIntegration(this.feature);  protected readonly controller = injectInterrupt({ agentId: this.agentId });  protected readonly payload = computed(() =>    parseInterruptPayload(this.controller.event()?.value),  );  protected readonly pickedLabel = signal<string | null>(null);  private lastInterruptEvent: object | null = null;  constructor() {    effect(() => {      const event = this.controller.event();      if (event && event !== this.lastInterruptEvent) {        this.lastInterruptEvent = event;        this.pickedLabel.set(null);      }    });    if (usesFrontendSchedulingTool(this.feature, integrationId())) {      const config: HumanInTheLoopConfig<ScheduleMeetingArgs> = {        agentId: this.agentId,        name: "schedule_meeting",        description:          "Ask the user to pick a meeting time and return the selected slot.",        parameters: z.object({          topic: z.string(),          attendee: z.string().optional(),        }),        component:          TimePickerCard as unknown as HumanInTheLoopConfig<ScheduleMeetingArgs>["component"],      };      registerHumanInTheLoop(config);    }  }  /** Resolve the active decision while retaining its visible confirmation. */  protected resolve(slot: InterruptSlot): void {    this.pickedLabel.set(slot.label);    this.controller      .resolve({        chosen_time: slot.iso,        chosen_label: slot.label,      })      .catch(() => undefined);  }  /** Cancel only the currently displayed interrupt. */  protected cancel(): void {    this.controller.cancel().catch(() => undefined);  }}

Use the controller's `enabled` option when several components listen to the same agent and each should accept only certain interrupt payloads. Use `handler` when the view needs async data prepared before it appears.

## Place the decision UI#

The tool renderer appears in the tool-call flow inside chat. An interrupt controller is headless: bind its signals anywhere in the application, including a route-level dialog, side panel, or task view.

## Next steps#

  * [registerHumanInTheLoop API](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)
  * [injectInterrupt API](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)
  * [Runnable interrupt examples](https://docs.copilotkit.ai/angular/features#gen-ui-interrupt)



### On this page

Register a decision toolHandle an interrupt from the storeHandle an interrupt with a typed controllerPlace the decision UINext steps
