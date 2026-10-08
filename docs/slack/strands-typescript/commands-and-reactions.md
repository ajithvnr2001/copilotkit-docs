---
url: https://docs.copilotkit.ai/slack/strands-typescript/commands-and-reactions/
title: Slack + AWS Strands (TypeScript): Commands and reactions
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:28:42.674559+00:00
---

# Slack + AWS Strands (TypeScript): Commands and reactions

> Source: https://docs.copilotkit.ai/slack/strands-typescript/commands-and-reactions/

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

Commands and reactions

Build

# Commands and reactions

Understand managed command routing and handle provider reactions through typed Channels APIs.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Managed Slack and Teams treat leading-slash text as ordinary message content. Reaction handlers let an agent respond to lightweight feedback without treating every emoji as a new chat message.

## Managed commands are not dispatched#

The generated Slack manifest does not register slash commands, and managed Teams does not interpret `/name` prefixes. A message such as `/triage customer` therefore reaches `onMessage` or `onMention` as normal text.

`defineChannelCommand`, `commands`, and `onCommand` remain available for direct adapters that emit native command events. They do not opt a managed Slack or Teams Channel into command routing.

## Route mentions and ordinary messages#

Register `onMessage` for ordinary provider messages. A bot mention selects `onMention` when that handler is registered; otherwise the mention falls back to `onMessage`. Non-mention messages select `onMessage`, and one inbound message runs exactly one of those handler paths.

The current generated manifest subscribes to ordinary channel, private-channel, group-DM, and direct-message events in addition to `app_mention`. A Slack app created from an older manifest may need the current event subscriptions and bot scopes applied, followed by an app reinstall.

## Handle incoming reactions#

Known Slack shortcodes and Teams reaction tokens are normalized to portable names. The portable outbound set is `thumbs_up`, `thumbs_down`, `heart`, `fire`, `eyes`, `refresh`, `thinking`, and `tada`.

channel.ts
    
    
    channel.onReaction("eyes", async ({ added, thread, user }) => {
      await thread.post(
        added
          ? `${user?.name ?? "Someone"} marked this response for follow-up.`
          : `${user?.name ?? "Someone"} removed the follow-up marker.`,
      );
    });

Omit the emoji argument to receive every added and removed reaction:

channel.ts
    
    
    channel.onReaction(async ({ emoji, rawEmoji, added, thread }) => {
      audit.record({ emoji, rawEmoji, added });
      await thread.post("Reaction recorded.");
    });

`emoji` is the normalized value when the SDK recognizes it. `rawEmoji` retains the provider token for custom or unmapped emoji.

Output-free handlers are supported

The SDK finalizes and acknowledges a managed turn even when its handler posts no message. Managed delivery is still at-least-once, so make silent audit or database writes idempotent.

The generated Slack manifest subscribes to `reaction_added` and `reaction_removed`. Managed ingress routes reactions on bot output and on user-authored roots and replies back to their existing managed conversation; reactions on unrelated workspace messages are ignored.

## Attach a reaction handler to one message#

Use `Message.onReaction` when only one posted component should react:

feedback-card.tsx
    
    
    import { Message, Section } from "@copilotkit/channels/ui";
    
    export function FeedbackCard({ answerId }: { answerId: string }) {
      return (
        <Message
          onReaction={async (emoji, reaction) => {
            if (reaction.added && emoji === "thumbs_up") {
              await feedback.record(answerId, reaction.user?.id);
              await reaction.thread.post("Thanks for the feedback.");
              return;
            }
            await reaction.thread.post("Reaction update received.");
          }}
        >
          <Section>React with 👍 if this solved the problem.</Section>
        </Message>
      );
    }

Register `FeedbackCard` in `createChannel({ components: [FeedbackCard] })`. Surviving a process restart also requires a durable `StateStore`, because the SDK must reload the component snapshot that owns the callback.

Add or remove the bot's reaction with the delivery-scoped reference from the current message or transcript:

channel.ts
    
    
    channel.onMessage(async ({ message, thread }) => {
      await thread.react(message.ref, "eyes");
      await thread.unreact(message.ref, "eyes");
    });

The portable set works on managed Slack and Teams. A provider-native string is allowed when your code branches on the native provider: use `message.platform` in a message handler or `reaction.thread.platform` in `onReaction`. Unsupported values fail explicitly.

See the [command reference](https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand) and [Message reference](https://docs.copilotkit.ai/reference/channels/components/Message) for the complete handler shapes.

### On this page

Managed commands are not dispatchedRoute mentions and ordinary messagesHandle incoming reactionsAttach a reaction handler to one message
