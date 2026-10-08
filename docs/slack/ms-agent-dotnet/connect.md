---
url: https://docs.copilotkit.ai/slack/ms-agent-dotnet/connect/
title: Connect and run your agent in Slack
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:28:12.149256+00:00
---

# Connect and run your agent in Slack

> Source: https://docs.copilotkit.ai/slack/ms-agent-dotnet/connect/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/ms-agent-dotnet)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/ms-agent-dotnet/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/ms-agent-dotnet/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/ms-agent-dotnet/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/ms-agent-dotnet/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/ms-agent-dotnet/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/ms-agent-dotnet/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/ms-agent-dotnet/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/ms-agent-dotnet/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/ms-agent-dotnet/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/ms-agent-dotnet/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/ms-agent-dotnet/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/ms-agent-dotnet/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Connect and run your agent

Getting Started

# Connect and run your agent in Slack

Run any supported agent framework in Slack through a cloud-hosted Intelligence connection.

In this guide, you will connect an AG-UI agent to a managed Slack app, start a long-running Channels SDK listener, and verify a real workspace message. CopilotKit Intelligence holds the Slack credentials; your process holds the agent and application logic.

New to the product? Start with the [Channels overview](https://docs.copilotkit.ai/slack/ms-agent-dotnet) to understand how the SDK, Runtime, Intelligence, and provider connection fit together.

Before you continue, [configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/ms-agent-dotnet/intelligence). You should have `CHANNEL_CODE` and `CPK_INTELLIGENCE_API_KEY`.

## Start with your coding agent#

Use this prompt to connect your agent to Slack, start the Channels SDK listener, and verify a real workspace message. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Before you start#

  * Node.js 22 or later; the managed launcher requires the global `WebSocket` available in Node.js 22+
  * A long-running Node host or container; serverless request handlers cannot own the persistent gateway connection



## Build and run your Channel#

### Create the runner#

Terminal
    
    
    mkdir my-slack-channel
    cd my-slack-channel
    npm init -y
    npm pkg set type=module

Use this tested package combination. Keep exact versions in your lockfile and verify compatibility before changing either package.

Terminal
    
    
    npm install --save-exact @copilotkit/channels@0.11.0 @copilotkit/runtime@1.73.3

Terminal
    
    
    npm install -D tsx typescript @types/node

Add a NodeNext TypeScript configuration:

tsconfig.json
    
    
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "NodeNext",
        "moduleResolution": "NodeNext",
        "strict": true,
        "skipLibCheck": true,
        "noEmit": true,
        "types": ["node"]
      },
      "include": ["*.ts", "*.tsx"]
    }

### Connect your agent backend#

The Channels process can use any supported backend. The selector's **Agent backend** controls the setup below. It must export a fresh `makeAgent(threadId)` result for each Slack conversation; do not share one stateful agent instance across threads.

Follow the [Microsoft Agent Framework .NET quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart) to configure your agent. Keep its AG-UI server running on `http://localhost:8000`: the CLI starter's `agent` project or the **Use an existing agent** path's `AGUIServer` project.

The shared Microsoft agent is mapped at the server root:

.env
    
    
    AGENT_URL=http://localhost:8000/

Install the HTTP adapter in the Channels process:

Terminal
    
    
    npm install @ag-ui/client@0.0.59

Create a new HTTP adapter for every channel thread:

agent.ts
    
    
    import { HttpAgent } from "@ag-ui/client";
    
    export function makeAgent(threadId: string) {
      const agent = new HttpAgent({ url: process.env.AGENT_URL! });
      agent.threadId = threadId;
      return agent;
    }

### Declare the managed Slack Channel#

Create the listener below. Replace `support-slack` with the exact Code shown in Intelligence.

Set `agent: makeAgent` on the Channel because this handler calls `thread.runAgent()`. Channels do not inherit `runtime.agents`. A Channel whose handlers reply directly without `runAgent()` can omit `agent`.

channel.ts
    
    
    import { createServer } from "node:http";
    import { createChannel } from "@copilotkit/channels";
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
    } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    import { makeAgent } from "./agent.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing required environment variable: ${name}`);
      return value;
    }
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
    });
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({
        // Combine text and attachments explicitly when both are present.
        prompt: message.contentParts?.length
          ? [
              ...(message.text
                ? [{ type: "text" as const, text: message.text }]
                : []),
              ...message.contentParts,
            ]
          : message.text,
        context: [
          { description: "Originating platform", value: message.platform },
        ],
      });
    });
    
    const intelligence = new CopilotKitIntelligence({
      apiKey: required("CPK_INTELLIGENCE_API_KEY"),
      // Cloud-hosted deployments use the default URLs. Override both URLs
      // together only for self-hosted or non-production Intelligence.
      apiUrl: process.env.INTELLIGENCE_API_URL,
      wsUrl: process.env.INTELLIGENCE_GATEWAY_WS_URL,
    });
    
    const runtime = new CopilotRuntime({
      agents: {},
      intelligence,
      channels: [channel],
    });
    
    // Wire teardown before the listener exists, because creating it is what
    // starts the Channel. A Ctrl-C during the connect window then still tears
    // the Channel down instead of hitting Node's default handler.
    let teardown: (() => Promise<void>) | undefined;
    const shutdown = async () => {
      await teardown?.();
    };
    process.once("SIGINT", shutdown);
    process.once("SIGTERM", shutdown);
    
    const listener = createCopilotNodeListener({
      runtime,
      basePath: "/api/copilotkit",
    });
    const channels = listener.channels;
    const server = createServer(listener);
    teardown = async () => {
      await channels.stop();
      if (server.listening) server.close();
    };
    
    // Optional: block startup until the activation above settles, so a broken
    // deploy fails loudly instead of serving as a bot that never answers.
    await channels.ready({ timeoutMs: 30_000 });
    const status = channels.status();
    if (status.overall !== "online") {
      throw new Error(`Slack Channel is not online: ${JSON.stringify(status)}`);
    }
    
    const port = Number(process.env.PORT ?? 3001);
    server.listen(port, () => {
      console.log(`Slack Channel online; lifecycle server listening on :${port}`);
    });

