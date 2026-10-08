---
url: https://docs.copilotkit.ai/reference/channels/functions/createChannel/
title: createChannel
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:19.792912+00:00
---

# createChannel

> Source: https://docs.copilotkit.ai/reference/channels/functions/createChannel/

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

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)Functions

# createChannel

Declare a managed Slack or Teams Channel, its agent, handlers, tools, components, and SDK persistence.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`createChannel(options)` creates the provider-neutral Channel registered with `CopilotRuntime({ channels })`.

## Signature
    
    
    function createChannel<TStateSchema>(
      options: CreateChannelOptions<TStateSchema>,
    ): Channel<ThreadStateOf<TStateSchema>>;

Import it from the umbrella package:
    
    
    import { createChannel } from "@copilotkit/channels";

## Managed example

channel.ts
    
    
    const channel = createChannel({
      name: "support",
      identifyUser: "platform",
      agent: makeAgent,
      tools: [getIncident],
      context: [
        {
          description: "Response style",
          value: "Put the next action first.",
        },
      ],
    });
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({ prompt: message.text });
    });

The Channel name is the project-unique Intelligence Code. A single managed runtime declares both Slack and Teams for that Channel; Intelligence routes each prepared delivery only to its originating provider.

Handlers that reply directly without `runAgent()` may omit `agent`.

## Options

Option| Type| Notes  
---|---|---  
`name`| `string`| Required for managed delivery. Must match the project-unique Intelligence Code.  
`identifyUser`| `"platform" | ChannelIdentifyUser`| Required. Maps each provider actor to an application user or `null`. See the Identity and Memory guide for [Slack](https://docs.copilotkit.ai/slack/identity-and-memory) or [Teams](https://docs.copilotkit.ai/teams/identity-and-memory).  
`showToolStatus`| `boolean`| Managed Slack hides tool-call progress by default. Set `true` to show it; tool history remains available in Intelligence either way.  
`replyContinuation`| `ReplyContinuationOptions`| Managed Slack continuation limits. Direct Slack configures the same option on `slack()`.  
`agent`| `AbstractAgent | (threadId) => AbstractAgent`| Required when calling `thread.runAgent()`. Not inherited from `runtime.agents`. Prefer a factory.  
`sanitizeAgentEvents`| `boolean`| Defaults to `true`. Repairs the known nullable AG-UI parent-message field before strict HTTP-stream validation.  
`tools`| `ChannelTool[]`| Channel-level typed tools.  
`context`| `ContextEntry[]`| Stable context added to every agent run.  
`components`| `ChannelComponent[]`| Named JSX components used to reconstruct callbacks.  
`commands`| `ChannelCommand[]`| Declared commands routed from provider ingress.  
`store`| `StoreConfig`| State, persistence, turn concurrency (`parallel` default), transcripts, and dedup.  
`adapters`| `PlatformAdapter[]`| Developer-owned direct transports that may coexist with the cloud-hosted Intelligence adapter.  
  
The managed runtime validates `name` as lowercase kebab-case, 3–64 characters, not equal to `channels`, and unique within the Runtime.

Handlers receive both the required provider `actor` and the nullable application `user`. The SDK resolves that pair once for each incoming event. Both objects are immutable snapshots. The SDK does not link accounts by email, name, or handle.

Malformed callback output rejects with `channel_identity_invalid`. A callback exception rejects with `channel_identity_failed` and never falls back to the standard platform policy.

### Tune long Slack replies

Slack replies continue into additional messages when they exceed one message's soft byte limit. The defaults are 11,000 UTF-8 bytes per message and 20 messages per reply, followed by a visible English truncation notice. Most Channels should keep those defaults; customize them when the product needs a tighter bound or a localized notice:

Field| Behavior  
---|---  
`messageByteLimit`| Soft UTF-8 byte limit before continuing into another Slack message.  
`maxMessages`| Maximum messages occupied by one reply before truncation.  
`truncationMarker`| Visible notice appended when the message limit is reached.  
      
    
    const channel = createChannel({
      name: "support",
      identifyUser: "platform",
      agent: makeAgent,
      replyContinuation: {
        maxMessages: 8,
        truncationMarker: "\n\n_This reply was shortened for Slack._",
      },
    });

### Sanitize HTTP agent events

`sanitizeAgentEvents` defaults to `true`. It repairs the nullable `parentMessageId` emitted by some LangGraph tool-call and interrupt streams so strict client validation does not abort the run. The sanitizer applies only to agents that stream over HTTP and only to the known malformed field. Set it to `false` to forward events unchanged and let malformed events fail validation.

Every run uses a distinct result from `agent.clone()`, including when `agent` is a factory. A custom agent whose subclass fields contain configuration should override `clone()` to preserve that configuration without sharing mutable per-run state. Channels 0.6.1 warns when enumerable fields are dropped; that warning alone no longer refuses the turn.

## Registration methods

The returned Channel supports:

  * `onMessage` and `onMention`
  * `onWelcome`
  * `onInterrupt`
  * `onInteraction`
  * `onCommand`
  * `onReaction`
  * `onThreadStarted`
  * `onModalSubmit` and `onModalClose` for adapters that support modals
  * `tool` to add a tool before the Channel starts



See [`Channel`](https://docs.copilotkit.ai/reference/channels/classes/Channel) for handler signatures and [`StoreConfig`](https://docs.copilotkit.ai/reference/channels/types/StoreConfig) for persistence.
