---
url: https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/markdown/
title: Markdown Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:44.657390+00:00
---

# Markdown Rendering

> Source: https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/markdown/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)Custom Look and Feel

# Markdown Rendering

Restyle the markdown in assistant messages, or replace the markdown renderer entirely, via the markdownRenderer slot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Assistant replies arrive as markdown. CopilotKit renders them through the `markdownRenderer` slot on `CopilotChatAssistantMessage`, whose default is a thin wrapper around [Streamdown](https://streamdown.ai) — a markdown renderer built for text that is still streaming in.

You reach the slot by drilling down from the chat component:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          markdownRenderer: {
            /* ... */
          },
        },
      }}
    />

Everything on this page works the same way on `CopilotSidebar` and `CopilotPopup`, and on `CopilotChatMessageView` (where the path starts one level in, at `assistantMessage`).

## Restyle individual HTML tags#

This is the route to reach for first. The slot forwards its props to Streamdown, so a props override can set Streamdown's `components` map, which swaps the React component used for one HTML tag:

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export function Chat() {
      return (
        <CopilotChat
          messageView={{
            assistantMessage: {
              markdownRenderer: {
                components: {
                  a: ({ node, children, ...props }) => (
                    <a {...props} className="my-link">
                      {children}
                    </a>
                  ),
                  h2: ({ node, children, ...props }) => (
                    <h2 {...props} className="my-heading">
                      {children}
                    </h2>
                  ),
                },
              },
            },
          }}
        />
      );
    }

Three things are worth knowing about the props your component receives.

**Drop`node`.** Every component is handed a `node` prop holding the parsed syntax-tree node. It is not a DOM attribute, so spreading it onto an element writes a literal `node="[object Object]"` into the HTML. Destructure it out, as above, and it disappears.

**Spread the rest.** The remaining props come from the sanitized document, not from the raw model output. An `a` is handed `href`, `target` and `rel`, with `target="_blank" rel="noopener noreferrer"` already applied by the renderer's link hardening; an `img` is handed `src` and `alt`. Spreading them keeps that work. Rebuilding the element by hand throws it away.

**You are replacing, not extending.** The default component for a tag carries Streamdown's own classes and a `data-streamdown` attribute — a default link renders as `<a class="wrap-anywhere font-medium text-primary underline" data-streamdown="link" …>`. Your component supplies neither unless you write them, so any CSS you have targeting `[data-streamdown="link"]` stops matching that tag.

## Restyle the whole markdown block#

To change the block as a whole rather than one tag, pass a class string. It is merged onto the markdown container:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: { markdownRenderer: "text-sm leading-7" },
      }}
    />

## Replace the renderer#

Passing a component instead of an object replaces the renderer outright. It receives exactly one prop, `content`, holding the assistant message's raw markdown:

page.tsx
    
    
    const PlainText = ({ content }: { content: string }) => (
      <pre className="whitespace-pre-wrap">{content}</pre>
    );
    
    <CopilotChat
      messageView={{ assistantMessage: { markdownRenderer: PlainText } }}
    />;

Reach for this only when you want a different markdown engine. Streamdown is doing real work that you take over with it: parsing markdown that is still half-written without flashing broken output, math and syntax highlighting, and sanitizing model-generated HTML. That last one matters — `content` is raw model output, so anything you render it with has to be safe against it.

## Custom tags are not supported#

You cannot teach the renderer a tag of your own, such as `<reference-chip>`. This is deliberate, and it is enforced twice.

The type only accepts real HTML tag names, so a custom key is a compile error:
    
    
    error TS2353: Object literal may only specify known properties,
    and '"reference-chip"' does not exist in type 'Components'.

And at runtime the renderer sanitizes model output against an allowlist of standard HTML elements before any component mapping happens. An unknown tag is stripped, its text kept: `Hi <reference-chip id="42">Doc 42</reference-chip>.` renders as `<p>Hi Doc 42.</p>`, and a component registered for it is never called.

Tags that are on the allowlist do survive, and are overridable like any other — `<kbd>` and `<sup>` written directly in a reply render as real elements.

If you need a richer, non-textual surface in the conversation, that is what [generative UI](https://docs.copilotkit.ai/pydantic-ai/generative-ui/tool-rendering) is for: the agent calls a tool and you render a React component for that tool call. Do not turn off sanitization to get a custom tag through.

## Other frontends#

This page describes the React API. The other frontends expose the same idea under different names, and the Streamdown `components` map is React-only:

  * **Vue** uses a `message-renderer` scoped slot over `streamdown-vue`. See the [Vue `CopilotChatAssistantMessage` reference](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage).
  * **Angular** uses a `#markdownRenderer` `ng-template` (or `markdownRendererComponent`) over `marked`, so there is no `components` prop. See the [Angular `CopilotChatAssistantMessage` reference](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage).



## Reference#

  * [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage) — every slot on the assistant message.
  * [Slots](https://docs.copilotkit.ai/pydantic-ai/custom-look-and-feel/slots) — how slot overrides work in general.



### On this page

Restyle individual HTML tagsRestyle the whole markdown blockReplace the rendererCustom tags are not supportedOther frontendsReference
