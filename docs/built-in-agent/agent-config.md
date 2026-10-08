---
url: https://docs.copilotkit.ai/built-in-agent/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:36:04.210297+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/built-in-agent/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[CopilotKit's Built-in Agent](https://docs.copilotkit.ai/)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

config-card.tsx

use-agent-config.ts

config-types.ts

route.ts
    
    
    "use client";/** * Agent Config Object — typed config knobs (tone / expertise / responseLength) * forwarded from the provider into the agent so its behavior changes per turn. * * Wiring: the toggles live in `useAgentConfig`. Each render the resolved * config is published to the agent via `useAgentContext` — the v2 idiom * for "frontend → agent runtime context" in LangGraph 0.6+. The Python * graph picks it up through `CopilotKitMiddleware`, which routes the * context entry into the model's prompt before each call. * * (LangGraph 0.6 deprecated `configurable` in favor of `context`; the * `properties` prop on `<CopilotKit>` still works for v1-style relays * but goes through `forwardedProps` and does not land in `RunnableConfig` * in @ag-ui/langgraph 0.0.31. `useAgentContext` is the supported path.) */import { CopilotKit } from "@copilotkit/react-core/v2";import { DemoLayout } from "./demo-layout";import { ConfigContextRelay } from "./config-context-relay";import { useAgentConfig } from "./use-agent-config";export default function AgentConfigDemoPage() {  const { config, setTone, setExpertise, setResponseLength } = useAgentConfig();  return (    <CopilotKit      runtimeUrl="/api/copilotkit-agent-config"      agent="agent-config-demo"    >      <ConfigContextRelay config={config} />      <DemoLayout        config={config}        onToneChange={setTone}        onExpertiseChange={setExpertise}        onResponseLengthChange={setResponseLength}      />    </CopilotKit>  );}

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

The runtime owns the agent in-process, so config travels through frontend runtime properties rather than agent state. There's no separate backend service to push state into: the typed object becomes the input to the agent factory directly.

Pass the typed object as `properties` on `<CopilotKit>`:

frontend/src/app/page.tsx — config flows through the provider
    
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      properties={{ tone, expertise, responseLength }}
      useSingleEndpoint
    >
      <Demo />
    </CopilotKit>

The runtime hands the same object to the agent factory on every call as `input.forwardedProps`. The factory uses those fields to build a system prompt before returning the agent for that turn:

backend/agent factory — synthesise the system prompt per turn
    
    
    export const agentConfigFactory = async (input: AgentFactoryInput) => {
      const { tone, expertise, responseLength } = input.forwardedProps ?? {};
      const systemPrompt = buildSystemPrompt(tone, expertise, responseLength);
      return makeAgent({ systemPrompt /* ... */ });
    };

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (agent-config).

### On this page

When to use thisHow it works
