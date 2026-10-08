---
url: https://docs.copilotkit.ai/slack/strands-typescript/history-and-transcripts/
title: Slack + AWS Strands (TypeScript): History and transcripts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:28:42.804508+00:00
---

# Slack + AWS Strands (TypeScript): History and transcripts

> Source: https://docs.copilotkit.ai/slack/strands-typescript/history-and-transcripts/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/strands-typescript)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/strands-typescript/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/strands-typescript/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/strands-typescript/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/strands-typescript/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/strands-typescript/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/strands-typescript/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/strands-typescript/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/strands-typescript/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/strands-typescript/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/strands-typescript/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/strands-typescript/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/strands-typescript/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

History and transcripts

Production

# History and transcripts

Distinguish Intelligence-managed conversation history from the optional SDK transcript store, and use each without duplicating turns.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Channels exposes two different history systems:

  * Intelligence-managed conversation history rebuilds the selected provider thread for the agent.
  * SDK transcripts create an application-owned, identity-keyed record that can span providers and conversations.



Choose one based on the behavior you need. They are not interchangeable.

## Use managed conversation history#

On each delivered turn, Intelligence fetches recent messages for that native conversation and seeds a fresh agent instance. The default history limit in the managed adapter is 20 messages.

The current inbound turn is not part of the fetched history. `runAgent()` automatically injects it when `prompt` is omitted. Build an explicit prompt when you need both the message text and hydrated attachments:

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({
        prompt: message.contentParts?.length
          ? [
              ...(message.text
                ? [{ type: "text" as const, text: message.text }]
                : []),
              ...message.contentParts,
            ]
          : message.text,
      });
    });

Create a fresh agent for every `conversationKey`; the managed adapter assigns the reconstructed messages to that instance. Sharing one mutable agent between threads can leak or overwrite history.

## Read the current provider thread#

`thread.getMessages()` returns a best-effort, oldest-first text view of recent history:

read-thread.ts
    
    
    const messages = await thread.getMessages();
    const transcript = messages
      .map((message) => `${message.isBot ? "Agent" : "User"}: ${message.text}`)
      .join("\n");

On the managed path, history-fetch failures return `[]` instead of failing the turn. The method is text-oriented: binary image, audio, and video content is available to the agent through multimodal history, but is not reproduced as binary data in `ThreadMessage`.

## Add cross-platform SDK transcripts#

Use SDK transcripts when your application needs a user-centric record across Slack and Teams. Configure top-level `identifyUser` and `store.transcripts`. When identity resolves to `null`, the transcript bridge skips personal reads and writes.

Resolve the current actor first

Read [Identity and Memory](https://docs.copilotkit.ai/slack/strands-typescript/identity-and-memory) before using a provider actor as an application user. A shared provider conversation has no personal owner, and each event resolves its actor independently.

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { durableStateStore } from "./state-store.js";
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: async ({ provider, actor }) => {
        const account = await accounts.findByExternalIdentity({
          provider,
          externalUserId: actor.id,
        });
        return account ? { id: account.id, name: account.name } : null;
      },
      agent: makeAgent,
      store: {
        adapter: durableStateStore,
        transcripts: {
          retention: "30d",
          maxPerUser: 500,
        },
      },
    });

Provider user ids are not cross-platform identities. Resolve them to a stable application user id, verified email, or another identity your application controls. Returning `null` skips transcript storage for that turn.

The transcript list facet must be durable if this record must survive a restart. The default `MemoryStore` is not sufficient.

## Let `runAgent` bridge the transcript once#

Set `transcript: true` to inject prior SDK transcript entries, append the current user turn, run the agent, and capture its reply:

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({
        prompt: message.text,
        transcript: { limit: 20 },
      });
    });

Do not also call `channel.transcripts.append()` for the same user and assistant turns. `runAgent({ transcript: ... })` owns that bridge and manual appends would duplicate the record.

## Query and delete the application record#

`channel.transcripts` is available after the runner starts the Channel:

transcripts.ts
    
    
    const recent = await channel.transcripts.list({
      userId: "usr_123",
      limit: 50,
    });
    
    const { deleted } = await channel.transcripts.delete({
      userId: "usr_123",
    });

`list()` returns entries oldest-first. You can filter by platform, thread id, or role. Managed entries use the native `"slack"` or `"teams"` provider. Resolve cross-provider identity through the application `userId`; use the platform filter only when you intentionally want one provider's entries.

`delete()` removes the SDK-owned transcript for that user; provider history and any separate Intelligence retention policy remain independent.

## Pick the right source#

Need| Use  
---|---  
Continue the current Slack or Teams conversation| Managed conversation history  
Inspect recent text in one provider thread| `thread.getMessages()`  
Carry user context between Slack and Teams| SDK transcripts with a stable identity  
Store workflow progress| `thread.state()`  
Meet application deletion or retention requirements| A durable SDK transcript store plus your provider/Intelligence policies  
  
See the [`Transcripts` reference](https://docs.copilotkit.ai/reference/channels/classes/Transcripts) and [persistence guide](https://docs.copilotkit.ai/slack/strands-typescript/persistence-and-scaling) before enabling this in production.

### On this page

Use managed conversation historyRead the current provider threadAdd cross-platform SDK transcriptsLet runAgent bridge the transcript onceQuery and delete the application recordPick the right source
