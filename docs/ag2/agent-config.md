---
url: https://docs.copilotkit.ai/ag2/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:43:20.801259+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/ag2/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[AG2](https://docs.copilotkit.ai/ag2)

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
    
    
    """AG2 agent backing the Agent Config Object demo.Reads three forwarded properties — tone, expertise, responseLength — fromshared state (ContextVariables on each run) and adapts its responsesaccordingly.Wire format-----------The frontend uses `agent.setState({ tone, expertise, responseLength })` fromthe demo page. AG2's AGUIStream maps that initial state into ContextVariableson every run. The agent has a `get_current_config` tool that returns thecurrent rulebook for the assistant to consult before answering.The system prompt instructs the agent to call `get_current_config` once atthe start of every conversation turn so the response style adapts to thelatest UI selection.References:- src/agents/shared_state_read_write.py — same ContextVariables pattern."""import loggingfrom autogen import ConversableAgent, LLMConfigfrom autogen.ag_ui import AGUIStreamfrom autogen.agentchat import ContextVariablesfrom autogen.tools import toolfrom fastapi import FastAPIlogger = logging.getLogger(__name__)VALID_TONES = {"professional", "casual", "enthusiastic"}VALID_EXPERTISE = {"beginner", "intermediate", "expert"}VALID_RESPONSE_LENGTHS = {"concise", "detailed"}DEFAULT_TONE = "professional"DEFAULT_EXPERTISE = "intermediate"DEFAULT_RESPONSE_LENGTH = "concise"TONE_RULES = {    "professional": "Use neutral, precise language. No emoji. Short sentences.",    "casual": (        "Use friendly, conversational language. Contractions OK. Light humor welcome."    ),    "enthusiastic": (        "Use upbeat, energetic language. Exclamation points OK. Emoji OK."    ),}EXPERTISE_RULES = {    "beginner": "Assume no prior knowledge. Define jargon. Use analogies.",    "intermediate": ("Assume common terms are understood; explain specialized terms."),    "expert": ("Assume technical fluency. Use precise terminology. Skip basics."),}LENGTH_RULES = {    "concise": "Respond in 1-3 sentences.",    "detailed": ("Respond in multiple paragraphs with examples where relevant."),}SYSTEM_PROMPT = (    "You are a helpful assistant whose response style is governed by a UI-"    "supplied configuration object. Before answering ANY user question, "    "call the `get_current_config` tool exactly once to read the latest "    "tone / expertise / response-length rulebook. Then answer the user's "    "question, strictly following those rules. Never mention the tool call "    "or the configuration in your reply — just adapt your style.")@tool()def get_current_config(context_variables: ContextVariables) -> str:    """Return the current rulebook (tone / expertise / length) for the assistant.    Reads the forwarded ``tone``, ``expertise``, and ``responseLength``    properties from shared state, falling back to defaults for any missing    or unrecognized value.    """    data = context_variables.data or {}    tone = data.get("tone", DEFAULT_TONE)    expertise = data.get("expertise", DEFAULT_EXPERTISE)    response_length = data.get("responseLength", DEFAULT_RESPONSE_LENGTH)    if tone not in VALID_TONES:        tone = DEFAULT_TONE    if expertise not in VALID_EXPERTISE:        expertise = DEFAULT_EXPERTISE    if response_length not in VALID_RESPONSE_LENGTHS:        response_length = DEFAULT_RESPONSE_LENGTH    return (        f"Tone ({tone}): {TONE_RULES[tone]}\n"        f"Expertise ({expertise}): {EXPERTISE_RULES[expertise]}\n"        f"Response length ({response_length}): {LENGTH_RULES[response_length]}"    )agent_config_agent = ConversableAgent(    name="agent_config_assistant",    system_message=SYSTEM_PROMPT,    llm_config=LLMConfig({"model": "gpt-5-mini", "stream": True}),    human_input_mode="NEVER",    max_consecutive_auto_reply=5,    functions=[get_current_config],)agent_config_stream = AGUIStream(agent_config_agent)agent_config_app = FastAPI()agent_config_app.mount("/", agent_config_stream.build_asgi())

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/ag2/shared-state) instead.

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/ag2/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
