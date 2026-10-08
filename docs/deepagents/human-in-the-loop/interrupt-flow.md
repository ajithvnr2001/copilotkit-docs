---
url: https://docs.copilotkit.ai/deepagents/human-in-the-loop/interrupt-flow/
title: Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:16.129120+00:00
---

# Interrupts

> Source: https://docs.copilotkit.ai/deepagents/human-in-the-loop/interrupt-flow/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Deep Agents](https://docs.copilotkit.ai/deepagents)[Human-in-the-Loop](https://docs.copilotkit.ai/deepagents/human-in-the-loop)

# Interrupts

Learn how to implement Human-in-the-Loop (HITL) using a interrupt-based flow.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates interrupt-based human-in-the-loop (HITL) in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/langgraph/feature/human_in_the_loop).

## What is this?#

[LangGraph's interrupt flow](https://docs.langchain.com/oss/python/langgraph/interrupts) provides an intuitive way to implement Human-in-the-loop workflows.

This guide will show you how to both use `interrupt` and how to integrate it with CopilotKit.

## When should I use this?#

Human-in-the-loop is a powerful way to implement complex workflows that are production ready. By having a human in the loop, you can ensure that the agent is always making the right decisions and ultimately is being steered in the right direction.

Interrupt-based flows are a very intuitive way to implement HITL. Instead of having a node await user input before or after its execution, nodes can be interrupted in the middle of their execution to allow for user input. The trade-off is that the agent is not aware of the interaction, however CopilotKit's SDKs provide helpers to alleviate this.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Set up your agent state#

We're going to have the agent ask us to name it, so we'll need a state property to store the name.

PythonTypeScript

agent.py
    
    
    from typing import NotRequired
    
    from copilotkit import CopilotKitState
    
    class AgentState(CopilotKitState):
        agent_name: NotRequired[str]

agent.ts
    
    
    import { createMiddleware } from "langchain";
    import { zodState } from "@copilotkit/sdk-js/langgraph"; 
    import { z } from "zod";
    
    export const agentNameMiddleware = createMiddleware({
        name: "AgentState",
        stateSchema: z.object({
            // zodState keeps this custom field in AG-UI state snapshots.
            agentName: zodState(z.string().optional()), 
        }),
    });

### Call `interrupt` in your Deep Agents agent#

Now we can call `interrupt` in our Deep Agents agent.

Your agent will not be aware of the `interrupt` interaction by default in LangGraph.

If you want this behavior, see the section on it below.

PythonTypeScript

agent.py
    
    
    from typing import Any, NotRequired
    
    from copilotkit import CopilotKitMiddleware, CopilotKitState
    from deepagents import create_deep_agent 
    from langchain.agents.middleware import AgentMiddleware 
    from langgraph.runtime import Runtime
    from langgraph.types import interrupt 
    
    class AgentState(CopilotKitState):
        agent_name: NotRequired[str]
    
    class AgentNameMiddleware(AgentMiddleware[AgentState, Any]):
        state_schema = AgentState
    
    def before_model(self, state: AgentState, runtime: Runtime[Any]) -> dict[str, Any] | None:
            if not state.get("agent_name"):
                # Interrupt and wait for the user to respond with a name
                name = interrupt("Before we start, what would you like to call me?") 
                return {"agent_name": name}
            return None
    
    agent = create_deep_agent(
        model="openai:gpt-4o",
        middleware=[
            AgentNameMiddleware(),
            CopilotKitMiddleware(expose_state=["agent_name"]), 
        ],
        system_prompt=(
            "You are a helpful assistant. After the user chooses a name, "
            "Current agent state contains agent_name. Use that value as your own name."
        ),
    )

In Deep Agents TypeScript, wire the interrupt into a middleware hook rather than a custom node. The hook below runs before the model call and asks the user for a name the first time.

agent.ts
    
    
    import {
        createCopilotkitMiddleware,
        zodState,
    } from "@copilotkit/sdk-js/langgraph"; 
    import { createMiddleware } from "langchain";
    import { createDeepAgent } from "deepagents"; 
    import { interrupt } from "@langchain/langgraph"; 
    import { z } from "zod";
    
    const agentNameMiddleware = createMiddleware({
        name: "AgentState",
        stateSchema: z.object({
            agentName: zodState(z.string().optional()), 
        }),
        beforeModel: (state) => {
            if (!state.agentName) {
                // Interrupt and wait for the user to respond with a name
                const name: string = interrupt("Before we start, what would you like to call me?"); 
                return { agentName: name };
            }
        },
    });
    
    const stateAwareCopilotKitMiddleware = createCopilotkitMiddleware({
        exposeState: ["agentName"], 
    });
    
    export const agent = createDeepAgent({
        model: "openai:gpt-4o",
        middleware: [
            agentNameMiddleware,
            stateAwareCopilotKitMiddleware,
        ],
        systemPrompt:
            "You are a helpful assistant. After the user chooses a name, " +
            "Current agent state contains agentName. Use that value as your own name.",
    });

### Handle the interrupt in your frontend#

At this point, your Deep Agents agent's `interrupt` will be called. However, we currently have no handling for rendering or responding to the interrupt in the frontend.

To do this, we'll use the `useInterrupt` hook, give it a component to render, and then call `resolve` with the user's response.

app/page.tsx
    
    
    import { useInterrupt } from "@copilotkit/react-core/v2"; 
    // ...
    
    const YourMainContent = () => {
    // ...
    // styles omitted for brevity
    useInterrupt({
        render: ({ event, resolve }) => (
            <div>
                <p>{event.value}</p>
                <form onSubmit={(e) => {
                    e.preventDefault();
                    resolve((e.target as HTMLFormElement).response.value);
                }}>
                    <input type="text" name="response" placeholder="Enter your response" />
                    <button type="submit">Submit</button>
                </form>
            </div>
        )
    });
    // ...
    
    return <div>{/* ... */}</div>
    }

When your app already selects an agent in its `CopilotKit` provider, `useInterrupt` uses that configured agent. Pass `agentId` only when this component must target a different agent in a multi-agent app.

### Give it a try!#

Try talking to your agent, you'll see that it now pauses execution and waits for you to respond!

## Make your agent aware of interruptions#

Resuming an interrupt and making the model aware of the result are separate concerns. The custom middleware saves the response in thread state. In TypeScript, `zodState` also preserves the custom field in the graph output schema so AG-UI can send it to the frontend.

The CopilotKit middleware then adds only the allowlisted name field to each model request. The system prompt explains what that field means, so after the run resumes the Deep Agent uses the selected name. Keep the allowlist narrow instead of exposing unrelated application state.

## Advanced usage#

### Condition UI executions#

When rendering multiple `interrupt` events in the agent, there could be conflicts between multiple `useInterrupt` hooks calls in the UI. For this reason, the hook can take an `enabled` argument which will apply it conditionally:

### Define multiple interrupts#

First, let's define two different interrupts. We will include a "type" property to differentiate them.

PythonTypeScript

agent.py
    
    
    from typing import Any
    from langchain.agents.middleware import AgentMiddleware
    from langgraph.runtime import Runtime
    from langgraph.types import interrupt 
    
    # ... your full state definition
    
    class ApprovalAndNameMiddleware(AgentMiddleware[AgentState, Any]):
        state_schema = AgentState
    
    def before_model(self, state: AgentState, runtime: Runtime[Any]) -> dict[str, Any] | None:
            approval = interrupt({ "type": "approval", "content": "please approve" }) 
            updates: dict[str, Any] = {"approval": approval}
    
            if not state.get("agent_name"):
                # Interrupt and wait for the user to respond with a name
                updates["agent_name"] = interrupt({ "type": "ask", "content": "Before we start, what would you like to call me?" }) 
    
            return updates

agent.ts
    
    
    import { zodState } from "@copilotkit/sdk-js/langgraph";
    import { createMiddleware } from "langchain";
    import { interrupt } from "@langchain/langgraph"; 
    import { z } from "zod";
    
    export const approvalAndNameMiddleware = createMiddleware({
        name: "AgentState",
        stateSchema: z.object({
            agentName: zodState(z.string().optional()),
            approval: zodState(z.unknown().optional()),
        }),
        beforeModel: (state) => {
            const approval = interrupt({ type: "approval", content: "please approve" }); 
            const updates: Record<string, unknown> = { approval };
    
            if (!state.agentName) {
                updates.agentName = interrupt({ type: "ask", content: "Before we start, what would you like to call me?" }); 
            }
    
            return updates;
        },
    });

### Add multiple frontend handlers#

With the differentiator in mind, we will add a handler that takes care of any "ask" and any "approve" types. With two `useInterrupt` hooks in our page, we can leverage the `enabled` property to enable each in the right time:

app/page.tsx
    
    
    import { useInterrupt } from "@copilotkit/react-core/v2"; 
    // ...
    
    const ApproveComponent = ({ content, onAnswer }: { content: string; onAnswer: (approved: boolean) => void }) => (
        // styles omitted for brevity
        <div>
            <h1>Do you approve?</h1>
            <button onClick={() => onAnswer(true)}>Approve</button>
            <button onClick={() => onAnswer(false)}>Reject</button>
        </div>
    )
    
    const AskComponent = ({ question, onAnswer }: { question: string; onAnswer: (answer: string) => void }) => (
    // styles omitted for brevity
        <div>
            <p>{question}</p>
            <form onSubmit={(e) => {
                e.preventDefault();
                onAnswer((e.target as HTMLFormElement).response.value);
            }}>
                <input type="text" name="response" placeholder="Enter your response" />
                <button type="submit">Submit</button>
            </form>
        </div>
    )
    
    const YourMainContent = () => {
        // ...
        useInterrupt({
            enabled: ({ eventValue }) => eventValue.type === 'ask',
            render: ({ event, resolve }) => (
                <AskComponent question={event.value.content} onAnswer={answer => resolve(answer)} />
            )
        });
    
        useInterrupt({
            enabled: ({ eventValue }) => eventValue.type === 'approval',
            render: ({ event, resolve }) => (
                <ApproveComponent content={event.value.content} onAnswer={answer => resolve(answer)} />
            )
        });
    
        // ...
    }

### Preprocessing of an interrupt and programmatically handling an interrupt value#

When opting for custom chat UI, some cases may require pre-processing of the incoming values of interrupt event or even resolving it entirely without showing a UI for it. This can be achieved using the `handler` property, which is not required to return a React component.

The return value of the handler will be passed to the `render` method as the `result` argument.

app/page.tsx
    
    
    // We will assume an interrupt event in the following shape
    type Department = 'finance' | 'engineering' | 'admin'
    interface AuthorizationInterruptEvent {
        type: 'auth',
        accessDepartment: Department,
    }
    
    import { useInterrupt } from "@copilotkit/react-core/v2";
    
    const YourMainContent = () => {
        const [userEmail, setUserEmail] = useState({ email: 'example@user.com' })
        function getUserByEmail(email: string): { id: string; department: Department } {
            // ... an implementation of user fetching
        }
    
        // ...
        // styles omitted for brevity
        useInterrupt({
            handler: async ({ result, event, resolve }) => {
                const { department } = await getUserByEmail(userEmail)
                if (event.value.accessDepartment === department || department === 'admin') {
                    // Following the resolution of the event, we will not proceed to the render method
                    resolve({ code: 'AUTH_BY_DEPARTMENT' })
                    return;
                }
    
                return { department, userId }
            },
            render: ({ result, event, resolve }) => (
                <div>
                    <h1>Request for {event.value.type}</h1>
                    <p>Members from {result.department} department cannot access this information</p>
                    <p>You can request access from an administrator to continue.</p>
                    <button
                        onClick={() => resolve({ code: 'REQUEST_AUTH', data: { department: result.department, userId: result.userId } })}
                    >
                        Request Access
                    </button>
                    <button
                        onClick={() => resolve({ code: 'CANCEL' })}
                    >
                        Cancel
                    </button>
                </div>
            )
        });
        // ...
    
        return <div>{/* ... */}</div>
    }

### On this page

What is this?When should I use this?Implementation
