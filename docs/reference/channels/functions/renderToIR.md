---
url: https://docs.copilotkit.ai/reference/channels/functions/renderToIR/
title: renderToIR
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:21.709943+00:00
---

# renderToIR

> Source: https://docs.copilotkit.ai/reference/channels/functions/renderToIR/

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

# renderToIR

Lower Channels JSX or text into the serializable ChannelNode intermediate representation.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`renderToIR(renderable)` expands fragments and function components into an array of intrinsic `ChannelNode` values.

## Signature
    
    
    function renderToIR(ui: Renderable): ChannelNode[];
    
    
    type Renderable =
      | string
      | ChannelNode
      | ChannelNode[]
      | { raw: unknown; provider?: "slack" | "teams" };

## Example
    
    
    import { Header, Message, renderToIR } from "@copilotkit/channels/ui";
    
    const ir = renderToIR(
      <Message>
        <Header>Incident update</Header>
      </Message>,
    );

The runtime calls this automatically before binding callbacks and rendering a message. Use it directly for component tests or a custom adapter.

Strings—and numbers used as component children—become `text` nodes. `false`, `null`, and `undefined` render nothing. Function components are evaluated immediately, so keep them pure and free of provider side effects.

The `{ raw, provider }` escape hatch produces a provider-specific `raw` node. Use `provider: "slack"` for native blocks and `provider: "teams"` for one Adaptive Card object. Omitting `provider` defaults to Slack. A raw node sent through the wrong active provider fails explicitly before that effect reaches the provider; it is never translated or silently dropped.
