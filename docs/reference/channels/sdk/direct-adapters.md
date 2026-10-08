---
url: https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters/
title: Direct provider adapters
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:21.770733+00:00
---

# Direct provider adapters

> Source: https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters/

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

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)Sdk

# Direct provider adapters

Public Slack, Teams, Discord, Telegram, and WhatsApp adapter entry points in @copilotkit/channels.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`@copilotkit/channels` supports two provider-connection models:

Model| Channel declaration| Provider connection| Available providers  
---|---|---|---  
Cloud-hosted Intelligence| `createChannel({ name, identifyUser, agent })`| CopilotKit Intelligence stores provider credentials and owns ingress and egress| Slack and Microsoft Teams  
Direct adapter| `createChannel({ name, adapters, identifyUser, agent })`| Your Channels process stores provider credentials and owns the provider socket or webhook| Slack, Microsoft Teams, Discord, Telegram, and WhatsApp  
  
Cloud-hosted Intelligence support for Discord and WhatsApp is coming soon. Their direct adapters already ship in `@copilotkit/channels`.

Direct does not mean standalone

A direct adapter moves the provider connection into your process. The `CopilotRuntime` still owns the Channel lifecycle and uses an Intelligence connection. Direct provider traffic does not traverse the managed Realtime Gateway or its canonical delivery, retry, and durability layer, so your process owns transport reliability. There is no public `channel.start()` method.

## Declare a direct adapter

Install the umbrella package and its tested runtime version:

Use this tested package combination. Keep exact versions in your lockfile and verify compatibility before changing either package.

Terminal
    
    
    npm install --save-exact @copilotkit/channels@0.11.0 @copilotkit/runtime@1.73.3

The package and all provider subpaths are ESM-only public exports. Use `import`; CommonJS `require()` is not supported.

Import adapters from the package's provider subpaths:

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { slack } from "@copilotkit/channels/slack";
    import { makeAgent } from "./agent.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing required environment variable: ${name}`);
      return value;
    }
    
    export const channel = createChannel({
      name: "support-direct",
      identifyUser: "platform",
      adapters: [
        slack({
          botToken: required("SLACK_BOT_TOKEN"),
          appToken: required("SLACK_APP_TOKEN"),
          replyContinuation: {
            maxMessages: 8,
          },
        }),
      ],
      agent: makeAgent,
    });
    
    channel.onMessage(async ({ thread }) => {
      await thread.runAgent();
    });

Pass this Channel to `new CopilotRuntime({ channels: [channel], ... })` and start it through the runtime's Channels control, just as in the managed quickstarts. Intelligence-attached Slack and Teams connections select the managed provider; there is no `provider` option on `createChannel`. Direct adapters may coexist on the same Channel and keep their own provider traffic.

One direct Channel may contain multiple direct adapters. Its `name` must still be present and unique among the Channels declared on that `CopilotRuntime`.

## Provider entry points

### Slack
    
    
    import {
      slack,
      SlackAdapter,
      type SlackAdapterOptions,
    } from "@copilotkit/channels/slack";

`SlackAdapterOptions` requires `botToken` and `appToken`. Socket Mode is on by default. HTTP mode requires `socketMode: false` and a `signingSecret`. `replyContinuation` accepts `messageByteLimit`, `maxMessages`, and `truncationMarker` for long replies; the defaults are 11,000 UTF-8 bytes and 20 messages with a visible truncation notice.

The Slack entry point also exports its listener, renderers, codec, streaming helpers, conversation store, built-in context and tools, file helpers, and `SLACK_LIMITS`. Lower-level render and codec entry points are available from `@copilotkit/channels/slack/render` and `@copilotkit/channels/slack/codec`.

### Microsoft Teams
    
    
    import {
      teams,
      TeamsAdapter,
      type TeamsAdapterOptions,
    } from "@copilotkit/channels/teams";

`TeamsAdapterOptions` accepts `clientId`, `clientSecret`, `tenantId`, and `port`. `clientId` and `clientSecret` are required for real Teams; `tenantId` may be omitted for a multi-tenant deployment. These values fall back to the lowercase `clientId`, `clientSecret`, and `tenantId` environment variables. All three may be omitted only for anonymous local development with the Microsoft 365 Agents Playground. The adapter serves `POST /api/messages` on port `3978` by default.

The Teams entry point also exports its server, Adaptive Card renderer, conversation store, message stream, interaction helpers, file helpers, and `TEAMS_LIMITS`. Renderer exports are also available from `@copilotkit/channels/teams/render`.

### Discord
    
    
    import {
      discord,
      DiscordAdapter,
      type DiscordAdapterOptions,
    } from "@copilotkit/channels/discord";

`DiscordAdapterOptions` requires `botToken` and `appId`; set `guildId` to register slash commands immediately in one development guild. The entry point also exports its listener, renderer, command registration, conversation store, streaming helpers, built-in context and tools, file helpers, and `DISCORD_LIMITS`.

Enable the privileged **Message Content Intent** and **Server Members Intent** for the bot in the Discord Developer Portal. The adapter requests `MessageContent` and `GuildMembers` on every connection.

### Telegram
    
    
    import {
      telegram,
      TelegramAdapter,
      type TelegramAdapterOptions,
    } from "@copilotkit/channels/telegram";

`TelegramAdapterOptions` requires a bot `token`. Ingress defaults to long-polling. Set `mode: "webhook"` and provide `webhook` configuration for a public webhook deployment. The entry point also exports its listener, renderer, conversation store, streaming helper, built-in context and tools, file helpers, and `TELEGRAM_LIMITS`.

### WhatsApp
    
    
    import {
      whatsapp,
      WhatsAppAdapter,
      type WhatsAppAdapterOptions,
    } from "@copilotkit/channels/whatsapp";

`WhatsAppAdapterOptions` requires `accessToken`, `phoneNumberId`, `appSecret`, and `verifyToken`. The webhook server uses port `3000` and path `/webhook` by default. The entry point also exports its client, renderer, conversation and history stores, built-in context and tools, file helpers, and `WA_LIMITS`.

## Capability boundaries

Direct and managed adapters do not have identical capabilities. For example, the direct Slack adapter supports modals, reactions, incremental streaming, and ephemeral messages. Managed Slack accepts the streaming API but buffers the stream and posts it once instead of updating incrementally; it does not support the other three capabilities. Check the direct adapter instance's read-only `capabilities` property when you own the adapter. Capability-result Thread methods can also return `{ ok: false }`; handle that result instead of assuming a provider name guarantees one behavior.

The provider guides document the managed contract and each provider's release status. Use this page when your deployment intentionally owns provider credentials, sockets, webhooks, and provider-specific operations.
