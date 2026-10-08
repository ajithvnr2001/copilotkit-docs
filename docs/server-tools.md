---
url: https://docs.copilotkit.ai/server-tools/
title: Server Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:30.116033+00:00
---

# Server Tools

> Source: https://docs.copilotkit.ai/server-tools/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Server Tools](https://docs.copilotkit.ai/server-tools)[MCP Servers](https://docs.copilotkit.ai/mcp-servers)[Model Selection](https://docs.copilotkit.ai/model-selection)[Advanced Configuration](https://docs.copilotkit.ai/advanced-configuration)

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Server Tools

Agent capabilitiesBuilt-in Agent

# Server Tools

Define backend tools for your Built-in Agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What are Server Tools?#

Server tools are functions that run on your backend that the Built-in Agent can invoke. They're defined using `defineTool()` with Zod schemas for type-safe parameters.

## When should I use this?#

  * Your agent needs to access databases, APIs, or other backend services
  * You want type-safe tool parameters with validation
  * The tool logic requires server-side secrets or resources



The tool runs on the server; the UI still runs in the browser

`execute` runs on your server, so it can reach secrets, a database, or an internal service — and it cannot touch the DOM, component state, or anything else in the page. When the _action_ itself belongs in the browser, register it as a [frontend tool](https://docs.copilotkit.ai/frontend-tools) instead.

Rendering is separate from executing. A server tool's call still streams to the browser, so you can give it UI with a render-only registration under the same tool name while `execute` keeps running on the server.

Use [`useFrontendTool`](https://docs.copilotkit.ai/frontend-tools) for the browser-side action and `useRenderTool` for the render-only registration.

## Defining a tool#

src/copilotkit.ts
    
    
    import { BuiltInAgent, defineTool } from "@copilotkit/runtime/v2";
    import { z } from "zod";
    
    const getWeather = defineTool({
      name: "getWeather",
      description: "Get the current weather for a location",
      parameters: z.object({
        location: z.string().describe("The location's name"),
      }),
      execute: async ({ location }) => {
        // Your implementation here
        return { temperature: 72, condition: "sunny", location };
      },
    });
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      tools: [getWeather],
      maxSteps: 2                   //Important for tool calls
    });

`parameters` takes a schema validator, not JSON Schema

`parameters` must be a Standard Schema v1 validator — Zod, Valibot, ArkType and others qualify. Handing it a plain JSON Schema object throws while the tool's schema is being converted. The validator is also what gives `execute` its inferred argument type, so a hand-written JSON Schema loses that too.

## Tool response#

Tools can return any JSON-serializable value. The agent uses the response to continue the conversation.

## Multiple tools#

Pass an array of tools — the agent chooses which to call based on the user's request:

Two names to avoid

`AGUISendStateSnapshot` and `AGUISendStateDelta` are injected for you whenever the Built-in Agent makes the model call itself. Defining your own tool under either name replaces the built-in one and breaks shared state.

A server tool also wins any name collision with a frontend tool: define `getWeather` on both sides and the model only ever sees the server one, so the frontend handler never fires. Give each side a distinct name when both need their own.

src/copilotkit.ts
    
    
    const searchDocs = defineTool({
      name: "searchDocs",
      description: "Search the documentation for relevant articles",
      parameters: z.object({
        query: z.string().describe("The search query"),
      }),
      execute: async ({ query }) => {
        const results = await search(query);
        return { results, count: results.length };
      },
    });
    
    const createTicket = defineTool({
      name: "createTicket",
      description: "Create a support ticket",
      parameters: z.object({
        title: z.string().describe("Ticket title"),
        priority: z.enum(["low", "medium", "high"]).describe("Ticket priority"),
        description: z.string().describe("Detailed description of the issue"),
      }),
      execute: async ({ title, priority, description }) => {
        const ticket = await db.tickets.create({ title, priority, description });
        return { ticketId: ticket.id, status: "created" };
      },
    });
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      tools: [searchDocs, createTicket], 
      maxSteps: 2                        
    });

## Complex Zod schemas#

Use nested objects, arrays, enums, and optional fields for sophisticated tool parameters:
    
    
    const bookFlight = defineTool({
      name: "bookFlight",
      description: "Search for and book flights",
      parameters: z.object({
        trip: z.object({
          origin: z.string().describe("Origin airport code (e.g., SFO)"),
          destination: z.string().describe("Destination airport code (e.g., JFK)"),
          date: z.string().describe("Departure date in YYYY-MM-DD format"),
        }),
        passengers: z.array(
          z.object({
            name: z.string(),
            seatPreference: z.enum(["window", "middle", "aisle"]).optional(),
          })
        ).describe("List of passengers"),
        class: z.enum(["economy", "business", "first"]).default("economy"),
      }),
      execute: async ({ trip, passengers, class: seatClass }) => {
        const flights = await searchFlights(trip, seatClass);
        return { flights, passengerCount: passengers.length };
      },
    });

## Error handling#

Throw errors or return error objects from your tool — the agent will see the error and can inform the user or try a different approach:
    
    
    const getUser = defineTool({
      name: "getUser",
      description: "Look up a user by email",
      parameters: z.object({
        email: z.string().email().describe("The user's email address"),
      }),
      execute: async ({ email }) => {
        const user = await db.users.findByEmail(email);
        if (!user) {
          throw new Error(`No user found with email: ${email}`); 
        }
        return { id: user.id, name: user.name, role: user.role };
      },
    });

Return plain data

Whatever a tool returns is serialized before the model sees it. A class instance, a circular reference, or anything else `JSON.stringify` refuses is replaced by a placeholder string naming the tool, and the model reasons over that instead of your data. Return plain objects, arrays and primitives — including for error shapes.

## Multi-step tool calling#

By default, the agent performs a single step. If your agent needs to chain tool calls (e.g., search first, then create a ticket), set `maxSteps`:
    
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      maxSteps: 5, 
      tools: [searchDocs, createTicket, getUser],
    });

With `maxSteps: 5`, the agent can:

  1. Call `searchDocs` to find relevant info
  2. Process the result
  3. Call `createTicket` with details from the search
  4. Continue until done (up to 5 iterations)



See [Advanced Configuration](https://docs.copilotkit.ai/advanced-configuration) for more options like `toolChoice`, `temperature`, and `providerOptions`.

A factory ignores the `tools` array

Everything on this page describes a Built-in Agent constructed with `model` and `tools`. If you build one from a `factory` instead, the `tools` array is not read — the factory owns the model call, so it has to pass the tools itself. Convert them with `convertToolDefinitionsToVercelAITools` for an AI SDK factory, or the equivalent converter for your runner, and pass the result into the call the factory makes.

Using a custom backend?

If you're using the [Custom Agent](https://docs.copilotkit.ai/backend/custom-agent) instead of `BuiltInAgent`, see the "With Tools" examples for how to wire tools with AI SDK, TanStack AI, or custom backends.

### On this page

What are Server Tools?When should I use this?Defining a toolTool responseMultiple toolsComplex Zod schemasError handlingMulti-step tool calling
