---
url: https://docs.copilotkit.ai/teams/google-adk/interactive/
title: Microsoft Teams + Google ADK: Interactive messages and approvals
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:33:03.144442+00:00
---

# Microsoft Teams + Google ADK: Interactive messages and approvals

> Source: https://docs.copilotkit.ai/teams/google-adk/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelTeamsAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/teams/google-adk)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/teams/google-adk/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/teams/google-adk/connect)

Build

[Tools and context](https://docs.copilotkit.ai/teams/google-adk/tools)[Identity and Memory](https://docs.copilotkit.ai/teams/google-adk/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/teams/google-adk/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/teams/google-adk/interactive)[Commands and reactions](https://docs.copilotkit.ai/teams/google-adk/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/teams/google-adk/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/teams/google-adk/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/teams/google-adk/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/teams/google-adk/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/teams/google-adk/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Interactive messages and approvals

Build

# Interactive messages and approvals

Render portable Slack and Teams UI, handle actions, and resume interrupted agent runs without blocking a managed delivery.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Channels JSX renders portable components as native channel UI. Use it for buttons, summaries, and human approval without maintaining provider payloads by hand.

On Microsoft Teams, Channels JSX renders as Adaptive Cards. Buttons render with `Action.Submit`, and clicks return to the managed connection as message activities. A Teams `Action.Submit` activity can arrive without a source message ref; in that case, `message.ref.id` is empty.

## Enable Channels JSX#

The package is ESM-only. Keep `"type": "module"` in `package.json` and add:

tsconfig.json
    
    
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "NodeNext",
        "moduleResolution": "NodeNext",
        "jsx": "react-jsx",
        "jsxImportSource": "@copilotkit/channels",
        "strict": true,
        "noEmit": true
      },
      "include": ["*.ts", "*.tsx"]
    }

## Post a native action#

Define a named component and register it on the Channel:

approval-card.tsx
    
    
    import {
      Actions,
      Button,
      Header,
      Message,
      Section,
    } from "@copilotkit/channels/ui";
    
    export function ApprovalCard({ summary }: { summary: string }) {
      return (
        <Message>
          <Header>Approval required</Header>
          <Section>{summary}</Section>
          <Actions>
            <Button
              style="primary"
              value={{ approved: true }}
              onClick={async ({ thread, message, action }) => {
                const value = action.value;
                if (value === undefined) {
                  await thread.post(
                    "The approval value was missing. Please try again.",
                  );
                  return;
                }
    
                if (message.ref.id) {
                  try {
                    await thread.update(
                      message.ref,
                      <Message>
                        <Header>Approved</Header>
                        <Section>{summary}</Section>
                      </Message>,
                    );
                  } catch {
                    // Updating the card is best-effort; always resume the agent.
                  }
                }
                await thread.resume(value);
              }}
            >
              Approve
            </Button>
            <Button
              style="danger"
              value={{ approved: false }}
              onClick={async ({ thread, message, action }) => {
                const value = action.value;
                if (value === undefined) {
                  await thread.post(
                    "The approval value was missing. Please try again.",
                  );
                  return;
                }
    
                if (message.ref.id) {
                  try {
                    await thread.update(
                      message.ref,
                      <Message>
                        <Header>Rejected</Header>
                        <Section>{summary}</Section>
                      </Message>,
                    );
                  } catch {
                    // Updating the card is best-effort; always resume the agent.
                  }
                }
                await thread.resume(value);
              }}
            >
              Reject
            </Button>
          </Actions>
        </Message>
      );
    }

channel.tsx
    
    
    import { createChannel } from "@copilotkit/channels";
    import { ApprovalCard } from "./approval-card.js";
    import { makeAgent } from "./agent.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing ${name}`);
      return value;
    }
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      components: [ApprovalCard],
    });
    
    channel.onInterrupt<{ summary: string }>(
      "on_interrupt",
      async ({ payload, thread }) => {
        await thread.post(<ApprovalCard summary={payload.summary} />);
      },
    );

Registration lets the action registry rebuild a named component when a later click arrives. Keep component props JSON-serializable.

Treat an interaction message as updateable only when `message.ref.id` is non-empty. The card update in this example is best-effort: a missing ref or a failed update must not prevent `thread.resume(value)` from continuing the approval.

## Use post-and-resume for managed approvals#

Managed deliveries cannot wait inside `thread.awaitChoice()`. The click arrives as a separate claimed delivery, so blocking the first delivery would prevent the approval from being processed.

For an agent that emits the SDK-supported `on_interrupt` event, the safe flow is:

  1. The agent emits an `on_interrupt` event.
  2. `channel.onInterrupt` posts the registered component and returns.
  3. Intelligence acknowledges the original turn.
  4. A later click updates the card when possible and calls `thread.resume(value)`.
  5. The SDK re-enters the agent with the approval result.



The selected agent framework decides how it emits and consumes the interrupt. Follow its [human-in-the-loop guide](https://docs.copilotkit.ai/teams/google-adk/human-in-the-loop) for the agent-side interrupt; keep the Channel handler limited to portable presentation and `resume`.

Framework interrupt support is not universal

The validated managed path is a DeepAgent tool-driven approval that emits `on_interrupt`, returns from delivery, then resumes from a later interaction. For every other backend, follow its human-in-the-loop guide and run a real provider test that confirms the interrupt reaches `onInterrupt`, the handler returns, the later click calls `resume`, and the agent consumes the value. Do not assume native AG-UI interrupts are portable. The default `sanitizeAgentEvents` behavior repairs a known event-validation issue; it does not add framework interrupt support by itself.

Restart durability needs a StateStore

The managed realtime connection does not automatically persist SDK action snapshots. The default MemoryStore keeps them only in the current process. Registered components make recovery possible, but clicks on pre-restart cards still require a durable `createChannel({ store: { adapter } })` backend. See [Threads and state](https://docs.copilotkit.ai/teams/google-adk/threads-and-state).

## Capability differences#

Text and sections are the portable baseline. Interactive behavior also depends on the selected provider's app configuration:

  * Teams can deliver `Action.Submit` buttons in Adaptive Cards as message activities.



Other provider-specific features remain capability-gated:

  * Incoming reactions can be handled when Intelligence delivers them, and the managed adapter supports adding or removing documented portable reactions.
  * Modal open/submit callbacks are direct-adapter capabilities, not part of the managed Slack or Teams realtime path.
  * Ephemeral messages, conversation titles, and suggested prompts may return `{ ok: false }`; check the result when your workflow depends on them.



Use the [JSX callback reference](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks) for handler arguments and the [Thread API](https://docs.copilotkit.ai/reference/channels/classes/Thread) for post, update, and resume signatures.

### On this page

Enable Channels JSXPost a native actionUse post-and-resume for managed approvalsCapability differences
