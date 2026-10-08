---
url: https://docs.copilotkit.ai/google-adk/agent-app-context/
title: Agent App Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:12.600115+00:00
---

# Agent App Context

> Source: https://docs.copilotkit.ai/google-adk/agent-app-context/

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

[Agent App Context](https://docs.copilotkit.ai/google-adk/agent-app-context)[LangSmith Platform](https://docs.copilotkit.ai/google-adk/deploy-langsmith)

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

Agent App Context

Agent capabilitiesGoogle ADK

# Agent App Context

Share app specific context with your ADK agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

One of the most common use cases for CopilotKit is to register app state and context using `useAgentContext`. This way, you can notify your agent of what is going on in your app in real time.

Some examples might be: the current user, the current page, the rows currently on screen.

## When should I use this?#

Use this when the agent's answer has to be about data your application holds rather than data the user retypes into the chat. A queue, a selection, a cart, a filtered table: the page already has it, and `useAgentContext` is how the agent gets it.

ADK needs one line on the agent side

Unlike the [built-in agent](https://docs.copilotkit.ai/agent-app-context), an ADK agent does **not** receive this context automatically. The AG-UI adapter stores it in ADK session state under `CONTEXT_STATE_KEY` (`"_ag_ui_context"`) and stops there. Nothing puts it in the prompt.

An `LlmAgent` built with a plain string `instruction` therefore never sees it. The agent still answers, fluently and in the right shape, from nothing — which reads like a working integration until you check the answer against your own records. Step 2 below is the step that connects them.

## Implementation#

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

### Share data with your agent#

The [`useAgentContext` hook](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext) adds data as context to the Copilot.

YourComponent.tsx
    
    
    "use client" // only necessary if you are using Next.js with the App Router.
    import { useAgentContext } from "@copilotkit/react-core/v2"; 
    import { useState } from 'react';
    
    export function YourComponent() {
        // Create colleagues state with some sample data
        const [colleagues, setColleagues] = useState([
            { id: 1, name: "John Doe", role: "Developer" },
            { id: 2, name: "Jane Smith", role: "Designer" },
            { id: 3, name: "Bob Wilson", role: "Product Manager" }
        ]);
    
        // Define agent context
        useAgentContext({
            description: "The current user's colleagues",
            value: colleagues,
        });
        return (
            // Your custom UI component
            <>...</>
        );
    }

### Read the context in your ADK agent#

Pass an [`InstructionProvider`](https://google.github.io/adk-docs/agents/llm-agents/#instructions) instead of a string. A provider receives a `ReadonlyContext`, and the adapter leaves the CopilotKit context at `ctx.state[CONTEXT_STATE_KEY]`.

agent.py
    
    
    import json
    
    from ag_ui_adk import ADKAgent, CONTEXT_STATE_KEY, add_adk_fastapi_endpoint 
    from google.adk.agents import LlmAgent
    from google.adk.agents.readonly_context import ReadonlyContext
    
    BASE_INSTRUCTION = """You are a helpful assistant that can help emailing colleagues.
    
    Answer only about the colleagues the page below sent you. If that list is empty, say the
    page sent no colleagues. If it holds colleagues but none of them match what the user asked
    about, say so and name the ones the page did send. Never invent a colleague."""
    
    
    def render_context(state) -> str:
        """Turn the entries the frontend sent into prompt text."""
        entries = state.get(CONTEXT_STATE_KEY) or [] 
        if not entries:
            return "The page sent no context entries."
    
        blocks = []
        for entry in entries:
            description = entry.get("description", "(no description)")
            value = entry.get("value", "")
            # `value` arrives already JSON-encoded as a string. Anything else is encoded
            # here so a dict never reaches the prompt as a Python repr.
            if not isinstance(value, str):
                value = json.dumps(value, ensure_ascii=False)
            blocks.append(f"### {description}\n{value}")
        return "\n\n".join(blocks)
    
    
    # An InstructionProvider, not a string.
    def build_instruction(ctx: ReadonlyContext) -> str:
        return f"{BASE_INSTRUCTION}\n\n## Context from the page\n\n{render_context(ctx.state)}\n"
    
    
    colleagues_agent = LlmAgent(
        name="colleagues_agent",
        model="gemini-2.5-flash",
        instruction=build_instruction, 
    )
    
    adk_agent = ADKAgent(
        adk_agent=colleagues_agent,
        app_name="demo_app",
        user_id="demo_user",
        use_in_memory_services=True,
    )

`ctx.state` is the form to reach for because it works on every `ag-ui-adk` version. On `ag-ui-adk` 0.7.0 with `google-adk` 1.22.0 or later the adapter also copies the same entries into `RunConfig.custom_metadata`, so `ctx.run_config.custom_metadata["ag_ui_context"]` reads them too. Neither path puts them in the prompt on its own — that is still the provider's job.

A provider is also the safer form for the braces. Under a string instruction ADK runs `inject_session_state` over the text; its regex matches any `{...}` run, but substitutes only when the contents are a valid state name. JSON such as `{"id": 1}` is therefore left verbatim, while an identifier-shaped block — a `{status}` inside one of your context values — is looked up in session state and raises `KeyError` when it is not there. A provider reports `bypass_state_injection=True` from `canonical_instruction` (a string reports `False`), so the rendered context is never scanned at all. Checked against `google-adk` at the `>=1.28.1` floor `ag-ui-adk` 0.7.0 requires.

### Or read it inside a tool#

The same entries reach any tool through `tool_context.state`, which is the better fit when only one tool needs the data rather than the whole prompt.

tools.py
    
    
    from ag_ui_adk import CONTEXT_STATE_KEY
    from google.adk.tools import ToolContext
    
    def find_colleague(tool_context: ToolContext, name: str) -> dict:
        """Look up one colleague among the ones the page sent."""
        entries = tool_context.state.get(CONTEXT_STATE_KEY) or [] 
        # ... read the entry whose `description` matches the one you registered
        return {"found": False}

### Give it a try!#

Ask your agent a question about the context. It should be able to answer.

Then check the answer against your own records, because this is the one integration that fails quietly. The reliable check is a control: send the same request once with the context and once with an empty context. Two answers that describe the same record mean the context changed nothing, and the agent is answering from its own invention.

### On this page

What is this?When should I use this?Implementation
