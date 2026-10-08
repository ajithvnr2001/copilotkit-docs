---
url: https://docs.copilotkit.ai/reference/channels/classes/Channel/
title: Channel
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:14.123944+00:00
---

# Channel

> Source: https://docs.copilotkit.ai/reference/channels/classes/Channel/

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

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)Classes

# Channel

Reference for createChannel options, managed providers, handlers, tools, storage, and runtime lifecycle.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`createChannel(options)` returns the Channel you declare on `CopilotRuntime({ channels })`.

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { makeAgent } from "./agent.js";
    
    const channel = createChannel({
      name: "support",
      identifyUser: "platform",
      agent: makeAgent,
    });

Use the project-unique Intelligence Channel Code. The managed runtime declares both Slack and Teams for this Channel and keeps each delivery provider-scoped.

## createChannel options

Option| Type| Description  
---|---|---  
`name`| `string`| Project-unique Intelligence Code. Required for managed Channels; lowercase kebab-case, 3–64 characters, and not `channels`.  
`identifyUser`| `"platform" | ChannelIdentifyUser`| Required identity policy. Returns one application user or `null` for each provider event.  
`showToolStatus`| `boolean`| Controls managed Slack tool-call progress. It is hidden by default; set `true` to show it.  
`replyContinuation`| `ReplyContinuationOptions`| Managed Slack long-reply limits: `messageByteLimit`, `maxMessages`, and `truncationMarker`.  
`agent`| `AbstractAgent | (threadId: string) => AbstractAgent`| Agent instance or factory. Factory preferred; every turn clones the configured result.  
`sanitizeAgentEvents`| `boolean`| Defaults to `true`; repairs a known malformed AG-UI parent-message field in HTTP event streams.  
`tools`| `ChannelTool[]`| Typed tools forwarded to the agent.  
`context`| `ContextEntry[]`| Stable `{ description, value }` context sent on each run.  
`components`| `ChannelComponent[]`| Named JSX components whose callbacks can be reconstructed from stored snapshots.  
`commands`| `ChannelCommand[]`| Declared commands for providers that support them.  
`store`| `StoreConfig`| State schema, persistence, turn concurrency (`parallel` default), dedup, and optional transcript bridge.  
`adapters`| `PlatformAdapter[]`| Low-level direct transports. They may coexist with the cloud-hosted Intelligence adapter on this Channel.  
  
One Channel may receive managed Slack and Teams deliveries. Names must be unique inside one `CopilotRuntime`.

For long-reply defaults, event sanitization, and agent clone requirements, see the detailed [`createChannel` options](https://docs.copilotkit.ai/reference/channels/functions/createChannel).

## StoreConfig

Option| Type| Description  
---|---|---  
`state`| `StandardSchema`| Types `thread.state()` and validates every `setState(value)`.  
`adapter`| `StateStore`| Persistence implementation for SDK state. Without it, the current managed realtime path falls back to process memory.  
`transcripts`| `TranscriptsConfig`| SDK-owned cross-platform transcript configuration keyed by the application user from top-level `identifyUser`.  
`actionRetentionMs`| `number`| Durable callback and one-use HITL continuation retention. Default: seven days.  
`concurrency`| `"parallel" | "serial" | "drop"`| How overlapping turns on the same conversation are handled. Default: `"parallel"`. See [`StoreConfig`](https://docs.copilotkit.ai/reference/channels/types/StoreConfig).  
`onLockConflict`| `"drop" | "force" | callback`| **Deprecated.** Prefer `concurrency`. Maps to drop/parallel when static.  
`lockTtl`| `number`| Conversation lock TTL in milliseconds (drop / legacy paths). Default: `60_000`.  
`dedupTtl`| `number`| Inbound event deduplication window in milliseconds. Default: `300_000`.  
  
`StateStore` contains `kv`, `list`, `lock`, `dedup`, and `queue` facets. Remote implementations must preserve JSON-serializable values.

### StateStore contract

A production adapter implements this asynchronous contract. Locks, deduplication, and queue operations must remain atomic when multiple runner instances share the same backend.

state-store.ts
    
    
    interface StateStore {
      kv: {
        get<T>(key: string): Promise<T | undefined>;
        set<T>(key: string, value: T, ttlMs?: number): Promise<void>;
        consume<T>(key: string): Promise<T | undefined>;
        delete(key: string): Promise<void>;
      };
      list: {
        append<T>(
          key: string,
          value: T,
          options?: { maxLen?: number; ttlMs?: number },
        ): Promise<number>;
        range<T>(key: string, start?: number, stop?: number): Promise<T[]>;
        trim(key: string, maxLen: number): Promise<void>;
        delete(key: string): Promise<void>;
      };
      lock: {
        acquire(
          key: string,
          options?: { ttlMs?: number },
        ): Promise<{ token: string } | null>;
        release(key: string, token: string): Promise<void>;
      };
      dedup: {
        // true means the key was already recorded inside the TTL.
        seen(key: string, ttlMs: number): Promise<boolean>;
      };
      queue: {
        enqueue<T>(
          key: string,
          value: T,
          options?: {
            maxSize?: number;
            onFull?: "drop-oldest" | "drop-newest";
          },
        ): Promise<number>;
        dequeue<T>(key: string): Promise<T | undefined>;
        depth(key: string): Promise<number>;
      };
    }

All values must round-trip through JSON. A distributed implementation must release a lock only when the supplied token still owns it.

## Properties

Property| Type| Description  
---|---|---  
`name`| `string | undefined`| Declared Intelligence Code.  
`showToolStatus`| `boolean | undefined`| Managed Slack tool-call visibility preference from `createChannel()`.  
`replyContinuation`| `ReplyContinuationOptions | undefined`| Managed Slack continuation preference from `createChannel()`.  
`adapters`| `readonly PlatformAdapter[]`| Attached transport snapshot. Managed Channels start empty and receive the Intelligence adapter at activation.  
`commandNames`| `string[]`| Normalized names declared through `commands` or `onCommand`.  
`transcripts`| `Transcripts`| Optional SDK transcript API. It is not the managed provider-history store.  
  
The `transcripts` getter is only available after Channel activation and throws if it is read before the runtime listener starts the Channel.

## Message handlers

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({
        prompt: message.contentParts?.length
          ? [
              ...(message.text
                ? [{ type: "text" as const, text: message.text }]
                : []),
              ...message.contentParts,
            ]
          : message.text,
      });
    });

