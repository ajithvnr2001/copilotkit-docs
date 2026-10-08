---
url: https://docs.copilotkit.ai/reference/channels/
title: Channels SDK
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:13.259435+00:00
---

# Channels SDK

> Source: https://docs.copilotkit.ai/reference/channels/

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

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)

# Channels SDK

API reference for managed and direct provider agents built with @copilotkit/channels.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The Channels SDK connects an agent to chat providers through a long-running `@copilotkit/channels` process. In the managed Slack and Microsoft Teams path, CopilotKit Intelligence owns the provider connection while your process owns the agent, tools, approvals, state, and deployment. The package also exports developer-operated direct adapters for Slack, Teams, Discord, Telegram, and WhatsApp.

Use this tested package combination. Keep exact versions in your lockfile and verify compatibility before changing either package.

Terminal
    
    
    npm install --save-exact @copilotkit/channels@0.11.0 @copilotkit/runtime@1.73.3

## API reference

### [createChannelDeclare a managed provider or developer-operated direct adapter and attach the Channel to CopilotRuntime.](https://docs.copilotkit.ai/reference/channels/functions/createChannel)### [ChannelConfigure managed or direct delivery, register handlers and tools, configure storage, and inspect the Channel declaration.](https://docs.copilotkit.ai/reference/channels/classes/Channel)### [ThreadPost and update messages, run or resume the agent, read history, and manage conversation state.](https://docs.copilotkit.ai/reference/channels/classes/Thread)### [StateStorePersist workflow state, callback snapshots, transcripts, locks, deduplication, and queues.](https://docs.copilotkit.ai/reference/channels/types/StateStore)

### Classes

  * [`Channel`](https://docs.copilotkit.ai/reference/channels/classes/Channel)
  * [`Thread`](https://docs.copilotkit.ai/reference/channels/classes/Thread)
  * [`MemoryStore`](https://docs.copilotkit.ai/reference/channels/classes/MemoryStore)
  * [`Transcripts`](https://docs.copilotkit.ai/reference/channels/classes/Transcripts)



### Functions

  * [`createChannel`](https://docs.copilotkit.ai/reference/channels/functions/createChannel)
  * [`defineChannelTool`](https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool)
  * [`defineChannelCommand`](https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand)
  * [`bind`](https://docs.copilotkit.ai/reference/channels/functions/bind)
  * [`renderToIR`](https://docs.copilotkit.ai/reference/channels/functions/renderToIR)



### Message components

  * [`Message`](https://docs.copilotkit.ai/reference/channels/components/Message)
  * [`Header`](https://docs.copilotkit.ai/reference/channels/components/Header)
  * [`Section`](https://docs.copilotkit.ai/reference/channels/components/Section) and [`Markdown`](https://docs.copilotkit.ai/reference/channels/components/Markdown)
  * [`Fields` and `Field`](https://docs.copilotkit.ai/reference/channels/components/Fields)
  * [`Context`](https://docs.copilotkit.ai/reference/channels/components/Context)
  * [`Image`](https://docs.copilotkit.ai/reference/channels/components/Image) and [`Divider`](https://docs.copilotkit.ai/reference/channels/components/Divider)
  * [`Table`, `Row`, and `Cell`](https://docs.copilotkit.ai/reference/channels/components/Table)
  * [`Chart`](https://docs.copilotkit.ai/reference/channels/components/Chart)



### Interactive components

  * [`Actions`](https://docs.copilotkit.ai/reference/channels/components/Actions)
  * [`Button`](https://docs.copilotkit.ai/reference/channels/components/Button)
  * [`Select`](https://docs.copilotkit.ai/reference/channels/components/Select)
  * [`Input`](https://docs.copilotkit.ai/reference/channels/components/Input)
  * [`Modal components`](https://docs.copilotkit.ai/reference/channels/components/Modal) — exported for direct adapters; unavailable on managed Slack and Teams
  * [`JSX callbacks`](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks)



### Types

  * [`IncomingMessage`](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage)
  * [`AgentContentPart`](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart)
  * [`InteractionContext`](https://docs.copilotkit.ai/reference/channels/types/InteractionContext)
  * [`MessageRef`](https://docs.copilotkit.ai/reference/channels/types/MessageRef)
  * [`StoreConfig`](https://docs.copilotkit.ai/reference/channels/types/StoreConfig)
  * [`StateStore`](https://docs.copilotkit.ai/reference/channels/types/StateStore)
  * [`ChannelNode`](https://docs.copilotkit.ai/reference/channels/types/ChannelNode)
  * [`ActionStore`](https://docs.copilotkit.ai/reference/channels/types/ActionStore) — deprecated migration reference



### Provider SDKs

  * [`Direct provider adapters`](https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters) — public entry points, required options, and the boundary between managed and developer-operated delivery



## Provider guides

Start with the provider and agent framework you are deploying:

  * [Connect and run your agent in Slack](https://docs.copilotkit.ai/slack/connect)
  * [Connect and run your agent in Microsoft Teams](https://docs.copilotkit.ai/teams/connect)



The provider picker in those guides keeps the same task and selected agent framework when you switch between Slack and Teams.
