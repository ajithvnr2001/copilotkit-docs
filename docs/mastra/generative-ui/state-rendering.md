---
url: https://docs.copilotkit.ai/mastra/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:29.445027+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/mastra/generative-ui/state-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/mastra/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/mastra/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/mastra/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

State Rendering

Generative UIControlled

# State Rendering

Render the state of your agent with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

All Mastra Agents are stateful through working memory. This means that as your agent progresses, working memory is preserved across the session. CopilotKit allows you to render this state in your application with custom UI components, which we call **Agentic Generative UI**.

## When should I use this?#

Rendering the state of your agent in the UI is useful when you want to provide the user with feedback about the overall state of a session. A great example of this is a situation where a user and an agent are working together to solve a problem. The agent can store a draft in its working memory which is then rendered in the UI.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Set up your agent with working memory#

Create your Mastra agent with working memory. Here's a complete example that tracks searches:

src/mastra/agents/index.ts
    
    
    import { openai } from "@ai-sdk/openai";
    import { Agent } from "@mastra/core/agent";
    import { LibSQLStore } from "@mastra/libsql";
    import { z } from "zod";
    import { Memory } from "@mastra/memory";
    import { createTool } from "@mastra/core/tools";
    
    // Define the agent state schema
    const AgentStateSchema = z.object({
      searches: z.array(
        z.object({
          query: z.string(),
          done: z.boolean(),
        })
      ).default([]),
    });
    
    export type AgentState = z.infer<typeof AgentStateSchema>;
    
    // Create tools that update working memory
    const addSearch = createTool({
      id: "addSearch",
      inputSchema: z.object({
        query: z.string(),
      }),
      description: "Add a search to the agent's list of searches",
      execute: async ({ query }) => {
        // Tool implementation - working memory is automatically updated
        return { success: true, query };
      },
    });
    
    export const searchAgent = new Agent({
      id: "search-agent",
      name: "Search Agent",
      model: openai("gpt-5.4"),
      instructions: `
        You are a helpful assistant for storing searches.
    
        IMPORTANT:
        - Use the addSearch tool to add a search to the agent's state
        - ONLY USE THE addSearch TOOL ONCE FOR A GIVEN QUERY
      `,
      tools: {
        addSearch,
      },
      memory: new Memory({
        storage: new LibSQLStore({ id: "mastra-storage", url: ":memory:" }),
        options: {
          workingMemory: {
            enabled: true,
            schema: AgentStateSchema,
          },
        },
      }),
    });

### Render state of the agent in the chat#

Now we can utilize `useAgent` with a `render` function to render the state of our agent **in the chat**.

app/page.tsx
    
    
    // ...
    import { useAgent } from "@copilotkit/react-core/v2";
    // ...
    
    // Define the state of the agent, should match the working memory of your Mastra Agent.
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
        agentId: "searchAgent",
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

Important

The `name` parameter must exactly match the agent name you defined in your Mastra instance (e.g., `searchAgent` from above).

### Render state outside of the chat#

You can also render the state of your agent **outside of the chat**. This is useful when you want to render the state of your agent anywhere other than the chat.

app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    // ...
    
    // Define the state of the agent, should match the working memory of your Mastra Agent.
    type AgentState = {
      searches: {
        query: string;
        done: boolean;
      }[];
    };
    
    function YourMainContent() {
      // ...
    
      const { agent } = useAgent({
        agentId: "searchAgent",
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

Important

The `name` parameter must exactly match the agent name you defined in your Mastra instance (e.g., `searchAgent` from above).

### Give it a try!#

You've now created a component that will render the agent's working memory in the chat.

### On this page

What is this?When should I use this?Implementation
