---
url: https://docs.copilotkit.ai/angular/strands/deploy/agentcore/
title: AWS AgentCore
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:35:03.015532+00:00
---

# AWS AgentCore

> Source: https://docs.copilotkit.ai/angular/strands/deploy/agentcore/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/strands)[Quickstart](https://docs.copilotkit.ai/angular/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/strands/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Copilot Runtime](https://docs.copilotkit.ai/angular/strands/copilot-runtime)[AG-UI](https://docs.copilotkit.ai/angular/strands/ag-ui)[AWS AgentCore](https://docs.copilotkit.ai/angular/strands/deploy/agentcore)

[Sub-agents](https://docs.copilotkit.ai/angular/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/strands/learning)

[User Memories](https://docs.copilotkit.ai/angular/strands/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/strands/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

AWS AgentCore

Agent capabilitiesAWS Strands (Python)

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## CopilotKit + AWS AgentCore#

[AWS Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) gives you a secure, serverless runtime for deploying AG-UI agents at scale — handling auth, session isolation, and infrastructure. CopilotKit gives those agents a production-ready frontend.

## How it works#

The two connect through **CopilotKit Runtime** , a lightweight server-side layer that sits between your browser and AgentCore. It's the same runtime you'd use with any CopilotKit-powered agent — AgentCore just requires it to run server-side (browsers can't call AgentCore directly due to SigV4/OAuth2 authentication).
    
    
    Browser → CopilotKit Runtime → AgentCore Runtime → your agent

## What you get#

  * **Chat UI** — prebuilt chat interface, or headless APIs to build your own
  * **Shared state** — bidirectional sync between agent state and your application UI
  * **Generative UI** — render custom components from tool calls in real time
  * **Human-in-the-loop** — let users review, approve, or redirect agent actions
  * **AgentCore memory** — conversation history persists across sessions via AgentCore's memory layer



## Quickstart#

AWS CLI required

Both paths below require AWS credentials configured locally. If you haven't done this yet, follow the [AWS CLI getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) before continuing.

## Troubleshooting#

### HTTP 401: `Missing Authentication Token`#
    
    
    Agent execution failed: Error: HTTP 401:
    {"jsonrpc":"2.0","error":{"code":-32001,"message":"Missing Authentication Token"},"id":"null"}

`Missing Authentication Token` is AWS's own error, not a CopilotKit or agent error. AWS returns it when a request reaches an AgentCore or API Gateway endpoint with no credentials, or when the request path matches no deployed route. Check the following, in order:

  * **The runtime is actually sending a token.** Set `AGENTCORE_ACCESS_TOKEN` in the environment of the Copilot Runtime **server** , not the frontend. If the variable is unset, the `Authorization` header interpolates to `Bearer undefined`, which AWS rejects exactly like a missing header.
  * **The token has not expired.** Cognito access tokens are short-lived. Mint a fresh one and retry before you debug anything else.
  * **`AGENTCORE_ENDPOINT_URL` is the full invocation URL**, ending in `/invocations`, with the agent ARN URL-encoded: `https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{encoded-arn}/invocations`. A URL that stops short of `/invocations` matches no route, and AWS reports that as `Missing Authentication Token` rather than as a 404.
  * **The browser is not calling AgentCore directly.** AgentCore requires SigV4 or OAuth2 signing, which a browser cannot perform. Point the frontend at your Copilot Runtime endpoint and let the runtime make the AgentCore call server-side.



This error does not apply to the local quickstart

The framework quickstarts run the agent locally on `http://localhost:8000`, and a local agent server never returns `Missing Authentication Token`. If you see this error, the runtime is pointed at a deployed AWS endpoint.

## What's next?#

  * [Generative UI](https://docs.copilotkit.ai/angular/strands/guides/frontend-tools-generative-ui) — render application components from agent tool calls.
  * [Shared State](https://docs.copilotkit.ai/angular/strands/guides/shared-state) — synchronize structured state between the agent and application.
  * [Authentication](https://docs.copilotkit.ai/angular/strands/auth) — validate the frontend session at Copilot Runtime before forwarding identity to AgentCore.



### On this page

CopilotKit + AWS AgentCoreHow it worksWhat you getQuickstartTroubleshootingHTTP 401: Missing Authentication TokenWhat's next?
