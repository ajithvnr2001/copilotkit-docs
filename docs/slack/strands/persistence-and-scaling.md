---
url: https://docs.copilotkit.ai/slack/strands/persistence-and-scaling/
title: Slack + AWS Strands (Python): Persistence and scaling
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:28:53.156061+00:00
---

# Slack + AWS Strands (Python): Persistence and scaling

> Source: https://docs.copilotkit.ai/slack/strands/persistence-and-scaling/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/strands)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/strands/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/strands/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/strands/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/strands/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/strands/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/strands/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/strands/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/strands/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/strands/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/strands/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/strands/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/strands/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Persistence and scaling

Production

# Persistence and scaling

Make Slack and Teams workflow state restart-safe, implement the StateStore contract, and deploy within the managed listener's concurrency model.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Intelligence durably owns provider ingress and canonical Thread history. Redis-backed claims and ordered packets coordinate active provider delivery. Your Channels process still owns SDK workflow state. Those are separate persistence boundaries.

## Know what is process-local by default#

Without `createChannel({ store: { adapter } })`, the SDK uses `MemoryStore`. These values disappear when the process restarts:

  * `thread.state()`
  * registered component snapshots used to restore callbacks
  * SDK transcript lists
  * SDK locks, deduplication windows, and queues



Managed conversation history is different: Intelligence reconstructs recent provider turns even when the SDK store is in memory.

Online does not mean restart-safe

The Intelligence **Online** state proves that the listener is connected. It does not prove that a pending approval or application workflow survives a deployment.

## Configure typed workflow state#

Use a Standard Schema to type reads and validate complete replacement values:

Terminal
    
    
    npm install zod

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { z } from "zod";
    import { durableStateStore } from "./state-store.js";
    
    const workflowState = z.object({
      incidentId: z.string(),
      stage: z.enum(["triage", "awaiting-approval", "resolved"]),
    });
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      store: {
        adapter: durableStateStore,
        state: workflowState,
      },
    });
    
    channel.onMessage(async ({ thread, message }) => {
      const current = await thread.state();
    
      await thread.setState({
        incidentId: current?.incidentId ?? "INC-421",
        stage: "triage",
      });
    
      await thread.runAgent({ prompt: message.text });
    });

`setState(value)` replaces the whole value. It does not merge a partial patch. Store JSON-serializable values; remote backends do not preserve `Date`, `Map`, class instances, or functions.

## Implement every StateStore facet#

A complete production store implements:

Facet| Required behavior  
---|---  
`kv`| Get, set with optional TTL, atomic consume, and delete  
`list`| Oldest-first append/range, cap, trim, delete, and list TTL  
`lock`| Atomic acquire plus token-checked release  
`dedup`| Atomic first-seen check with TTL  
`queue`| FIFO enqueue/dequeue/depth with bounded overflow policy  
  
Locks, deduplication, and queues must be atomic across every process sharing the backend. Namespacing must prevent one project or Channel from reading another one's keys.

Run the SDK's Vitest conformance suite against your adapter:

Terminal
    
    
    npm install -D vitest

state-store.test.ts
    
    
    import { runStateStoreConformance } from "@copilotkit/channels/testing";
    import { createRedisStateStore, closeRedisStateStore } from "./redis-store.js";
    
    runStateStoreConformance(
      "redis",
      () => createRedisStateStore(),
      (store) => closeRedisStateStore(store),
    );

Run it against the real backend:

Terminal
    
    
    npx vitest run state-store.test.ts

The SDK ships `MemoryStore` and the conformance suite; it does not ship a fully durable Redis or Postgres implementation in the umbrella package.

## Preserve interactive callbacks across restarts#

A callback survives only when both conditions are true:

  1. The JSX comes from a named component registered in `createChannel({ components })`.
  2. The action snapshot is stored in a durable `StateStore`.



channel.tsx
    
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      components: [ApprovalCard],
      store: { adapter: durableStateStore },
    });

Keep registered component props JSON-serializable and derive the handler from those props. Test by posting a card, restarting the process, then clicking the old card.

## Match the managed concurrency model#

### Delivery claims (multi-replica)#

Each prepared delivery has one claim winner. Every connected Runtime that declares the matching Channel can receive the invitation, check local capacity, and attempt the claim. Different replicas can serve different conversations at the same time; there is no Channel-wide leader.

Keep each replica's Channel declarations and agent code aligned. The managed listener bounds active and pending delivery work internally. A Runtime that has reached its internal capacity declines new invitations before claiming them; that capacity is not currently a public Channel configuration option.

Provider effects use one ordered packet at a time. The SDK retries that exact packet after a known retry wait or reconnect. If a provider call becomes uncertain, Gateway records an uncertain terminal result instead of sending it again. Application tools still need their own idempotency keys when the application may call them more than once; use `message.eventId`, `message.turnId`, or a durable operation ID.

### Turn concurrency (same conversation)#

Managed admission keeps one canonical Thread exclusive on a Runtime. A second invitation for that Thread is not claimed while the first delivery is active. Unrelated Threads continue in parallel within the managed listener's bounded capacity.

This delivery guard is separate from the SDK `store.concurrency` setting used by other adapter paths. Choose that setting for your application-state rules; do not use it to raise the managed same-Thread delivery limit. See [`StoreConfig`](https://docs.copilotkit.ai/reference/channels/types/StoreConfig).

## Production checklist#

  * Prefer an agent factory; singletons are cloned per run automatically.
  * Choose `store.concurrency` deliberately if you need serial workflow state.
  * Provide a durable store before promising restart-safe state or callbacks.
  * Run the StateStore conformance suite against the real backend.
  * Test a restart while a card is awaiting a click.
  * Make external writes idempotent.
  * Keep Channel declarations aligned across replicas and scale horizontally when the managed listener's bounded local capacity is insufficient.
  * Alert on Intelligence **Conflict** , **Offline** , and **Delivery failing**.
  * Stop the listener on `SIGINT` and `SIGTERM`.



Continue with [history and transcripts](https://docs.copilotkit.ai/slack/strands/history-and-transcripts), or use the [`StateStore` reference](https://docs.copilotkit.ai/reference/channels/types/StateStore).

### On this page

Know what is process-local by defaultConfigure typed workflow stateImplement every StateStore facetPreserve interactive callbacks across restartsMatch the managed concurrency modelDelivery claims (multi-replica)Turn concurrency (same conversation)Production checklist
