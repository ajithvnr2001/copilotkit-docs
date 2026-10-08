---
url: https://docs.copilotkit.ai/reference/components/CopilotThreadsDrawer/
title: CopilotThreadsDrawer
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:30.449072+00:00
---

# CopilotThreadsDrawer

> Source: https://docs.copilotkit.ai/reference/components/CopilotThreadsDrawer/

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

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Components

# CopilotThreadsDrawer

Prebuilt threads drawer that lists, switches, and manages conversations next to CopilotChat

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotThreadsDrawer` is a prebuilt thread switcher. Dropped in next to [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat), it lists the user's conversations and lets them switch, start, archive, and delete threads — with **no active-thread state to wire up**. (Thread rename is available headlessly via [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads), not through the drawer's row menu.) It is a thin React wrapper around the framework-agnostic `<copilotkit-threads-drawer>` shadow-DOM web component, fed by the [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads) hook and the surrounding chat configuration.

When `onThreadSelect` / `onNewThread` are omitted, the drawer drives the surrounding chat configuration directly: selecting a row connects the chat to that thread (and replays its history); the "New Conversation" row resets the chat to a fresh welcome screen. Pass the callbacks only to take control of the active thread yourself.

Pair it with the v2 `CopilotChat` or `CopilotSidebar` from `@copilotkit/react-core/v2`. `@copilotkit/react-ui` exports components with those same two names, and those are the [deprecated v1 components](https://docs.copilotkit.ai/migrate/v2).

See the [CopilotThreadsDrawer guide](https://docs.copilotkit.ai/prebuilt-components/copilot-threads-drawer) for a walkthrough, and [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads) for the headless data layer underneath.

## Import
    
    
    import { CopilotThreadsDrawer } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## Props

Prop

Type

`agentId?`string

Prop

Type

`onThreadSelect?`(threadId: string) => void

Prop

Type

`onNewThread?`() => void

Prop

Type

`renderRow?`(thread: Thread) => React.ReactNode

Prop

Type

`label?`string

Prop

Type

`recentLabel?`string

Prop

Type

`limit?`number

Prop

Type

`collapsible?`boolean

Prop

Type

`onCollapseChange?`(collapsed: boolean) => void

Prop

Type

`data-testid?`string

## Customization

The drawer renders inside a shadow root and ships its own self-contained, theme-inheriting styles, so it looks correct in any host (including dark mode) with zero config. Three bounded escape hatches pierce the boundary.

### Slots

Project light-DOM children with a `slot` attribute to replace a region:

Slot| Replaces  
---|---  
`header`| The drawer header region (renders only when you project content).  
`empty`| The empty-state body shown when there are no threads.  
`footer`| A footer region (hidden until you project content).  
`memories`| A reserved region for a future memories surface.  
`launcher-icon`| The icon inside the floating mobile launcher.  
`row:{id}`| Per-row content — prefer the `renderRow` prop, which manages this.  
      
    
    <CopilotThreadsDrawer>
      <span slot="header">My conversations</span>
    </CopilotThreadsDrawer>

### CSS parts

Style structural elements with `::part()`:

  * **Structure** — `root`, `header`, `list`, `footer`
  * **Rows** — `row`, `row-active` (the selected row), `row-name`, `row-menu` (kebab), `row-menu-popover`, `row-archive`, `row-unarchive`, `row-delete`
  * **New conversation & sections** — `new-thread-button`, `section-heading`
  * **Filter** — `filter-toggle`, `filter-indicator`, `filter-active`, `filter-all`, `filters`
  * **Collapse, mobile & launcher** — `collapse-toggle` (desktop), `close-toggle` (mobile), `backdrop` (mobile scrim), `launcher`, `launcher-cluster`, `launcher-new-thread`
  * **Pagination** — `load-more`, `fetching-more`, `fetch-more-error`, `fetch-more-retry`
  * **States & upsell** — `loading`, `empty`, `error`, `retry-button`, `licensed`, `licensed-cta`, `memories`
  * **Delete confirm dialog** — `confirm-dialog`, `confirm-cancel`, `confirm-delete`



The Active/All filter lives behind the `filter-toggle` funnel, whose `filter-indicator` dot shows when a non-default filter is applied. Per-row Archive/Delete actions live in the `row-menu` kebab and its `row-menu-popover`. When the list is collapsed on desktop (or closed on mobile), the floating `launcher-cluster` holds the `launcher` toggle and the `launcher-new-thread` button.

### CSS variable tokens

Tokens override the bundled defaults and fall back to the host theme's vars (so the drawer follows light/dark automatically): `--cpk-drawer-bg`, `--cpk-drawer-fg`, `--cpk-drawer-border`, `--cpk-drawer-surface`, `--cpk-drawer-surface-fg`, `--cpk-drawer-muted`, `--cpk-drawer-muted-fg`, `--cpk-drawer-accent`, `--cpk-drawer-accent-fg`, `--cpk-drawer-primary`, `--cpk-drawer-primary-fg`, `--cpk-drawer-danger`, `--cpk-drawer-indicator` (default `#5b94e4`, color of the filter-applied dot), `--cpk-drawer-ring`, `--cpk-drawer-radius`, `--cpk-drawer-width`, `--cpk-drawer-font-family`, `--cpk-drawer-font-size`, `--cpk-drawer-line-height`, `--cpk-drawer-launcher-top`, `--cpk-drawer-launcher-left`.

