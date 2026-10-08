---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:05.252281+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/state-rendering/

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

[Components as Tools](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/crewai-crews/generative-ui/state-rendering)

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

State Rendering

Generative UIControlled

# State Rendering

Render the state of your agent with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video demonstrates the implementation section applied to our [coagents starter project](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter-crewai-flows).

## What is this?#

All CrewAI Flow agents are stateful. This means that as your agent progresses through nodes, a state object is passed between them perserving the overall state of a session. CopilotKit allows you to render this state in your application with custom UI components, which we call **Agentic Generative UI**.

## When should I use this?#

Rendering the state of your agent in the UI is useful when you want to provide the user with feedback about the overall state of a session. A great example of this is a situation where a user and an agent are working together to solve a problem. The agent can store a draft in its state which is then rendered in the UI.

## Implementation#

### Run and Connect your CrewAI Flow to CopilotKit#

First, you'll need to make sure you have a running CrewAI Flow. If you haven't already done this, you can follow the [getting started guide](https://docs.copilotkit.ai/crewai-flows/quickstart)

This guide uses the [CoAgents starter repo](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter-crewai-flows) as its starting point.

### Define your agent state#

If you're not familiar with CrewAI, your flows are stateful. As you progress through function, a state object is updated between them. CopilotKit allows you to easily render this state in your application.

For the sake of this guide, let's say our state looks like this in our agent.

Python

agent.py
    
    
    # ...
    from copilotkit.crewai import CopilotKitState # extends MessagesState
    # ...
    
    # This is the state of the agent.
    # It inherits from the CopilotKitState properties from CopilotKit.
    class AgentState(CopilotKitState):
        searches: list[dict]

### Simulate state updates#

Next, let's write some logic into our agent that will simulate state updates occurring.

Python

agent.py
    
    
    from crewai.flow.flow import start
    from litellm import completion
    from copilotkit.crewai import copilotkit_stream, CopilotKitState, copilotkit_emit_state
    from typing import TypedDict
    
    class Searches(TypedDict):
        query: str
        done: bool
    
    class AgentState(CopilotKitState):
        searches: list[Searches] = [] 
    
    @start
    async def chat(self):
        self.state.searches = [
            {"query": "Initial research", "done": False},
            {"query": "Retrieving sources", "done": False},
            {"query": "Forming an answer", "done": False},
        ]
        await copilotkit_emit_state(self.state)
    
        # Simulate state updates 
        for search in self.state.searches:
            await asyncio.sleep(1)
            search["done"] = True
            await copilotkit_emit_state(self.state)
    
        # Run the model to generate a response
        response = await copilotkit_stream(
            completion(
                model="openai/gpt-5.4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *self.state.get("messages", [])
                ],
                stream=True
            )
        )

### Render state of the agent in the chat#

Now we can utilize `useAgent` with a `render` function to render the state of our agent **in the chat**.

app/page.tsx
    
    
    // ...
    // ...
    
    // Define the state of the agent, should match the state of the agent in your Flow.
    type AgentState = {
      searches: {
        query: string;
        done: boolean;
      }[];
    };
    
    function YourMainContent() {
      // ...
    
      // styles omitted for brevity
      useAgent({
        agentId: "sample_agent",
        render: ({ state }) => (
          <div>
            {state.searches?.map((search, index) => (
              <div key={index}>
                {search.done ? "✅" : "❌"} {search.query}{search.done ? "" : "..."}
              </div>
            ))}
          </div>
        ),
      });
    
      // ...
    
      return <div>...</div>;
    }

### Render state outside of the chat#

You can also render the state of your agent **outside of the chat**. This is useful when you want to render the state of your agent anywhere other than the chat.

app/page.tsx
    
    
    // ...
    
    // Define the state of the agent, should match the state of the agent in your Flow.
    type AgentState = {
      searches: {
        query: string;
        done: boolean;
      }[];
    };
    
    function YourMainContent() {
      // ...
    
      const { agent } = useAgent({
        agentId: "sample_agent",
      })
    
      // ...
    
      return (
        <div>
          {/* ... */}
          <div className="flex flex-col gap-2 mt-4">
            {agent.state?.searches?.map((search, index) => (
              <div key={index} className="flex flex-row">
                {search.done ? "✅" : "❌"} {search.query}
              </div>
            ))}
          </div>
        </div>
      )
    }

### Give it a try!#

You've now created a component that will render the agent's state in the chat.

### On this page

What is this?When should I use this?Implementation
