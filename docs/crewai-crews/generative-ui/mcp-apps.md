---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:02.473691+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/mcp-apps/

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

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/crewai-crews/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/crewai-crews/generative-ui/open-generative-ui)

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

MCP Apps

Generative UIOpen-ended

# MCP Apps

Render interactive UI components from MCP servers directly in your chat interface.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An OpenAI API key (or API key for your preferred LLM provider)
  * Node.js 20+
  * Your favorite package manager
  * An MCP server running (see Example MCP Servers below)



## What are MCP Apps?#

MCP Apps are MCP servers that expose tools with associated UI resources. When the agent calls one of these tools, CopilotKit automatically fetches and renders the UI component in the chat - no additional frontend code required.

Key benefits:

  * **Zero frontend code** \- UI components are served by the MCP server
  * **Full interactivity** \- Components can use HTML, CSS, and JavaScript
  * **Secure sandboxing** \- Content runs in isolated iframes
  * **Direct server communication** \- The middleware securely proxies communication between the rendered UI and the MCP server, enabling real-time interactions
  * **Thread persistence** \- MCP Apps are stored in conversation history and restored on reconnect



## Quickstart#

Want to try MCP Apps out with a new application? We have a pre-built example app you can use via our CLI.
    
    
    npx copilotkit create -f mcp-apps

## Getting started#

If you're looking to add an MCP App into an existing application, let's walk through the process.

### (Optional) Create a new application#

We'll be starting from scratch for this example, but feel free to skip this step if you already have an application.

For the sake of this example, we'll be using Next.js but the process will slot into any frontend React framework.
    
    
    npx create-next-app@latest

### Add the dependencies#
    
    
    npm install @copilotkit/react-core @copilotkit/runtime @ag-ui/mcp-apps-middleware

### Configure your agent#

Add your agent configuration to CopilotRuntime with your MCP server configurations:

This same process will work with any agent configuration.
    
    
    touch app/api/copilotkit/route.ts

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    import { BuiltInAgent } from "@copilotkit/runtime/v2";
    
    // 1. Create your agent
    const agent = new BuiltInAgent({
      model: "openai/gpt-5.4",
      prompt: "You are a helpful assistant.",
    });
    
    // 2. Create a service adapter, empty if not relevant
    
    // 3. Create the runtime with mcpApps configured
    const runtime = new CopilotRuntime({
      agents: {
        default: agent,
      },
      mcpApps: {
        servers: [
          {
            type: "http",
            url: "http://localhost:3108/mcp",
            serverId: "my-server", // Recommended: stable identifier
          },
        ],
      },
      runner: new InMemoryAgentRunner(),
    });
    
    // 4. Create the API route
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

Server ID

Always provide a `serverId` for production deployments. Without it, CopilotKit generates a hash from the server URL. If your URL changes (e.g., different environments), previously stored MCP Apps in conversation history won't load correctly.

Alternatively, if you want to scope MCP Apps to specific agents, you can use `MCPAppsMiddleware` directly on the agent via `.use()`:

app/api/copilotkit/route.ts
    
    
    import { MCPAppsMiddleware } from "@ag-ui/mcp-apps-middleware";
    
    const agent = new BuiltInAgent({
      model: "openai/gpt-5.4",
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

### Configure environment#

Create a `.env.local` file in your frontend directory and add your API key:

.env.local
    
    
    OPENAI_API_KEY=your_openai_api_key

What about other models?

The example is configured to use OpenAI's GPT-4o by default, but you can modify the BuiltInAgent to use any language model supported by CopilotKit.

### Configure CopilotKit Provider#

Wrap your application with the CopilotKit provider:

app/providers.tsx
    
    
    "use client";
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    export function Providers({ children }: { children: React.ReactNode }) {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" useSingleEndpoint={false}>
          {children}
        </CopilotKit>
      );
    }

`app/layout.tsx` is a server component and cannot import the provider directly, so it renders your client file instead:

app/layout.tsx
    
    
    import { Providers } from "./providers";
    import "@copilotkit/react-core/v2/styles.css";
    
    // ...
    
    export default function RootLayout({ children }: {children: React.ReactNode}) {
        return (
            <html lang="en">
                <body>
                    <Providers>
                        {children}
                    </Providers>
                </body>
            </html>
        );
    }

### Add the chat interface#

Add the CopilotSidebar component to your page:

app/page.tsx
    
    
    "use client";
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    
    export default function Page() {
        return (
            <main>
                <h1>Your App</h1>
                <CopilotSidebar />
            </main>
        );
    }

### Start your UI#

Start the development server:

npmpnpmyarnbun
    
    
    npm run dev
    
    
    pnpm dev
    
    
    yarn dev
    
    
    bun dev

Your application will be available at `http://localhost:3000`.

That's it! MCP Apps will now render automatically when the agent uses tools that have associated UI resources.

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

## Threading Support#

MCP Apps integrate fully with CopilotKit's threading system:

  * **Persistence** \- When you save a thread, MCP Apps are stored as part of the conversation history
  * **Restoration** \- Loading a thread restores all MCP Apps with their original state
  * **Server ID stability** \- Using consistent `serverId` values ensures MCP Apps load correctly across sessions



## Example MCP Servers#

Try these open-source MCP Apps servers to get started:

<https://github.com/modelcontextprotocol/ext-apps>

This repo contains multiple demo servers with tools like budget allocators, data visualizations, and interactive dashboards.

### On this page

PrerequisitesWhat are MCP Apps?QuickstartGetting startedTransport TypesHTTP TransportSSE TransportThreading SupportExample MCP Servers
