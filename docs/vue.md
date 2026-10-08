---
url: https://docs.copilotkit.ai/vue/
title: Vue quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:24.625696+00:00
---

# Vue quickstart

> Source: https://docs.copilotkit.ai/vue/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Quickstart](https://docs.copilotkit.ai/vue)[Docs status](https://docs.copilotkit.ai/vue/using-these-docs)

Guides

[Generative UI in Vue](https://docs.copilotkit.ai/vue/guides/generative-ui)[Reference docs](https://docs.copilotkit.ai/reference)

Guides coming soon...Vue is feature complete, but the docs are still catching up. The [quickstart](https://docs.copilotkit.ai/vue) and [reference](https://docs.copilotkit.ai/reference) guides are ready with more guides on the way.

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Getting Started

# Vue

Connect a Vue app to Copilot Runtime with CopilotKit.

`@copilotkit/vue` provides Vue 3 components and composables for CopilotKit. This guide gets you to a working Vue app with a chat UI backed by a local [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime) and `BuiltInAgent`.

The runtime runs on your server, keeps model credentials out of the browser, and exposes the `default` agent that `CopilotChat` uses automatically.

## Start with your coding agent#

Use this prompt to connect your Vue app to Copilot Runtime with the selected agent backend, then verify a working conversation. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/model-selection))
  * Vue 3.3+
  * Node.js 20+



## Getting started#

### Create your Vue app#

If you don't have one already:
    
    
    npm create vue@latest my-copilot-app
    cd my-copilot-app
    npm install

### Install CopilotKit#

Install the Vue frontend package and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/vue @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/vue @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/vue @copilotkit/runtime
    yarn add -D tsx typescript @types/node

### Create the Copilot Runtime#

Add a small Node server that hosts Copilot Runtime at `/api/copilotkit` and registers a `default` built-in agent:

server.ts
    
    
    import { createServer } from "node:http";
    import { BuiltInAgent, CopilotRuntime } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({
          model: "openai:gpt-5-mini",
          prompt: "You are a helpful assistant for a Vue app.",
        }),
      },
    });
    
    const port = Number(process.env.PORT ?? 8200);
    
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

### Import the styles#

Import the package stylesheet once in your app entry. It's self-contained, so the chat renders without any other CSS.

src/main.ts
    
    
    import { createApp } from "vue";
    import App from "./App.vue";
    import "@copilotkit/vue/styles.css"; 
    
    createApp(App).mount("#app");

### Connect to Copilot Runtime#

Point `CopilotKitProvider` at the runtime endpoint and drop in `CopilotChat`. Because the runtime registers an agent named `default`, the chat picks it up automatically.

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider, CopilotChat } from "@copilotkit/vue/v2"; 
    </script>
    
    <template>
      <CopilotKitProvider
        runtime-url="http://localhost:8200/api/copilotkit"
        show-dev-console="auto"
      >
        <div style="height: 100vh">
          <CopilotChat />
        </div>
      </CopilotKitProvider>
    </template>

Pick your chat layout

`CopilotChat` is a full-height chat. Swap it for `CopilotSidebar` (a collapsible side panel) or `CopilotPopup` (a floating widget) for a different layout. They take the same props.

### Run the runtime and app#

Start Copilot Runtime in one terminal:
    
    
    export OPENAI_API_KEY=sk-...
    npx tsx server.ts

Start the Vue app in another terminal:
    
    
    npm run dev

Open the dev server URL (Vite prints it, usually `http://localhost:5173`), send a message, and you'll see it stream back through Copilot Runtime.

Troubleshooting

  * **Chat renders unstyled** : Make sure you imported `@copilotkit/vue/styles.css` in your app entry.
  * **No response from the agent** : Confirm the runtime server is running and `http://localhost:8200/api/copilotkit/info` returns agent information.
  * **CORS errors** : Keep `cors: true` in `createCopilotNodeListener` for local development, or configure CORS to allow your Vue app's origin in production.
  * **Model auth errors** : Confirm `OPENAI_API_KEY` is set in the terminal running `npx tsx server.ts`.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/inspector).

## Where to go next#

  * [Generative UI in Vue](https://docs.copilotkit.ai/vue/guides/generative-ui): render a tool result as a card, an A2UI surface, or sandboxed UI instead of plain text. This is the same regardless of which agent framework you put behind the runtime.
  * [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime): runtime setup, auth, middleware, and routing.
  * [Built-in Agent quickstart](https://docs.copilotkit.ai/quickstart): configure the in-process agent used in this quickstart.
  * [Integrations](https://docs.copilotkit.ai/integrations/langgraph): connect LangGraph, CrewAI, Mastra, and other agents through the runtime.



The composables (`useAgent`, `useFrontendTool`, `useHumanInTheLoop`, and more) mirror the React SDK. See the [`@copilotkit/vue` README](https://github.com/CopilotKit/CopilotKit/tree/main/packages/vue) for the full API, slot-based customization, and Nuxt SSR setup.
