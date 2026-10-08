---
url: https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/governed-actions/
title: Governed Action Approval UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:27.585019+00:00
---

# Governed Action Approval UI

> Source: https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/governed-actions/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Governed Action Approval UI

Gate side-effecting agent actions with an approval UI before they execute.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Some agent actions are safe to run immediately, while others should be blocked or paused for user approval before they create side effects. A governed action approval UI gives the user a clear checkpoint:

  * **What** the agent wants to do
  * **Why** it wants to do it
  * **Which reference or policy decision** produced the verdict
  * **What happens next** if the user approves or rejects it



Use this pattern when the agent proposes an action such as sending an email, updating a record, creating a ticket, applying a discount, or calling any write API.

## Action envelope#

Keep the approval payload small, serializable, and vendor-neutral. The agent or backend can attach any policy engine result to the action as long as the UI receives the same basic envelope:
    
    
    type GovernedAction = {
      id: string;
      summary: string;
      tool: string;
      reference: string;
      verdict: "allow" | "deny" | "require_approval";
      arguments: Record<string, unknown>;
    };

The frontend should handle each verdict deterministically:

Verdict| UI behavior  
---|---  
`allow`| Execute the action without asking again, optionally showing an audit note.  
`deny`| Do not execute the action. Show the reason or reference and ask the agent to choose a safer path.  
`require_approval`| Render a user approval card. Execute only if the user approves.  
  
## Inline approval with `useInterrupt`#

If your runtime can pause an agent run, model the approval as an interrupt. The agent proposes the action, the UI renders the checkpoint, and the run resumes with the user's decision:
    
    
    import { useEffect } from "react";
    import { useInterrupt } from "@copilotkit/react-core/v2";
    
    function GovernedActionApproval() {
      useInterrupt({
        render: ({ interrupt, resolve, cancel }) => {
          const action = interrupt?.metadata?.action as GovernedAction | undefined;
    
          if (!action) {
            return null;
          }
    
          return (
            <GovernedActionCard
              action={action}
              onApprove={() =>
                resolve({
                  approved: true,
                  actionId: action.id,
                  reference: action.reference,
                })
              }
              onReject={() =>
                resolve({
                  approved: false,
                  actionId: action.id,
                  reference: action.reference,
                })
              }
              onBlock={() => cancel()}
            />
          );
        },
      });
    
      return null;
    }
    
    function GovernedActionCard({
      action,
      onApprove,
      onReject,
      onBlock,
    }: {
      action: GovernedAction;
      onApprove: () => void;
      onReject: () => void;
      onBlock: () => void;
    }) {
      useEffect(() => {
        if (action.verdict === "allow") onApprove();
        if (action.verdict === "deny") onBlock();
      }, [action.id, action.verdict]);
    
      const status =
        action.verdict === "allow"
          ? "Allowed by policy"
          : action.verdict === "deny"
            ? "Blocked by policy"
            : "User approval required";
    
      return (
        <section className="rounded-lg border p-4 shadow-sm">
          <div className="space-y-1">
            <p className="text-sm font-medium">{status}</p>
            <h3 className="text-base font-semibold">{action.summary}</h3>
            <p className="text-sm text-muted-foreground">Tool: {action.tool}</p>
            <p className="text-sm text-muted-foreground">
              Reference: {action.reference}
            </p>
          </div>
    
          <pre className="mt-3 overflow-auto rounded bg-muted p-3 text-xs">
            {JSON.stringify(action.arguments, null, 2)}
          </pre>
    
          {action.verdict === "require_approval" && (
            <div className="mt-4 flex gap-2">
              <button type="button" onClick={onApprove}>
                Approve and run
              </button>
              <button type="button" onClick={onReject}>
                Reject
              </button>
            </div>
          )}
        </section>
      );
    }

On resume, the agent should execute only when it receives an approved response for the same action id and reference:
    
    
    type ApprovalResponse = {
      approved: boolean;
      actionId: string;
      reference: string;
    };
    
    async function handleApproval(action: GovernedAction, response: ApprovalResponse) {
      if (
        response.approved &&
        response.actionId === action.id &&
        response.reference === action.reference
      ) {
        return executeSideEffect(action.tool, action.arguments);
      }
    
      return {
        skipped: true,
        reason: "The user did not approve this action.",
      };
    }

## Tool-call approval with `useHumanInTheLoop`#

For LLM-initiated pauses, register the approval checkpoint as a human-in-the-loop tool. The model asks to call `approve_governed_action`, your UI renders the card, and the tool result tells the agent whether it may continue:
    
    
    import { ToolCallStatus, useHumanInTheLoop } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    const governedActionSchema = z.object({
      id: z.string(),
      summary: z.string(),
      tool: z.string(),
      reference: z.string(),
      verdict: z.enum(["allow", "deny", "require_approval"]),
      arguments: z.record(z.unknown()),
    });
    
    function GovernedActionTool() {
      useHumanInTheLoop(
        {
          name: "approve_governed_action",
          description:
            "Ask the user to approve a governed side-effect action before it runs.",
          parameters: governedActionSchema,
          render: ({ args, status, respond }) => {
            if (status !== ToolCallStatus.Executing || !respond) {
              return null;
            }
    
            return (
              <GovernedActionCard
                action={args}
                onApprove={() =>
                  respond({
                    approved: true,
                    actionId: args.id,
                    reference: args.reference,
                  })
                }
                onReject={() =>
                  respond({
                    approved: false,
                    actionId: args.id,
                    reference: args.reference,
                  })
                }
                onBlock={() =>
                  respond({
                    approved: false,
                    actionId: args.id,
                    reference: args.reference,
                  })
                }
              />
            );
          },
        },
        [],
      );
    
      return null;
    }

## Recommended guardrails#

  * Check policy on the server before presenting the approval, not only in the browser.
  * Include a stable `action.id` and `reference` so the approval cannot be replayed for a different action.
  * Show the exact action arguments before the user approves.
  * Treat `deny` as terminal for that proposed action; do not execute a denied side effect from a later UI callback.
  * Log the proposal, verdict, user decision, and execution result so the action is auditable.



## Going further#

  * [Pausing the Agent for Input](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/governed-actions/useInterrupt) — use graph-enforced interrupts when the backend must stop before a side effect.
  * [HITL Overview](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/human-in-the-loop) — compare tool-based and interrupt-based human-in-the-loop patterns.
  * [Frontend Tools](https://docs.copilotkit.ai/claude-sdk-python/human-in-the-loop/frontend-tools) — register browser-side tools that can display approval UI or update application state.


