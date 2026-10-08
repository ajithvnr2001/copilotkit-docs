---
url: https://docs.copilotkit.ai/ms-agent-python/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:22.854305+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/ms-agent-python/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)

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
    
    
    """MS Agent Framework agent backing the Agent Config Object demo.Reads three forwarded properties -- tone, expertise, responseLength -- from theAG-UI run input's ``forwardedProps`` and composes its system prompt dynamicallyper turn.The CopilotKit provider's ``properties`` prop is wired through the runtime as``forwardedProps`` on each AG-UI run. We subclass ``AgentFrameworkAgent`` andprepend a request-local system message built from those properties. Each turnreplaces the prior injected message instead of mutating the shared agent.Invalid or missing values fall back to the corresponding ``DEFAULT_*``constant -- this function never raises so the demo can't deadlock on a badpayload."""from __future__ import annotationsfrom collections.abc import AsyncGeneratorfrom textwrap import dedentfrom typing import Any, Literalfrom uuid import uuid4from ag_ui.core import BaseEventfrom agent_framework import Agent, BaseChatClientfrom agent_framework_ag_ui import AgentFrameworkAgentTone = Literal["professional", "casual", "enthusiastic"]Expertise = Literal["beginner", "intermediate", "expert"]ResponseLength = Literal["concise", "detailed"]DEFAULT_TONE: Tone = "professional"DEFAULT_EXPERTISE: Expertise = "intermediate"DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise"VALID_TONES: set[str] = {"professional", "casual", "enthusiastic"}VALID_EXPERTISE: set[str] = {"beginner", "intermediate", "expert"}VALID_RESPONSE_LENGTHS: set[str] = {"concise", "detailed"}def read_properties(forwarded_props: Any) -> dict[str, str]:    """Read forwarded props with defensive defaults.    Any missing or unrecognized value falls back to the corresponding    ``DEFAULT_*`` constant. Never raises.    """    props = forwarded_props if isinstance(forwarded_props, dict) else {}    tone = props.get("tone", DEFAULT_TONE)    expertise = props.get("expertise", DEFAULT_EXPERTISE)    response_length = props.get("responseLength", DEFAULT_RESPONSE_LENGTH)    if tone not in VALID_TONES:        tone = DEFAULT_TONE    if expertise not in VALID_EXPERTISE:        expertise = DEFAULT_EXPERTISE    if response_length not in VALID_RESPONSE_LENGTHS:        response_length = DEFAULT_RESPONSE_LENGTH    return {        "tone": tone,        "expertise": expertise,        "response_length": response_length,    }def build_system_prompt(tone: str, expertise: str, response_length: str) -> str:    """Compose the system prompt from the three axes."""    tone_rules = {        "professional": ("Use neutral, precise language. No emoji. Short sentences."),        "casual": (            "Use friendly, conversational language. Contractions OK. "            "Light humor welcome."        ),        "enthusiastic": (            "Use upbeat, energetic language. Exclamation points OK. Emoji OK."        ),    }    expertise_rules = {        "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",        "intermediate": (            "Assume common terms are understood; explain specialized terms."        ),        "expert": ("Assume technical fluency. Use precise terminology. Skip basics."),    }    length_rules = {        "concise": "Respond in 1-3 sentences.",        "detailed": ("Respond in multiple paragraphs with examples where relevant."),    }    return (        "You are a helpful assistant.\n\n"        f"Tone: {tone_rules[tone]}\n"        f"Expertise level: {expertise_rules[expertise]}\n"        f"Response length: {length_rules[response_length]}"    )class AgentConfigFrameworkAgent(AgentFrameworkAgent):    """AgentFrameworkAgent that rebuilds its system prompt per request.    Overrides ``run`` to read ``forwardedProps`` from the AG-UI input and add    the resulting instructions to a request-local system message.    """    async def run(  # type: ignore[override]        self,        input_data: dict[str, Any],    ) -> AsyncGenerator[BaseEvent, None]:        props = read_properties(input_data.get("forwardedProps"))        system_prompt = build_system_prompt(            props["tone"], props["expertise"], props["response_length"]        )        messages = input_data.get("messages")        if not isinstance(messages, list) or len(messages) == 0:            async for event in super().run(input_data):                yield event            return        run_id = input_data.get("runId") or str(uuid4())        request_input = dict(input_data)        request_input["runId"] = run_id        request_input["messages"] = [            {                "id": f"{run_id}-agent-config",                "role": "system",                "content": system_prompt,            },            *[                message                for message in messages                if not (                    isinstance(message, dict)                    and isinstance(message.get("id"), str)                    and message["id"].endswith("-agent-config")                )            ],        ]        async for event in super().run(request_input):            yield eventdef create_agent_config_agent(chat_client: BaseChatClient) -> AgentConfigFrameworkAgent:    """Instantiate the Agent Config demo agent.    The base MS Agent Framework ``Agent`` carries only a neutral fallback    instruction. The real behavioural steering happens in the request-local    system message applied by ``AgentConfigFrameworkAgent.run``.    """    base_agent = Agent(        client=chat_client,        name="agent_config",        instructions=dedent(            """            You are a helpful assistant. Follow the tone, expertise level, and            response-length directives provided in the system message for each            turn. If no directive is provided, use professional / intermediate            / concise defaults.            """.strip()        ),        tools=[],    )    return AgentConfigFrameworkAgent(        agent=base_agent,        name="AgentConfigObjectDemo",        description=(            "Reads tone / expertise / responseLength from forwardedProps "            "and builds its system prompt per turn."        ),        require_confirmation=False,    )

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/ms-agent-python/shared-state) instead.

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/ms-agent-python/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
