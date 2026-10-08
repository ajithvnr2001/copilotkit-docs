---
url: https://docs.copilotkit.ai/llamaindex/shared-state/predictive-state-updates/
title: Predictive state updates
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:28.531705+00:00
---

# Predictive state updates

> Source: https://docs.copilotkit.ai/llamaindex/shared-state/predictive-state-updates/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/llamaindex/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/llamaindex/shared-state/in-app-agent-write)[Workflow Execution](https://docs.copilotkit.ai/llamaindex/shared-state/workflow-execution)[Predictive state updates](https://docs.copilotkit.ai/llamaindex/shared-state/predictive-state-updates)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Predictive state updates

InteractivityShared state

# Predictive state updates

Stream in-progress agent state updates to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

A LlamaIndex agent's state updates discontinuously; only when state changes are explicitly made. But even a _single operation_ often takes many seconds to run and contains sub-steps of interest to the user.

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
    
    
    from typing import List
    from llama_index.llms.openai import OpenAI
    from llama_index.protocols.ag_ui.router import get_ag_ui_workflow_router
    from fastapi import FastAPI
    
    # Define initial state with observed_steps
    initial_state = {
        "observed_steps": []
    }

### Emit the intermediate state#

### Observe the predictions#

These predictions will be emitted as the agent runs, allowing you to track its progress before the final state is determined.

ui/app/page.tsx
    
    
    "use client";
    
    import { useAgent } from "@copilotkit/react-core/v2";
    import { CopilotSidebar } from '@copilotkit/react-ui';
    import '@copilotkit/react-core/v2/styles.css';
    
    interface Step {
        description: string;
    status: 'pending' | 'completed';
    }
    
    interface AgentState {
        observed_steps: Step[];
    }
    
    export default function Page() {
        // Get access to both predicted and final states
        const { agent } = useAgent({ agentId: "my_agent" });
    
        // Add a state renderer to show progress in the chat
        useAgent({
            agentId: "my_agent",
            render: ({ state, status }) => {
                if (!state?.observed_steps?.length) return null;
                return (
                    <div className="p-4 bg-gray-50 rounded-lg border border-gray-200 my-2">
                        <h3 className="font-semibold text-gray-700 mb-2">
                            {status === 'inProgress' ? '⏳ Progress:' : '✅ Completed:'}
                        </h3>
                        <ul className="space-y-1">
                            {state.observed_steps.map((step, i) => (
                                <li key={i} className="flex items-center gap-2">
                                    <span>
                                        {step.status === 'completed' ? '✅' : '⏳'}
                                    </span>
                                    <span className={step.status === 'completed' ? 'text-green-700' : 'text-gray-600'}>
                                        {step.description}
                                    </span>
                                </li>
                            ))}
                        </ul>
                    </div>
                );
            },
        });
    
        return (
            <div>
                <header>
                    <h1>Agent Progress Demo</h1>
                </header>
    
                <main>
                    {/* Side panel showing final state */}
                    <aside>
                        <h2>Agent State</h2>
                        {agent.state?.observed_steps?.length > 0 ? (
                            <ul>
                                {agent.state.observed_steps.map((step, i) => (
                                    <li key={i}>
                                        <span>{step.status === 'completed' ? '✅' : '⏳'}</span>
                                        <span>{step.description}</span>
                                    </li>
                                ))}
                            </ul>
                        ) : (
                            <p>
                                {"No steps yet. Try asking to build a plan like \"create a recipe for ___\" or \"teach me how to fix a tire.\""}
                            </p>
                        )}
                    </aside>
    
                    {/* Chat area */}
                    <CopilotSidebar
                        labels={{
                            welcomeMessageText: "Hi! Ask me to do a task like \"teach me how to fix a tire.\""
                        }}
                    />
                </main>
            </div>
        );
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try!#

Now you'll notice that the state predictions are emitted as the agent makes progress, giving you insight into its work before the final state is determined. You can apply this pattern to any long-running task in your agent.

### On this page

What is this?When should I use this?Important NoteImplementation
