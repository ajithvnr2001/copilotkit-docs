---
url: https://docs.copilotkit.ai/llamaindex/intelligence/managed-intelligence-platform/
title: Cloud-hosted Intelligence
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:03.067857+00:00
---

# Cloud-hosted Intelligence

> Source: https://docs.copilotkit.ai/llamaindex/intelligence/managed-intelligence-platform/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

[Cloud-hosted](https://docs.copilotkit.ai/llamaindex/intelligence/managed-intelligence-platform)[Self-hosted](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting)[AWS ECS/Fargate](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-ecs)[Local evaluation](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-local)

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Cloud-hosted

IntelligenceHosting

# Cloud-hosted Intelligence

Sign in, create a project, and connect your runtime with a project API key.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

Cloud-hosted Intelligence runs the platform for you, with a project and an API key and no cluster to operate. Your app still uses the CopilotKit SDK.

![The cloud-hosted Intelligence ready page.](https://docs.copilotkit.ai/images/cloud-hosted/cloud-hosted-ready.png)

The cloud-hosted service stores the project's threads, events, and API keys. You create the project once, connect your app with the CLI, and everything else is in the web app.

The web app is for the people who build and operate the app. The people who chat with your agent do not sign in there. Your app still identifies those people and passes that identity through the runtime.

Compare this deployment with self-hosted on the [architecture page](https://docs.copilotkit.ai/llamaindex/intelligence/intelligence-platform).

## Get started#

Start at [intelligence.copilotkit.ai](https://intelligence.copilotkit.ai) or in the CopilotKit CLI.

### Sign in#

New accounts accept the CopilotKit Self-Service Agreement. An account that already accepted it does not accept it again.

[Start cloud-hosted setupSign in, create an organization, then return to the CLI or the web app and select a project.Start cloud-hosted setup](https://intelligence.copilotkit.ai/?utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_intelligence_managed_platform_intro&utm_frontend=react&utm_backend=llamaindex)

A new organization chooses the Developer plan or a paid plan. Developer is the no-cost plan. Read [Plans](https://docs.copilotkit.ai/llamaindex/intelligence/plans) when you want to change that choice.

### Create or select an organization#

Select an organization in the browser, or create one.

### Return to the tool that sent you#

After the organization step, the browser returns to the CLI or the web app that opened it. If the CLI opened the browser, return to the terminal and let the command continue.

### Select or create a project#

A project holds one app or one environment. Create a separate project for production, staging, demos, and experiments. Their API keys and threads stay separate.

Sign in and select the project in the [quickstart](https://docs.copilotkit.ai/llamaindex/intelligence/quickstart#select-an-intelligence-project). That page writes `CPK_INTELLIGENCE_API_KEY` to `.env`.

Two other commands fit a different starting point:

  * `npx copilotkit@latest create` creates a new app and writes the same key.
  * `npx copilotkit@latest skills onboard` adds CopilotKit to an existing app.



The [CopilotKit CLI](https://docs.copilotkit.ai/llamaindex/cli) uses the same sign-in. The first `login` opens a browser sign-in page and stores a local session. Later commands reuse that session. `project select` creates the project API key and writes it to `.env`.

![The cloud-hosted project list.](https://docs.copilotkit.ai/images/cloud-hosted/cloud-hosted-projects.png)

Choose a project to open its **Overview**. The project navigation groups its pages into two areas:

  * **Overview** , **Product Analytics** , and **Automatic Learning** show project activity and analysis. During the Developer trial, Product Analytics and Automatic Learning are marked **TRIAL**.
  * **Project resources** contains [Threads](https://docs.copilotkit.ai/llamaindex/threads), [Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels), [User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories), and API Keys.



Each page is scoped to the selected project. Its project API key connects your runtime to that same project.

Inside a project, open **Threads** to find the conversations saved for that project.

![A cloud-hosted project and its threads.](https://docs.copilotkit.ai/images/cloud-hosted/cloud-hosted-thread-list.png)

Open one thread to read its event timeline.

![A cloud-hosted thread with its event timeline.](https://docs.copilotkit.ai/images/cloud-hosted/cloud-hosted-thread-detail.png)

The thread page shows the agent, the app user, the status, the last update time, and the event timeline. Open an event when you need the raw payload. **Rename** , **Archive** , and **Delete** match the thread API in your app: archive hides the thread from the active list and keeps the history, delete removes it. Read [AG-UI Streams](https://docs.copilotkit.ai/llamaindex/threads) for how a thread works in your app.

## Create an API key#

A project API key connects your runtime to this project. The [quickstart](https://docs.copilotkit.ai/llamaindex/intelligence/quickstart#select-an-intelligence-project) writes it to `.env` as `CPK_INTELLIGENCE_API_KEY`. `init` or its `create` alias writes the same key when it creates an app.

Cloud-hosted setup does not issue `COPILOTKIT_LICENSE_TOKEN`. A license key is only for a self-hosted deployment. It does not replace the project API key.

Keep `CPK_INTELLIGENCE_API_KEY` on the server.

![The cloud-hosted API keys page.](https://docs.copilotkit.ai/images/cloud-hosted/cloud-hosted-api-keys.png)

The CLI writes the full key into `.env`. A later run of `project select` creates another key for the same project. Deleting a key stops every app that still uses it.

Connect the key in the [quickstart](https://docs.copilotkit.ai/llamaindex/intelligence/quickstart).

## Next#

  * [Plans](https://docs.copilotkit.ai/llamaindex/intelligence/plans) shows limits and how to change the plan.
  * [Self-host Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting) when the platform must run in your cluster.



### On this page

OverviewGet startedCreate an API keyNext
