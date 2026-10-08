---
url: https://docs.copilotkit.ai/llamaindex/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:13:58.596298+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/llamaindex/agent-config/

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

On this page

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)

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
    
    
    """LlamaIndex agent backing the Agent Config Object demo.Mirrors `langgraph-python/src/agents/agent_config_agent.py`. The LangGraphoriginal reads three forwarded properties — `tone`, `expertise`,`responseLength` — from the run's `RunnableConfig.configurable.properties`and composes the system prompt dynamically per turn.`get_ag_ui_workflow_router` does not expose the same `RunnableConfig` hooksurface, so the LlamaIndex port applies the default profile at startup andexposes the same three-axis prompt composition for parity. The frontendprovider wiring (`<CopilotKitProvider properties={{ tone, ... }}>`) stilldemonstrates the client-side API — the forwarded props are visible in therun payload even if the current router does not yet recompose the promptper turn. Extending the router to read forwarded props is tracked as aTODO in the package-level PARITY_NOTES."""from __future__ import annotationsimport osfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.router import get_ag_ui_workflow_routerDEFAULT_TONE = "professional"DEFAULT_EXPERTISE = "intermediate"DEFAULT_RESPONSE_LENGTH = "concise"TONE_RULES = {    "professional": "Use neutral, precise language. No emoji. Short sentences.",    "casual": "Use friendly, conversational language. Contractions OK. Light humor welcome.",    "enthusiastic": "Use upbeat, energetic language. Exclamation points OK. Emoji OK.",}EXPERTISE_RULES = {    "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",    "intermediate": "Assume common terms are understood; explain specialized terms.",    "expert": "Assume technical fluency. Use precise terminology. Skip basics.",}LENGTH_RULES = {    "concise": "Respond in 1-3 sentences.",    "detailed": "Respond in multiple paragraphs with examples where relevant.",}def build_system_prompt(tone: str, expertise: str, response_length: str) -> str:    return (        "You are a helpful assistant.\n\n"        f"Tone: {TONE_RULES[tone]}\n"        f"Expertise level: {EXPERTISE_RULES[expertise]}\n"        f"Response length: {LENGTH_RULES[response_length]}"    )DEFAULT_SYSTEM_PROMPT = build_system_prompt(    DEFAULT_TONE, DEFAULT_EXPERTISE, DEFAULT_RESPONSE_LENGTH)_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]agent_config_router = get_ag_ui_workflow_router(    llm=OpenAI(model="gpt-5-mini", temperature=0.4, **_openai_kwargs),    frontend_tools=[],    backend_tools=[],    system_prompt=DEFAULT_SYSTEM_PROMPT,    initial_state={},)

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/llamaindex/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/llamaindex/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
