---
url: https://docs.copilotkit.ai/strands/community-frameworks/
title: Community frameworks
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:54.207250+00:00
---

# Community frameworks

> Source: https://docs.copilotkit.ai/strands/community-frameworks/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Community frameworks

Other

# Community frameworks

Frontend packages for CopilotKit that the community builds and maintains.

CopilotKit maintains official packages for React, React Native, Vue and Angular. Community frameworks add other frontends. People outside the core team build and maintain them.

## What community means#

  * **Tested with one version.** Each package lists the `@copilotkit/core` version it is tested with. Use that version.
  * **Updates are best effort.** A community package can fall behind CopilotKit releases. Report problems on GitHub. We read every report, but we do not promise a response time.
  * **Separate releases.** A community package releases on its own schedule. It does not block CopilotKit releases.
  * **Each package's README is its setup guide.** The CopilotKit documentation does not cover community packages.



## Frameworks#

Framework| Status| Tested with| Details  
---|---|---|---  
  
## Request or contribute a framework#

To ask for a framework, [open an issue](https://github.com/CopilotKit/CopilotKit/issues/new/choose). Each request tells us which frontends people need.

To build one, start from `@copilotkit/core`. It is the framework-neutral layer that the official packages use for agents, tools, context and threads. A community package adds the bindings and the chat UI for its framework.

### On this page

What community meansFrameworksRequest or contribute a framework
