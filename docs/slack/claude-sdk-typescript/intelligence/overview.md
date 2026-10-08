---
url: https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/overview/
title: CopilotKit Intelligence
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:23.835138+00:00
---

# CopilotKit Intelligence

> Source: https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/overview/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/claude-sdk-typescript)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/claude-sdk-typescript/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/claude-sdk-typescript/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/claude-sdk-typescript/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/claude-sdk-typescript/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/claude-sdk-typescript/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/claude-sdk-typescript/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/claude-sdk-typescript/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/claude-sdk-typescript/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/claude-sdk-typescript/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/claude-sdk-typescript/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/claude-sdk-typescript/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# CopilotKit Intelligence

CopilotKit Intelligence adds AG-UI Streams, User Memories, Automatic Learning, Channels, and Product Analytics to the CopilotKit app you already run.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/intelligence/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is CopilotKit Intelligence?#

You want AG-UI Streams, User Memory, Automatic Learning, Channels, and Product Analytics without operating that storage yourself. CopilotKit Intelligence adds that layer to the CopilotKit app you already have. Your frontend, your agent, and your model stay where they are.

Keep your existing thread system. You do not need to replace your thread storage when you connect Intelligence. [Bring your own thread system](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/bring-your-own-thread-system) explains how Intelligence records its own copy while your framework keeps managing the original conversation and agent state.

Open the page for the one thing you want to add. Each page below owns that topic.

Connect an existing app in the [quickstart](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/quickstart), with setup tabs for TypeScript, Python, Go, Ruby, and C#/.NET. TypeScript also works without Intelligence; the other runtime implementations require it.

## What Intelligence gives you

Each capability is a page of its own, and every one works with the agent and frontend you already run. Open the one you want to add first.

### [AG-UI StreamsLet users reconnect, catch up, and resume conversations across devices.](https://docs.copilotkit.ai/threads)### [User MemoriesKeep facts about a person after the conversation ends.](https://docs.copilotkit.ai/intelligence/memories)### [Automatic LearningTurn real usage into skills you can review and publish.](https://docs.copilotkit.ai/learning)### [Product AnalyticsSee what people do with your agent.](https://docs.copilotkit.ai/intelligence/analytics)### [ChannelsRun the same agent in Slack or Microsoft Teams.](https://docs.copilotkit.ai/intelligence/channels)### [InspectorWatch threads, learning, and tool calls from your app on localhost.](https://docs.copilotkit.ai/inspector)

## Already have LangGraph threads or ADK sessions?#

Connect your existing app to Intelligence and add AG-UI streams around your current agent. If you need earlier history, import it once:

  * [Import LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import) from LangGraph Server, LangGraph Platform, or LangSmith Deployments that expose the LangGraph SDK thread and run APIs. Arbitrary LangChain message stores, LangSmith traces, and embedded checkpointers are not supported sources.
  * [Import Google ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import) from supported ADK database session stores or Vertex/Agent Engine session history.



Import copies history; it does not establish ongoing database replication. Future CopilotKit-mediated runs persist to Intelligence and continue through native persistence when your agent remains connected to a durable LangGraph checkpointer or deployment, or an ADK session service with appropriate retention. Keep that native persistence in place.

[Skill delivery](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/learned-skills) combines published Skills from several Learning containers in one agent, with one request for each refresh.

To record what people do in your app as AG-UI events:

  * [Capture interactions](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/capture-interactions) links clicks, page changes, and requests to the Thread, message, and tool call they belong to.
  * [Standalone collector](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/standalone-collector) captures the same events in an app without CopilotKit.
  * [Captured data](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/captured-data) lists every field and how to block or add data.



## Choose where Intelligence runs#

Cloud-hosted and self-hosted use the same app APIs, so you can start on one and move later.

### [Cloud-hostedCopilotKit runs Intelligence for you. Create a project, get a key, and manage your plan in the web app.](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/managed-intelligence-platform)### [Self-hostedRun Intelligence in your own Kubernetes cluster or AWS account with the Helm chart or the ECS bundle.](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/self-hosting)

Want to try Intelligence before you choose? [Evaluate Intelligence locally](https://docs.copilotkit.ai/slack/claude-sdk-typescript/intelligence/self-hosting-local) in Docker on your Mac with the CLI (preview).
