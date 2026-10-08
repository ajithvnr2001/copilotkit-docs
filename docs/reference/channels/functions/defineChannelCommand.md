---
url: https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand/
title: defineChannelCommand
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:21.594110+00:00
---

# defineChannelCommand

> Source: https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand/

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

# defineChannelCommand

Define a normalized direct-adapter command and its free-text or structured arguments.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`defineChannelCommand` preserves a command definition and infers structured options when the provider supplies them.

## Signature
    
    
    function defineChannelCommand<Schema extends ObjectSchema>(
      command: ChannelCommand<Schema>,
    ): ChannelCommand<Schema>;
    
    
    interface ChannelCommand<Schema extends ObjectSchema> {
      name: string;
      description?: string;
      options?: Schema;
      handler(
        context: CommandContext<InferSchemaOutput<Schema>>,
      ): void | Promise<void>;
    }

## Example

commands.ts
    
    
    import { defineChannelCommand } from "@copilotkit/channels";
    
    export const triage = defineChannelCommand({
      name: "triage",
      description: "Triage the current conversation.",
      async handler({ thread, text, user, platform }) {
        await thread.runAgent({
          prompt: text || "Triage this conversation.",
          context: [
            { description: "Provider", value: platform },
            {
              description: "Invoking user",
              value: user?.name ?? user?.id ?? "unknown",
            },
          ],
        });
      },
    });

Register it with `createChannel({ commands: [triage] })` or `channel.onCommand(triage)` before startup.

Managed Slack and Teams do not dispatch commands: leading-slash content remains a normal message. This API applies when a developer-owned direct adapter emits an `IncomingCommand`.

## CommandContext

Field| Type| Notes  
---|---|---  
`thread`| `Thread`| Conversation where the command was invoked.  
`command`| `string`| Normalized name: no leading slash, lowercase, hyphens and underscores route equivalently.  
`text`| `string`| Raw argument text supplied by the direct adapter.  
`options`| `TOptions`| Structured options when the adapter supplies them.  
`user`| `ApplicationUser | null`| Application user selected by `identifyUser`.  
`actor`| `ProviderActor`| Provider account that invoked the command.  
`platform`| `string`| Native provider reported by the direct adapter.  
`openModal`| function or `undefined`| Present only when the adapter supports modal opening.  
  
See [Commands and reactions](https://docs.copilotkit.ai/slack/commands-and-reactions) for the managed provider boundary.
