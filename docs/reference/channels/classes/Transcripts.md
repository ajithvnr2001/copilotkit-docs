---
url: https://docs.copilotkit.ai/reference/channels/classes/Transcripts/
title: Transcripts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:15.970217+00:00
---

# Transcripts

> Source: https://docs.copilotkit.ai/reference/channels/classes/Transcripts/

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

# Transcripts

Append, query, retain, and delete an application-owned transcript keyed by a stable user identity.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`Transcripts` stores an optional SDK-owned record on the Channel's `StateStore`. Configure top-level `identifyUser` and `store.transcripts`.

## Configuration
    
    
    const channel = createChannel({
      name: "support-slack",
      identifyUser: ({ actor }) => accounts.resolveApplicationUser(actor.id),
      agent: makeAgent,
      store: {
        adapter: durableStateStore,
        transcripts: {
          retention: "30d",
          maxPerUser: 500,
        },
      },
    });

`retention` accepts milliseconds or a duration string. Entries are stored on the `list` facet, so that facet must be durable for production transcripts.

## append
    
    
    await channel.transcripts.append(
      thread,
      {
        role: "assistant",
        text: "The incident owner is Payments.",
      },
      { userId: "usr_123" },
    );

Append silently does nothing when `userId` is `null`.

## list
    
    
    const entries = await channel.transcripts.list({
      userId: "usr_123",
      limit: 20,
      roles: ["user", "assistant"],
    });

Entries are oldest-first and can be filtered by platform, `threadId`, or role. On managed Channels, `platform` is the native provider (`"slack"` or `"teams"`). Use the stable application `userId` to carry context between providers, and filter by platform only when you want one provider's entries.

## delete
    
    
    const { deleted } = await channel.transcripts.delete({
      userId: "usr_123",
    });

This deletes only the SDK-owned transcript. It does not delete provider history or a separate Intelligence record.

## Automatic bridge

`thread.runAgent({ transcript: true })` injects prior entries, appends the current user turn, runs the agent, and appends its response. Do not manually append those same turns.

`channel.transcripts` becomes available after the runtime starts the Channel. See [History and transcripts](https://docs.copilotkit.ai/slack/history-and-transcripts).
