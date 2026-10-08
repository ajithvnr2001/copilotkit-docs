---
url: https://docs.copilotkit.ai/frontends/react-spa/
title: React SPA quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:28.427584+00:00
---

# React SPA quickstart

> Source: https://docs.copilotkit.ai/frontends/react-spa/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact SPAAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Quickstart](https://docs.copilotkit.ai/react-spa)[Docs status](https://docs.copilotkit.ai/react-spa/using-these-docs)[Reference docs](https://docs.copilotkit.ai/reference)

Guides coming soon...React SPA is feature complete, but the docs are still catching up. The [quickstart](https://docs.copilotkit.ai/react-spa) and [reference](https://docs.copilotkit.ai/reference) guides are ready with more guides on the way.

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Getting Started

# React SPA

Host Copilot Runtime for a React single-page app that has no server of its own.

The rest of these docs are the React docs. [Frontend tools](https://docs.copilotkit.ai/frontend-tools), [generative UI](https://docs.copilotkit.ai/generative-ui), [human-in-the-loop](https://docs.copilotkit.ai/human-in-the-loop), [headless UI](https://docs.copilotkit.ai/headless), [prebuilt components](https://docs.copilotkit.ai/prebuilt-components) and the [React reference](https://docs.copilotkit.ai/reference/v2) all work unchanged in a Vite or Create React App project.

Exactly one instruction does not carry over: **where Copilot Runtime lives.** The quickstarts assume Next.js serves your app and the runtime from one origin, so they use a relative `runtimeUrl` of `/api/copilotkit`. A single-page app has no server and no shared origin, so that path resolves to nothing. This page covers that one difference and sends you back to the pages above for everything else.

## Start with your coding agent#

Use this prompt to connect your React single-page app to a separately hosted Copilot Runtime and verify a working conversation. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/model-selection))
  * React 18+
  * Node.js 20.6+ (for `--env-file`)



## Getting started#

### Create your React app#

If you don't have one already:
    
    
    npm create vite@latest my-copilot-app -- --template react-ts
    cd my-copilot-app
    npm install

An existing Create React App project works the same way — only the dev server command in the last step differs.

### Install CopilotKit#

Install the React frontend package and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/react-core @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/react-core @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/react-core @copilotkit/runtime
    yarn add -D tsx typescript @types/node

### Create the Copilot Runtime#

Your SPA has no server, so the runtime needs one of its own. Add a small Node server that hosts Copilot Runtime at `/api/copilotkit` on its own port and registers a `default` built-in agent:

server.ts
    
    
    import { createServer } from "node:http";
    import { BuiltInAgent, CopilotRuntime } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({
          model: "openai:gpt-5-mini",
          prompt: "You are a helpful assistant for a React app.",
        }),
      },
    });
    
    const port = 8200;
    
    createServer(
      createCopilotNodeListener({
        runtime,
        basePath: "/api/copilotkit",
        cors: true, 
      }),
    ).listen(port, () => {
      console.log(
        `Copilot Runtime listening at http://localhost:${port}/api/copilotkit`,
      );
    });

cors: true is required here, and it is not the default

Your app and your runtime are on different origins, so the runtime has to opt into CORS. `createCopilotNodeListener` and `createCopilotRuntimeHandler` are **off by default** — omit `cors` and every browser request fails preflight. This differs from the Express and Hono adapters, which default to permissive CORS. See [Runtime endpoints](https://docs.copilotkit.ai/backend/runtime-endpoints) for per-origin and credentialed configuration before you deploy.

### Import the styles#

Import the package stylesheet once in your app entry. It's self-contained, so the chat renders without any other CSS.

src/main.tsx
    
    
    import React from "react";
    import ReactDOM from "react-dom/client";
    import App from "./App";
    import "@copilotkit/react-core/v2/styles.css"; 
    
    ReactDOM.createRoot(document.getElementById("root")!).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
    );

### Connect to Copilot Runtime#

Point `CopilotKitProvider` at the runtime endpoint and drop in `CopilotChat`. Because the runtime registers an agent named `default`, the chat picks it up automatically.

