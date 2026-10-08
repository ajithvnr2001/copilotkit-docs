---
url: https://docs.copilotkit.ai/agno/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:45:53.476767+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/agno/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agno/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agno/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agno/learning)

[User Memories](https://docs.copilotkit.ai/agno/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agno/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Agno](https://docs.copilotkit.ai/agno)

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
    
    
    """Agno agent backing the Agent Config Object demo.Reads three forwarded properties — ``tone``, ``expertise``,``responseLength`` — that the CopilotKit provider forwards on every run,and composes the system prompt dynamically per turn.Agno does not have a LangGraph-style ``configurable`` channel; instead thecustom AGUI handler in ``agent_server.py`` (mounted at``/agent-config/agui``) reads ``RunAgentInput.forwarded_props``, builds afresh system prompt, and constructs a per-request Agno ``Agent`` with thatprompt before invoking it. The factory in this module produces thoseper-request agents."""from typing import Literalfrom agno.agent.agent import Agentfrom agno.models.openai import OpenAIChatfrom dotenv import load_dotenvload_dotenv()Tone = Literal["professional", "casual", "enthusiastic"]Expertise = Literal["beginner", "intermediate", "expert"]ResponseLength = Literal["concise", "detailed"]DEFAULT_TONE: Tone = "professional"DEFAULT_EXPERTISE: Expertise = "intermediate"DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise"VALID_TONES: set[str] = {"professional", "casual", "enthusiastic"}VALID_EXPERTISE: set[str] = {"beginner", "intermediate", "expert"}VALID_RESPONSE_LENGTHS: set[str] = {"concise", "detailed"}def read_properties(forwarded_props: dict | None) -> dict[str, str]:    """Read the forwarded ``properties`` dict with defensive defaults.    The CopilotKit provider forwards its ``properties`` prop as top-level    keys on ``forwarded_props`` (see the runtime's run handler). This    function never raises — every unrecognized value falls back to the    matching ``DEFAULT_*`` constant.    """    props = forwarded_props or {}    tone = props.get("tone", DEFAULT_TONE)    expertise = props.get("expertise", DEFAULT_EXPERTISE)    response_length = props.get("responseLength", DEFAULT_RESPONSE_LENGTH)    if tone not in VALID_TONES:        tone = DEFAULT_TONE    if expertise not in VALID_EXPERTISE:        expertise = DEFAULT_EXPERTISE    if response_length not in VALID_RESPONSE_LENGTHS:        response_length = DEFAULT_RESPONSE_LENGTH    return {        "tone": tone,        "expertise": expertise,        "response_length": response_length,    }def build_system_prompt(tone: str, expertise: str, response_length: str) -> str:    """Compose a system prompt from the three axes."""    tone_rules = {        "professional": ("Use neutral, precise language. No emoji. Short sentences."),        "casual": (            "Use friendly, conversational language. Contractions OK. "            "Light humor welcome."        ),        "enthusiastic": (            "Use upbeat, energetic language. Exclamation points OK. Emoji OK."        ),    }    expertise_rules = {        "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",        "intermediate": (            "Assume common terms are understood; explain specialized terms."        ),        "expert": ("Assume technical fluency. Use precise terminology. Skip basics."),    }    length_rules = {        "concise": "Respond in 1-3 sentences.",        "detailed": ("Respond in multiple paragraphs with examples where relevant."),    }    return (        "You are a helpful assistant.\n\n"        f"Tone: {tone_rules[tone]}\n"        f"Expertise level: {expertise_rules[expertise]}\n"        f"Response length: {length_rules[response_length]}"    )def build_agent(forwarded_props: dict | None) -> Agent:    """Build a per-request Agno agent whose system prompt reflects the    forwarded provider properties.    Constructed fresh on each run so the system prompt is current; the    Agno session DB still tracks history via ``session_id`` (the AGUI    handler passes ``thread_id`` through).    """    props = read_properties(forwarded_props)    system_prompt = build_system_prompt(        props["tone"], props["expertise"], props["response_length"]    )    return Agent(        model=OpenAIChat(id="gpt-4o-mini", temperature=0.4, timeout=120),        tools=[],        description=system_prompt,    )# A neutral default so AgentOS' agent-registry init doesn't fail before the# first run materialises a per-request agent.agent = build_agent(None)

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/agno/shared-state) instead.

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/agno/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
