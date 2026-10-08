---
url: https://docs.copilotkit.ai/reference/channels/types/IncomingMessage/
title: IncomingMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:23.623219+00:00
---

# IncomingMessage

> Source: https://docs.copilotkit.ai/reference/channels/types/IncomingMessage/

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

# IncomingMessage

The normalized provider message passed to Channels handlers, including user, multimodal parts, and managed correlation ids.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`IncomingMessage` is the normalized inbound turn passed to `onMessage`, `onMention`, tools, and interaction contexts.

## Shape
    
    
    interface IncomingMessage {
      text: string;
      user: ApplicationUser | null;
      actor: ProviderActor;
      ref: MessageRef;
      platform: string;
      contentParts?: AgentContentPart[];
      eventId?: string;
      turnId?: string;
      deliveryId?: string;
    }

Field| Managed Slack and Teams behavior  
---|---  
`text`| Provider text after ingress normalization.  
`user`| Nullable application user returned by the Channel's `identifyUser` policy.  
`actor`| Provider account that caused the event. It includes a required actor kind.  
`ref`| In ordinary message handlers this may have an empty id; do not assume every inbound turn can be edited.  
`platform`| Native source: `"slack"` or `"teams"` for message deliveries.  
`contentParts`| Hydrated file/media parts when attachments were retrieved.  
`eventId`| Stable provider-event id for application idempotency.  
`turnId`| Managed turn correlation id.  
`deliveryId`| Managed lease/delivery correlation id.  
  
## Multimodal prompt
    
    
    const prompt = message.contentParts?.length
      ? [
          ...(message.text ? [{ type: "text" as const, text: message.text }] : []),
          ...message.contentParts,
        ]
      : message.text;
    
    await thread.runAgent({ prompt });

Managed history excludes the current inbound turn. `runAgent()` injects the message automatically when `prompt` is omitted; use the explicit combined prompt above when a turn can contain both text and attachments. See [Files and multimodal input](https://docs.copilotkit.ai/slack/files-and-multimodality).
