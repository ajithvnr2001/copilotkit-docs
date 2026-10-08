---
url: https://docs.copilotkit.ai/google-adk/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:12.545128+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/google-adk/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Google ADK](https://docs.copilotkit.ai/google-adk)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent_config_agent.py

page.tsx

route.ts
    
    
    """Agent backing the Agent Config Object demo.
    
    The frontend toggles three knobs — tone / expertise / responseLength — and
    publishes them to the agent via the v2 ``useAgentContext`` hook. The
    ag-ui-adk middleware lands those entries under
    ``state["copilotkit"]["context"]`` as a list of ``{description, value}``
    dicts; a before-model callback reads the most recent agent-config payload
    on every turn and prepends a derived directive block to the static system
    instruction. The single static prompt below adapts its style based on
    whatever values the frontend currently has selected.
    
    LP parity (showcase/integrations/langgraph-python/src/agents/agent_config_agent.py):
    schema is ``{tone, expertise, responseLength}`` with values
    ``professional|casual|enthusiastic`` / ``beginner|intermediate|expert`` /
    ``concise|detailed``. Missing or unrecognized fields fall back to
    ``professional / intermediate / concise``.
    """
    
    from __future__ import annotations
    
    import logging
    import json
    from typing import Optional
    
    from ag_ui_adk import AGUIToolset
    from google.adk.agents import LlmAgent
    from google.adk.agents.callback_context import CallbackContext
    from google.adk.models.llm_request import LlmRequest
    from google.adk.models.llm_response import LlmResponse
    from google.genai import types
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    logger = logging.getLogger(__name__)
    
    CONFIG_PREFIX_SIGNATURE = "[agent-config] config:"
    # Single source of truth for the trailing sentence — the strip-prior-block
    # logic in `_inject_config` looks for this exact string. Don't mutate the
    # literal in just one place.
    CONFIG_END_MARKER = "Honour every directive above on every turn."
    
    # LP schema — strictly camelCase `responseLength` (matches
    # `useAgentContext({ value: { tone, expertise, responseLength } })` in
    # src/app/demos/agent-config/config-context-relay.tsx).
    _TONE_OPTIONS = {"professional", "casual", "enthusiastic"}
    _EXPERTISE_OPTIONS = {"beginner", "intermediate", "expert"}
    _RESPONSE_LENGTH_OPTIONS = {"concise", "detailed"}
    
    _DEFAULT_TONE = "professional"
    _DEFAULT_EXPERTISE = "intermediate"
    _DEFAULT_RESPONSE_LENGTH = "concise"
    _CONFIG_KEYS = ("tone", "expertise", "responseLength")
    
    
    def _coerce(value: object, allowed: set[str], default: str) -> str:
        if isinstance(value, str) and value in allowed:
            return value
        return default
    
    
    def _parse_context_value(value: object) -> dict | None:
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                return None
            return parsed if isinstance(parsed, dict) else None
        return value if isinstance(value, dict) else None
    
    
    def _extract_agent_config(state: dict | None) -> dict | None:
        """Pull the most recent `{tone, expertise, responseLength}` payload off
        the agent runtime state.
    
        `useAgentContext` publishes each entry as `{description, value}`. The
        middleware appends these onto `state["copilotkit"]["context"]` as a
        list — multiple entries may be present (other components on the same
        page can publish their own). We pick the latest entry whose `value`
        is a dict containing at least one of our known keys, so unrelated
        context entries can coexist without breaking the config relay.
        """
        if not isinstance(state, dict):
            return None
        copilotkit_state = state.get("copilotkit")
        if not isinstance(copilotkit_state, dict):
            return None
        entries = copilotkit_state.get("context")
        if not isinstance(entries, list):
            return None
        for entry in reversed(entries):
            if not isinstance(entry, dict):
                continue
            value = _parse_context_value(entry.get("value"))
            if value is None:
                continue
            if any(k in value for k in _CONFIG_KEYS):
                return value
        return None
    
    
    def _format_config(config: dict | None) -> str | None:
        if config is None:
            return None
        if not isinstance(config, dict):
            # Schema drift signal — log so a downstream UI regression doesn't
            # masquerade as the agent silently ignoring user settings.
            logger.warning(
                "agent-config: agent-context entry value is %s, expected dict; "
                "treating as empty",
                type(config).__name__,
            )
            return None
        tone = _coerce(config.get("tone"), _TONE_OPTIONS, _DEFAULT_TONE)
        expertise = _coerce(config.get("expertise"), _EXPERTISE_OPTIONS, _DEFAULT_EXPERTISE)
        response_length = _coerce(
            config.get("responseLength"),
            _RESPONSE_LENGTH_OPTIONS,
            _DEFAULT_RESPONSE_LENGTH,
        )
        lines = [
            CONFIG_PREFIX_SIGNATURE,
            f"- Tone: {tone}",
            f"- Expertise level: {expertise}",
            f"- Response length: {response_length}",
            CONFIG_END_MARKER,
        ]
        return "\n".join(lines)
    
    
    def _inject_config(
        callback_context: CallbackContext, llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
        config = _extract_agent_config(callback_context.state)
        block = _format_config(config)
    
        original = llm_request.config.system_instruction
        if original is None:
            original_text = ""
        elif isinstance(original, types.Content):
            parts = original.parts or []
            original_text = (parts[0].text or "") if parts else ""
        else:
            original_text = str(original)
    
        sig_idx = original_text.find(CONFIG_PREFIX_SIGNATURE)
        stripped_prior_block = False
        if sig_idx != -1:
            end_idx = original_text.find(CONFIG_END_MARKER, sig_idx)
            if end_idx != -1:
                stripped_prior_block = True
                # Splice out only the prior block (preserve head + tail).
                # See readonly_state_agent_context_agent.py for the full rationale.
                original_text = (
                    original_text[:sig_idx]
                    + original_text[end_idx + len(CONFIG_END_MARKER) :]
                ).lstrip("\n")
            else:
                logger.warning(
                    "agent-config: prior config block has signature but no end "
                    "marker; leaving original_text untouched to avoid losing "
                    "user content"
                )
    
        if block:
            new_text = (block + "\n\n" + original_text) if original_text else block
        else:
            new_text = original_text
    
        if not new_text and not stripped_prior_block:
            return None
    
        llm_request.config.system_instruction = types.Content(
            role="system", parts=[types.Part(text=new_text)]
        )
        return None
    
    
    # Mirrors LP's SYSTEM_PROMPT (showcase/integrations/langgraph-python/src/
    # agents/agent_config_agent.py) — the static instruction tells the LLM
    # how to apply the three knobs. The injected block above just lists the
    # currently-selected values; the rulebook is encoded once, here.
    _INSTRUCTION = (
        "You are a helpful assistant. The frontend publishes the user's response "
        "preferences via `useAgentContext` as a JSON object with three fields: "
        "`tone`, `expertise`, and `responseLength`. Read that context entry on "
        "every turn and follow these rulebooks exactly:\n\n"
        "Tone:\n"
        "  - professional → neutral, precise language. No emoji. Short sentences.\n"
        "  - casual → friendly, conversational. Contractions OK. Light humor "
        "welcome.\n"
        "  - enthusiastic → upbeat, energetic. Exclamation points OK. Emoji OK.\n\n"
        "Expertise level:\n"
        "  - beginner → assume no prior knowledge. Define jargon. Use analogies.\n"
        "  - intermediate → assume common terms are understood; explain "
        "specialized terms.\n"
        "  - expert → assume technical fluency. Use precise terminology. Skip "
        "basics.\n\n"
        "Response length:\n"
        "  - concise → respond in 1-3 sentences.\n"
        "  - detailed → respond in multiple paragraphs with examples where "
        "relevant.\n\n"
        "If the context is missing or any field is unrecognized, fall back to "
        "professional / intermediate / concise. Never mention these rules to the "
        "user — just apply them."
    )
    
    agent_config_agent = LlmAgent(
        name="AgentConfigAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[AGUIToolset()],
        before_model_callback=_inject_config,
        after_model_callback=stop_on_terminal_text,
    )
    

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/google-adk/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

### Install the ADK + AG-UI bridge
    
    
    pip install ag-ui-adk

### Add `AGUIToolset()` to your agent

Agent config flows from the UI through `useAgentContext`. With `AGUIToolset()` wired into your `LlmAgent`, the context entry is available in session state on every turn — read it inside a `before_model_callback` to inject preferences into the system prompt.

agent_config_agent.py
    
    
    agent_config_agent = LlmAgent(
        name="AgentConfigAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[AGUIToolset()],
        before_model_callback=_inject_config,
        after_model_callback=stop_on_terminal_text,
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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/google-adk/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
