---
url: https://docs.copilotkit.ai/strands/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:31:11.856061+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/strands/custom-look-and-feel/reasoning-messages/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/strands/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/strands/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/strands/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/strands/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/strands/custom-look-and-feel/reasoning-messages)

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

Reasoning Messages

BasicsChatCustom Look and Feel

# Reasoning Messages

Customize how reasoning (thinking) tokens from models like o1, o3, and o4-mini are displayed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning_agent.py

page.tsx

suggestions.ts

route.ts
    
    
    """Reasoning agent: emits AG-UI REASONING_MESSAGE_* events.Shared by reasoning-default (CopilotKit's built-in reasoning slot) andreasoning-custom (a custom amber ReasoningBlock).Why a reasoning model plus the Responses API: the OpenAI Responses API streams`response.reasoning_summary_text.delta` items only for native reasoning models(gpt-5, o3, o4-mini and friends). The Strands bridge translates those intoAG-UI REASONING_MESSAGE_* events with `role: "reasoning"`, which the frontendrenders through the `reasoningMessage` slot. gpt-4o emits no reasoning items, sothe showcase's default chat-completions model would never light the slot up.`summary: "detailed"` rather than `"auto"` is deliberate: with `"auto"` themodel decides, and it frequently skips the summary entirely, which leaves thereasoning slot unmounted. Override the model with `OPENAI_REASONING_MODEL`.Mirrors `langgraph-python/src/agents/reasoning_agent.py`."""from __future__ import annotationsimport osfrom strands import Agentfrom ag_ui_strands import StrandsAgentSYSTEM_PROMPT = (    "You are a helpful assistant. For each user question, first think "    "step-by-step about the approach, then give a concise answer.")DEFAULT_REASONING_MODEL = "gpt-5.4"def reasoning_model_id() -> str:    """Resolve the reasoning model at call time.    Read here rather than at module scope: the agent server imports this module    before it calls `load_dotenv()`, so a module-level read would always miss an    `OPENAI_REASONING_MODEL` set in `.env`.    """    return os.environ.get("OPENAI_REASONING_MODEL", DEFAULT_REASONING_MODEL)def build_reasoning_model():    """Construct the Responses-API model that streams reasoning summaries.    `OpenAIResponsesModel` is imported here rather than at module scope so the    dependency shows up where it is used; it needs openai>=2, which the pinned    requirements provide. The agent server builds these agents at import time,    so an older install still fails the whole server, not just these demos.    """    from strands.models.openai_responses import OpenAIResponsesModel    api_key = os.getenv("OPENAI_API_KEY", "")    if not api_key:        raise RuntimeError("OPENAI_API_KEY must be set for the strands showcase agent")    return OpenAIResponsesModel(        client_args={"api_key": api_key},        model_id=reasoning_model_id(),        params={"reasoning": {"effort": "medium", "summary": "detailed"}},    )def build_reasoning_agent() -> StrandsAgent:    """Construct the tool-free StrandsAgent backing both reasoning demos."""    strands_agent = Agent(        model=build_reasoning_model(),        system_prompt=SYSTEM_PROMPT,        tools=[],    )    return StrandsAgent(        agent=strands_agent,        name="reasoning",        description="Strands agent that streams reasoning summaries alongside its answer",    )

