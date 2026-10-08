---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useThreads/
title: useThreads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:54.100194+00:00
---

# useThreads

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useThreads/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Hooks

# useThreads

React hook for listing, managing, and syncing conversation threads with useThreads. Rename, archive, delete, and paginate threads with realtime updates via WebSocket.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useThreads` is a React hook for managing conversation threads in CopilotKit Intelligence. It fetches the thread list for a given agent, keeps it synchronized in realtime via WebSocket, and exposes mutation methods for renaming, archiving, and deleting threads.

Thread persistence runs in CopilotKit Intelligence, which is accessed with a `publicLicenseKey`. That key is **not yet supported on React Native** (see [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)), so `useThreads` is documented here for API parity but is not yet usable on React Native.

Re-exported from `@copilotkit/react-core/v2`, identical to the [React (V2) `useThreads`](https://docs.copilotkit.ai/reference/v2/hooks/useThreads). The only difference is the import path.

Threads are sorted by most recently updated first. The hook supports cursor-based pagination when a `limit` is provided.

## Signature
    
    
    import { useThreads } from "@copilotkit/react-native";
    
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
    
    
    import { useThreads } from "@copilotkit/react-native"; 
    import { FlatList, Text, TouchableOpacity, View } from "react-native";
    
    function ThreadList() {
      const {
        threads,
        isLoading,
        renameThread,
        archiveThread,
        deleteThread,
      } = useThreads({ agentId: "my-agent" }); 
    
      if (isLoading) {
        return (
          <View>
            <Text>Loading threads...</Text>
          </View>
        );
      }
    
      return (
        <FlatList
          data={threads}
          keyExtractor={(thread) => thread.id}
          renderItem={({ item: thread }) => (
            <View>
              <Text>{thread.name ?? "Untitled"}</Text>
              <TouchableOpacity onPress={() => renameThread(thread.id, "New name")}>
                <Text>Rename</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => archiveThread(thread.id)}>
                <Text>Archive</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => deleteThread(thread.id)}>
                <Text>Delete</Text>
              </TouchableOpacity>
            </View>
          )}
        />
      );
    }

## Behavior

  * On mount, fetches the thread list and establishes a realtime WebSocket subscription.
  * Thread creates, renames, archives, and deletes from any client are reflected immediately without polling.
  * All mutation methods use **pessimistic updates** : the UI updates only after the server confirms the operation via WebSocket, not immediately on dispatch. Promises resolve on confirmation (15-second timeout) and reject on failure.
  * The `error` state updates with the most recent error from any operation.
  * The `threads` array stays sorted by `updatedAt` descending (most recent first).
  * New threads are **automatically named** by the LLM after their first run (a short title of 2 to 5 words). This is configurable via `generateThreadNames` on the runtime.



## Next steps

  * **Thread architecture:** [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/intelligence/threads-explained) covers the event replay model and WebSocket sync
  * **Step-by-step guide:** [Headless Threads](https://docs.copilotkit.ai/headless-threads) walks you through building a custom thread-management UI
  * **React (V2) reference:** [`useThreads`](https://docs.copilotkit.ai/reference/v2/hooks/useThreads), the web `useThreads` this hook mirrors


