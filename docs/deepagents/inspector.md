---
url: https://docs.copilotkit.ai/deepagents/inspector/
title: Inspector
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:18.943543+00:00
---

# Inspector

> Source: https://docs.copilotkit.ai/deepagents/inspector/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

[Inspector](https://docs.copilotkit.ai/deepagents/inspector)

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Inspector

BackendDebugging

# Inspector

Verify your setup, debug agent runs, reproduce issues, and review AG-UI streams and Automatic Learning.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The CopilotKit Inspector is a debugging overlay for the live connection between your frontend and agents. Use it while developing to follow a run from the application UI through the AG-UI event stream, tools, state, and saved Threads.

Reach for Inspector after a [quickstart](https://docs.copilotkit.ai/deepagents/quickstart) to verify that the pieces are connected, while adding tools or shared state, or when you need to reproduce an issue from a real conversation. Inspector shows what the browser received; [Runtime Debug Mode](https://docs.copilotkit.ai/deepagents/troubleshooting/debug-mode) adds the server-side view, and [Error Debugging & Observability](https://docs.copilotkit.ai/deepagents/troubleshooting/error-debugging) covers production error reporting.

## Choose what you need to do#

Your goal| Start here  
---|---  
Confirm that CopilotKit is connected| **Home** , then **Agent**  
Find out why a run or tool failed| The red launcher or error pill  
Inspect one `CopilotChat` response| **View in Inspector** on the message  
Follow messages, events, tools, state, context| **Agent** and the **Inspect** panes  
Reproduce a saved conversation safely| **Rich Threads** → **Try from here**  
Continue a saved Thread in your application| **Rich Threads** → **View in your app**  
Enable or repair Intelligence| **Home** or a locked **Rich Threads**  
Review what Learning found| **Automatic Learning**  
Move or hide the overlay| The Inspector header and settings  
  
## Show Inspector and confirm your setup#

Inspector appears by default in development builds of React, Vue, and Angular browser applications. Open your application and click the Inspector button in the corner. The first open lands on **Home** ; later opens return to the last pane you used.

Confirm the connection before debugging anything else:

  1. Open **Agent**. Your connected agent should be listed.
  2. Send a message in your application, then open **AG-UI Events**. You should see events arrive while the run is active.
  3. Open **Rich Threads**. A connected Intelligence setup shows your saved Threads. Without Intelligence, the pane is locked and offers a setup path instead.



Home summarizes project, Runtime, and service status. When Intelligence is connected, it shows an **Intelligence connected** chip. Otherwise, choose **Copy setup prompt** to give the setup task to your coding agent. If the Runtime supplies a trusted setup URL, you can also choose **Set it up yourself**.

If the agent is missing or no events arrive, first confirm the [Copilot Runtime](https://docs.copilotkit.ai/deepagents/backend/copilot-runtime) connection. If Threads is the only missing piece, follow the [Intelligence quickstart](https://docs.copilotkit.ai/deepagents/intelligence/quickstart) instead of changing the agent connection.

## Find the cause of a failed run#

When CopilotKit reports an error, the Inspector launcher turns red. When there is room, an error pill briefly names the failure. Click either one to open the pane with the most useful evidence:

Failure| Where Inspector takes you| What to check  
---|---|---  
Runtime or connection| **Home**|  Runtime and service status  
Loading the Thread list| **Rich Threads**|  The list error and Intelligence state  
Agent run or `RUN_ERROR`| **AG-UI Events**|  The highlighted event, agent name, and error  
Tool handler or missing tool| **Agent**|  The agent, tool, call, and error  
Loading Learning data| **Automatic Learning**|  The pane error and setup state  
  
A `RUN_ERROR` is highlighted and expanded while it remains in the event buffer. A tool call is highlighted when the error includes its call id; a missing tool has no call to highlight.

Learning data is fetched the first time you open **Automatic Learning** , so a Learning load error can only be routed there after that first visit.

Inspector is best for locating the failing layer during development. If the event stream stops before it reaches the browser, enable [Runtime Debug Mode](https://docs.copilotkit.ai/deepagents/troubleshooting/debug-mode) to inspect the server-side pipeline. Use `onError` on `CopilotKit` or `CopilotChat` when the application UI or your production observability system should also receive the error. See [Error Debugging & Observability](https://docs.copilotkit.ai/deepagents/troubleshooting/error-debugging) for that setup.

## What's New#

What's New lists updates that match your stable frontend SDK version and confirmed runtime configuration. A single preview beside the launcher highlights an update. Read it or close its preview to quiet the updates already available to you. They remain in What's New for later reading. Reading a different update does not dismiss the highlight.

New updates can show a preview later. Copy edits to an update you already read stay quiet. The Inspector shares recent read and dismissed updates across ports on the current host. It keeps the selected update and full history in storage for each origin. Updates load once per page and do not poll. If cookies are blocked, read and dismissed updates stay on the current origin. Production, server rendering, and disabled Inspectors do not fetch notifications.

React, Vue, and Angular set the notification context when they mount Inspector. If you mount `<cpk-web-inspector>` yourself, set its `notificationContext` property before connecting it to the page. Include `development: true`, your `framework`, and the version of that frontend SDK package as `sdkVersion`. Without that context, the element leaves notifications off.

The cohort-capable Inspector reads only the versioned notification feed. Older SDK releases continue reading the separate legacy `announcements.json` feed. A legacy announcement reaches those older clients without cohort targeting; it is not a fallback for the updated Inspector when the cohort feed is empty or unavailable.

## Follow a run from input to result#

Send a message in your application, then use these views to answer the next debugging question:

Question| Open| Related guide  
---|---|---  
Which agent ran, and what did it do?| **Agent**| [Agent configuration](https://docs.copilotkit.ai/deepagents/agent-config)  
Which events crossed the AG-UI connection?| **AG-UI Events**| [AG-UI protocol](https://docs.copilotkit.ai/deepagents/agentic-protocols/ag-ui)  
Which browser-side tools are registered?| **Frontend Tools**| [Frontend Tools](https://docs.copilotkit.ai/deepagents/frontend-tools)  
What readable or document context was shared?| **Context**| [Agent read-only context](https://docs.copilotkit.ai/deepagents/shared-state/agent-readonly)  
What did a saved conversation contain?| **Rich Threads** → **Conversation** , **AG-UI Events** , or **State**| [AG-UI Streams](https://docs.copilotkit.ai/deepagents/threads) and [Shared State](https://docs.copilotkit.ai/deepagents/shared-state)  
  
In an official React `CopilotChat`, open an assistant message's toolbar and choose **View in Inspector** to jump directly to that message in its Thread. This local development shortcut is useful when you already know which response you need to explain. See the [`CopilotChat` reference](https://docs.copilotkit.ai/reference/components/CopilotChat) for its configuration.

**Conversation** shows messages, expandable tool calls, and Generative UI component names. Generated interfaces render in your application, not inside Inspector. Choose **Show event timeline** for run markers and state changes, or **AG-UI Events** for raw events. **Hide thread list** gives the conversation more room; the title and conversation actions stay visible while scrolling.

**Frontend Tools** appears only after your application registers a frontend tool. **Capabilities** appears only when an A2UI catalog is present; use it to toggle tools and catalog components while experimenting.

On narrow windows, or when Inspector is docked left, the sidebar collapses to icons. **Talk to an Engineer** remains in the sidebar footer.

## Reproduce an issue without changing the saved Thread#

Use **Playground** when you have already observed a problem and want to vary the prompt, state, or next message without touching the original [Rich Thread](https://docs.copilotkit.ai/deepagents/threads). Its messages and state stay separate from your application chat and stored Threads, so you can run, stop, retry, and continue an experiment safely.

To reproduce a problem from a real conversation:

  1. Open **Rich Threads** and select the saved Thread.
  2. Choose **Try from here**.
  3. Continue the copied conversation in **Playground**.



Inspector copies the Thread's messages and state but leaves the original untouched. If the copy fails, neither the saved Thread nor the existing Playground session changes.

When Threads has no real rows, or when it is locked, Inspector shows an overview video, three local example Threads, their detail tabs, and a guided tour. These examples do not send real Thread requests. With reduced motion enabled, the video starts paused. If the video fails, the examples and tour still work.

## Continue a saved Thread in your application#

Selecting a Thread in Inspector does not change the live chat. To continue the conversation in an official `CopilotChat`, sidebar, or popup:

  1. Open a real saved Thread.
  2. Choose **View in your app** in its detail header.
  3. Send messages in the application chat on that Thread.
  4. Choose **Stop viewing** to restore the previous application Thread.



The Thread list marks the conversation currently open in the application. If you select another Thread in the application, the Inspector override ends. Example Threads do not offer this action.

If no official chat for the agent is present, Inspector shows an error. The action addresses the chat by `agentId`, regardless of the backend framework.

A custom chat can use the bridge exported by `@copilotkit/core`. Return `true` from `onInspectorViewThread` only when the chat accepts the request, and include the same `requestId` in every lifecycle event:

  * `onInspectorViewThread` receives `{ requestId, threadId, agentId }`
  * `onInspectorStopViewing` receives `{ requestId, agentId }`
  * `emitInspectorActiveThread` sends `{ requestId, threadId, agentId, source }`
  * `emitInspectorViewThreadResult` sends `{ requestId, threadId, agentId, ok }`



If you are building the Thread picker and conversation surface yourself, see [Headless Threads](https://docs.copilotkit.ai/deepagents/headless-threads) for the persistence and lifecycle APIs.

## Enable or repair Intelligence#

Intelligence unlocks real Threads and Learning. When it is not connected, open **Home** and choose **Copy setup prompt**. Give that prompt to your coding agent, then return to Inspector to follow setup through the first eligible Thread. The [Intelligence quickstart](https://docs.copilotkit.ai/deepagents/intelligence/quickstart) explains the project, credentials, and Runtime routes that prompt configures.

If Threads remains locked, Inspector shows one Rich Threads setup view with **Copy setup prompt** and **Talk to an Engineer**. The view is based on Runtime Threads capability rather than license metadata. To configure incomplete routes, use the Runtime route guide. [Enable AG-UI Streams routes](https://docs.copilotkit.ai/deepagents/backend/runtime-endpoints#enable-rich-threads-routes) explains how to configure application-user identity, mount every required HTTP method, and verify the capability response.

## Review what Learning found#

Open **Automatic Learning** to trace completed Threads into evidence-backed Insights and reviewed Skills. A configured pane shows:

  * new Threads ready for analysis;
  * published Skills and their `SKILL.md` content;
  * the Insights supporting each Skill; and
  * the source Thread evidence behind each pattern.



Select evidence to open the matching Thread and message. Use **Open Intelligence** in the results header to open the Intelligence app in a new tab. The analysis and Skill-review links open the selected Learning Space in Intelligence. Inspector lets you inspect the evidence, but does not approve or publish a candidate.

If Learning is not configured, choose **Copy setup prompt**. If the Runtime cannot select one Learning Space for the active agent, Inspector sends you to the web app to choose it. See [Automatic Learning](https://docs.copilotkit.ai/deepagents/learning) for the complete workflow.

## Control when Inspector appears#

Use the option that matches what you are trying to do:

Goal| Action  
---|---  
Close the current view| Use the close control; reopen it from the Inspector button  
See your application without an overlay| Use the pop-out control in the Inspector header  
Hide chat message shortcuts until reload| Open a message's Inspector shortcut menu and choose **Hide this icon**  
Hide Inspector temporarily on this domain| Choose **Hide Inspector for a day** from the launcher HUD, or **Hide Inspector for one week** in settings  
Hide Inspector indefinitely on this domain| Choose **Always hide Inspector** in settings; see below to bring it back  
Disable Inspector for the development app| Set `enableInspector` to `false`  
  
Pop-out opens the same live Inspector session in a separate browser window and hides the overlay and floating button on the application page. Close the extra window to return Inspector to its previous floating or docked position. If no window opens, allow popups and try again. Refreshing closes the extra window; Inspector does not restore pop-out mode after a refresh.

A temporary hide removes the overlay and launcher only on the current domain. They return automatically after the selected period.

**Always hide Inspector** keeps the overlay and launcher hidden on the current domain until you bring them back. To restore Inspector, run this in the browser console on the page where you hid it, then reload:
    
    
    document.cookie = "cpk_inspector_dismissed_until=; Path=/; Max-Age=0";
    localStorage.removeItem("cpk:inspector:dismissed_until");

To disable Inspector in a React development build:
    
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      enableInspector={false}
    >
      {children}
    </CopilotKit>

For cloud-hosted Intelligence, keep `CPK_INTELLIGENCE_API_KEY` on the runtime server. The runtime reports Intelligence access to the browser. Do not expose the project API key in a `NEXT_PUBLIC_` environment variable.

Vue uses the template prop `:enable-inspector="false"`. Angular uses `provideCopilotKit({ enableInspector: false })`. An explicit `true` keeps Inspector enabled in development but cannot override production or server-rendering guards. Legacy `showDevConsole` props no longer control it.

See the [`CopilotKit` provider reference](https://docs.copilotkit.ai/reference/components/CopilotKit) for the complete React provider API.

Inspector is never loaded or rendered in a production build or during server-side rendering.

## Understand project and usage information#

An Intelligence-backed Runtime can send trusted organization, project, plan, Thread usage, retention, and action metadata. Home shows valid project context; the Threads footer shows valid usage and relevant actions. Missing identity data does not hide valid usage, and missing usage does not hide a valid action.

Inspector opens only action URLs supplied by the Runtime. It never constructs a project URL or uses a fixed signup fallback. If metadata and Runtime license states conflict, Runtime status wins and Inspector hides the incompatible action.

Usage state| What Inspector shows  
---|---  
Finite limit| `used / limit Threads` and a progress bar  
Over the finite limit| `limit+ / limit Threads`, with the bar capped at 100%  
Unlimited| The used count and **Unlimited** , without a progress bar  
Unknown limit| The used count and **Limit unavailable**  
Known expiry count| The count, including `0 Expiring Soon`  
Missing or malformed expiry| No expiry value  
  
**Expiring Soon** means a Thread is within a retention threshold in the next 24 hours. It does not mean Inspector locked or deleted that Thread.

Older Runtime, Core, and Inspector versions remain compatible without a synchronized deployment. Newer components feature-detect optional metadata; older components ignore fields they do not understand. Explicit `threadEndpoints` remain authoritative, and metadata never enables Thread work.

## Where Inspector runs#

Inspector is a browser overlay: it mounts a custom element into the page's DOM. It runs on React, Next.js, React SPA, Vue, and Angular.

There is no React Native build of Inspector, and `@copilotkit/react-native` does not ship it. Channels such as Slack and Teams do not have a browser surface either.

Use these alternatives for React Native:

What you need to debug| Use  
---|---  
Whether the Runtime answers| `npx copilotkit verify --round-trip`. See [Proving it works](https://docs.copilotkit.ai/deepagents/react-native#proving-it-works).  
Errors and tool calls| Runtime [Debug Mode](https://docs.copilotkit.ai/deepagents/troubleshooting/debug-mode) beside the device log, such as `adb logcat` on Android  
Saved Threads| The Thread view in [CopilotKit Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)  
  
Inspector telemetry has its own browser identity and direct delivery path. It works whether or not the Runtime has `CPK_TELEMETRY_ID` and follows the existing telemetry opt-outs.

Want to preview A2UI catalog components directly in your editor? See the [VS Code Extension](https://docs.copilotkit.ai/deepagents/vs-code-extension) for live preview with hot reload.

### On this page

Choose what you need to doShow Inspector and confirm your setupFind the cause of a failed runWhat's NewFollow a run from input to resultReproduce an issue without changing the saved ThreadContinue a saved Thread in your applicationEnable or repair IntelligenceReview what Learning foundControl when Inspector appearsUnderstand project and usage informationWhere Inspector runs
