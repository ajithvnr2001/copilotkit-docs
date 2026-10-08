---
url: https://docs.copilotkit.ai/reference/channels/types/InteractionContext/
title: InteractionContext
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:23.749776+00:00
---

# InteractionContext

> Source: https://docs.copilotkit.ai/reference/channels/types/InteractionContext/

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

# InteractionContext

The thread, message reference, typed action value, user, and capabilities passed to a component callback.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Buttons, selects, and inputs receive an `InteractionContext<TValue>`.

## Shape
    
    
    interface InteractionContext<TValue = unknown> {
      thread: Thread;
      message: IncomingMessage;
      action: {
        id: string;
        value?: TValue;
      };
      values: Record<string, unknown>;
      user: ApplicationUser | null;
      actor: ProviderActor;
      platform: string;
      openModal?(view: ModalView): Promise<{ ok: boolean; error?: string }>;
    }

Field| Notes  
---|---  
`thread`| Post, update, or resume the current conversation.  
`message`| Message containing the control. Check `message.ref.id` before updating it.  
`action.id`| Opaque SDK action id.  
`action.value`| Round-tripped `Button.value`, selected value, or submitted text. Guard `undefined`.  
`values`| Other submitted form values. Teams `Action.Submit` callbacks include named Adaptive Card input values.  
`user`| Nullable application user selected by `identifyUser`.  
`actor`| Provider account that caused the interaction.  
`platform`| Native provider; managed callbacks report `"slack"` or `"teams"`.  
`openModal`| Capability-gated and omitted on the managed Slack and Teams path.  
      
    
    <Button
      value={{ approved: true }}
      onClick={async ({ thread, message, action }) => {
        if (action.value === undefined) return;
    
        if (message.ref.id) {
          try {
            await thread.update(message.ref, "Approved");
          } catch {
            // Best-effort visual update.
          }
        }
    
        await thread.resume(action.value);
      }}
    >
      Approve
    </Button>

Managed interactions arrive as a later delivery. Return after posting the original control and use `resume()` in its callback; do not block with `awaitChoice()`.
