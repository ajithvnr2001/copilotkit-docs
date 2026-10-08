---
url: https://docs.copilotkit.ai/slack/strands-typescript/deploy-and-operate/
title: Slack + AWS Strands (TypeScript): Deploy and operate
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:28:42.745944+00:00
---

# Slack + AWS Strands (TypeScript): Deploy and operate

> Source: https://docs.copilotkit.ai/slack/strands-typescript/deploy-and-operate/

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

Deploy and operate

Production

# Deploy and operate

Run a production Channels listener, expose truthful health checks, handle reconnects and shutdown, and diagnose Intelligence status.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

A managed Channel is a long-running worker with an outbound realtime connection. It is not a serverless request handler. Deploy it like a queue consumer or WebSocket worker.

## Use the tested runtime pair#

Use this tested package combination. Keep exact versions in your lockfile and verify compatibility before changing either package.

Terminal
    
    
    npm install --save-exact @copilotkit/channels@0.11.0 @copilotkit/runtime@1.73.3

Run Node.js 22 or later. The managed launcher relies on the global `WebSocket` available in Node.js 22+.

After changing either package, run the same real-provider smoke test used for the initial quickstart.

## Settle before reporting ready#

Creating the Node listener starts the managed connection — a declared Channel connects because it was declared, with no start call to forget. Await `ready()` to observe that activation settling, then inspect `status()`:

health.ts
    
    
    const channels = listener.channels;
    
    await channels.ready({ timeoutMs: 30_000 });
    
    const initial = channels.status();
    if (initial.overall !== "online") {
      throw new Error(`Channels not online: ${JSON.stringify(initial)}`);
    }

`ready()` can resolve in `setup_required`; it means activation settled, not that delivery is healthy. Treat only `status().overall === "online"` as a healthy connected activation.

The runtime status values are:

Runtime status| Meaning  
---|---  
`connecting`| Activation has not settled  
`online`| The managed connection is healthy and can claim delivery invitations  
`setup_required`| The Intelligence provider setup is incomplete  
`reconnecting`| The gateway connection dropped and is retrying  
`error`| Activation failed, or reconnect give-up (~60s default) marked the session not-sendable  
`stopped`| The Channels control was stopped  
  
Treat post-online `error` carefully: after reconnect give-up the client marks `error` while Phoenix **keeps retrying underneath**. A successful rejoin restores `online` without a process restart. Activation-time `error` (bad key, unreachable gateway, config) is different — fix configuration and restart the worker.

The Intelligence UI translates provider and runtime details into its own operator-facing states such as **Waiting for runtime** , **Conflict** , **Offline** , **Delivery failing** , and **Online**.

## Expose liveness and readiness separately#

  * Liveness answers whether the Node process and event loop are running.
  * Readiness answers whether `channels.status().overall` is `online`.



Do not restart immediately for a short `reconnecting` episode; the realtime client owns bounded reconnect and rejoin (default reconnect give-up window is about 60 seconds, then status becomes `error` while retries continue). Alert on `error`; restart only when your own outage budget is exceeded or activation failed before ever going online.

Poll `status()` from your health endpoint or monitoring loop. Do not cache the startup result forever because an online session can later become reconnecting or error.

## Shut down cleanly#

Register signal handlers before **creating the listener** , not just before `ready()`. Creating it begins activation, so a signal that arrives during the connect window must already have somewhere to land — otherwise it hits Node's default handler and leaves a live gateway session behind:

channel.ts
    
    
    let teardown: (() => Promise<void>) | undefined;
    const shutdown = async () => {
      await teardown?.();
    };
    
    process.once("SIGINT", shutdown);
    process.once("SIGTERM", shutdown);
    
    const listener = createCopilotNodeListener({ runtime });
    const server = createServer(listener);
    teardown = async () => {
      await listener.channels.stop();
      if (server.listening) server.close();
    };
    
    await listener.channels.ready({ timeoutMs: 30_000 });

Give the worker enough termination grace to stop its managed sessions. Avoid cutting power before `channels.stop()` has released ownership when a graceful shutdown is possible.

## Store and rotate secrets#

Keep these server-side:

.env
    
    
    CPK_INTELLIGENCE_API_KEY=<project-runtime-key>
    CHANNEL_CODE=<exact-intelligence-code>
    
    # Optional paired overrides for self-hosted or non-production Intelligence:
    # INTELLIGENCE_API_URL=https://intelligence.example.com
    # INTELLIGENCE_GATEWAY_WS_URL=wss://realtime.intelligence.example.com

Cloud-hosted Intelligence supplies the default endpoints. For a self-hosted or non-production deployment, override both bases together. Do not derive one from the other or append `/api`, `/socket`, `/runner`, `/client`, or `/channels`.

Provider credentials stay in Intelligence. The runner should not contain Slack tokens or the Teams client secret. Rotate the project runtime key through your secret manager, restart the listener with the new value, and verify it returns to **Online**.

## Bound active replicas#

Intelligence offers each prepared delivery to connected Runtimes that declare the matching Channel. One Runtime claims that delivery; other replicas can claim different deliveries at the same time.

Run the same build and Channel declarations on every replica. The managed listener bounds active and pending delivery work internally. A full Runtime declines an invitation before it claims the delivery, which leaves another eligible replica free to claim it. That capacity is not currently exposed as a public Channel configuration option.

## Observe the full delivery path#

At minimum, record:

  * startup and the first non-online status
  * transitions to `reconnecting`, `error`, and back to `online`
  * Channel Code and provider, without credentials
  * application tool errors and their idempotency ids
  * `message.eventId`, `message.turnId`, and `message.deliveryId` for correlation
  * `thread.postFile()` failures



Do not log message bodies, hydrated files, API keys, Slack tokens, Teams secrets, or raw provider payloads by default.

## Release checklist#

  1. Build and typecheck the runner on Node.js 22.
  2. Confirm the exact package pair is in the lockfile.
  3. Start the intended replica set and wait for each listener to report `online`.
  4. Send a real provider message and verify a reply.
  5. Exercise one tool, one rich message, and one interaction.
  6. Restart with a pending approval and confirm your persistence promise.
  7. Test a brief network drop and observe `reconnecting` recovery.
  8. Send concurrent messages and verify replicas claim distinct deliveries within their local bounds.
  9. Send `SIGTERM` and confirm graceful shutdown.



Use the [Intelligence walkthrough](https://docs.copilotkit.ai/slack/strands-typescript/intelligence) for control-plane statuses and [persistence and scaling](https://docs.copilotkit.ai/slack/strands-typescript/persistence-and-scaling) for restart-safe application state.

### On this page

Use the tested runtime pairSettle before reporting readyExpose liveness and readiness separatelyShut down cleanlyStore and rotate secretsBound active replicasObserve the full delivery pathRelease checklist
