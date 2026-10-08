---
url: https://docs.copilotkit.ai/teams/ms-agent-dotnet/
title: Microsoft Teams: Channels
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:33:40.076721+00:00
---

# Microsoft Teams: Channels

> Source: https://docs.copilotkit.ai/teams/ms-agent-dotnet/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelTeamsAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/teams/ms-agent-dotnet)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/teams/ms-agent-dotnet/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/teams/ms-agent-dotnet/connect)

Build

[Tools and context](https://docs.copilotkit.ai/teams/ms-agent-dotnet/tools)[Identity and Memory](https://docs.copilotkit.ai/teams/ms-agent-dotnet/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/teams/ms-agent-dotnet/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/teams/ms-agent-dotnet/interactive)[Commands and reactions](https://docs.copilotkit.ai/teams/ms-agent-dotnet/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/teams/ms-agent-dotnet/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/teams/ms-agent-dotnet/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/teams/ms-agent-dotnet/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/teams/ms-agent-dotnet/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/teams/ms-agent-dotnet/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Overview

Getting Started

# Channels

Run one AG-UI agent in Slack, Microsoft Teams, and more through cloud-hosted Intelligence connections.

## Start with your coding agent#

Copy this prompt into your coding agent to choose a framework, set up your agent, and connect it to Slack or Microsoft Teams with CopilotKit Intelligence. Prefer to work through the setup yourself? Follow the guides below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Channels brings your agent into the conversations where work already happens. Your agent still runs in your infrastructure. CopilotKit Intelligence owns the channel connection (Slack, Teams, Discord, etc.), delivers each turn to your Channels SDK listener, and sends the response back as native channel UI.

## How Channels connects your agent#

Channels connects the agent and application logic you run to the provider connection managed by CopilotKit Intelligence. The diagram shows the boundaries between those systems and the path each message takes.

![Channels architecture showing agent frameworks connected through AG-UI and the CopilotKit Runtime to the Channels SDK, with the channel runner — CopilotKit Intelligence's managed runner or your own — connecting to Slack, Microsoft Teams, WhatsApp, Discord, and more.](https://docs.copilotkit.ai/images/channels/channels-architecture-light.png)![Channels architecture showing agent frameworks connected through AG-UI and the CopilotKit Runtime to the Channels SDK, with the channel runner — CopilotKit Intelligence's managed runner or your own — connecting to Slack, Microsoft Teams, WhatsApp, Discord, and more.](https://docs.copilotkit.ai/images/channels/channels-architecture-dark.png)

As explained in the [CopilotKit Intelligence overview](https://docs.copilotkit.ai/teams/ms-agent-dotnet/intelligence/overview), the dividing line between CopilotKit open source and CopilotKit Intelligence is durable data: functionality that runs without it is open source, while functionality built on connections to durable data — databases and the state kept in them — is part of CopilotKit Intelligence. A channel runner needs durable data to run correctly in production: simultaneous participants, race conditions, retries, and delivery guarantees all depend on it. CopilotKit Intelligence provides the managed channel runner, and channels running on it also get the rest of CopilotKit Intelligence, including Product Analytics, Automatic Learning, and governance. You can absolutely build and operate your own channel runner on the open-source Channels SDK — you implement the durable-data layer yourself.

[More channels are on the waySlack and Microsoft Teams are generally available on cloud-hosted Intelligence. Direct SDK adapters also support Teams, Discord, WhatsApp, and Telegram.Book time with an engineer](https://copilotkit.ai/talk-to-an-engineer?utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_channels_more_channels_contact&utm_frontend=teams&utm_backend=ms-agent-dotnet)

Each message moves through the same five stages:

  1. A person messages your app in Slack or Teams.
  2. CopilotKit Intelligence receives the platform event using the credentials configured for that Channel.
  3. A persistent Intelligence gateway connection delivers the turn to your long-running Channels SDK process.
  4. The SDK runs your agent over [AG-UI](https://docs.copilotkit.ai/agentic-protocols/ag-ui), executes channel tools, and renders the response.
  5. Intelligence sends the result back as native Slack Block Kit or Teams Adaptive Card content.



This split keeps platform credentials out of your agent process without moving your agent, tools, or business logic into CopilotKit.

You run| CopilotKit Intelligence manages  
---|---  
The agent and its model credentials| Slack and Teams platform credentials  
A long-running Channels SDK listener| Platform ingress and credentialed delivery  
Tools and approval business logic| Runtime registration, health, and reconnects  
Deployment, logs, and application auth| Conversation-history delivery to the listener  
  
## Production self-hosting: Run CopilotKit Intelligence in your own infrastructure#

Production self-hosting keeps your Channels configuration, provider credentials, delivery state, and platform operations inside your network, giving your organization control over data residency, security, and infrastructure. You can fully self-host the Channels SDK. Onboarding guides are coming soon; in the meantime, if you're comfortable with Docker and Kubernetes, go right ahead — and we're happy to help. [Book time with a CopilotKit engineer](https://copilotkit.ai/talk-to-an-engineer).

## Next step#

Continue to [Configure the Channel in Intelligence](https://docs.copilotkit.ai/teams/ms-agent-dotnet/intelligence) to create the managed Microsoft Teams connection.

### On this page

Start with your coding agentHow Channels connects your agentProduction self-hosting: Run CopilotKit Intelligence in your own infrastructureNext step