## Usage

### Basic usage

Wrap the drawer and `CopilotChat` in a shared `CopilotChatConfigurationProvider` so they operate on the **same** chat configuration — that shared config is how selecting a thread (or "New Conversation") drives the chat. Without a shared provider the drawer sits beside the chat's own scoped configuration and can't switch its thread.
    
    
    import {
      CopilotThreadsDrawer,
      CopilotChat,
      CopilotChatConfigurationProvider,
    } from "@copilotkit/react-core/v2";
    
    function App() {
      return (
        <CopilotChatConfigurationProvider>
          <div style={{ display: "flex", height: "100%" }}>
            <CopilotThreadsDrawer />
            <CopilotChat />
          </div>
        </CopilotChatConfigurationProvider>
      );
    }

### Custom row content + label
    
    
    function App() {
      return (
        <CopilotThreadsDrawer
          label="History"
          renderRow={(thread) => <em>{thread.name ?? "New conversation"}</em>}
        />
      );
    }

## Behavior

  * **Self-connecting** : without `onThreadSelect`/`onNewThread`, the drawer drives the chat configuration — select connects + replays; the "New Conversation" row shows the welcome screen.
  * **Collapsible sidebar** : on larger screens the drawer is an expanded sidebar by default with a collapse toggle (sidebar glyph) in the header. Collapsing replaces the panel with a small floating cluster — a sidebar toggle to expand plus a "New Conversation" button — and (via `--cpk-drawer-reserved-width`) lets a host grid reclaim the column. Set `collapsible={false}` to omit the toggle. "New Conversation" is its own row below the header; project `slot="header"` content to add your own chrome beside the toggle.
  * **Row actions** : per-row **Archive/Delete** live behind a per-row kebab (⋮) menu (`row-menu`), not always-visible inline buttons; delete still asks for confirmation.
  * **Optimistic mutations** : archive/unarchive/rename/delete are optimistic in the core thread store; delete rolls back if the server rejects.
  * **Deleting the active thread** resets to a fresh thread; **archiving** the active thread keeps you viewing it. Archived threads render italic/muted inline in the "All" view.
  * **Filter** : an Active/All filter lives behind a **funnel** icon popover under the "Recent Conversations" heading; a small indicator dot appears on the funnel when a non-default filter is applied. Toggling the filter refetches server-side.
  * **Mobile** : below 768px the drawer is an off-canvas modal. Closed, it shows the same floating cluster (a launcher to open it + a "New Conversation" button); open, it slides in and is dismissed by tapping the backdrop or pressing Escape. The launcher icon (`launcher-icon` slot) and position (`--cpk-drawer-launcher-*`) are customizable.
  * **Intelligence access** : threads require CopilotKit Intelligence. If the runtime reports that Threads are unavailable, the drawer shows a locked view in place of the list. Cloud-hosted projects use `CPK_INTELLIGENCE_API_KEY` on the server. A licensed self-hosted deployment uses `COPILOTKIT_LICENSE_TOKEN` on the server.



## Related

  * [CopilotThreadsDrawer guide](https://docs.copilotkit.ai/prebuilt-components/copilot-threads-drawer) — walkthrough and setup
  * [`useThreads`](https://docs.copilotkit.ai/reference/hooks/useThreads) — the headless thread data + mutations
  * [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) — the chat the drawer connects to


