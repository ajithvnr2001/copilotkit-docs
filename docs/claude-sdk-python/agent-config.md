---
url: https://docs.copilotkit.ai/claude-sdk-python/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:52:31.565620+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/claude-sdk-python/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Claude Agent SDK (Python)](https://docs.copilotkit.ai/claude-sdk-python)

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

route.ts
    
    
    """Claude Agent SDK backing the Agent Config Object demo.Reads three forwarded properties — tone, expertise, responseLength — fromthe AG-UI run's ``forwarded_props`` (which the dedicated runtime route at``/api/copilotkit-agent-config`` repacks from the CopilotKit provider's``properties`` prop) and builds the system prompt dynamically per turn.The companion Next.js route(``src/app/api/copilotkit-agent-config/route.ts``) ensures the frontend's``<CopilotKitProvider properties={{tone, expertise, responseLength}}>``values reach the AG-UI ``forwardedProps`` field on the request body, fromwhich this backend reads them.Unlike the langgraph-python reference — which routes through``RunnableConfig["configurable"]["properties"]`` inside a LangGraph node— Claude Agent SDK here reads the values directly off the AG-UI runinput's ``forwardedProps`` / ``forwarded_props`` envelope beforeconstructing the system prompt."""from __future__ import annotationsfrom typing import Any, LiteralTone = Literal["professional", "casual", "enthusiastic"]Expertise = Literal["beginner", "intermediate", "expert"]ResponseLength = Literal["concise", "detailed"]DEFAULT_TONE: Tone = "professional"DEFAULT_EXPERTISE: Expertise = "intermediate"DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise"VALID_TONES: set[str] = {"professional", "casual", "enthusiastic"}VALID_EXPERTISE: set[str] = {"beginner", "intermediate", "expert"}VALID_RESPONSE_LENGTHS: set[str] = {"concise", "detailed"}def read_properties(forwarded_props: Any) -> dict[str, str]:    """Read the three config axes with defensive defaults.    ``forwarded_props`` may arrive as either the raw top-level dict (when    the Next.js route forwards provider ``properties`` straight through)    or nested under ``config.configurable.properties`` (the LangGraph    convention the shared runtime route adopts for compatibility). We    accept both shapes — unknown values fall back to the defaults; the    function never raises.    """    if not isinstance(forwarded_props, dict):        forwarded_props = {}    # Prefer the nested shape (mirrors the langgraph-python convention    # the dedicated route repacks into) but fall back to top-level keys    # so the demo still works if a caller forwards properties directly.    nested = ((forwarded_props.get("config") or {}).get("configurable") or {}).get(        "properties"    ) or {}    props = nested if isinstance(nested, dict) and nested else forwarded_props    tone = props.get("tone", DEFAULT_TONE)    expertise = props.get("expertise", DEFAULT_EXPERTISE)    response_length = props.get("responseLength", DEFAULT_RESPONSE_LENGTH)    if tone not in VALID_TONES:        tone = DEFAULT_TONE    if expertise not in VALID_EXPERTISE:        expertise = DEFAULT_EXPERTISE    if response_length not in VALID_RESPONSE_LENGTHS:        response_length = DEFAULT_RESPONSE_LENGTH    return {        "tone": tone,        "expertise": expertise,        "response_length": response_length,    }def build_system_prompt(tone: str, expertise: str, response_length: str) -> str:    """Compose the system prompt from the three axes."""    tone_rules = {        "professional": ("Use neutral, precise language. No emoji. Short sentences."),        "casual": (            "Use friendly, conversational language. Contractions OK. "            "Light humor welcome."        ),        "enthusiastic": (            "Use upbeat, energetic language. Exclamation points OK. Emoji OK."        ),    }    expertise_rules = {        "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",        "intermediate": (            "Assume common terms are understood; explain specialized terms."        ),        "expert": ("Assume technical fluency. Use precise terminology. Skip basics."),    }    length_rules = {        "concise": "Respond in 1-3 sentences.",        "detailed": ("Respond in multiple paragraphs with examples where relevant."),    }    return (        "You are a helpful assistant.\n\n"        f"Tone: {tone_rules[tone]}\n"        f"Expertise level: {expertise_rules[expertise]}\n"        f"Response length: {length_rules[response_length]}"    )__all__ = [    "DEFAULT_TONE",    "DEFAULT_EXPERTISE",    "DEFAULT_RESPONSE_LENGTH",    "VALID_TONES",    "VALID_EXPERTISE",    "VALID_RESPONSE_LENGTHS",    "read_properties",    "build_system_prompt",]

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/claude-sdk-python/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

### Make runtime configuration explicit

The Claude Agent SDK demo reads configuration from shared state and folds it into the system prompt. This keeps the agent behavior visible to the UI and lets users tune model behavior without rebuilding the backend.

agent_config_agent.py
    
    
    Tone = Literal["professional", "casual", "enthusiastic"]
    Expertise = Literal["beginner", "intermediate", "expert"]
    ResponseLength = Literal["concise", "detailed"]
    
    DEFAULT_TONE: Tone = "professional"
    DEFAULT_EXPERTISE: Expertise = "intermediate"
    DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise"
    
    VALID_TONES: set[str] = {"professional", "casual", "enthusiastic"}
    VALID_EXPERTISE: set[str] = {"beginner", "intermediate", "expert"}
    VALID_RESPONSE_LENGTHS: set[str] = {"concise", "detailed"}
    
    
    def read_properties(forwarded_props: Any) -> dict[str, str]:
        """Read the three config axes with defensive defaults.
    
        ``forwarded_props`` may arrive as either the raw top-level dict (when
        the Next.js route forwards provider ``properties`` straight through)
        or nested under ``config.configurable.properties`` (the LangGraph
        convention the shared runtime route adopts for compatibility). We
        accept both shapes — unknown values fall back to the defaults; the
        function never raises.
        """
        if not isinstance(forwarded_props, dict):
            forwarded_props = {}
    
        # Prefer the nested shape (mirrors the langgraph-python convention
        # the dedicated route repacks into) but fall back to top-level keys
        # so the demo still works if a caller forwards properties directly.
        nested = ((forwarded_props.get("config") or {}).get("configurable") or {}).get(
            "properties"
        ) or {}
        props = nested if isinstance(nested, dict) and nested else forwarded_props
    
        tone = props.get("tone", DEFAULT_TONE)
        expertise = props.get("expertise", DEFAULT_EXPERTISE)
        response_length = props.get("responseLength", DEFAULT_RESPONSE_LENGTH)
    
        if tone not in VALID_TONES:
            tone = DEFAULT_TONE
        if expertise not in VALID_EXPERTISE:
            expertise = DEFAULT_EXPERTISE
        if response_length not in VALID_RESPONSE_LENGTHS:
            response_length = DEFAULT_RESPONSE_LENGTH
    
        return {
            "tone": tone,
            "expertise": expertise,
            "response_length": response_length,
        }
    
    
    def build_system_prompt(tone: str, expertise: str, response_length: str) -> str:
        """Compose the system prompt from the three axes."""
        tone_rules = {
            "professional": ("Use neutral, precise language. No emoji. Short sentences."),
            "casual": (
                "Use friendly, conversational language. Contractions OK. "
                "Light humor welcome."
            ),
            "enthusiastic": (
                "Use upbeat, energetic language. Exclamation points OK. Emoji OK."
            ),
        }
        expertise_rules = {
            "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",
            "intermediate": (
                "Assume common terms are understood; explain specialized terms."
            ),
            "expert": ("Assume technical fluency. Use precise terminology. Skip basics."),
        }
        length_rules = {
            "concise": "Respond in 1-3 sentences.",
            "detailed": ("Respond in multiple paragraphs with examples where relevant."),
        }
        return (
            "You are a helpful assistant.\n\n"
            f"Tone: {tone_rules[tone]}\n"
            f"Expertise level: {expertise_rules[expertise]}\n"
            f"Response length: {length_rules[response_length]}"
        )
    
    

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/claude-sdk-python/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
