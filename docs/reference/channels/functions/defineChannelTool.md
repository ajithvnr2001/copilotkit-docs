---
url: https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool/
title: defineChannelTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:21.627716+00:00
---

# defineChannelTool

> Source: https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool/

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

# defineChannelTool

Define a Standard Schema-validated tool with inferred arguments and Channels thread context.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`defineChannelTool` preserves a tool definition while inferring the handler argument type from its Standard Schema.

## Signature
    
    
    function defineChannelTool<Schema extends ObjectSchema>(
      tool: ChannelTool<Schema>,
    ): ChannelTool<Schema>;
    
    
    interface ChannelTool<Schema extends ObjectSchema> {
      name: string;
      description: string;
      parameters: Schema;
      handler(
        args: InferSchemaOutput<Schema>,
        context: ChannelToolContext,
      ): unknown | Promise<unknown>;
    }

## Example

tools.ts
    
    
    import { defineChannelTool } from "@copilotkit/channels";
    import { z } from "zod";
    
    export const getIncident = defineChannelTool({
      name: "get_incident",
      description: "Read an incident by id.",
      parameters: z.object({
        incidentId: z.string(),
      }),
      async handler({ incidentId }) {
        const incident = await incidents.get(incidentId);
        return incident;
      },
    });

Register tools in `createChannel({ tools })`, add one with `channel.tool(tool)` before startup, or pass turn-scoped tools to `thread.runAgent({ tools })`.

## Handler context

Field| Type| Managed behavior  
---|---|---  
`thread`| `Thread`| Current conversation handle.  
`message`| `IncomingMessage | undefined`| Current inbound message when the run began from a message trigger.  
`user`| `ApplicationUser | null`| Application user selected for this event.  
`actor`| `ProviderActor`| Provider account that caused this event.  
`signal`| `AbortSignal | undefined`| Reserved optional field; the current SDK tool runner leaves it undefined.  
`platform`| `string`| Normalized source provider, such as `"slack"` or `"teams"`.  
  
Return raw objects or arrays for data. The SDK JSON-serializes non-string results for the model. A tool that already posted UI should return a short natural-language confirmation so the model does not repeat the card.

See [Tools and context](https://docs.copilotkit.ai/slack/tools) for a complete managed example.
