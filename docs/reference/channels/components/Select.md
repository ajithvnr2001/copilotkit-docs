---
url: https://docs.copilotkit.ai/reference/channels/components/Select/
title: Select
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:19.694088+00:00
---

# Select

> Source: https://docs.copilotkit.ai/reference/channels/components/Select/

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

# Select

Render a portable single- or multi-select control and understand its current managed-provider limits.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`Select` describes a list of string choices.
    
    
    import { Actions, Button, Select } from "@copilotkit/channels/ui";
    
    <Actions>
      <Select
        name="owner"
        placeholder="Choose an owner"
        options={[
          { label: "Payments", value: "payments" },
          { label: "Identity", value: "identity" },
        ]}
        onSelect={async (ctx) => {
          await ctx.thread.post(`Selected ${String(ctx.action.value)}.`);
        }}
      />
      <Button
        value="assign"
        onClick={async (ctx) => {
          const owner = ctx.values?.owner;
          if (owner !== undefined) {
            await ctx.thread.post(`Selected ${String(owner)}.`);
          }
        }}
      >
        Assign
      </Button>
    </Actions>;

## Props

Prop| Type| Description  
---|---|---  
`name`| `string`| Stable field key used in Teams `ctx.values` when a Button submits the card.  
`options`| `{ label: string; value: string }[]`| Required choices.  
`placeholder`| `string`| Native placeholder text.  
`multi`| `boolean`| Allows multiple selections where the provider supports them.  
`onSelect`| `ClickHandler<string | string[]>`| Selection callback. `multi` selections use a string array.  
  
Managed Slack emits a dispatching static select; `multi` becomes a `multi_static_select` input block. Managed Teams renders an Adaptive Card `Input.ChoiceSet`. Slack invokes `Select.onSelect` when the selection is dispatched; Teams sends the selected field to the submitting Button in `ctx.values[name]`. Teams does not dispatch `Select.onSelect` independently.
