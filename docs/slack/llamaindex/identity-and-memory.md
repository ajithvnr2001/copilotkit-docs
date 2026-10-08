---
url: https://docs.copilotkit.ai/slack/llamaindex/identity-and-memory/
title: Slack + LlamaIndex: Identity and Memory
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:28:00.642798+00:00
---

# Slack + LlamaIndex: Identity and Memory

> Source: https://docs.copilotkit.ai/slack/llamaindex/identity-and-memory/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/llamaindex)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/llamaindex/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/llamaindex/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/llamaindex/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/llamaindex/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/llamaindex/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/llamaindex/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/llamaindex/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/llamaindex/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/llamaindex/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/llamaindex/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/llamaindex/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/llamaindex/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Identity and Memory

Build

# Identity and Memory

Resolve provider actors to application users and grant Intelligence Memory safely for each Channel run.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Your Channel already receives provider-scoped conversations and actors. This guide maps those actors to your application's users, then grants user or project Memory explicitly for each agent run.

## Separate the conversation, actor, and application user#

One provider conversation can contain several people. Channels therefore keeps three identities separate:

Concept| Meaning| Scope  
---|---|---  
Conversation| Slack thread, channel, or DM represented by the Channels `Thread`| Shared Slack conversation  
Actor| Slack account that caused the current message, reaction, or interaction| Resolved for each event  
Application user| Canonical user returned by your `identifyUser` policy| Developer-owned project identity  
  
A `Thread` does not have a personal owner. The person who installed the app, started the conversation, or sent the first message does not become the Memory subject for later participants. Resolve the current actor independently on every event.

### Map the current provider actor#

`identifyUser` receives the normalized provider, tenant, installation, actor, conversation, and event. Return an application-controlled `{ id, name }` when a trusted mapping exists, or `null` when the actor is intentionally unlinked.

For Slack, `tenant.id` identifies the workspace and `actor.id` identifies the Slack account. Channels, private channels, group DMs, and shared threads can all contain several actors, so include the workspace in the external-identity key.

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { makeAgent } from "./agent.js";
    
    const linkedAccounts = new Map([
      [
        "slack:T0123:U0456",
        { id: "user_42", name: "Ada Lovelace" },
      ],
    ]);
    
    export const channel = createChannel({
      name: "support",
      identifyUser: async ({ provider, tenant, actor }) =>
        linkedAccounts.get(`${provider}:${tenant.id}:${actor.id}`) ?? null,
      agent: makeAgent,
    });

Replace the map with a lookup in the account-linking data your application owns. Do not automatically link accounts by email address, display name, or handle. Those attributes can change or collide across provider tenants.

Returning `null` means that the actor is deliberately unlinked. Throw only when the identity system itself failed. When the adapter provides `lookupProfile`, you may use it to enrich a confirmed provider identity, but profile data does not establish a canonical application account by itself.

### Grant Memory for one run#

Intelligence Memory is off unless the current `runAgent` call grants access. Each `user` or `project` scope accepts `"none"`, `"read"`, or `"read-write"`:

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({
        prompt: message.text,
        memory: {
          user: "read",
          project: "read-write",
        },
      });
    });

Omitting a scope disables it for that run. Project-only Memory works when `identifyUser` returns `null`; user Memory fails before the agent starts unless the current event resolved to an application user.

In a shared channel or group chat, project Memory is the safer default. Grant user Memory only when the current turn clearly acts for the resolved individual. Never reuse the installer, thread creator, or first participant as the personal Memory subject for everyone else.

### Choose the subject when resuming an approval#

A resumed run can grant Memory too. In the callback for a registered component, choose which trusted participant supplies the subject when you grant user Memory:

approval-button.tsx
    
    
    import { Button } from "@copilotkit/channels/ui";
    
    export function ApprovalButton() {
      return (
        <Button
          value={{ approved: true }}
          onClick={async ({ thread, action }) => {
            const value = action.value;
            if (value === undefined) {
              await thread.post("The approval value was missing.");
              return;
            }
    
            await thread.resume(value, {
              memory: {
                user: "read",
                project: "read",
              },
              subject: "initiator",
            });
          }}
        >
          Approve
        </Button>
      );
    }

  * `"initiator"` keeps the application user who started the continuation chain.
  * `"actor"` uses the application user resolved for the current interaction.
  * Project-only Memory needs no subject.
  * Callers cannot provide an arbitrary raw user ID.



Use `"initiator"` when an approval belongs to the person who started the workflow. Use `"actor"` when the current approver should supply the personal context. See [Interactive messages and approvals](https://docs.copilotkit.ai/slack/llamaindex/interactive) for the complete registered component and post-and-resume flow.

### Verify the identity boundary#

Exercise the mapping with separate provider accounts before enabling it in a shared conversation:

  1. Send a message from two actors in the same conversation. Confirm each event looks up the full provider, tenant, and actor tuple and resolves the correct application user independently.
  2. Test an intentionally unlinked actor. A project-only run should work; requesting user Memory should fail with `channel_memory_user_required` before the agent starts.
  3. If the Channel uses approvals, start a workflow as one user and click it as another. Verify `"initiator"` preserves the starter and `"actor"` selects the current approver.
  4. Check application logs and telemetry. Record the stable error code and your application user ID when needed, but do not log provider tokens, message contents, or Memory contents.



The boundary is ready when every event resolves its current actor, personal Memory follows only that resolved user, and project Memory follows the explicit grant for the run.

## Handle stable identity and Memory failures#

Identity and Memory validation fails before the agent runs. The public errors expose stable codes:

Code| Meaning  
---|---  
`channel_identity_invalid`| `identifyUser` returned neither `null` nor a non-empty `{ id, name }` user.  
`channel_identity_failed`| The custom identity resolver threw.  
`channel_memory_grant_invalid`| A Memory scope used an unsupported access value.  
`channel_memory_user_required`| The run requested user Memory without a resolved application user.  
`channel_memory_unavailable`| The Channel has no attached Intelligence Memory-capable runtime or adapter.  
`channel_memory_subject_required`| A resumed run requested user Memory without `"initiator"` or `"actor"`.  
  
Use [Threads and state](https://docs.copilotkit.ai/slack/llamaindex/threads-and-state) for conversation-scoped workflow state and [History and transcripts](https://docs.copilotkit.ai/slack/llamaindex/history-and-transcripts) for provider history and SDK-owned user transcripts. Those records are separate from per-run Intelligence Memory.

### On this page

Separate the conversation, actor, and application userHandle stable identity and Memory failures
