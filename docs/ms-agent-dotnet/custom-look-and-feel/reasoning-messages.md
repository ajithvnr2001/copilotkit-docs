---
url: https://docs.copilotkit.ai/ms-agent-dotnet/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:18:22.181460+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/custom-look-and-feel/reasoning-messages/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (.NET)](https://docs.copilotkit.ai/ms-agent-dotnet)Custom Look and Feel

# Reasoning Messages

Customize how reasoning (thinking) tokens from models like o1, o3, and o4-mini are displayed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

ReasoningAgent.cs

page.tsx

route.ts
    
    
    using System.Diagnostics.CodeAnalysis;using System.Runtime.CompilerServices;using System.Text;using Microsoft.Agents.AI;using Microsoft.Extensions.AI;using Microsoft.Extensions.Logging;using Microsoft.Extensions.Logging.Abstractions;/// <summary>/// Agent wrapper that exposes the model's step-by-step thinking as a/// first-class AG-UI reasoning message, independent of the inner chat/// client actually supporting native reasoning tokens.////// The inner agent is prompted to produce output of the shape://////   &lt;reasoning&gt;///   step-by-step thinking...///   &lt;/reasoning&gt;///   final concise answer...////// This wrapper streams the response, detects the reasoning block, and/// re-emits the content inside the block as <see cref="TextReasoningContent"/>/// chunks while the content after the closing tag is emitted as ordinary/// <see cref="TextContent"/>. AG-UI hosting surfaces/// <see cref="TextReasoningContent"/> as <c>REASONING_MESSAGE_*</c> events,/// which CopilotKit's React packages render via the <c>reasoningMessage</c>/// slot./// </summary>[SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes", Justification = "Instantiated by ReasoningAgentFactory")]internal sealed class ReasoningAgent : DelegatingAIAgent{    private const string OpenTag = "<reasoning>";    private const string CloseTag = "</reasoning>";    private readonly ILogger<ReasoningAgent> _logger;    public ReasoningAgent(AIAgent innerAgent, ILogger<ReasoningAgent>? logger = null)        : base(innerAgent)    {        ArgumentNullException.ThrowIfNull(innerAgent);        _logger = logger ?? NullLogger<ReasoningAgent>.Instance;    }    public override Task<AgentRunResponse> RunAsync(IEnumerable<ChatMessage> messages, AgentThread? thread = null, AgentRunOptions? options = null, CancellationToken cancellationToken = default)    {        return RunStreamingAsync(messages, thread, options, cancellationToken).ToAgentRunResponseAsync(cancellationToken);    }    /// <summary>    /// Streams from the inner agent, splitting the produced text into a    /// reasoning segment (content inside <c>&lt;reasoning&gt;...&lt;/reasoning&gt;</c>)    /// and an answer segment (everything else).    /// </summary>    /// <remarks>    /// The splitter is deliberately simple: it buffers text across chunks    /// just enough to reliably detect the open/close tags, then forwards    /// chunks straight through to minimize perceived latency. Non-text    /// content (tool calls, data, etc.) is forwarded unchanged so the    /// split never interferes with the rest of the AG-UI event stream.    /// </remarks>    public override async IAsyncEnumerable<AgentRunResponseUpdate> RunStreamingAsync(        IEnumerable<ChatMessage> messages,        AgentThread? thread = null,        AgentRunOptions? options = null,        [EnumeratorCancellation] CancellationToken cancellationToken = default)    {        ArgumentNullException.ThrowIfNull(messages);        var buffer = new StringBuilder();        var state = SplitState.LookingForOpen;        await foreach (var update in InnerAgent.RunStreamingAsync(messages, thread, options, cancellationToken).ConfigureAwait(false))        {            // Pass through any non-text content (tool calls, data, usage, …)            // untouched — only text routing is affected by the split.            var textPieces = new List<string>();            var passthroughContents = new List<AIContent>();            foreach (var content in update.Contents)            {                if (content is TextContent tc && tc.Text is { Length: > 0 } text)                {                    textPieces.Add(text);                }                else if (content is not TextContent)                {                    passthroughContents.Add(content);                }            }            if (passthroughContents.Count > 0)            {                yield return new AgentRunResponseUpdate                {                    AuthorName = update.AuthorName,                    Role = update.Role,                    MessageId = update.MessageId,                    ResponseId = update.ResponseId,                    CreatedAt = update.CreatedAt,                    Contents = passthroughContents,                };            }            foreach (var piece in textPieces)            {                foreach (var emitted in RouteText(piece, buffer, ref state))                {                    yield return BuildUpdate(update, emitted.Content, emitted.IsReasoning);                }            }        }        // Flush anything left in the buffer as whichever stream we're        // currently in. If we never saw an opening tag the remaining text        // is an answer; if we're mid-reasoning we conservatively emit the        // tail as reasoning so the user still sees it.        if (buffer.Length > 0)        {            var remainder = buffer.ToString();            buffer.Clear();            var isReasoning = state == SplitState.InsideReasoning;            yield return BuildTrailingUpdate(remainder, isReasoning);        }    }    private static AgentRunResponseUpdate BuildUpdate(AgentRunResponseUpdate source, string content, bool isReasoning)    {        AIContent aiContent = isReasoning ? new TextReasoningContent(content) : new TextContent(content);        return new AgentRunResponseUpdate        {            AuthorName = source.AuthorName,            Role = source.Role,            MessageId = source.MessageId,            ResponseId = source.ResponseId,            CreatedAt = source.CreatedAt,            Contents = [aiContent],        };    }    private static AgentRunResponseUpdate BuildTrailingUpdate(string content, bool isReasoning)    {        AIContent aiContent = isReasoning ? new TextReasoningContent(content) : new TextContent(content);        return new AgentRunResponseUpdate        {            Contents = [aiContent],        };    }    /// <summary>    /// Incremental splitter. Appends <paramref name="piece"/> to    /// <paramref name="buffer"/> and yields zero or more text fragments    /// classified as reasoning vs. answer, advancing <paramref name="state"/>    /// as open/close tags are encountered.    /// </summary>    /// <remarks>    /// We only hold back the suffix of <paramref name="buffer"/> that could    /// be the start of the tag we're currently searching for — everything    /// older is safe to emit. That keeps streaming latency close to the    /// inner agent's.    /// </remarks>    private static IEnumerable<(string Content, bool IsReasoning)> RouteText(string piece, StringBuilder buffer, ref SplitState state)    {        buffer.Append(piece);        var results = new List<(string, bool)>();        while (true)        {            if (state == SplitState.LookingForOpen)            {                var full = buffer.ToString();                var openIdx = full.IndexOf(OpenTag, StringComparison.Ordinal);                if (openIdx >= 0)                {                    // Anything before the open tag is answer text.                    if (openIdx > 0)                    {                        results.Add((full[..openIdx], false));                    }                    // Drop the tag itself and switch state.                    buffer.Clear();                    buffer.Append(full[(openIdx + OpenTag.Length)..]);                    state = SplitState.InsideReasoning;                    continue;                }                // No open tag yet. Emit everything except a trailing                // partial-match suffix that could still become the tag.                var safe = SafePrefix(full, OpenTag);                if (safe > 0)                {                    results.Add((full[..safe], false));                    buffer.Clear();                    buffer.Append(full[safe..]);                }                break;            }            if (state == SplitState.InsideReasoning)            {                var full = buffer.ToString();                var closeIdx = full.IndexOf(CloseTag, StringComparison.Ordinal);                if (closeIdx >= 0)                {                    if (closeIdx > 0)                    {                        results.Add((full[..closeIdx], true));                    }                    buffer.Clear();                    buffer.Append(full[(closeIdx + CloseTag.Length)..]);                    state = SplitState.AfterReasoning;                    continue;                }                var safe = SafePrefix(full, CloseTag);                if (safe > 0)                {                    results.Add((full[..safe], true));                    buffer.Clear();                    buffer.Append(full[safe..]);                }                break;            }            // AfterReasoning — everything is answer text; flush buffer.            if (buffer.Length > 0)            {                results.Add((buffer.ToString(), false));                buffer.Clear();            }            break;        }        return results;    }    /// <summary>    /// Returns the largest index <c>k</c> such that the suffix starting at    /// <c>k</c> of <paramref name="text"/> cannot itself be the start of    /// <paramref name="tag"/>. Everything up to <c>k</c> is safe to emit.    /// </summary>    private static int SafePrefix(string text, string tag)    {        var maxHoldback = Math.Min(text.Length, tag.Length - 1);        for (var hold = maxHoldback; hold > 0; hold--)        {            var suffix = text[^hold..];            if (tag.StartsWith(suffix, StringComparison.Ordinal))            {                return text.Length - hold;            }        }        return text.Length;    }    private enum SplitState    {        LookingForOpen,        InsideReasoning,        AfterReasoning,    }}/// <summary>/// Builds a reasoning-capable <see cref="AIAgent"/> on top of an OpenAI/// chat client. The agent is instructed to bracket its chain-of-thought in/// <c>&lt;reasoning&gt;...&lt;/reasoning&gt;</c> tags so <see cref="ReasoningAgent"/>/// can reroute it into AG-UI reasoning events./// </summary>internal static class ReasoningAgentFactory{    internal const string SystemPrompt =        "You are a helpful assistant. For each user question, first think step-by-step " +        "about the approach, then give a concise final answer.\n\n" +        "Format your response EXACTLY like this, with no other preamble:\n" +        "<reasoning>\n" +        "your step-by-step thinking here, one thought per line\n" +        "</reasoning>\n" +        "your concise final answer here\n\n" +        "The <reasoning>...</reasoning> tags are mandatory and must appear before the final answer.";    public static AIAgent Create(IChatClient chatClient, ILoggerFactory loggerFactory)    {        ArgumentNullException.ThrowIfNull(chatClient);        ArgumentNullException.ThrowIfNull(loggerFactory);        var inner = new ChatClientAgent(            chatClient,            name: "ReasoningAgent",            instructions: SystemPrompt);        return new ReasoningAgent(inner, loggerFactory.CreateLogger<ReasoningAgent>());    }}

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

