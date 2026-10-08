---
url: https://docs.copilotkit.ai/frontends/vue/guides/threads-and-drawer/
title: Threads and the threads drawer
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:33.176273+00:00
---

# Threads and the threads drawer

> Source: https://docs.copilotkit.ai/frontends/vue/guides/threads-and-drawer/

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

On this page

Guides

# Threads and the threads drawer

Persist Vue agent conversations and add a ready-made thread switcher with CopilotThreadsDrawer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`CopilotChat` covers the common conversation path. Use the thread APIs when you want conversations that survive a reload, and `CopilotThreadsDrawer` when you want a thread switcher beside the chat without wiring active-thread state yourself.

Threads are persisted by [CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/managed-intelligence-platform). The drawer reads the platform's `threads` license feature and renders its locked state instead of a thread list when that feature is unavailable.

## Resume a specific thread#

Pass `threadId` to connect the chat to an existing conversation:
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChat } from "@copilotkit/vue";
    
    const selectedThreadId = ref<string | undefined>(undefined);
    </script>
    
    <template>
      <CopilotChat agentId="support" :threadId="selectedThreadId" />
    </template>

## Add the threads drawer#

`CopilotThreadsDrawer` lists, switches, starts, archives and deletes threads. Put the drawer and chat under the same `CopilotChatConfigurationProvider` so selection and new-thread actions update the chat:
    
    
    <script setup lang="ts">
    import {
      CopilotChat,
      CopilotChatConfigurationProvider,
      CopilotThreadsDrawer,
    } from "@copilotkit/vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider agentId="support">
        <div class="flex">
          <CopilotThreadsDrawer :limit="20" />
          <CopilotChat />
        </div>
      </CopilotChatConfigurationProvider>
    </template>

### Options#

Prop| Type| Default| What it does  
---|---|---|---  
`agentId`| `string`| the default agent| Which agent's threads the drawer lists.  
`limit`| `number`| the element's own default| How many threads to list.  
`label`| `string`| the element's own default| Accessible label for the drawer.  
`recentLabel`| `string`| `"Recent Conversations"`| Heading above the thread list.  
`collapsible`| `boolean`| `true`| Whether the drawer offers a collapse toggle.  
`onThreadSelect`| `(threadId: string) => void`| —| Called when a thread is selected.  
`onNewThread`| `() => void`| —| Called when a new thread is started.  
`licenseUrl`| `string`| —| Where the locked state sends a developer without Intelligence.  
`onLicensed`| `() => void`| —| Called when the locked state's action is taken.  
  
### Server-side rendering#

The drawer wraps a custom element, which needs a DOM. `@copilotkit/vue` imports that element lazily on mount, so importing the component is safe under Nuxt and other SSR setups; the drawer renders on the client.

## Build your own thread UI#

`useThreads` exposes the same data and actions headlessly when you want your own interface:
    
    
    <script setup lang="ts">
    import { useThreads } from "@copilotkit/vue";
    
    const { threads, isLoading } = useThreads({ agentId: "support" });
    </script>
    
    <template>
      <ul v-if="!isLoading">
        <li v-for="thread in threads" :key="thread.id">{{ thread.name ?? "Untitled conversation" }}</li>
      </ul>
    </template>

### On this page

Resume a specific threadAdd the threads drawerOptionsServer-side renderingBuild your own thread UI
