---
url: https://docs.copilotkit.ai/strands/prebuilt-components/chat-controls/
title: Open, close, and feedback
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:31:44.691562+00:00
---

# Open, close, and feedback

> Source: https://docs.copilotkit.ai/strands/prebuilt-components/chat-controls/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Prebuilt Components

[CopilotChat](https://docs.copilotkit.ai/strands/prebuilt-components/chat)[CopilotSidebar](https://docs.copilotkit.ai/strands/prebuilt-components/sidebar)[CopilotPopup](https://docs.copilotkit.ai/strands/prebuilt-components/popup)[Open, close, and feedback](https://docs.copilotkit.ai/strands/prebuilt-components/chat-controls)

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/strands/multimodal-attachments)[Voice](https://docs.copilotkit.ai/strands/voice)[Reasoning](https://docs.copilotkit.ai/strands/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Open, close, and feedback

BasicsChatPrebuilt Components

# Open, close, and feedback

Open and close the prebuilt chat from your UI, and capture assistant message feedback.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Two common controls for the prebuilt chat are opening it from your own UI and capturing thumbs-up / thumbs-down feedback on assistant messages.

## Control the open state from your own UI#

Pass `open` and `onOpenChange` to `<CopilotSidebar>` or `<CopilotPopup>` to own the open state yourself. This is the controlled pattern: the surface renders whatever `open` says, and every request to open or close (the toggle button, click-outside on the popup) arrives on `onOpenChange` instead of moving the surface directly.
    
    
    import { useState } from "react";
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    
    function Layout() {
      const [chatOpen, setChatOpen] = useState(false);
    
      return (
        <>
          <nav>
            <button onClick={() => setChatOpen(true)}>Ask the assistant</button>
          </nav>
    
          <CopilotSidebar open={chatOpen} onOpenChange={setChatOpen} />
        </>
      );
    }

The button lives outside the sidebar, which is the point: nothing has to be rendered inside the chat subtree to open or close it. Because `open` is the source of truth, you can also keep the chat in sync with a route, a keyboard shortcut, or any other state you already have.

`onOpenChange` reports a request, not a change. If you do not feed the new value back into `open`, the surface stays where it is. That is what makes it possible to gate opening the chat, for example behind a sign-in check. You can also pass `onOpenChange` on its own, without `open`: the surface keeps managing itself and you are notified each time it opens or closes.

## Programmatically open or close the chat#

If you would rather not lift the state into your own component, the open state for `<CopilotPopup>` and `<CopilotSidebar>` also lives in the **chat configuration context**. Read it with `useCopilotChatConfiguration()` and call `setModalOpen(true | false)` from anywhere inside the provider:
    
    
    import { useCopilotChatConfiguration } from "@copilotkit/react-core/v2";
    
    function OpenChatButton() {
      const config = useCopilotChatConfiguration();
    
      // setModalOpen is only present when a provider in the tree owns modal state
      // (the prebuilt CopilotPopup / CopilotSidebar create it for you).
      if (!config?.setModalOpen) return null;
    
      return (
        <button onClick={() => config.setModalOpen(true)}>
          Ask the assistant
        </button>
      );
    }

To toggle, read `config.isModalOpen` and flip it:
    
    
    <button onClick={() => config.setModalOpen(!config.isModalOpen)}>
      {config.isModalOpen ? "Close chat" : "Open chat"}
    </button>

`setModalOpen` / `isModalOpen` are only defined when a provider in the tree owns modal state. The prebuilt `<CopilotPopup>` and `<CopilotSidebar>` create it automatically. If you compose chat yourself, wrap the relevant subtree in `<CopilotChatConfigurationProvider isModalDefaultOpen={false}>` so the modal state exists. See the [`useCopilotChatConfiguration` reference](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration#modal-state-management).

You can also set the **initial** open state declaratively, and then let the surface manage itself. The prebuilt surfaces accept a `defaultOpen` prop:
    
    
    <CopilotSidebar defaultOpen={false} />

`defaultOpen` and `open` are the usual uncontrolled/controlled pair: use `defaultOpen` for a starting point, and `open` when your own state decides. When both are passed, `open` wins.

## Capture message feedback (thumbs up / down)#

The assistant-message toolbar can show thumbs-up and thumbs-down buttons. In v2 you opt in by passing `onThumbsUp` / `onThumbsDown` to the **assistant message slot**. The buttons only render when a handler is provided:
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          onThumbsUp: (message) => {
            analytics.track("feedback", { messageId: message.id, value: "up" });
          },
          onThumbsDown: (message) => {
            analytics.track("feedback", { messageId: message.id, value: "down" });
          },
        },
      }}
    />;

Each handler receives the assistant `message`, so you can record the feedback against the specific response (`message.id`). The same `messageView` slot works on `<CopilotPopup>` and `<CopilotSidebar>` since they wrap `<CopilotChat>`.

When the slot is rendered through `CopilotChatMessageView`, a live assistant message created by a direct AG-UI `TEXT_MESSAGE_START` can also include that event's opaque `rawEvent` value. The join happens when the thumbs callback runs; canonical messages and future run input stay unchanged. Chunk, snapshot, persisted, legacy, and direct `CopilotChatAssistantMessage` paths don't provide this callback metadata.

The button labels come from the chat labels (`assistantMessageToolbarThumbsUpLabel` defaults to `"Good response"`, `assistantMessageToolbarThumbsDownLabel` to `"Bad response"`); override them via [chat labels](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration#copilotchatlabels).

Building a fully custom message component instead of using the slot? The underlying [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage) exposes the same `onThumbsUp` / `onThumbsDown` props directly, but callback metadata enrichment is owned by `CopilotChatMessageView`.

## Related#

  * [CopilotPopup](https://docs.copilotkit.ai/strands/prebuilt-components/popup) and [CopilotSidebar](https://docs.copilotkit.ai/strands/prebuilt-components/sidebar): the prebuilt surfaces that own modal state.
  * [`useCopilotChatConfiguration` reference](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration): full context shape, modal state, and labels.
  * [Slots](https://docs.copilotkit.ai/strands/custom-look-and-feel/slots): the `messageView` / `assistantMessage` slot system used above.
  * [Programmatic Control](https://docs.copilotkit.ai/strands/programmatic-control): driving agent runs from code without a chat UI.



### On this page

Control the open state from your own UIProgrammatically open or close the chatCapture message feedback (thumbs up / down)Related
