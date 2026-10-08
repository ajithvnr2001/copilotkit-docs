---
url: https://docs.copilotkit.ai/reference/channels/components/Message/
title: Message
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:17.874859+00:00
---

# Message

> Source: https://docs.copilotkit.ai/reference/channels/components/Message/

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

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)Components

# Message

Root container for portable Channels content and reaction behavior.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`Message` groups one portable message tree.
    
    
    import { Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Checkout latency is above the SLO.</Section>
    </Message>;

## Props

Prop| Type| Description  
---|---|---  
`accent`| `string`| Optional renderer hint. Direct adapters may map it natively; the current managed Slack and Teams connectors ignore it.  
`onReaction`| `MessageReactionHandler`| Handles an added or removed reaction on this posted message.  
`children`| `BotChildren`| Portable Channels content.  
  
`onReaction` receives the normalized emoji first and a reaction context second. The context contains `added`, `rawEmoji`, `user`, `thread`, `messageId`, and `messageRef`.
    
    
    <Message
      onReaction={async (emoji, reaction) => {
        const marked = reaction.added && emoji === "eyes";
        await reaction.thread.post(
          marked ? "Marked for follow-up." : "Reaction update received.",
        );
      }}
    >
      <Section>React with 👀 to request follow-up.</Section>
    </Message>

Managed Slack routes reactions on bot-authored messages. Managed Teams routes delivered `messageReaction` activities. The managed adapter cannot add or remove the bot's own reactions.

An output-free managed reaction callback is finalized and acknowledged. Silent audit-only work is supported, but make the side effect idempotent because managed delivery is at-least-once.

Register named components containing `onReaction` in `createChannel({ components })`; a durable `StateStore` is also required for a reaction to an older message to survive a process restart.