ReasoningAgent.cs

page.tsx

reasoning-block.tsx

route.ts
    
    
    using System.Diagnostics.CodeAnalysis;using System.Runtime.CompilerServices;using System.Text;using Microsoft.Agents.AI;using Microsoft.Extensions.AI;using Microsoft.Extensions.Logging;using Microsoft.Extensions.Logging.Abstractions;/// <summary>/// Agent wrapper that exposes the model's step-by-step thinking as a/// first-class AG-UI reasoning message, independent of the inner chat/// client actually supporting native reasoning tokens.////// The inner agent is prompted to produce output of the shape://////   &lt;reasoning&gt;///   step-by-step thinking...///   &lt;/reasoning&gt;///   final concise answer...////// This wrapper streams the response, detects the reasoning block, and/// re-emits the content inside the block as <see cref="TextReasoningContent"/>/// chunks while the content after the closing tag is emitted as ordinary/// <see cref="TextContent"/>. AG-UI hosting surfaces/// <see cref="TextReasoningContent"/> as <c>REASONING_MESSAGE_*</c> events,/// which CopilotKit's React packages render via the <c>reasoningMessage</c>/// slot./// </summary>[SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes", Justification = "Instantiated by ReasoningAgentFactory")]internal sealed class ReasoningAgent : DelegatingAIAgent{    private const string OpenTag = "<reasoning>";    private const string CloseTag = "</reasoning>";    private readonly ILogger<ReasoningAgent> _logger;    public ReasoningAgent(AIAgent innerAgent, ILogger<ReasoningAgent>? logger = null)        : base(innerAgent)    {        ArgumentNullException.ThrowIfNull(innerAgent);        _logger = logger ?? NullLogger<ReasoningAgent>.Instance;    }    public override Task<AgentRunResponse> RunAsync(IEnumerable<ChatMessage> messages, AgentThread? thread = null, AgentRunOptions? options = null, CancellationToken cancellationToken = default)    {        return RunStreamingAsync(messages, thread, options, cancellationToken).ToAgentRunResponseAsync(cancellationToken);    }    /// <summary>    /// Streams from the inner agent, splitting the produced text into a    /// reasoning segment (content inside <c>&lt;reasoning&gt;...&lt;/reasoning&gt;</c>)    /// and an answer segment (everything else).    /// </summary>    /// <remarks>    /// The splitter is deliberately simple: it buffers text across chunks    /// just enough to reliably detect the open/close tags, then forwards    /// chunks straight through to minimize perceived latency. Non-text    /// content (tool calls, data, etc.) is forwarded unchanged so the    /// split never interferes with the rest of the AG-UI event stream.    /// </remarks>    public override async IAsyncEnumerable<AgentRunResponseUpdate> RunStreamingAsync(        IEnumerable<ChatMessage> messages,        AgentThread? thread = null,        AgentRunOptions? options = null,        [EnumeratorCancellation] CancellationToken cancellationToken = default)    {        ArgumentNullException.ThrowIfNull(messages);        var buffer = new StringBuilder();        var state = SplitState.LookingForOpen;        await foreach (var update in InnerAgent.RunStreamingAsync(messages, thread, options, cancellationToken).ConfigureAwait(false))        {            // Pass through any non-text content (tool calls, data, usage, …)            // untouched — only text routing is affected by the split.            var textPieces = new List<string>();            var passthroughContents = new List<AIContent>();            foreach (var content in update.Contents)            {                if (content is TextContent tc && tc.Text is { Length: > 0 } text)                {                    textPieces.Add(text);                }                else if (content is not TextContent)                {                    passthroughContents.Add(content);                }            }            if (passthroughContents.Count > 0)            {                yield return new AgentRunResponseUpdate                {                    AuthorName = update.AuthorName,                    Role = update.Role,                    MessageId = update.MessageId,                    ResponseId = update.ResponseId,                    CreatedAt = update.CreatedAt,                    Contents = passthroughContents,                };            }            foreach (var piece in textPieces)            {                foreach (var emitted in RouteText(piece, buffer, ref state))                {                    yield return BuildUpdate(update, emitted.Content, emitted.IsReasoning);                }            }        }        // Flush anything left in the buffer as whichever stream we're        // currently in. If we never saw an opening tag the remaining text        // is an answer; if we're mid-reasoning we conservatively emit the        // tail as reasoning so the user still sees it.        if (buffer.Length > 0)        {            var remainder = buffer.ToString();            buffer.Clear();            var isReasoning = state == SplitState.InsideReasoning;            yield return BuildTrailingUpdate(remainder, isReasoning);        }    }    private static AgentRunResponseUpdate BuildUpdate(AgentRunResponseUpdate source, string content, bool isReasoning)    {        AIContent aiContent = isReasoning ? new TextReasoningContent(content) : new TextContent(content);        return new AgentRunResponseUpdate        {            AuthorName = source.AuthorName,            Role = source.Role,            MessageId = source.MessageId,            ResponseId = source.ResponseId,            CreatedAt = source.CreatedAt,            Contents = [aiContent],        };    }    private static AgentRunResponseUpdate BuildTrailingUpdate(string content, bool isReasoning)    {        AIContent aiContent = isReasoning ? new TextReasoningContent(content) : new TextContent(content);        return new AgentRunResponseUpdate        {            Contents = [aiContent],        };    }    /// <summary>    /// Incremental splitter. Appends <paramref name="piece"/> to    /// <paramref name="buffer"/> and yields zero or more text fragments    /// classified as reasoning vs. answer, advancing <paramref name="state"/>    /// as open/close tags are encountered.    /// </summary>    /// <remarks>    /// We only hold back the suffix of <paramref name="buffer"/> that could    /// be the start of the tag we're currently searching for — everything    /// older is safe to emit. That keeps streaming latency close to the    /// inner agent's.    /// </remarks>    private static IEnumerable<(string Content, bool IsReasoning)> RouteText(string piece, StringBuilder buffer, ref SplitState state)    {        buffer.Append(piece);        var results = new List<(string, bool)>();        while (true)        {            if (state == SplitState.LookingForOpen)            {                var full = buffer.ToString();                var openIdx = full.IndexOf(OpenTag, StringComparison.Ordinal);                if (openIdx >= 0)                {                    // Anything before the open tag is answer text.                    if (openIdx > 0)                    {                        results.Add((full[..openIdx], false));                    }                    // Drop the tag itself and switch state.                    buffer.Clear();                    buffer.Append(full[(openIdx + OpenTag.Length)..]);                    state = SplitState.InsideReasoning;                    continue;                }                // No open tag yet. Emit everything except a trailing                // partial-match suffix that could still become the tag.                var safe = SafePrefix(full, OpenTag);                if (safe > 0)                {                    results.Add((full[..safe], false));                    buffer.Clear();                    buffer.Append(full[safe..]);                }                break;            }            if (state == SplitState.InsideReasoning)            {                var full = buffer.ToString();                var closeIdx = full.IndexOf(CloseTag, StringComparison.Ordinal);                if (closeIdx >= 0)                {                    if (closeIdx > 0)                    {                        results.Add((full[..closeIdx], true));                    }                    buffer.Clear();                    buffer.Append(full[(closeIdx + CloseTag.Length)..]);                    state = SplitState.AfterReasoning;                    continue;                }                var safe = SafePrefix(full, CloseTag);                if (safe > 0)                {                    results.Add((full[..safe], true));                    buffer.Clear();                    buffer.Append(full[safe..]);                }                break;            }            // AfterReasoning — everything is answer text; flush buffer.            if (buffer.Length > 0)            {                results.Add((buffer.ToString(), false));                buffer.Clear();            }            break;        }        return results;    }    /// <summary>    /// Returns the largest index <c>k</c> such that the suffix starting at    /// <c>k</c> of <paramref name="text"/> cannot itself be the start of    /// <paramref name="tag"/>. Everything up to <c>k</c> is safe to emit.    /// </summary>    private static int SafePrefix(string text, string tag)    {        var maxHoldback = Math.Min(text.Length, tag.Length - 1);        for (var hold = maxHoldback; hold > 0; hold--)        {            var suffix = text[^hold..];            if (tag.StartsWith(suffix, StringComparison.Ordinal))            {                return text.Length - hold;            }        }        return text.Length;    }    private enum SplitState    {        LookingForOpen,        InsideReasoning,        AfterReasoning,    }}/// <summary>/// Builds a reasoning-capable <see cref="AIAgent"/> on top of an OpenAI/// chat client. The agent is instructed to bracket its chain-of-thought in/// <c>&lt;reasoning&gt;...&lt;/reasoning&gt;</c> tags so <see cref="ReasoningAgent"/>/// can reroute it into AG-UI reasoning events./// </summary>internal static class ReasoningAgentFactory{    internal const string SystemPrompt =        "You are a helpful assistant. For each user question, first think step-by-step " +        "about the approach, then give a concise final answer.\n\n" +        "Format your response EXACTLY like this, with no other preamble:\n" +        "<reasoning>\n" +        "your step-by-step thinking here, one thought per line\n" +        "</reasoning>\n" +        "your concise final answer here\n\n" +        "The <reasoning>...</reasoning> tags are mandatory and must appear before the final answer.";    public static AIAgent Create(IChatClient chatClient, ILoggerFactory loggerFactory)    {        ArgumentNullException.ThrowIfNull(chatClient);        ArgumentNullException.ThrowIfNull(loggerFactory);        var inner = new ChatClientAgent(            chatClient,            name: "ReasoningAgent",            instructions: SystemPrompt);        return new ReasoningAgent(inner, loggerFactory.CreateLogger<ReasoningAgent>());    }}

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
