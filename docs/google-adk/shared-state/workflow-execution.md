---
url: https://docs.copilotkit.ai/google-adk/shared-state/workflow-execution/
title: Workflow Execution
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:37.985905+00:00
---

# Workflow Execution

> Source: https://docs.copilotkit.ai/google-adk/shared-state/workflow-execution/

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

ADK agents are stateful. As you execute tools and callbacks, that state is updated and available throughout the session. For this example, let's assume that the state our agent should be using can be described like this:

agent.py
    
    
    from typing import Dict, List
    from pydantic import BaseModel
    
    
    class AgentState(BaseModel):
        """Full state for the agent."""
        question: str = ""       # Input from user
        answer: str = ""         # Output to user
        resources: List[str] = []  # Internal use only

### Organize state by purpose#

Our example case lists several state properties, each with its own purpose:

  * The **question** is being asked by the user, expecting the LLM to answer
  * The **answer** is what the LLM returns
  * The **resources** list will be used by the LLM to answer the question, and should not be communicated to the user, or set by them



Here's a complete example showing how to structure your agent with these considerations:

agent.py
    
    
    from typing import Dict, List
    from fastapi import FastAPI
    from pydantic import BaseModel
    from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    
    class AgentState(BaseModel):
        """State for the agent."""
        question: str = ""       # Input: received from frontend
        answer: str = ""         # Output: sent to frontend
        resources: List[str] = []  # Internal: not shared with frontend
    
    
    def answer_question(tool_context: ToolContext, answer: str) -> Dict[str, str]:
        """Stores the answer to the user's question.
    
        Args:
            tool_context (ToolContext): The tool context for accessing state.
            answer (str): The answer to store in state.
    
        Returns:
            Dict[str, str]: A dictionary indicating success status.
        """
        tool_context.state["answer"] = answer
        return {"status": "success", "message": "Answer stored."}
    
    
    def add_resource(tool_context: ToolContext, resource: str) -> Dict[str, str]:
        """Adds a resource to the internal resources list.
    
        Args:
            tool_context (ToolContext): The tool context for accessing state.
            resource (str): The resource URL or reference to add.
    
        Returns:
            Dict[str, str]: A dictionary indicating success status.
        """
        resources = tool_context.state.get("resources", [])
        resources.append(resource)
        tool_context.state["resources"] = resources
        return {"status": "success", "message": "Resource added."}
    
    
    agent = LlmAgent(
        name="my_agent",
        model="gemini-2.5-flash",
        instruction="""
        You are a helpful assistant. When answering questions:
        1. Use add_resource to track any sources you reference (internal use)
        2. Use answer_question to provide your final answer to the user
    
        The question from the user is available in state as 'question'.
        """,
        tools=[answer_question, add_resource],
    )
    
    adk_agent = ADKAgent(
        adk_agent=agent,
        app_name="demo_app",
        user_id="demo_user",
        session_timeout_seconds=3600,
        use_in_memory_services=True,
    )
    
    app = FastAPI()
    add_adk_fastapi_endpoint(app, adk_agent, path="/")
    
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)

### Use the state in your frontend#

Now that we know which state properties our agent uses, we can work with them in the UI:

  * **question** : Set by the UI to ask the agent something
  * **answer** : Read from the agent's response
  * **resources** : Not accessible to the UI (internal agent use only)



ui/app/page.tsx
    
    
    "use client";
    
    import { useState } from "react";
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    // Define the agent state type, should match the actual state of your agent
    type AgentState = {
      question: string;
      answer: string;
    }
    
    /* Example usage in a pseudo React component */
    function YourMainContent() { 
      const [inputQuestion, setInputQuestion] = useState("What's the capital of France?");
      const [isLoading, setIsLoading] = useState(false);
    
      const { agent } = useAgent({
        agentId: "my_agent",
      });
      const { copilotkit } = useCopilotKit();
    
      const askQuestion = async (newQuestion: string) => {
        setIsLoading(true);
    
        // Update the state with the new question
        agent.setState({ ...agent.state, question: newQuestion, answer: "" });
    
        try {
          // Add a message and trigger the agent to run
          agent.addMessage({
            id: crypto.randomUUID(),
            role: "user",
            content: newQuestion,
          });
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("Error running agent:", error);
        } finally {
          setIsLoading(false);
        }
      };
    
      return (
        <div style={{ padding: "2rem", fontFamily: "system-ui, sans-serif" }}>
          <h1>Q&A Assistant</h1>
          
          <div style={{ marginBottom: "1rem" }}>
            <input
              type="text"
              value={inputQuestion}
              onChange={(e) => setInputQuestion(e.target.value)}
              placeholder="Enter your question..."
              style={{ 
                padding: "0.5rem", 
                width: "300px", 
                marginRight: "0.5rem",
                borderRadius: "4px",
                border: "1px solid #ccc"
              }}
            />
            <button 
              onClick={() => askQuestion(inputQuestion)}
    disabled={isLoading || !inputQuestion.trim()}
              style={{
                padding: "0.5rem 1rem",
                borderRadius: "4px",
                border: "none",
                backgroundColor: isLoading ? "#ccc" : "#0070f3",
                color: "white",
                cursor: isLoading ? "not-allowed" : "pointer"
              }}
            >
              {isLoading ? "Thinking..." : "Ask Question"}
            </button>
          </div>
    
          <div style={{ marginTop: "1.5rem" }}>
    <p><strong>Question:</strong> {agent.state?.question || "(none yet)"}</p>
    <p><strong>Answer:</strong> {agent.state?.answer || (isLoading ? "Thinking..." : "Waiting for question...")}</p>
          </div>
        </div>
      );
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
