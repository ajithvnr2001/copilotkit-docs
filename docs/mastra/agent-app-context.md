---
url: https://docs.copilotkit.ai/mastra/agent-app-context/
title: Agent App Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:48.082902+00:00
---

# Agent App Context

> Source: https://docs.copilotkit.ai/mastra/agent-app-context/

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

On this page

[Mastra](https://docs.copilotkit.ai/mastra)

# Agent App Context

Share app specific context with your agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

One of the most common use cases for CopilotKit is to register app state and context using `useAgentContext`. This way, you can notify your agent of what is going on in your app in real time.

## When should I use this?#

You can use this when you want to provide the user with feedback about what is in your working memory. As your agent's state updates, you can reflect these updates natively in your application.

Some examples might be: the current user, the current page, etc. This can be shared with your agent in real time.

## Implementation#

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

### Share data with your agent#

The [`useAgentContext` hook](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext) is used to add data as context to the Copilot.

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

### Consume the data in your Mastra agent#

Mastra has `RuntimeContext` class that can be used to set and access the extra context at run time. The context from CopilotKit is automatically injected there, and can be used immediately. You can read more about it [here](https://mastra.ai/en/docs/agents/runtime-context)

agent.ts
    
    
    import { openai } from "@ai-sdk/openai";
    import { Agent } from "@mastra/core/agent";
    
    export const colleaguesContactAgent = new Agent({
        id: "colleague-agent",
        name: "Colleagues contact Agent",
        model: openai("gpt-4o"),
        // Use the injected runtime context
        instructions: ({ requestContext }) => {
            const aguiContext = requestContext.get('ag-ui')?.context;
            const colleaguesContextItem = aguiContext?.find(contextItem => contextItem.description === "The current user's colleagues")
    
            // The value is already a JSON string, so parse it instead of stringifying it
            const colleagues = colleaguesContextItem ? JSON.parse(colleaguesContextItem.value) : [];
            const colleagueList = colleagues.map((c) => `${c.name} (${c.role})`).join(", ");
    
            return `
                You are a helpful assistant that can help emailing colleagues.
                The user's colleagues are: ${colleagueList}
            `
        },
        // ... Everything else used to configure your agent
    });

### Give it a try!#

Ask your agent a question about the context. It should be able to answer!

### On this page

What is this?When should I use this?Implementation
