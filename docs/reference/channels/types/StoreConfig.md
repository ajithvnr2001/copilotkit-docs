---
url: https://docs.copilotkit.ai/reference/channels/types/StoreConfig/
title: StoreConfig
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:26.335103+00:00
---

# StoreConfig

> Source: https://docs.copilotkit.ai/reference/channels/types/StoreConfig/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁ChannelsSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[Actions](https://docs.copilotkit.ai/reference/channels/components/Actions)[Button](https://docs.copilotkit.ai/reference/channels/components/Button)[Chart](https://docs.copilotkit.ai/reference/channels/components/Chart)[Context](https://docs.copilotkit.ai/reference/channels/components/Context)[Divider](https://docs.copilotkit.ai/reference/channels/components/Divider)[Fields and Field](https://docs.copilotkit.ai/reference/channels/components/Fields)[Header](https://docs.copilotkit.ai/reference/channels/components/Header)[Image](https://docs.copilotkit.ai/reference/channels/components/Image)[Input](https://docs.copilotkit.ai/reference/channels/components/Input)[Markdown](https://docs.copilotkit.ai/reference/channels/components/Markdown)[Message](https://docs.copilotkit.ai/reference/channels/components/Message)[Modal](https://docs.copilotkit.ai/reference/channels/components/Modal)[Section](https://docs.copilotkit.ai/reference/channels/components/Section)[Select](https://docs.copilotkit.ai/reference/channels/components/Select)[Table, Row, and Cell](https://docs.copilotkit.ai/reference/channels/components/Table)

Functions

[bind](https://docs.copilotkit.ai/reference/channels/functions/bind)[createChannel](https://docs.copilotkit.ai/reference/channels/functions/createChannel)[defineChannelCommand](https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand)[defineChannelTool](https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool)[renderToIR](https://docs.copilotkit.ai/reference/channels/functions/renderToIR)

Classes

[Channel](https://docs.copilotkit.ai/reference/channels/classes/Channel)[MemoryStore](https://docs.copilotkit.ai/reference/channels/classes/MemoryStore)[Thread](https://docs.copilotkit.ai/reference/channels/classes/Thread)[Transcripts](https://docs.copilotkit.ai/reference/channels/classes/Transcripts)

Types

[ActionStore](https://docs.copilotkit.ai/reference/channels/types/ActionStore)[AgentContentPart](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart)[ChannelNode](https://docs.copilotkit.ai/reference/channels/types/ChannelNode)[IncomingMessage](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage)[InteractionContext](https://docs.copilotkit.ai/reference/channels/types/InteractionContext)[JSX callbacks](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks)[MessageRef](https://docs.copilotkit.ai/reference/channels/types/MessageRef)[StateStore](https://docs.copilotkit.ai/reference/channels/types/StateStore)[StoreConfig](https://docs.copilotkit.ai/reference/channels/types/StoreConfig)

SDKs

[Direct provider adapters](https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)Types

# StoreConfig

Configure per-thread state, the StateStore backend, transcripts, and turn concurrency controls.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`StoreConfig` is the `createChannel({ store })` value.
    
    
    interface StoreConfig<TStateSchema> {
      adapter?: StateStore;
      state?: TStateSchema;
      transcripts?: TranscriptsConfig;
      actionRetentionMs?: number;
      concurrency?: "parallel" | "serial" | "drop";
      /** @deprecated Prefer `concurrency`. */
      onLockConflict?:
        | "drop"
        | "force"
        | ((
            conversationKey: string,
            message: IncomingMessage,
          ) => "drop" | "force" | Promise<"drop" | "force">);
      lockTtl?: number;
      dedupTtl?: number;
    }

Option| Default| Behavior  
---|---|---  
`adapter`| `MemoryStore`| Persistence backend for SDK state.  
`state`| none| Standard Schema that types and validates `thread.state()` and `setState()`.  
`transcripts`| none| Optional retention and per-user cap, keyed by the application user from top-level `identifyUser`.  
`actionRetentionMs`| `604_800_000`| Retention for durable callbacks and one-use HITL continuations.  
`concurrency`| `"parallel"`| How overlapping turns on the same conversation are handled (see below).  
`onLockConflict`| (maps into `concurrency`)| **Deprecated.** Prefer `concurrency`. Static `"drop"` / `"force"` map to `"drop"` / `"parallel"`. A callback keeps the legacy exclusive-lock path.  
`lockTtl`| `60_000`| Per-conversation turn-lock TTL in milliseconds (used by `drop` / legacy lock paths).  
`dedupTtl`| `300_000`| Inbound event deduplication window in milliseconds.  
  
### Turn concurrency

Mode| Behavior  
---|---  
`"parallel"` (default)| Overlapping turns on the same conversation run together. Multiple people asking questions in one Slack thread each get a concurrent reply.  
`"serial"`| Later turns on the same conversation wait until the in-flight turn finishes (per-conversation queue).  
`"drop"`| Later turns are discarded while a turn is already in flight.  
  
A configured **singleton** agent (`agent: sharedInstance`) is isolated per run via `agent.clone()` under the hood, so parallel mode does not mutate one shared agent object. Prefer an agent factory when you want explicit control:
    
    
    agent: (threadId) => {
      const a = new HttpAgent({ url });
      a.threadId = threadId;
      return a;
    };
    
    
    const stateSchema = z.object({
      stage: z.enum(["draft", "review", "done"]),
    });
    
    const channel = createChannel({
      name: "support-slack",
      identifyUser: "platform",
      agent: makeAgent,
      store: {
        adapter: durableStateStore,
        state: stateSchema,
        // Opt into one-at-a-time processing for stateful workflows:
        // concurrency: "serial",
      },
    });

`thread.setState(value)` replaces the entire stored value and validates it against `state`. It does not merge patches. Under `"parallel"`, concurrent turns that both call `setState` can race — use `"serial"` for workflows that depend on exclusive state updates.

On the managed path, Intelligence owns cross-instance delivery claims and ordered provider effects. Managed admission also keeps one canonical Thread delivery active at a time on a Runtime, so `"parallel"` does not raise that delivery limit. The SDK store still owns application state and callback snapshots.
