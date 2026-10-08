---
url: https://docs.copilotkit.ai/reference/v2/hooks/useThreads/
title: useThreads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:48.947459+00:00
---

# useThreads

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useThreads/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useThreads

React hook for listing, managing, and syncing conversation threads with useThreads — rename, archive, delete, and paginate threads with realtime updates via WebSocket.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

[useThreads needs a CopilotKit Intelligence projectCreate a cloud-hosted project or connect a self-hosted deployment to start syncing threads.Create a free account](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_reference_use_threads)

## Overview

Intelligence’s [AG-UI streams](https://docs.copilotkit.ai/threads) provide the event history and delivery behind these conversations. Use `useThreads` to manage the conversation list, then pass the selected `threadId` to your chat. Your framework keeps its own conversation and model-context management.

`useThreads` is a React hook for managing conversation threads in CopilotKit Intelligence. It fetches the thread list for a given agent, keeps it synchronized in realtime via WebSocket, and exposes mutation methods for renaming, archiving, and deleting threads.

Threads are sorted by most recently updated first. The hook supports cursor-based pagination when a `limit` is provided.

`useThreads` only activates when the connected runtime advertises compatible REST thread endpoints. Cloud-hosted Intelligence provides those endpoints for thread metadata and realtime updates. Self-managed runner persistence, such as `AgentRunner`, `SqliteAgentRunner`, or a custom runner, can still persist and replay chat history, but it does not automatically provide the managed `useThreads` list/mutation/realtime contract.

## Signature
    
    
    import { useThreads } from "@copilotkit/react-core/v2";
    
    function useThreads(input: UseThreadsInput): UseThreadsResult

## Parameters

Prop

Type

`input?`UseThreadsInput

## Return Value

Prop

Type

`result?`UseThreadsResult

## Usage

ThreadList.tsx
    
    
    import { useThreads } from "@copilotkit/react-core/v2"; 
    
    function ThreadList() {
      const {
        threads,
        isLoading,
        renameThread,
        archiveThread,
        deleteThread,
      } = useThreads({ agentId: "my-agent" }); 
    
      if (isLoading) return <div>Loading threads...</div>;
    
      return (
        <ul>
          {threads.map((thread) => (
            <li key={thread.id}>
              <span>{thread.name ?? "Untitled"}</span>
              <button onClick={() => renameThread(thread.id, "New name")}>
                Rename
              </button>
              <button onClick={() => archiveThread(thread.id)}>Archive</button>
              <button onClick={() => deleteThread(thread.id)}>Delete</button>
            </li>
          ))}
        </ul>
      );
    }

## Behavior

  * On mount, fetches the thread list and establishes a realtime WebSocket subscription.
  * If the runtime does not advertise thread endpoints, no `/threads` request is made and `error` explains that thread endpoints are unavailable.
  * Thread creates, renames, archives, and deletes from any client are reflected immediately without polling.
  * All mutation methods use **pessimistic updates** — the UI updates only after the server confirms the operation via WebSocket, not immediately on dispatch. Promises resolve on confirmation (15-second timeout) and reject on failure.
  * The `error` state updates with the most recent error from any operation.
  * The `threads` array stays sorted by `updatedAt` descending (most recent first).
  * New threads are **automatically named** by the LLM after their first run (2–5 word title). This is configurable via `generateThreadNames` on the runtime.



## Next steps

  * **Thread architecture:** [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/intelligence/threads-explained) — event replay model and WebSocket sync
  * **Step-by-step guide:** [Headless Threads](https://docs.copilotkit.ai/headless-threads) — build a custom thread-management UI


