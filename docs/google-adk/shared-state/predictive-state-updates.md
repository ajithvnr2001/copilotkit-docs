---
url: https://docs.copilotkit.ai/google-adk/shared-state/predictive-state-updates/
title: Predictive state updates
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:35.469082+00:00
---

# Predictive state updates

> Source: https://docs.copilotkit.ai/google-adk/shared-state/predictive-state-updates/

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

[Google ADK](https://docs.copilotkit.ai/google-adk)[Shared State](https://docs.copilotkit.ai/google-adk/shared-state)

# Predictive state updates

Stream in-progress agent state updates to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

An ADK agent's state updates discontinuously; only when state changes are explicitly made. But even a _single operation_ often takes many seconds to run and contains sub-steps of interest to the user.

**Agent-native applications** reflect to the end-user what the agent is doing **as continuously as possible.**

CopilotKit enables this through its concept of **_predictive state updates_**.

## When should I use this?#

Use predictive state updates when you want to:

  * **Keep users engaged** by avoiding long loading indicators
  * **Build trust** by demonstrating what the agent is working on
  * Enable **agent steering** \- allowing users to course-correct the agent if needed



## Important Note#

When your agent finishes executing, **its final state becomes the single source of truth**. While intermediate state updates are great for real-time feedback, any changes you want to persist must be explicitly included in the final state. Otherwise, they will be overwritten when the operation completes.

## Implementation#

### Define the state#

We'll be defining an `observed_steps` field in the state, which will be updated as the agent performs different steps of a task.

agent.py
    
    
    from typing import Dict, List
    from fastapi import FastAPI
    from pydantic import BaseModel
    from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    
    class AgentState(BaseModel):
        """State for the agent."""
        observed_steps: List[str] = []

### Emit the intermediate state#

### Observe the predictions#

These predictions will be emitted as the agent runs, allowing you to track its progress before the final state is determined.

ui/app/page.tsx
    
    
    "use client";
    
    
    // ...
    type AgentState = {
        observed_steps: string[];
    };
    
    const YourMainContent = () => {
        // Get access to both predicted and final states
        const { agent } = useAgent({ agentId: "my_agent" });
    
        // Add a state renderer to observe predictions
        useAgent({
            agentId: "my_agent",
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

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try!#

Now you'll notice that the state predictions are emitted as the agent makes progress, giving you insight into its work before the final state is determined. You can apply this pattern to any long-running task in your agent.

### On this page

What is this?When should I use this?Important NoteImplementation