Some models (like OpenAI's o1, o3, and o4-mini) emit **reasoning tokens** : internal "thinking" traces that show the model's chain-of-thought before it produces a final answer. CopilotKit surfaces these tokens automatically with a collapsible **Reasoning Message** card.

## Default Behavior#

When reasoning events arrive from the agent, CopilotKit renders them inside a built-in card that:

  * Shows a **"Thinking…"** label with a pulsating indicator while the model is reasoning.
  * Expands automatically so you can follow the model's thought process in real-time.
  * Collapses and switches to **"Thought for X seconds"** once reasoning finishes.
  * Renders the reasoning content as **Markdown**.
  * Includes a chevron toggle so users can re-expand and review the reasoning at any time.



No extra configuration is needed; if your model emits reasoning tokens, the card appears automatically.

The only requirement is connecting your agent to CopilotKit; no extra props or configuration needed:

page.tsx
    
    
    const AGENT_ID = "reasoning-default";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

## Customizing the Reasoning Message#

The reasoning message is composed of three sub-components that can each be replaced independently via **slot props** :

Sub-component| Slot prop| Description  
---|---|---  
`Header`| `header`| The clickable bar with the brain icon, label, and chevron  
`Content`| `contentView`| The reasoning text area (Markdown)  
`Toggle`| `toggle`| The expand/collapse animation wrapper  
  
You pass custom sub-components through the `messageView` prop on `CopilotChat`, `CopilotPopup`, or `CopilotSidebar`:
    
    
    <CopilotChat
      messageView={{
        reasoningMessage: {
          header: CustomHeader,
          contentView: CustomContent,
        },
      }}
    />

### Custom Header#

Replace the header to change the icon, label text, or styling. The header receives these props:

Prop| Type| Description  
---|---|---  
`isOpen`| `boolean`| Whether the content panel is currently expanded  
`label`| `string`| `"Thinking…"` while streaming, `"Thought for X seconds"` after  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`isStreaming`| `boolean`| Whether reasoning is actively streaming  
`onClick`| `() => void`| Toggle handler (only present when `hasContent` is `true`)  
      
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function CustomHeader({
      isOpen,
      label,
      hasContent,
      isStreaming,
      ...props
    }: React.ButtonHTMLAttributes<HTMLButtonElement> & {
      isOpen?: boolean;
      label?: string;
      hasContent?: boolean;
      isStreaming?: boolean;
    }) {
      return (
        <button
          className="flex w-full items-center gap-2 px-3 py-2 text-sm font-medium"
          {...props}
        >
          {isStreaming ? "🧠" : "💡"}
          <span>{label}</span>
          {hasContent && (
            <span className="ml-auto text-xs">{isOpen ? "Hide" : "Show"}</span>
          )}
        </button>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { header: CustomHeader },
      }}
    />

### Custom Content#

Replace the content area to change how reasoning text is displayed:

Prop| Type| Description  
---|---|---  
`isStreaming`| `boolean`| Whether reasoning tokens are still arriving  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`children`| `string`| The raw reasoning text  
      
    
    function CustomContent({
      isStreaming,
      hasContent,
      children,
      ...props
    }: React.HTMLAttributes<HTMLDivElement> & {
      isStreaming?: boolean;
      hasContent?: boolean;
    }) {
      if (!hasContent && !isStreaming) return null;
    
      return (
        <div className="px-4 pb-3 text-sm text-gray-500 font-mono" {...props}>
          {children}
          {isStreaming && <span className="animate-pulse ml-1">▊</span>}
        </div>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { contentView: CustomContent },
      }}
    />

## Fully Custom Reasoning Message#

For complete control over the entire reasoning card, pass a **component** instead of slot props. Your component receives the same top-level props as the built-in one:

Prop| Type| Description  
---|---|---  
`message`| `ReasoningMessage`| The reasoning message object (`.content` holds the text)  
`messages`| `Message[]`| All messages in the conversation  
`isRunning`| `boolean`| Whether the agent is currently running  
  
DemoCode

reasoning_agent.py

page.tsx

reasoning-block.tsx

route.ts
    
    
    """Reasoning agent: emits AG-UI REASONING_MESSAGE_* events.Shared by reasoning-default (CopilotKit's built-in reasoning slot) andreasoning-custom (a custom amber ReasoningBlock).Why a reasoning model plus the Responses API: the OpenAI Responses API streams`response.reasoning_summary_text.delta` items only for native reasoning models(gpt-5, o3, o4-mini and friends). The Strands bridge translates those intoAG-UI REASONING_MESSAGE_* events with `role: "reasoning"`, which the frontendrenders through the `reasoningMessage` slot. gpt-4o emits no reasoning items, sothe showcase's default chat-completions model would never light the slot up.`summary: "detailed"` rather than `"auto"` is deliberate: with `"auto"` themodel decides, and it frequently skips the summary entirely, which leaves thereasoning slot unmounted. Override the model with `OPENAI_REASONING_MODEL`.Mirrors `langgraph-python/src/agents/reasoning_agent.py`."""from __future__ import annotationsimport osfrom strands import Agentfrom ag_ui_strands import StrandsAgentSYSTEM_PROMPT = (    "You are a helpful assistant. For each user question, first think "    "step-by-step about the approach, then give a concise answer.")DEFAULT_REASONING_MODEL = "gpt-5.4"def reasoning_model_id() -> str:    """Resolve the reasoning model at call time.    Read here rather than at module scope: the agent server imports this module    before it calls `load_dotenv()`, so a module-level read would always miss an    `OPENAI_REASONING_MODEL` set in `.env`.    """    return os.environ.get("OPENAI_REASONING_MODEL", DEFAULT_REASONING_MODEL)def build_reasoning_model():    """Construct the Responses-API model that streams reasoning summaries.    `OpenAIResponsesModel` is imported here rather than at module scope so the    dependency shows up where it is used; it needs openai>=2, which the pinned    requirements provide. The agent server builds these agents at import time,    so an older install still fails the whole server, not just these demos.    """    from strands.models.openai_responses import OpenAIResponsesModel    api_key = os.getenv("OPENAI_API_KEY", "")    if not api_key:        raise RuntimeError("OPENAI_API_KEY must be set for the strands showcase agent")    return OpenAIResponsesModel(        client_args={"api_key": api_key},        model_id=reasoning_model_id(),        params={"reasoning": {"effort": "medium", "summary": "detailed"}},    )def build_reasoning_agent() -> StrandsAgent:    """Construct the tool-free StrandsAgent backing both reasoning demos."""    strands_agent = Agent(        model=build_reasoning_model(),        system_prompt=SYSTEM_PROMPT,        tools=[],    )    return StrandsAgent(        agent=strands_agent,        name="reasoning",        description="Strands agent that streams reasoning summaries alongside its answer",    )

The `ReasoningBlock` used above renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone:

page.tsx
    
    
    const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}

## Render-Prop Children#

The built-in `CopilotChatReasoningMessage` also supports a **render-prop** pattern for cases where you want to rearrange the built-in sub-components without reimplementing them:
    
    
    import {
      CopilotChatReasoningMessage,
    } from "@copilotkit/react-core/v2";
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function MyReasoningLayout(props: React.ComponentProps<typeof CopilotChatReasoningMessage>) {
      return (
        <CopilotChatReasoningMessage {...props}>
          {({ header, toggle }) => (
            <div className="rounded-lg border bg-yellow-50 my-2">
              {header}
              {toggle}
            </div>
          )}
        </CopilotChatReasoningMessage>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: MyReasoningLayout,
      }}
    />

The render-prop callback receives:

Property| Description  
---|---  
`header`| Pre-rendered header element  
`contentView`| Pre-rendered content element  
`toggle`| Pre-rendered expand/collapse wrapper (contains `contentView`)  
`message`| The reasoning message object  
`messages`| All messages  
`isRunning`| Whether the agent is running  
  
### On this page

Default BehaviorCustomizing the Reasoning MessageCustom HeaderCustom ContentFully Custom Reasoning MessageRender-Prop Children