src/App.tsx
    
    
    import { CopilotKitProvider, CopilotChat } from "@copilotkit/react-core/v2";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl="http://localhost:8200/api/copilotkit">
          <div style={{ height: "100vh" }}>
            <CopilotChat />
          </div>
        </CopilotKitProvider>
      );
    }

The runtimeUrl must be absolute

Every framework quickstart uses a relative `runtimeUrl="/api/copilotkit"`. That works **only** because Next.js serves the app and the runtime from the same origin. In a single-page app the runtime is a separate process on a separate port, so the URL has to name it in full — host and port included. Read it from an env var (`import.meta.env.VITE_COPILOT_RUNTIME_URL` in Vite) so you can point it at your deployed runtime in production.

To use a named agent from an integration quickstart, set `agentId` to the key registered in the runtime's `agents` map:
    
    
    <CopilotKitProvider
      runtimeUrl="http://localhost:8200/api/copilotkit"
      agentId="sample_agent"
    >
      <CopilotChat />
    </CopilotKitProvider>

`CopilotKitProvider` uses `agentId`; the `agent` prop shown in legacy `<CopilotKit>` examples is not a provider prop. Omit `agentId` when using the `default` agent above.

Pick your chat layout

`CopilotChat` is a full-height chat. Swap it for `CopilotSidebar` (a collapsible side panel) or `CopilotPopup` (a floating widget) for a different layout. They take the same props.

### Run the runtime and app#

You are running two dev servers, so they need two different ports. Before creating the server credential file, add this entry to your project's `.gitignore`:

.gitignore
    
    
    .env

Create `.env` beside `server.ts`:

.env
    
    
    OPENAI_API_KEY=sk-...

Start Copilot Runtime from that directory in one terminal:
    
    
    npx tsx --env-file=.env server.ts

A standalone Node process does not load `.env` automatically. The flag loads it before runtime imports run, including `CPK_INTELLIGENCE_API_KEY` when you connect [Intelligence](https://docs.copilotkit.ai/intelligence/quickstart). If the CLI wrote `.env` in a parent directory, point `--env-file` at that file instead. Keep server credentials out of `VITE_*` variables, which are exposed to the browser.

The `--env-file` flag preserves variables already set in the shell. If the project's `.env` should override those values for local development, install `dotenv` and add this before constructing the agent in `server.ts`:

npmpnpmyarn
    
    
    npm install dotenv
    
    
    pnpm add dotenv
    
    
    yarn add dotenv

server.ts — load the project environment
    
    
    import { config } from "dotenv";
    
    config({
      path: new URL("./.env", import.meta.url),
      override: true,
    });

This path selects the `.env` beside `server.ts`. Use `override: true` only when that file should take precedence over the inherited shell environment. Without it, an exported `OPENAI_API_KEY` wins even when `.env` contains a different key, which can send calls to the wrong project or cause model authentication errors. Keep the key server-side; do not prefix it with `VITE_` or include it in frontend code.

Start the React app in another terminal:
    
    
    npm run dev

Vite serves on `http://localhost:5173` and the runtime on `8200`, so the defaults don't collide. If you need to move the app, pass `--port` — **Vite ignores the`PORT` environment variable**, unlike Create React App:
    
    
    npm run dev -- --port 3000

Before opening the app, confirm the runtime is ready:
    
    
    curl --fail --silent --show-error http://localhost:8200/api/copilotkit/info

Wait until this succeeds and the JSON includes the `default` agent registered above.

If a dev script starts both processes together, wait for that same runtime readiness check before opening the browser. A listening Vite server does not mean the separate runtime is ready. Opening the app too early can leave its initial runtime connection in an error state; reload after `/info` succeeds if that has already happened.

Open the dev server URL, send a message, and you'll see it stream back through Copilot Runtime.

Troubleshooting

  * **CORS errors, or requests failing on preflight** : Keep `cors: true` in `createCopilotNodeListener`. It is off by default, and this is the most common cause of a chat that renders but never responds.
  * **404s on`/api/copilotkit`**: Your `runtimeUrl` is relative. A SPA needs the absolute `http://localhost:8200/api/copilotkit`.
  * **No response from the agent** : Confirm the runtime server is running and `http://localhost:8200/api/copilotkit/info` returns agent information.
  * **Chat renders unstyled** : Make sure you imported `@copilotkit/react-core/v2/styles.css` in your app entry.
  * **Model auth errors or Intelligence remains unconfigured** : Confirm the runtime starts with `npx tsx --env-file=.env server.ts` and the selected env file contains the required server credentials. Vite loading its own env file does not configure the runtime process.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/inspector).