Method| Handler input| Notes  
---|---|---  
`onMessage(handler)`| `{ thread, message }`| Use this for managed Slack and Teams turns.  
`onMention(handler)`| `{ thread, message }`| A bot mention selects this handler when registered; otherwise it falls back to `onMessage`. Other content selects `onMessage`.  
`onWelcome(handler)`| `{ thread, user, actor, platform }`| Runs once for a supported provider installation or conversation activation. No handler means no welcome output.  
`onThreadStarted(handler)`| `{ thread, user, actor }`| Fires for provider surfaces that report a conversation-open event.  
  
`message.platform` is the native provider (`"slack"` or `"teams"`). `thread.platform` carries that same native provider on a managed Channel.

## Interaction and interrupt handlers

Method| Purpose| Managed Slack/Teams  
---|---|---  
`onInteraction(id, handler)`| Handle a specific opaque action id.| Supported for delivered actions. JSX callbacks are usually simpler.  
`onInterrupt(eventName, handler)`| Post UI for an agent interrupt; later call `thread.resume(value)`.| Use `eventName: "on_interrupt"` for the current managed renderer.  
`onReaction(emoji?, handler)`| Handle delivered reaction events.| Inbound support is provider-dependent.  
`onCommand(command)`| Register a typed or free-text command.| Provider-dependent.  
`onModalSubmit(callbackId, handler)`| Handle a modal form submission.| Not delivered by the managed realtime path.  
`onModalClose(callbackId, handler)`| Handle a modal dismissal.| Not delivered by the managed realtime path.  
  
See the [Slack interactive messages guide](https://docs.copilotkit.ai/slack/interactive), the [Teams interactive messages guide](https://docs.copilotkit.ai/teams/interactive), and the [JSX callback reference](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks).

## Register a tool

Pass tools in `createChannel({ tools })`, or add one before activation:

channel.ts
    
    
    channel.tool(getIncident);

See [Tools and context for Slack](https://docs.copilotkit.ai/slack/tools) or [Tools and context for Teams](https://docs.copilotkit.ai/teams/tools).

## Runtime lifecycle

A Channel has no public `start()` method. Node and Express listeners own a long-running process lifetime, so creating either listener starts the managed Channel automatically. On those mounts, `ready()` is optional: await it when startup must observe the initial managed status before the rest of the process continues.

Hono and generic Fetch mounts are request-oriented and remain lazy. Call and await `ready()` during an explicit long-running startup path before expecting managed traffic; creating one of those handlers alone does not open the Realtime Gateway connection.

Runtime mount| Start behavior| Role of `ready()`  
---|---|---  
Node listener| Starts when the listener is created| Optional readiness wait and initial status check  
Express listener| Starts when the listener is created| Optional readiness wait and initial status check  
Hono mount| Lazy| Explicitly await before expecting managed traffic  
Generic Fetch mount| Lazy| Explicitly await before expecting managed traffic  
  
Install shutdown handlers before waiting for readiness so a slow or incomplete provider setup cannot prevent graceful teardown:

channel.ts
    
    
    const listener = createCopilotNodeListener({ runtime });
    
    const channels = listener.channels;
    if (!channels) throw new Error("Channels were not configured.");
    
    const shutdown = async () => {
      await channels.stop();
      process.exit(0);
    };
    
    process.once("SIGTERM", shutdown);
    process.once("SIGINT", shutdown);
    
    await channels.ready({ timeoutMs: 30_000 });
    const status = channels.status();
    if (status.overall !== "online") {
      throw new Error(`Channel not online: ${JSON.stringify(status)}`);
    }

`ready()` observes the first `online` or `setup_required` outcome; it does not initiate Node or Express activation. Inspect `status()` before accepting managed traffic. A configured direct adapter still starts when managed setup is incomplete, while the Channel remains `setup_required` until its managed providers are configured. Observe later drops and reconnects through `status()`.

Status| Meaning  
---|---  
`connecting`| Activation is in progress, or a lazy mount has not started the Channel yet.  
`online`| The managed session is healthy and can receive delivery invitations.  
`setup_required`| The runtime declaration exists but provider setup is incomplete.  
`reconnecting`| The gateway connection dropped and is retrying.  
`error`| Activation or bounded reconnect failed.  
`stopped`| The listener was torn down.
