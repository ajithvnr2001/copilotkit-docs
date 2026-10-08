---
url: https://docs.copilotkit.ai/reference/angular/functions/injectThreads/
title: injectThreads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:59.207821+00:00
---

# injectThreads

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectThreads/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁AngularSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Guides

[Public API inventory](https://docs.copilotkit.ai/reference/angular/public-api)[Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle)

Components

[CopilotActivity](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity)[CopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)[CopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)

Functions

[connectAgentContext](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)[injectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)[injectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)[injectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)[injectCopilotKitConfig](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)[injectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)[injectThreads](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)[provideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)[provideCopilotKit](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)[provideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)[registerComponent](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)[registerFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)[registerHumanInTheLoop](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)[registerRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)[registerRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)

Services

[CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)

Directives

[CopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Functions

# injectThreads

Angular function for listing and managing CopilotKit Intelligence threads with signals, pagination, realtime updates, and injector-scoped cleanup.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`injectThreads` returns the thread list and mutations for one agent as Angular signals and stable callbacks. It fetches the runtime-authenticated user's threads from CopilotKit Intelligence, keeps metadata current through realtime updates when available, and sorts the list by most recent agent activity.

Call it from an Angular injection context such as a component field initializer or constructor. The list subscription, realtime connection, and core store registration are removed automatically when the owning injector is destroyed.

## Signature
    
    
    import { injectThreads } from "@copilotkit/angular";
    
    function injectThreads(input: InjectThreadsInput): InjectThreadsResult;

## Input

Prop

Type

`agentId`string | Signal<string>

Prop

Type

`includeArchived?`boolean | Signal<boolean | undefined>

Prop

Type

`limit?`number | Signal<number | undefined>

Prop

Type

`enabled?`boolean | Signal<boolean | undefined>

## Return value

The returned `InjectThreadsResult` contains:

Member| Type| Purpose  
---|---|---  
`threads`| `Signal<Thread[]>`| Server-authoritative list, sorted by most recent agent activity  
`isLoading`| `Signal<boolean>`| Initial-list loading state  
`listError`| `Signal<Error | null>`| User-safe list or mutation error  
`error`| `Signal<Error | null>`| Most recent error, including developer configuration errors  
`fetchMoreError`| `Signal<Error | null>`| Error from the most recent next-page request  
`hasMoreThreads`| `Signal<boolean>`| Whether another page is available  
`isFetchingMoreThreads`| `Signal<boolean>`| Whether the next page is loading  
`isMutating`| `Signal<boolean>`| Whether a rename, archive, restore, or delete is in flight  
`fetchMoreThreads()`| `() => void`| Fetch the next page when one exists  
`refetchThreads()`| `() => void`| Refresh without clearing the visible list  
`startNewThread()`| `() => void`| Reset to a fresh client-side thread; persistence starts with its first run  
`renameThread(id, name)`| `Promise<void>`| Rename a thread  
`archiveThread(id)`| `Promise<void>`| Hide a thread through a reversible archive  
`unarchiveThread(id)`| `Promise<void>`| Restore an archived thread  
`deleteThread(id)`| `Promise<void>`| Permanently delete a thread  
  
Each `Thread` has `id`, `agentId`, `name`, `archived`, `createdAt`, `updatedAt`, and an optional `lastRunAt`. Prefer `lastRunAt` for user-facing activity timestamps because metadata-only changes can update `updatedAt`.

## Usage

src/app/thread-list.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { injectThreads } from "@copilotkit/angular";
    
    @Component({
      selector: "app-thread-list",
      standalone: true,
      template: `
        <button type="button" (click)="threads.startNewThread()">
          New conversation
        </button>
    
        @if (threads.isLoading()) {
          <p>Loading conversations…</p>
        } @else {
          @for (thread of threads.threads(); track thread.id) {
            <button type="button" (click)="selectedThreadId.set(thread.id)">
              {{ thread.name ?? "Untitled conversation" }}
            </button>
          }
        }
    
        @if (threads.listError()) {
          <p>Conversations could not be loaded.</p>
          <button type="button" (click)="threads.refetchThreads()">Retry</button>
        }
    
        @if (threads.hasMoreThreads()) {
          <button
            type="button"
            [disabled]="threads.isFetchingMoreThreads()"
            (click)="threads.fetchMoreThreads()"
          >
            Load more
          </button>
        }
      `,
    })
    export class ThreadListComponent {
      readonly selectedThreadId = signal<string | undefined>(undefined);
      readonly threads = injectThreads({
        agentId: "support",
        limit: 20,
      });
    }

Bind the selected id to a chat component in the same feature:
    
    
    <copilot-chat agentId="support" [threadId]="selectedThreadId()" />

## Mutation behavior

Rename, archive, unarchive, and delete update the visible list optimistically and return a promise that settles when the platform confirms the operation. Handle rejection in the calling UI. Deletion is irreversible and rolls back its optimistic removal if the request fails; ask the user for confirmation before calling it.

Use `listError` for end-user messaging. The broader `error` signal can include configuration details such as a missing runtime URL or unavailable thread endpoints and is intended for developer diagnostics.

## Related

### [Angular threads and headless UI guideBuild thread selection, memory, attachments, and a custom signal-based chat.](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless)### [Threads explainedUnderstand persistence, realtime synchronization, naming, replay, and failure behavior.](https://docs.copilotkit.ai/angular/intelligence/threads-explained)### [CopilotChatConnect the selected thread to the prebuilt Angular chat.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
