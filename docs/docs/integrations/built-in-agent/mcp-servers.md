---
url: https://docs.copilotkit.ai/docs/integrations/built-in-agent/mcp-servers/
title: MCP Servers
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:35:23.503914+00:00
---

# MCP Servers

> Source: https://docs.copilotkit.ai/docs/integrations/built-in-agent/mcp-servers/

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

MCP Servers

Agent capabilitiesBuilt-in Agent

# MCP Servers

Connect MCP servers to your Built-in Agent, with support for persistent clients, tool caching, and dynamic auth.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What are MCP Servers?#

MCP (Model Context Protocol) servers provide additional tools and capabilities to your agent. The Built-in Agent supports connecting to MCP servers via **HTTP** or **SSE** transports.

## When should I use this?#

  * You want to connect your agent to existing MCP-compatible tool servers
  * You need to add capabilities from third-party MCP providers
  * You want to share tools across multiple agents or applications



## SSE transport#

The SSE (Server-Sent Events) transport is the most common option:

src/copilotkit.ts
    
    
    import { BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpServers: [
        {
          type: "sse", 
          url: "https://my-mcp-server.example.com/sse",
        },
      ],
    });

### Authentication headers#

Pass custom headers for authentication:
    
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpServers: [
        {
          type: "sse",
          url: "https://my-mcp-server.example.com/sse",
          headers: { 
            Authorization: `Bearer ${process.env.MCP_API_KEY}`,
          },
        },
      ],
    });

## HTTP transport#

The HTTP (Streamable HTTP) transport uses standard HTTP requests:
    
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpServers: [
        {
          type: "http", 
          url: "https://my-mcp-server.example.com/mcp",
        },
      ],
    });

The HTTP transport also accepts optional `options` for advanced configuration of the underlying `StreamableHTTPClientTransport`.

## Multiple servers#

Connect multiple MCP servers — tools from all servers are available to the agent:
    
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpServers: [
        {
          type: "sse",
          url: "https://search-mcp.example.com/sse",
        },
        {
          type: "sse",
          url: "https://db-mcp.example.com/sse",
          headers: { Authorization: `Bearer ${process.env.DB_MCP_KEY}` },
        },
        {
          type: "http",
          url: "https://analytics-mcp.example.com/mcp",
        },
      ],
    });

### Tool name collisions#

Two servers can expose tools with the same name. For example, a staging server and a production server expose the same tools. The agent keeps every copy. When a name collides, each MCP copy gets a prefix, and the agent logs a warning:
    
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpServers: [
        { type: "http", url: "https://staging.example.com/mcp", name: "staging" }, 
        { type: "http", url: "https://prod.example.com/mcp", name: "production" }, 
      ],
    });
    // Both servers expose `search`, so the model sees `staging_search` and `production_search`.

  * Only names that collide get a prefix. Other tools keep their names.
  * If an MCP tool has the same name as one of your own tools, your tool keeps the name, and the MCP tool gets the prefix.
  * If a server has no `name`, the prefix is `mcp<N>`, where N is the server's position in `mcpClients` and then `mcpServers`, from 1. Entries in `mcpClients` have no `name`, so they always use `mcp<N>`.
  * Characters other than letters, digits, `_` and `-` in `name` become `_`.
  * If a prefixed name is already in use, a number is added, for example `production_search_2`. This happens when two servers have the same `name`, so give each server a different `name`.
  * A tool renderer that you register in the frontend matches only the exposed name. If `search` becomes `production_search`, register the renderer for `production_search`.



## Combining with server tools#

MCP servers work alongside `defineTool` server tools — the agent sees all tools from both sources:
    
    
    import { BuiltInAgent, defineTool } from "@copilotkit/runtime/v2";
    import { z } from "zod";
    
    const customTool = defineTool({
      name: "getUser",
      description: "Get the current user",
      parameters: z.object({}),
      execute: async () => {
        return { name: "Jane", role: "Admin" };
      },
    });
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      tools: [customTool], // Your custom tools
      mcpServers: [        // Plus tools from MCP servers
        { type: "sse", url: "https://search-mcp.example.com/sse" },
      ],
    });

## User-managed MCP clients#

The `mcpServers` approach creates a fresh MCP connection on every agent run. For latency-sensitive setups — or when you need persistent connections, dynamic auth, or tool caching — use `mcpClients` instead. You create and manage the MCP client yourself; the agent just calls `.tools()` to get tool definitions.
    
    
    import { BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createMCPClient } from "@ai-sdk/mcp";
    import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
    
    // Create a persistent client at startup
    const transport = new StreamableHTTPClientTransport(
      new URL("https://my-mcp-server.example.com/mcp"),
    );
    const client = await createMCPClient({ transport });
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpClients: [client], 
    });

Unlike `mcpServers`, the agent **never** creates or closes these clients — you control the full lifecycle.

### Tool caching#

By default, `.tools()` fetches from the MCP server on every agent run. To cache tools at startup:
    
    
    const client = await createMCPClient({ transport });
    
    let cachedTools: ToolSet | null = null;
    const warmupPromise = client.tools().then(tools => { cachedTools = tools; });
    
    const provider = {
      async tools() {
        if (cachedTools) return cachedTools;
        await warmupPromise;
        return cachedTools!;
      },
    };
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpClients: [provider], 
    });

Tool discovery runs once in the background. The first request waits only if warmup hasn't finished yet; subsequent requests return instantly from cache.

### Dynamic authentication#

When using a persistent client, auth tokens may expire between requests. Handle this inside your provider:
    
    
    const provider = {
      async tools() {
        if (isTokenExpired()) {
          await currentClient.close();
          currentClient = await createMCPClient({
            transport: makeTransport(getFreshToken()),
          });
        }
        return currentClient.tools();
      },
    };
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpClients: [provider],
    });

You only pay the reconnection cost when the token actually expires, not on every request.

### Combining with mcpServers#

`mcpClients` and `mcpServers` can be used together. Tools from both are merged — on name collision, `mcpServers` tools take precedence:
    
    
    const builtInAgent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      mcpClients: [persistentClient],  // User-managed, persistent
      mcpServers: [                     // Agent-managed, per-request
        { type: "sse", url: "https://other-mcp.example.com/sse" },
      ],
    });

## Transport reference#

Property| SSE| HTTP| Description  
---|---|---|---  
`type`| `"sse"`| `"http"`| Transport type  
`url`| string| string| MCP server URL  
`headers`| `Record<string, string>`| —| Custom HTTP headers (SSE only)  
`options`| —| `StreamableHTTPClientTransportOptions`| Transport options (HTTP only)  
  
### On this page

What are MCP Servers?When should I use this?SSE transportAuthentication headersHTTP transportMultiple serversTool name collisionsCombining with server toolsUser-managed MCP clientsTool cachingDynamic authenticationCombining with mcpServersTransport reference
