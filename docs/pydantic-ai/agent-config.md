---
url: https://docs.copilotkit.ai/pydantic-ai/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:11.853349+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/pydantic-ai/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent_config_agent.py

page.tsx

config-card.tsx

route.ts
    
    
    """PydanticAI agent backing the Agent Config Object demo.Reads three forwarded properties — tone, expertise, responseLength —from the AG-UI run's ``context`` (populated by the TS runtime route)and builds its system prompt dynamically per turn.PydanticAI-specific wiring--------------------------The CopilotKit provider's ``properties`` prop is forwarded by the runtimeas ``forwardedProps`` on each AG-UI run. PydanticAI's AG-UI adapter(``AGUIAdapter.dispatch_request``) surfaces that via ``ctx.deps.copilotkit.context`` when the runtimeroute repacks it (see ``src/app/api/copilotkit-agent-config/route.ts``)— the TS route appends a synthetic ``agent-config-properties`` contextentry whose JSON payload carries the three properties.A ``@agent.system_prompt`` dynamic prompt reads that context entry atcall-time and composes the system prompt from the three axes. When thecontext entry is missing (or contains an unknown value), we fall back tothe ``DEFAULT_*`` constants — same defensive behaviour as thelanggraph-python reference."""from __future__ import annotationsimport jsonfrom typing import Any, Literalfrom pydantic import BaseModelfrom pydantic_ai import Agent, RunContextfrom pydantic_ai.ui import StateDepsfrom pydantic_ai.models.openai import OpenAIResponsesModelclass AgentConfigState(BaseModel):    """Agent-config demo carries no shared state — the provider properties    ride on ``context`` instead."""Tone = Literal["professional", "casual", "enthusiastic"]Expertise = Literal["beginner", "intermediate", "expert"]ResponseLength = Literal["concise", "detailed"]DEFAULT_TONE: Tone = "professional"DEFAULT_EXPERTISE: Expertise = "intermediate"DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise"VALID_TONES: set[str] = {"professional", "casual", "enthusiastic"}VALID_EXPERTISE: set[str] = {"beginner", "intermediate", "expert"}VALID_RESPONSE_LENGTHS: set[str] = {"concise", "detailed"}PROPERTIES_CONTEXT_DESCRIPTION = "agent-config-properties"def _read_properties_from_context(    ctx: RunContext[StateDeps[AgentConfigState]],) -> dict[str, str]:    """Read the forwarded ``properties`` object with defensive defaults.    The TS runtime route at ``copilotkit-agent-config/route.ts`` appends a    context entry with ``description == "agent-config-properties"`` and a    JSON payload containing ``{tone, expertise, responseLength}``. Any    missing or unrecognized value falls back to the corresponding    ``DEFAULT_*`` constant. The function never raises.    """    copilotkit_state = getattr(ctx.deps, "copilotkit", None)    context_entries: list[Any] = []    if copilotkit_state and hasattr(copilotkit_state, "context"):        context_entries = copilotkit_state.context or []    payload: dict[str, Any] = {}    for entry in context_entries:        if not isinstance(entry, dict):            continue        if entry.get("description") != PROPERTIES_CONTEXT_DESCRIPTION:            continue        raw_value = entry.get("value")        if isinstance(raw_value, dict):            payload = raw_value        elif isinstance(raw_value, str):            try:                parsed = json.loads(raw_value)                if isinstance(parsed, dict):                    payload = parsed            except json.JSONDecodeError:                continue        if payload:            break    tone = payload.get("tone", DEFAULT_TONE)    expertise = payload.get("expertise", DEFAULT_EXPERTISE)    response_length = payload.get("responseLength", DEFAULT_RESPONSE_LENGTH)    if tone not in VALID_TONES:        tone = DEFAULT_TONE    if expertise not in VALID_EXPERTISE:        expertise = DEFAULT_EXPERTISE    if response_length not in VALID_RESPONSE_LENGTHS:        response_length = DEFAULT_RESPONSE_LENGTH    return {        "tone": tone,        "expertise": expertise,        "response_length": response_length,    }def _build_system_prompt(tone: str, expertise: str, response_length: str) -> str:    """Compose the system prompt from the three axes."""    tone_rules = {        "professional": ("Use neutral, precise language. No emoji. Short sentences."),        "casual": (            "Use friendly, conversational language. Contractions OK. "            "Light humor welcome."        ),        "enthusiastic": (            "Use upbeat, energetic language. Exclamation points OK. Emoji OK."        ),    }    expertise_rules = {        "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",        "intermediate": (            "Assume common terms are understood; explain specialized terms."        ),        "expert": ("Assume technical fluency. Use precise terminology. Skip basics."),    }    length_rules = {        "concise": "Respond in 1-3 sentences.",        "detailed": ("Respond in multiple paragraphs with examples where relevant."),    }    return (        "You are a helpful assistant.\n\n"        f"Tone: {tone_rules[tone]}\n"        f"Expertise level: {expertise_rules[expertise]}\n"        f"Response length: {length_rules[response_length]}"    )agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    deps_type=StateDeps[AgentConfigState],)@agent.system_promptdef build_prompt(ctx: RunContext[StateDeps[AgentConfigState]]) -> str:    props = _read_properties_from_context(ctx)    return _build_system_prompt(        props["tone"], props["expertise"], props["response_length"]    )__all__ = ["AgentConfigState", "agent"]

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/pydantic-ai/shared-state) instead.

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/pydantic-ai/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
