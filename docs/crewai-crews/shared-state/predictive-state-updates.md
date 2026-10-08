---
url: https://docs.copilotkit.ai/crewai-crews/shared-state/predictive-state-updates/
title: Predictive state updates
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:58:04.972011+00:00
---

# Predictive state updates

> Source: https://docs.copilotkit.ai/crewai-crews/shared-state/predictive-state-updates/

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

[Reading agent state](https://docs.copilotkit.ai/crewai-crews/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/crewai-crews/shared-state/in-app-agent-write)[Predictive state updates](https://docs.copilotkit.ai/crewai-crews/shared-state/predictive-state-updates)

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

Predictive state updates

InteractivityShared state

# Predictive state updates

Stream in-progress agent state updates to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it!

## What is this?#

A CrewAI Flow's state updates discontinuosly; only across function transitions in the flow. But even a _single function_ in the flow often takes many seconds to run and contain sub-steps of interest to the user.

**Agent-native applications** reflect to the end-user what the agent is doing **as continuously possible.**

CopilotKit enables this through its concept of **_predictive state updates_**.

## When should I use this?#

You can use this when you want to provide the user with feedback about what your agent is doing, specifically to:

  * **Keep users engaged** by avoiding long loading indicators
  * **Build trust** by demonstrating what the agent is working on
  * Enable **agent steering** \- allowing users to course-correct the agent if needed



## Important Note#

When a function in your CrewAI flow finishes executing, **its returned state becomes the single source of truth**. While intermediate state updates are great for real-time feedback, any changes you want to persist must be explicitly included in the function's final returned state. Otherwise, they will be overwritten when the function completes.

## Implementation#

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Define the state#

We'll be defining a `observed_steps` field in the state, which will be updated as the agent writes different sections of the report.

Python

agent.py
    
    
    from copilotkit.crewai import CopilotKitState
    from typing import Literal
    
    class AgentState(CopilotKitState):
        observed_steps: list[str]  # Array of completed steps

### Emit the intermediate state#

### Observe the predictions#

These predictions will be emitted as the agent runs, allowing you to track its progress before the final state is determined.

ui/app/page.tsx
    
    
    // ...
    
    const YourMainContent = () => {
        // Get access to both predicted and final states
        const { agent } = useAgent({ agentId: "sample_agent" });
    
        // Add a state renderer to observe predictions
        useAgent({
            agentId: "sample_agent",
            render: ({ state }) => {
                if (!state.observed_steps?.length) return null;
                return (
                    <div>
                        <h3>Current Progress:</h3>
                        <ul>
                            {state.observed_steps.map((step, i) => (
                                <li key={i}>{step}</li>
                            ))}
                        </ul>
                    </div>
                );
            },
        });
    
        return (
            <div>
                <h1>Agent Progress</h1>
                {agent.state?.observed_steps?.length > 0 && (
                    <div>
                        <h3>Final Steps:</h3>
                        <ul>
                            {agent.state.observed_steps.map((step, i) => (
                                <li key={i}>{step}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        )
    }

### Give it a try!#

Now you'll notice that the state predictions are emitted as the agent makes progress, giving you insight into its work before the final state is determined. You can apply this pattern to any long-running task in your agent.

### On this page

What is this?When should I use this?Important NoteImplementation
