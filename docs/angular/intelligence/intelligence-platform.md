---
url: https://docs.copilotkit.ai/angular/intelligence/intelligence-platform/
title: CopilotKit Intelligence architecture
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:51.572295+00:00
---

# CopilotKit Intelligence architecture

> Source: https://docs.copilotkit.ai/angular/intelligence/intelligence-platform/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

[Quickstart](https://docs.copilotkit.ai/angular/intelligence/quickstart)[Architecture](https://docs.copilotkit.ai/angular/intelligence/intelligence-platform)[Plans](https://docs.copilotkit.ai/angular/intelligence/plans)

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Architecture

IntelligenceGet started

# CopilotKit Intelligence architecture

How a CopilotKit runtime connects to Intelligence, and how cloud-hosted differs from self-hosted.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

You want to see how your app, your runtime, and Intelligence fit together, and which deployment to run. This page is that map. It applies to [cloud-hosted Intelligence](https://docs.copilotkit.ai/angular/intelligence/managed-intelligence-platform) and to [self-hosted Intelligence](https://docs.copilotkit.ai/angular/intelligence/self-hosting).

To connect a runtime, follow the [quickstart](https://docs.copilotkit.ai/angular/intelligence/quickstart). For the Kubernetes install, go to [self-host on Kubernetes](https://docs.copilotkit.ai/angular/intelligence/self-hosting).

[Start with cloud-hosted IntelligenceCreate a project, get a project API key, and inspect the first thread before you decide to self-host.Start cloud-hosted setup](https://intelligence.copilotkit.ai/?utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_intelligence_architecture_intro&utm_frontend=angular&utm_backend=built-in-agent)

## Runtime and platform roles#

A CopilotKit app has three layers:

  * **Frontend.** Your application uses the CopilotKit frontend SDK to render chat, generative UI, tools, and thread controls.
  * **Runtime.** Your application server hosts the CopilotKit runtime and connects to your agent framework through AG-UI.
  * **CopilotKit Intelligence.** The platform service that stores threads, serves project APIs, and powers the web app.



The runtime is the bridge. It receives requests from your app, streams AG-UI events to and from your agent, and uses CopilotKit Intelligence when a capability needs durable platform state.

## Project boundaries#

The platform scopes data through three concepts:

  * **Organization.** The billing and workspace boundary.
  * **Project.** One application or environment inside an organization, such as production, staging, or a demo.
  * **User.** The signed-in person from your application.



Project API keys are issued per project. Threads, events, and dashboard history are visible only inside the project that owns them, so production and staging can share the same platform deployment without sharing conversation data.

## Threads#

A thread is the saved conversation for one user in one project. Read [AG-UI Streams](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless) for the product. Read [how a thread is saved](https://docs.copilotkit.ai/angular/intelligence/threads-explained) for replay and sync.

## Realtime sync#

Realtime sync keeps thread metadata and active conversation state aligned across clients. When enabled, clients subscribe to platform-backed updates so changes such as renames, archives, and active-run status can appear without a page reload.

The important application-level contract is simple: your app uses the same frontend APIs, while the runtime points at the platform endpoint for the selected deployment.

## Inspection#

Open a stored thread in the [cloud-hosted project](https://docs.copilotkit.ai/angular/intelligence/managed-intelligence-platform#get-started). API keys and plans live on [Cloud-hosted](https://docs.copilotkit.ai/angular/intelligence/managed-intelligence-platform) and [Plans](https://docs.copilotkit.ai/angular/intelligence/plans).

## Hosting model#

Cloud-hosted and self-hosted CopilotKit Intelligence share the same application contract:

Deployment| What changes| What stays the same  
---|---|---  
Cloud-hosted| CopilotKit runs the platform, database, web app, project API keys, and plan management.| Your frontend APIs, runtime APIs, AG-UI agent connection, and thread APIs.  
Self-hosted| You run the platform in your own Kubernetes cluster and own its infrastructure dependencies.| Your frontend APIs, runtime APIs, AG-UI agent connection, and thread APIs.  
  
Self-hosted changes who operates the platform. The frontend integration stays the same. Moving from cloud-hosted to self-hosted is available on the Team Self-hosted plan or the Enterprise plan. See [Plans](https://docs.copilotkit.ai/angular/intelligence/plans).

## Error handling model#

Platform-backed features are networked features. If the platform endpoint is unavailable or credentials are invalid, thread operations surface as runtime errors rather than silently falling back to local-only state.

Common debugging checks:

  * Confirm the runtime is using the right platform URL for the selected deployment.
  * Confirm the runtime API key or license is valid for the project or self-hosted environment.
  * Confirm the user and project context you pass from the app match the thread history you expect to see.
  * Confirm realtime sync is configured when you expect cross-tab or cross-device updates.



## Next steps#

  * [Overview](https://docs.copilotkit.ai/angular/intelligence/overview) lists each feature on its own page.
  * [Cloud-hosted](https://docs.copilotkit.ai/angular/intelligence/managed-intelligence-platform) creates the project and the API key.
  * [Self-host on Kubernetes](https://docs.copilotkit.ai/angular/intelligence/self-hosting) installs the platform in your cluster.
  * [How a thread is saved](https://docs.copilotkit.ai/angular/intelligence/threads-explained) covers replay and sync.



### On this page

OverviewRuntime and platform rolesProject boundariesThreadsRealtime syncInspectionHosting modelError handling modelNext steps