## Next steps#

The runtime is the only SPA-specific piece. From here the root React docs apply as written:

  * [Frontend tools](https://docs.copilotkit.ai/frontend-tools) — let the agent call into your app
  * [Generative UI](https://docs.copilotkit.ai/generative-ui) — render your own components from agent output
  * [Human-in-the-loop](https://docs.copilotkit.ai/human-in-the-loop) — pause a run for user approval
  * [Headless UI](https://docs.copilotkit.ai/headless) — build your own chat surface
  * [Prebuilt components](https://docs.copilotkit.ai/prebuilt-components) — the chat, sidebar and popup layouts
  * [React reference](https://docs.copilotkit.ai/reference/v2) — full provider, hook and component API



To connect an agent framework instead of `BuiltInAgent`, follow any [integration quickstart](https://docs.copilotkit.ai/quickstart) and keep the `server.ts` host and absolute `runtimeUrl` from this page in place of its Next.js route handler.

## Connect a remote agent with Intelligence#

Most integration quickstarts run the agent as its own server and show the runtime as a Next.js route handler. For a single-page app, put the same runtime in `server.ts`. This example registers an agent server at `http://localhost:8000/` with `HttpAgent` and connects the runtime to [Intelligence](https://docs.copilotkit.ai/intelligence/quickstart).

Install the AG-UI client at the version that `@copilotkit/runtime` depends on:
    
    
    npm install @ag-ui/client@1.0.2

server.ts
    
    
    import { createServer } from "node:http";
    import { HttpAgent } from "@ag-ui/client";
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
    } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        my_agent: new HttpAgent({ url: "http://localhost:8000/" }),
      },
      intelligence: new CopilotKitIntelligence({
        apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
      }),
      // Local development only. See the warning below.
      identifyUser: (request) => ({
        id: request.headers.get("x-user-id") ?? "anonymous",
        name: request.headers.get("x-user-name") ?? "Anonymous",
      }),
    });
    
    const port = 8200;
    
    createServer(
      createCopilotNodeListener({
        runtime,
        basePath: "/api/copilotkit",
        cors: true,
      }),
    ).listen(port, () => {
      console.log(
        `Copilot Runtime listening at http://localhost:${port}/api/copilotkit`,
      );
    });

Replace the header identity before you deploy

This `identifyUser` trusts the `x-user-id` header, so any caller can pick a user, and a request without the header shares the `anonymous` threads. Return the user from a verified session or token, and reject requests that have none. `identifyUser` does not scope the `threads/events` and `threads/state` routes, so add your own ownership check for them. See [Thread authorization](https://docs.copilotkit.ai/auth#thread-authorization).

Run `npx copilotkit@latest project select` beside `server.ts` to write `CPK_INTELLIGENCE_API_KEY` to `.env`. Then start the runtime with `npx tsx --env-file=.env server.ts`, as in the steps above.

On the frontend, set `agentId` to the key in the `agents` map:
    
    
    <CopilotKitProvider
      runtimeUrl="http://localhost:8200/api/copilotkit"
      agentId="my_agent"
    >
      <CopilotChat />
    </CopilotKitProvider>

With Intelligence, the run route does not stream events to the browser. The provider reads them from Intelligence over a websocket. See [Run and connect with Intelligence](https://docs.copilotkit.ai/backend/runtime-endpoints#run-and-connect-with-intelligence).
