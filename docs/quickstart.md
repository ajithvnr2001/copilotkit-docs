---
url: https://docs.copilotkit.ai/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:50.492933+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/quickstart/

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

Quickstart

# Quickstart

Build a working AI chat with CopilotKit in minutes.

## Start with your coding agent#

Use this prompt to build a working chat with CopilotKit's built-in agent. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An OpenAI API key (or Anthropic/Google — see [Model Selection](https://docs.copilotkit.ai/model-selection))
  * Node.js 20+
  * Your favorite package manager



## Getting started#

### Create your frontend#

CopilotKit's React components work with Next.js, React Router, Remix, TanStack Start, Vite, and other React apps. This walkthrough uses Next.js because it can host the frontend and runtime in one project.
    
    
    npx create-next-app@latest my-copilot-app
    cd my-copilot-app

Already have an app?

Keep your current setup and install CopilotKit there. The CopilotKit CLI (`npx copilotkit@latest create`, aliased as `init`) creates a separate project; it does not modify an existing app.

Use the [React SPA guide](https://docs.copilotkit.ai/react-spa) for a client-only Vite app, or [deploy the runtime to your server framework](https://docs.copilotkit.ai/runtime-server-adapter) with the React Router or TanStack Start examples.

### Install CopilotKit packages#
    
    
    npm install @copilotkit/react-core @copilotkit/runtime

The components used below (`CopilotKitProvider`, `CopilotSidebar`) and the stylesheet all come from `@copilotkit/react-core/v2`, so `@copilotkit/react-ui` is not needed for this setup.

TypeScript: use bundler module resolution

CopilotKit's `/v2` subpaths are published through the package `exports` map, which TypeScript's legacy `"moduleResolution": "node"` (`node10`) ignores. Under that setting, type checking fails with `Cannot find module '@copilotkit/react-core/v2'` even though the app runs. Set `"moduleResolution": "bundler"` in `tsconfig.json`; if `module` is `commonjs` or unset, also set `"module": "esnext"`. `create-next-app` already uses `bundler`.

### Configure your environment#

Create a `.env` file and add your OpenAI API key:

.env
    
    
    OPENAI_API_KEY=your_openai_api_key

What about other models?

This example uses an OpenAI model. See [Model Selection](https://docs.copilotkit.ai/model-selection) for Anthropic, Google, or custom model setup.

### Setup Copilot Runtime#

Create an API route with the `BuiltInAgent` and `CopilotRuntime`:

Already have an agent? Do not use BuiltInAgent

`BuiltInAgent` is CopilotKit's _own_ agent — it calls the model directly. Registering it as `default` means chat talks to it, not to any agent you already wrote. It replaces your agent rather than connecting to it.

If you already have a LangGraph, CrewAI, Mastra, ADK, Pydantic AI or other agent, take the frontend steps from this page but get the runtime wiring from **your framework's** quickstart, which registers _your_ agent instead — for example [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/quickstart). Pick yours from [the docs landing](https://docs.copilotkit.ai/).

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { BuiltInAgent } from "@copilotkit/runtime/v2"; 
    
    const builtInAgent = new BuiltInAgent({ 
      model: "openai:gpt-5.4-mini",
    });
    
    const runtime = new CopilotRuntime({
      agents: { default: builtInAgent }, //,
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

### Configure CopilotKit Provider#

Wrap your application with the CopilotKit provider:

app/providers.tsx
    
    
    "use client";
    
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    
    export function Providers({ children }: { children: React.ReactNode }) {
      return (
        <CopilotKitProvider runtimeUrl="/api/copilotkit">
          {children}
        </CopilotKitProvider>
      );
    }

`app/layout.tsx` is a server component and cannot import the provider directly, so it renders your client file instead:

app/layout.tsx
    
    
    import { Providers } from "./providers"; 
    import "@copilotkit/react-core/v2/styles.css"; 
    import './globals.css';
    
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

This relative runtimeUrl assumes Next.js serves the runtime

`/api/copilotkit` resolves only because Next.js serves your app and the runtime from the same origin. A client-only frontend has no shared origin, so it needs a standalone runtime server of its own and an absolute `runtimeUrl` such as `http://localhost:8200/api/copilotkit`. The per-frontend guides at `/react-spa`, `/vue`, `/angular` and `/react-native` each show that setup.

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

### Start the development server#

npmpnpmyarnbun
    
    
    npm run dev
    
    
    pnpm dev
    
    
    yarn dev
    
    
    bun dev

### Start chatting#

Your AI agent is now ready to use! Try asking it some questions:
    
    
    Can you tell me a joke?
    
    
    Can you help me understand AI?
    
    
    What do you think about React?

Troubleshooting

  * If you're having connection issues, try using `0.0.0.0` or `127.0.0.1` instead of `localhost`
  * Check that your API key is correctly set in the `.env` file
  * Make sure the runtime endpoint path matches the `runtimeUrl` in your CopilotKit provider



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/inspector).

## Keep conversations between visits#

Your sample chat is running. When you need production conversation history, CopilotKit Intelligence can keep each user's messages, generated interfaces, and tool activity available across sessions and devices.

[Your sample chat is runningAdd persistent threads, analytics, inspection, and learning when your app is ready for them.Explore Intelligence](https://docs.copilotkit.ai/intelligence/overview)

## What's next?#

Now that your basic chat is running, explore these advanced features:

[🔧Server ToolsGive your agent backend capabilities with custom tools.](https://docs.copilotkit.ai/server-tools)[🔌MCP ServersConnect MCP servers for extended tool support.](https://docs.copilotkit.ai/mcp-servers)[💻Model SelectionSwitch to Anthropic, Google, or a custom model.](https://docs.copilotkit.ai/model-selection)[🖥️Frontend ToolsLet the agent interact with your UI.](https://docs.copilotkit.ai/frontend-tools)

### On this page

Start with your coding agentPrerequisitesGetting startedKeep conversations between visitsWhat's next?
