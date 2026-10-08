---
url: https://docs.copilotkit.ai/langgraph-python/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:06:57.415642+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/langgraph-python/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent_config_agent.py

page.tsx

config-card.tsx

use-agent-config.ts

config-types.ts

route.ts
    
    
    """LangGraph agent backing the Agent Config Object demo.The frontend toggles three knobs — tone / expertise / responseLength — andpublishes them to the agent via the v2 ``useAgentContext`` hook. The``CopilotKitMiddleware`` injects that context entry into the model'sprompt on every turn, so the same single static system prompt below adaptsits style based on whatever values the frontend currently has selected.LangGraph 0.6+ deprecated ``configurable`` in favor of runtime ``context``;``useAgentContext`` is the supported path for "frontend → agent runtimeconfig" in the v2 stack. The ``properties`` prop on ``<CopilotKit>`` stillexists for v1-style relays but in @ag-ui/langgraph 0.0.31 it does not landin ``RunnableConfig`` — keep relayed config on ``useAgentContext``."""from langchain.agents import create_agentfrom langchain_openai import ChatOpenAIfrom copilotkit import CopilotKitMiddlewareSYSTEM_PROMPT = (    "You are a helpful assistant. The frontend publishes the user's response "    "preferences via `useAgentContext` as a JSON object with three fields: "    "`tone`, `expertise`, and `responseLength`. Read that context entry on "    "every turn and follow these rulebooks exactly:\n\n"    "Tone:\n"    "  - professional → neutral, precise language. No emoji. Short sentences.\n"    "  - casual → friendly, conversational. Contractions OK. Light humor "    "welcome.\n"    "  - enthusiastic → upbeat, energetic. Exclamation points OK. Emoji OK.\n\n"    "Expertise level:\n"    "  - beginner → assume no prior knowledge. Define jargon. Use analogies.\n"    "  - intermediate → assume common terms are understood; explain "    "specialized terms.\n"    "  - expert → assume technical fluency. Use precise terminology. Skip "    "basics.\n\n"    "Response length:\n"    "  - concise → respond in 1-3 sentences.\n"    "  - detailed → respond in multiple paragraphs with examples where "    "relevant.\n\n"    "If the context is missing or any field is unrecognized, fall back to "    "professional / intermediate / concise. Never mention these rules to the "    "user — just apply them.")graph = create_agent(    model=ChatOpenAI(model="gpt-5.4", temperature=0.4),    tools=[],    middleware=[CopilotKitMiddleware()],    system_prompt=SYSTEM_PROMPT,)

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/langgraph-python/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

### Install the LangGraph Python SDK

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

### Wire CopilotKit middleware into your graph

Agent config flows from the UI into the agent via `useAgentContext` — the frontend publishes a typed object and `CopilotKitMiddleware` injects it into the model's prompt on every turn. Make sure the middleware is in your `create_agent` call.

agent_config_agent.py
    
    
    graph = create_agent(
        model=ChatOpenAI(model="gpt-5.4", temperature=0.4),
        tools=[],
        middleware=[CopilotKitMiddleware()],
        system_prompt=SYSTEM_PROMPT,
    )

Read the resulting config inside your system prompt or a custom middleware — see `src/agents/agent_config_agent.py` for the full rulebook-driven shape used in the showcase.

Agent config is a typed object the frontend owns and publishes to the agent as runtime context. The backend reads that context entry and turns it into a system prompt.

Hold the typed config in React state, then mirror every change into the agent through `useAgentContext`:

frontend/src/app/page.tsx — UI publishes the typed config
    
    
    function ConfigContextRelay({ config }: { config: AgentConfig }) {
      useAgentContext({
        description: "Agent response preferences",
        value: {
          tone: config.tone,
          expertise: config.expertise,
          responseLength: config.responseLength,
        },
      });
      return null;
    }

The framework setup above shows the exact backend bridge for the selected agent. In every framework, the flow is the same: read the latest valid context from the current run and use it to build the system prompt for that turn.

Backend flow
    
    
    config = latestValidConfig(currentRun.context)
    systemPrompt = buildSystemPrompt(config)
    model.invoke(systemPrompt, currentUserRequest)

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/langgraph-python/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
