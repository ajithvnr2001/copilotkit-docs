---
url: https://docs.copilotkit.ai/angular/llamaindex/shared-state/workflow-execution/
title: Workflow Execution
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:38.799615+00:00
---

# Workflow Execution

> Source: https://docs.copilotkit.ai/angular/llamaindex/shared-state/workflow-execution/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/llamaindex)[Quickstart](https://docs.copilotkit.ai/angular/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/llamaindex/intelligence/overview)

Basics

Generative UI

Interactivity

Shared state

[Workflow Execution](https://docs.copilotkit.ai/angular/llamaindex/shared-state/workflow-execution)

[WebMCP](https://docs.copilotkit.ai/angular/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/angular/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/angular/llamaindex/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Workflow Execution

InteractivityShared state

# Workflow Execution

Decide which state properties are received and returned to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Not all state properties are relevant for frontend-backend sharing. This guide shows how to ensure only the right portion of state is communicated back and forth.

## When should I use this?#

Depending on your implementation, some properties are meant to be processed internally, while some others are the way for the UI to communicate user input. In addition, some state properties contain a lot of information. Syncing them back and forth between the agent and UI can be costly, while it might not have any practical benefit.

## Implementation#

### Examine your state structure#

LlamaIndex agents using the AG-UI workflow router are stateful. As you execute tools and process messages, that state is updated and available throughout the session. For this example, let's assume that the state our agent should be using can be described like this:

agent.py
    
    
    # Full state structure for the agent
    initial_state = {
        "question": "",         # Input from user
        "answer": "",           # Output to user
        "resources": []         # Internal use only
    }

### Organize state by purpose#

Our example case lists several state properties, each with its own purpose:

  * The **question** is being asked by the user, expecting the LLM to answer
  * The **answer** is what the LLM returns
  * The **resources** list will be used by the LLM to answer the question, and should not be communicated to the user, or set by them



Here's a complete example showing how to structure your agent with these considerations:

agent.py
    
    
    from typing import Annotated, List
    from fastapi import FastAPI
    from llama_index.llms.openai import OpenAI
    from llama_index.core.workflow import Context
    from llama_index.protocols.ag_ui.router import get_ag_ui_workflow_router
    from llama_index.protocols.ag_ui.events import StateSnapshotWorkflowEvent
    
    async def answerQuestion(
        ctx: Context,
        answer: Annotated[str, "The answer to store in state."]
    ) -> str:
        """Stores the answer to the user's question in shared state.
    
        Args:
            ctx: The workflow context for state management.
            answer: The answer to store in state.
    
        Returns:
            str: A message indicating the answer was stored.
        """
        async with ctx.store.edit_state() as global_state:
            state = global_state.get("state", {})
            if state is None:
                state = {}
            
            state["answer"] = answer
            
            # Emit state update to frontend
            ctx.write_event_to_stream(
                StateSnapshotWorkflowEvent(snapshot=state)
            )
            
            global_state["state"] = state
        
        return f"Answer stored: {answer}"
    
    async def addResource(
        ctx: Context,
        resource: Annotated[str, "The resource URL or reference to add."]
    ) -> str:
        """Adds a resource to the internal resources list in shared state.
    
        Args:
            ctx: The workflow context for state management.
            resource: The resource URL or reference to add.
    
        Returns:
            str: A message indicating the resource was added.
        """
        async with ctx.store.edit_state() as global_state:
            state = global_state.get("state", {})
            if state is None:
                state = {}
            
            resources = state.get("resources", [])
            resources.append(resource)
            state["resources"] = resources
            
            global_state["state"] = state
        
        return f"Resource added: {resource}"
    
    # Initialize the LLM
    llm = OpenAI(model="gpt-5.4")
    
    # Create the AG-UI workflow router
    agentic_chat_router = get_ag_ui_workflow_router(
        llm=llm,
        system_prompt="""
        You are a helpful assistant. When the user asks a question:
        1. Think through your answer
        2. Optionally use addResource to track any sources you reference
        3. Use answerQuestion to provide your final answer - this stores it in state for the user to see
        
        Always use the answerQuestion tool to provide your response so it appears in the UI.
        """,
        backend_tools=[answerQuestion, addResource],
        initial_state={
            "question": "",       # Input: received from frontend
            "answer": "",         # Output: sent to frontend
            "resources": []       # Internal: tracking resources
        },
    )
    
    # Create FastAPI app
    app = FastAPI(
        title="LlamaIndex Agent",
        description="A LlamaIndex agent integrated with CopilotKit",
        version="1.0.0"
    )
    
    # Include the router
    app.include_router(agentic_chat_router)
    
    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "agent": "llamaindex"}
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="localhost", port=8000)

### Use the state in your frontend#

Now that we know which state properties our agent uses, we can work with them in the UI:

  * **question** : Set by the UI to ask the agent something
  * **answer** : Read from the agent's response
  * **resources** : Not accessible to the UI (internal agent use only)



src/app/agent-state.component.ts
    
    
    import { Component, computed, inject, signal } from "@angular/core";
    import { CopilotKit, injectAgentStore } from "@copilotkit/angular";
    
    type AgentState = {
    question?: string;
    answer?: string;
    };
    
    @Component({
    selector: "app-agent-state",
    template: `
    <button type="button" (click)="askQuestion(question())">
    Ask agent
    </button>
    <p>{{ answer() || "Waiting for an answer..." }}</p>
    `,
    })
    export class AgentStateComponent {
    private readonly copilotKit = inject(CopilotKit);
    readonly store = injectAgentStore("my_agent");
    readonly question = signal("What's the capital of France?");
    readonly state = computed(
    () => (this.store().state() as AgentState | undefined) ?? {},
    );
    readonly answer = computed(() => this.state().answer);
    
    async askQuestion(question: string): Promise<void> {
    const agent = this.store().agent;
    agent.setState({ ...this.state(), question, answer: "" });
    agent.addMessage({
    id: crypto.randomUUID(),
    role: "user",
    content: question,
    });
    await this.copilotKit.core.runAgent({ agent });
    }
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try!#

Now that we've organized state by purpose:

  * The UI can set `question` and read `answer`
  * The agent uses `resources` internally without exposing it to the frontend
  * State updates flow efficiently between frontend and backend



### On this page

What is this?When should I use this?Implementation
