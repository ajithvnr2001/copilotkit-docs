---
url: https://docs.copilotkit.ai/crewai-crews/agent-app-context/
title: Agent App Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:56:04.610877+00:00
---

# Agent App Context

> Source: https://docs.copilotkit.ai/crewai-crews/agent-app-context/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)

# Agent App Context

Share app specific context with your CrewAI Flow.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

One of the most common use cases for CopilotKit is to register app state and context using `useAgentContext`. This way, you can notify your agent of what is going on in your app in real time.

Some examples might be: the current user, the current page, the rows currently on screen.

## When should I use this?#

Use this when the agent's answer has to be about data your application holds rather than data the user retypes into the chat. A queue, a selection, a cart, a filtered table: the page already has it, and `useAgentContext` is how the agent gets it.

CrewAI needs a field on your state class

Unlike the [built-in agent](https://docs.copilotkit.ai/agent-app-context), a CrewAI Flow does **not** receive this context automatically, and the gap is easy to miss because it does not look like a missing field. The AG-UI adapter writes your entries into the run state under a `context` key — but `CopilotKitState` does not declare `context`, and a Flow state is a Pydantic model, so the key is dropped on validation before any `@start()` method runs.

That means `self.state.context` does not exist in the shape the quickstart shows, and reading it raises nothing — it is simply never there. Your crew still answers, fluently and in the right shape, from nothing. Step 2 below declares the field so the value survives, and step 3 puts it in front of the model.

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

### Declare `context` on your state class#

This is the step that is easy to skip, because nothing fails loudly without it. Subclass `CopilotKitState` as usual and add the field yourself.

flow.py
    
    
    from typing import Any
    
    from ag_ui_crewai import CopilotKitState
    from pydantic import Field
    
    class ColleaguesState(CopilotKitState):
        # Without this field Pydantic drops the entries the adapter just wrote.
        context: list[dict[str, Any]] = Field(default_factory=list) 

Each entry is a plain dict with the `description` and `value` you registered on the frontend. `value` arrives JSON-encoded as a string for anything that is not already a string.

### Render the context into the crew's work#

Declaring the field makes the data reachable. It does not put it in the prompt. Fold the entries into the text your crew actually reads, the same way you fold in the user's message.

flow.py
    
    
    import json
    
    from crewai import Agent, Crew, LLM, Process, Task
    from crewai.flow.flow import Flow, start
    
    BASE_BACKSTORY = """You are a helpful assistant that can help emailing colleagues.
    
    Answer only about the colleagues the page below sent you. If that list is empty, say the
    page sent no colleagues. If it holds colleagues but none of them match what the user asked
    about, say so and name the ones the page did send. Never invent a colleague."""
    
    
    def render_context(entries: list[dict[str, Any]]) -> str:
        """Turn the entries the frontend sent into prompt text."""
        if not entries:
            return "The page sent no context entries."
    
        blocks = []
        for entry in entries:
            description = entry.get("description", "(no description)")
            value = entry.get("value", "")
            if not isinstance(value, str):
                value = json.dumps(value, ensure_ascii=False)
            blocks.append(f"### {description}\n{value}")
        return "\n\n".join(blocks)
    
    
    class ColleaguesFlow(Flow[ColleaguesState]):
        @start()
        async def answer(self) -> str:
            question = "\n".join(
                str(message.get("content", ""))
                for message in self.state.messages
                if message.get("role") == "user"
            ).strip()
    
            # The field declared in step 2 is what makes this readable.
            page_context = render_context(self.state.context) 
    
            agent = Agent(
                role="Colleague assistant",
                goal="Answer about the colleagues the page sent, and nothing else.",
                backstory=BASE_BACKSTORY,
                llm=LLM(model="openai/gpt-4.1-mini"),
            )
            task = Task(
                description=(
                    "## Context from the page\n\n{page_context}\n\n"
                    "## The user asked\n\n{question}"
                ),
                expected_output="A direct answer grounded only in the context above.",
                agent=agent,
            )
            crew = Crew(agents=[agent], tasks=[task], process=Process.sequential)
            result = await crew.kickoff_async(
                inputs={"page_context": page_context, "question": question},
            )
    
            # A Flow's return value is not sent to the UI. Append the answer to
            # `messages` or the turn finishes with nothing rendered.
            self.state.messages.append({"role": "assistant", "content": str(result)})
            return str(result)

Pass the rendered context through `inputs` rather than formatting it into the `description` string yourself. CrewAI interpolates `{placeholder}` in a task description from `inputs`, so context full of JSON braces stays verbatim instead of being read as more placeholders.

### Give it a try!#

Ask your agent a question about the context. It should be able to answer.

Then check the answer against your own records, because this integration fails quietly. The reliable check is a control: send the same request once with the context and once with an empty context. Two answers that describe the same record mean the context changed nothing, and the agent is answering from its own invention.

A crew whose backstory forbids invention refuses instead of inventing, which looks safer and is the same defect — it is still answering with nothing. Compare against the empty control either way.

### On this page

What is this?When should I use this?Implementation
