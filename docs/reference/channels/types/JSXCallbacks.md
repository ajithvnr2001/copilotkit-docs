---
url: https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks/
title: JSX callbacks
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:23.686028+00:00
---

# JSX callbacks

> Source: https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks/

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

# JSX callbacks

Reference for portable component handlers and their managed Slack and Teams interaction context.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Portable Channels components can carry callbacks. Slack and Teams receive opaque action ids; the SDK resolves the original handler when the interaction returns.

Slack renders the controls as Block Kit. With Slack app Interactivity enabled, clicks arrive as `block_actions` through the signed managed webhook.

Teams renders the controls in Adaptive Cards. Buttons use `Action.Submit`, and clicks return through the managed connection as message activities. A Teams `Action.Submit` activity can arrive without a source message ref; in that case, `message.ref.id` is empty.

## Callback props

Component| Prop| Handler value  
---|---|---  
`Button`| `onClick`| `InteractionContext<TValue>`; read the Button's `value` from `action.value`  
`Select`| `onSelect`| `InteractionContext<string | string[]>`; arrays are used when `multi` is set  
`Input`| `onSubmit`| `InteractionContext<string>` containing the submitted text  
`Message`| `onReaction`| `(emoji, reaction)`  
  
Managed Teams control boundary

Managed Teams dispatches `Button` submissions. Named `Select` and `Input` fields from the same Adaptive Card are available on that Button callback as `ctx.values`, but Teams does not dispatch their `onSelect` or `onSubmit` callbacks independently.

## Portable component props

Import these components from `@copilotkit/channels/ui`. Renderers may simplify or omit a component when the native provider has no equivalent.

Component| Key props  
---|---  
`Message`| `accent?`, `onReaction?`, `children?`  
`Header`, `Section`, `Markdown`, `Context`, `Actions`| `children?`  
`Fields` / `Field`| `children?`; `Field` also accepts `label?`  
`Button`| `value?`, `onClick?`, `url?`, `style?: "primary" | "danger"`, `children?`  
`Select`| `name?`, `options`, `placeholder?`, `multi?`, `onSelect?`  
`Input`| `name?`, `placeholder?`, `multiline?`, `onSubmit?`  
`Image`| `url`, `alt?`  
`Divider`| No props or children  
`Table` / `Row` / `Cell`| `Table.columns?`; nested rows and cells are children  
`Chart`| `data`, plus optional `type`, `title`, `xAxisTitle`, and `yAxisTitle`  
  
`Button.url` creates a link button and ignores `value` and `onClick`. `Select.options` is an array of `{ label, value }`. `Chart.data` is an array of `{ label, value }`; unsupported native chart surfaces omit the chart.

## InteractionContext

`Button`, `Select`, and `Input` callbacks receive:

Field| Type| Description  
---|---|---  
`thread`| `Thread`| Post, update, run, or resume the conversation.  
`message`| `IncomingMessage`| Message containing the control. Its ref is updateable only when the interaction carries a non-empty `message.ref.id`.  
`action.id`| `string`| Opaque action identifier.  
`action.value`| `TValue | undefined`| The control's round-tripped value. Guard it before use even when the component declares `value`.  
`values`| `Record<string, unknown>`| Submitted form values.  
`user`| `ApplicationUser | null`| Application user selected by `identifyUser`.  
`actor`| `ProviderActor`| Provider account that caused the interaction.  
`platform`| `string`| Normalized source provider, such as `"slack"` or `"teams"`.  
`openModal`| function or `undefined`| Capability-gated modal opener. Not part of the managed Slack/Teams realtime path.  
  
decision.tsx
    
    
    import { Actions, Button, Message, Section } from "@copilotkit/channels/ui";
    
    export function Decision({ id }: { id: string }) {
      return (
        <Message>
          <Section>{`Approve ${id}?`}</Section>
          <Actions>
            <Button
              value={{ id, approved: true }}
              onClick={async ({ thread, message, action }) => {
                const value = action.value;
                if (value === undefined) return;
    
                if (message.ref.id) {
                  try {
                    await thread.update(message.ref, `Approved ${value.id}.`);
                  } catch {
                    // Updating the card is best-effort; always resume the agent.
                  }
                }
                await thread.resume(value);
              }}
            >
              Approve
            </Button>
          </Actions>
        </Message>
      );
    }

An interaction ref is updateable only when `message.ref.id` is non-empty. Always resume outside the update guard and error handler so an omitted ref or failed card update cannot strand the interrupted run.

## Reaction callback

`Message.onReaction` receives `(emoji, reaction)`. The reaction contains `added`, `user`, `messageId`, `messageRef`, and `thread`. Managed reaction delivery is provider-dependent; do not require it for a cross-platform approval. An output-free managed callback is finalized and acknowledged, but application side effects should remain idempotent because managed delivery is at-least-once.

## Registration and persistence

Register every named component that carries a callback:

channel.tsx
    
    
    import { createChannel } from "@copilotkit/channels";
    import { makeAgent } from "./agent.js";
    import { Decision } from "./decision.js";
    import { durableStateStore } from "./state-store.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing ${name}`);
      return value;
    }
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      components: [Decision],
      store: { adapter: durableStateStore },
    });

The same Channel declaration handles managed Slack and Teams deliveries.

Registration allows the action registry to rebuild the callback from the component name and serializable props. A durable `StateStore` is still required for clicks on messages posted before a process restart.

See the interactive messages and approvals guide for [Slack](https://docs.copilotkit.ai/slack/interactive) or [Teams](https://docs.copilotkit.ai/teams/interactive) for the full post-and-resume flow.
