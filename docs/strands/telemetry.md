---
url: https://docs.copilotkit.ai/strands/telemetry/
title: Open-source Telemetry
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:31:54.913922+00:00
---

# Open-source Telemetry

> Source: https://docs.copilotkit.ai/strands/telemetry/

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

Open-source telemetry

Other

# Open-source Telemetry

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit uses metadata-only product telemetry to learn how to improve the open-source packages.

  * We do not collect prompts, messages, agent state, tool data, or other application content.
  * We do not sell or share telemetry data with third parties.
  * We do not use cookies or trackers for open-source telemetry.



Runtime uses the first nonblank telemetry identity that is valid in an HTTP header, in this order: explicit `telemetryId`, `CPK_TELEMETRY_ID`, then the identity carried by `COPILOTKIT_LICENSE_TOKEN`.

`CPK_TELEMETRY_ID` is optional and non-secret. The CopilotKit CLI does not create or write `CPK_TELEMETRY_ID`, and a value you choose does not automatically link Runtime events to a CLI scaffold event. Setting it does not enable telemetry, grant product access, or replace the project's Intelligence API key.

Cloud-hosted Intelligence starters use `CPK_INTELLIGENCE_API_KEY` for platform access. The project API key is not a telemetry identity.

Cloud-hosted setup does not issue `COPILOTKIT_LICENSE_TOKEN`. That token is only for offline or self-hosted licensing, so a cloud-hosted starter carries no license-token identity. When a self-hosted deployment sets the token, it supplies the fallback identity. With none of these identities, Runtime sends anonymous telemetry.

The Inspector stores a random browser ID in local storage and sends it directly with feature-use events. CopilotKit signup links can carry that ID so we can measure the path from Inspector use to signup. Inspector delivery does not depend on `CPK_TELEMETRY_ID`.

## Inspector metadata events#

The Inspector sends coarse events when trusted project-context modules become visible and when a user follows a plan action:

Event| Feature-specific properties  
---|---  
`oss.inspector.metadata_module_viewed`| `module`, `license_bucket`, and `action_kind` when the visible module is an action  
`oss.inspector.metadata_action_clicked`| `module: "action"`, `action_kind`, and `license_bucket` for **Manage plan** and **Renew** clicks  
  
`module` is `identity`, `plan`, or `action`. `action_kind` is `manage_plan`, `renew`, or `enable_intelligence`. `license_bucket` is `valid`, `none`, `expired`, or `unknown`.

An **Enable Intelligence** click keeps the existing `oss.inspector.threads_intelligence_signup_clicked` event so existing reports stay continuous. The same click does not also send `oss.inspector.metadata_action_clicked`.

The feature-specific payload never includes organization, project, account, or user names; account, organization, project, user, thread, run, or message IDs; action or runtime URLs; usage values, limits, or counts; or conversation and tool content. Metadata usage impressions are not sent. The standard anonymous telemetry envelope includes package identity, anonymous distinct IDs, and an event timestamp.

## How to opt out of open-source telemetry#

Set `COPILOTKIT_TELEMETRY_DISABLED=true` in your runtime environment. This disables telemetry for both the CopilotRuntime and Inspector. We also respect [Do Not Track (DNT)](https://consoledonottrack.com/).

## Get in touch#

Send telemetry questions to [hello@copilotkit.ai](mailto:hello@copilotkit.ai).

### On this page

Inspector metadata eventsHow to opt out of open-source telemetryGet in touch
