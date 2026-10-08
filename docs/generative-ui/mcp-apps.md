---
url: https://docs.copilotkit.ai/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:01.487808+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/generative-ui/mcp-apps/

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

[MCP Apps](https://docs.copilotkit.ai/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/generative-ui/open-generative-ui)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

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

MCP Apps

Generative UIOpen-ended

# MCP Apps

Render interactive UI components from MCP servers directly in your chat interface.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

MCP Apps are MCP servers that expose tools with associated UI resources. When the agent calls one of these tools, CopilotKit automatically fetches and renders the UI component in the chat — no additional frontend code required.

Key benefits:

  * **Zero frontend code** — UI components are served by the MCP server
  * **Full interactivity** — Components can use HTML, CSS, and JavaScript
  * **Secure sandboxing** — Content runs in isolated iframes
  * **Thread persistence** — MCP Apps are stored in conversation history and restored on reconnect



## Implementation#

### Install the middleware#
    
    
    npm install @ag-ui/mcp-apps-middleware

### Add MCP Apps middleware to your agent#

Use `.use()` to attach the `MCPAppsMiddleware` to your `BuiltInAgent`:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    import { BuiltInAgent } from "@copilotkit/runtime/v2"; 
    import { MCPAppsMiddleware } from "@ag-ui/mcp-apps-middleware"; 
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      prompt: "You are a helpful assistant.",
    }).use( 
      new MCPAppsMiddleware({
        mcpServers: [
          {
            type: "http",
            url: "http://localhost:3108/mcp",
            serverId: "my-server",
          },
        ],
      }),
    );
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      runner: new InMemoryAgentRunner(),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

Server ID

Always provide a `serverId` for production deployments. Without it, CopilotKit generates a hash from the server URL. If your URL changes (e.g., different environments), previously stored MCP Apps in conversation history won't load correctly.

### Give it a try!#

That's it. MCP Apps will render automatically when the agent uses tools that have associated UI resources. No changes to your frontend are needed.

## Transport Types#

The middleware supports two transport types:

### HTTP Transport#

For MCP servers using HTTP-based communication:
    
    
    {
      type: "http",
      url: "http://localhost:3101/mcp",
      serverId: "my-http-server"
    }

### SSE Transport#

For MCP servers using Server-Sent Events:
    
    
    {
      type: "sse",
      url: "https://mcp.example.com/sse",
      headers: {
        "Authorization": "Bearer token"
      },
      serverId: "my-sse-server"
    }

## Example MCP Servers#

Try these open-source MCP Apps servers to get started:

<https://github.com/modelcontextprotocol/ext-apps>

### On this page

What is this?ImplementationTransport TypesHTTP TransportSSE TransportExample MCP Servers