Creating the Node listener starts the Channel: it owns its own process lifetime, so a declared Channel connects because it was declared. `ready()` is therefore optional and purely await-and-observe — it resolves once activation settles and rejects with the activation failure. Because it can settle with setup still required, inspect `status()` before reporting the Channel online. Skip `ready()` and activation failures land in your logs instead.

### Configure secrets and start#

.env
    
    
    CPK_INTELLIGENCE_API_KEY=<project-api-key>
    CHANNEL_CODE=support-slack
    # Add the agent variables shown for your selected backend.
    PORT=3001
    
    # Optional paired overrides for self-hosted or non-production Intelligence:
    # INTELLIGENCE_API_URL=https://intelligence.example.com
    # INTELLIGENCE_GATEWAY_WS_URL=wss://realtime.intelligence.example.com

The lifecycle server uses port `3001` so it can run alongside a web app on port `3000`. If `3001` is already in use, set `PORT` to another free port.

#### Where these values come from

Three variables matter here, and you supply only one:

  * `OPENAI_API_KEY`, or the key for whichever model provider your agent uses. This one is yours to create and paste.
  * `CPK_INTELLIGENCE_API_KEY` is written for you by `copilotkit project select`, which provisions the project and its key.
  * `CHANNEL_CODE` is written for you by the onboarding run once it has declared the Channel; the run knows the Code it just created.



So both Intelligence values land in the environment file your app loads and you never copy either one by hand. Setting them yourself still works: see [configure the runtime handoff](https://docs.copilotkit.ai/slack/ms-agent-dotnet/intelligence#configure-the-runtime-handoff) for where each value appears in Intelligence.

Cloud-hosted Intelligence supplies both default base URLs. For a self-hosted or non-production deployment, override both together. The REST and realtime planes use separate hosts, so do not derive the WebSocket URL from the API URL. Pass each as a bare base URL without `/api`, `/socket`, `/runner`, or `/client`. Create the project-scoped runtime key from **API Keys** in the Intelligence project sidebar.

Keep `.env` out of source control, start the selected agent backend, then run:

Terminal
    
    
    node --env-file=.env --import tsx channel.ts

Intelligence should change from **Waiting for runtime** to **Online**.

#### Know the healthy state

Starting the process is what connects the Channel, so it should become **Online** on its own; the `await channels.ready(...)` in this guide only waits for that to settle.

Status| What to check  
---|---  
**Disabled**|  Enable the Channel before expecting delivery.  
**Setup incomplete**|  Finish the selected provider's required setup fields before starting the runtime.  
**Setup failed**|  Reopen platform setup and correct the rejected credentials or configuration.  
**Waiting for runtime**|  Start the process — creating the listener connects the Channel — and match its Code and provider to this Channel.  
**Conflict**|  Compare every replica's complete Channel declaration set. Identical replicas should elect one active owner and connected standbys; different but overlapping sets are unsafe.  
**Offline**|  Check the listener process, network, and Intelligence gateway connection.  
**Delivery failing**|  Check platform credentials, app permissions, and the provider response.  
**Online**|  The runtime is connected; send a real provider message to verify the full path.  
  
### Verify a real Slack message#

Invite the app if needed, then mention it in a channel:

Slack
    
    
    /invite @your-app
    @your-app summarize the decisions in this thread

Also test a direct message. A response in the real workspace validates the Slack token pair, Intelligence delivery, gateway listener, AG-UI agent, and reply path end to end.

## Tool-call progress#

Managed Slack keeps tool-call progress out of the streamed reply by default, so the conversation ends with a clean result. Tool lifecycle events still remain in Intelligence history and are available during replay.

Opt in per Channel when the live tool timeline is useful:

channel.ts
    
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      showToolStatus: true,
    });

## Troubleshooting#

The Channel stays at Waiting for runtime

Confirm `CHANNEL_CODE` exactly matches the Intelligence Code and the project-scoped `CPK_INTELLIGENCE_API_KEY` belongs to the same project. Provider routing comes from the Slack connection attached in Intelligence, not from a `createChannel` option.

Startup reports setup_required

Reopen the Channel in Intelligence and finish the Slack credential steps. `ready()` settling does not by itself mean the provider is online.

The app is Online but never receives a mention

Invite it to the channel, then verify the `xoxb-…` Bot User OAuth token and Signing Secret came from the same Slack app. Intelligence cannot fully detect valid but mismatched credentials during setup. If you updated the manifest or scopes, reinstall the app and save the current bot token in Intelligence before retrying.

The agent mixes conversations

Ensure `makeAgent` creates a new agent for every `threadId` and assigns that id where the selected framework requires it.

Next, [map application users and choose Memory grants](https://docs.copilotkit.ai/slack/ms-agent-dotnet/identity-and-memory), add [tools and context](https://docs.copilotkit.ai/slack/ms-agent-dotnet/tools), or build [interactive approvals](https://docs.copilotkit.ai/slack/ms-agent-dotnet/interactive).

### On this page

Start with your coding agentBefore you startBuild and run your ChannelTool-call progressTroubleshooting
