---
url: https://docs.copilotkit.ai/ag2/intelligence/overview/
title: CopilotKit Intelligence
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:25.858329+00:00
---

# CopilotKit Intelligence

> Source: https://docs.copilotkit.ai/ag2/intelligence/overview/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Intelligence

# CopilotKit Intelligence

CopilotKit Intelligence adds persistent AG-UI Streams, User Memories, Product Analytics, Automatic Learning, and production operations on top of the runtime you already run.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/intelligence/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is CopilotKit Intelligence?#

You want AG-UI Streams, User Memory, Automatic Learning, Channels, and Product Analytics without operating that storage yourself. CopilotKit Intelligence adds that layer to the CopilotKit app you already have. Your frontend, your agent, and your model stay where they are.

Keep your existing thread system. You do not need to replace your thread storage when you connect Intelligence. [Bring your own thread system](https://docs.copilotkit.ai/ag2/intelligence/bring-your-own-thread-system) explains how Intelligence records its own copy while your framework keeps managing the original conversation and agent state.

Open the page for the one thing you want to add. Each page below owns that topic.

Connect an existing app in the [quickstart](https://docs.copilotkit.ai/ag2/intelligence/quickstart), with setup tabs for TypeScript, Python, Go, Ruby, and C#/.NET. TypeScript also works without Intelligence; the other runtime implementations require it.

## What Intelligence gives you

Each capability is a page of its own, and every one works with the agent and frontend you already run. Open the one you want to add first.

### [AG-UI StreamsLet users reconnect, catch up, and resume conversations across devices.](https://docs.copilotkit.ai/threads)### [User MemoriesKeep facts about a person after the conversation ends.](https://docs.copilotkit.ai/intelligence/memories)### [Automatic LearningTurn real usage into skills you can review and publish.](https://docs.copilotkit.ai/learning)### [Product AnalyticsSee what people do with your agent.](https://docs.copilotkit.ai/intelligence/analytics)### [ChannelsRun the same agent in Slack or Microsoft Teams.](https://docs.copilotkit.ai/intelligence/channels)### [InspectorWatch threads, learning, and tool calls from your app on localhost.](https://docs.copilotkit.ai/inspector)

## Already have LangGraph threads or ADK sessions?#

Connect your existing app to Intelligence and add AG-UI streams around your current agent. If you need earlier history, import it once:

  * [Import LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import) from LangGraph Server, LangGraph Platform, or LangSmith Deployments that expose the LangGraph SDK thread and run APIs. Arbitrary LangChain message stores, LangSmith traces, and embedded checkpointers are not supported sources.
  * [Import Google ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import) from supported ADK database session stores or Vertex/Agent Engine session history.



Import copies history; it does not establish ongoing database replication. Future CopilotKit-mediated runs persist to Intelligence and continue through native persistence when your agent remains connected to a durable LangGraph checkpointer or deployment, or an ADK session service with appropriate retention. Keep that native persistence in place.

[Skill delivery](https://docs.copilotkit.ai/ag2/intelligence/learned-skills) combines published Skills from several Learning containers in one agent, with one request for each refresh.

To record what people do in your app as AG-UI events:

  * [Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions) links clicks, page changes, and requests to the Thread, message, and tool call they belong to.
  * [Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector) captures the same events in an app without CopilotKit.
  * [Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data) lists every field and how to block or add data.



## Choose where Intelligence runs#

Cloud-hosted and self-hosted use the same app APIs, so you can start on one and move later.

### [Cloud-hostedCopilotKit runs Intelligence for you. Create a project, get a key, and manage your plan in the web app.](https://docs.copilotkit.ai/ag2/intelligence/managed-intelligence-platform)### [Self-hostedRun Intelligence in your own Kubernetes cluster or AWS account with the Helm chart or the ECS bundle.](https://docs.copilotkit.ai/ag2/intelligence/self-hosting)

Want to try Intelligence before you choose? [Evaluate Intelligence locally](https://docs.copilotkit.ai/ag2/intelligence/self-hosting-local) in Docker on your Mac with the CLI (preview).

### On this page

What is CopilotKit Intelligence?Already have LangGraph threads or ADK sessions?Choose where Intelligence runs
