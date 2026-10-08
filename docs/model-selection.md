---
url: https://docs.copilotkit.ai/model-selection/
title: Model Selection
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:38.787101+00:00
---

# Model Selection

> Source: https://docs.copilotkit.ai/model-selection/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Server Tools](https://docs.copilotkit.ai/server-tools)[MCP Servers](https://docs.copilotkit.ai/mcp-servers)[Model Selection](https://docs.copilotkit.ai/model-selection)[Advanced Configuration](https://docs.copilotkit.ai/advanced-configuration)

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Model Selection

Agent capabilitiesBuilt-in Agent

# Model Selection

Choose and configure models for your Built-in Agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The Built-in Agent uses the [Vercel AI SDK](https://sdk.vercel.ai), so you can use built-in model strings or pass any custom AI SDK model.

## Supported Models#

Specify a model using the `"provider:model"` format. `"provider/model"` also works.

The tables list the models these docs use. The quickstart uses `openai:gpt-5.4-mini`. The Built-in Agent sends the model id to the provider unchanged, so other model ids from the same provider also work.

### OpenAI#

Model| Specifier  
---|---  
GPT-5.5| `openai:gpt-5.5`  
GPT-5.4| `openai:gpt-5.4`  
GPT-5.4 Mini| `openai:gpt-5.4-mini`  
GPT-5| `openai:gpt-5`  
GPT-5 Mini| `openai:gpt-5-mini`  
GPT-4.1| `openai:gpt-4.1`  
GPT-4.1 Mini| `openai:gpt-4.1-mini`  
GPT-4.1 Nano| `openai:gpt-4.1-nano`  
GPT-4o| `openai:gpt-4o`  
GPT-4o Mini| `openai:gpt-4o-mini`  
o3| `openai:o3`  
o3-mini| `openai:o3-mini`  
o4-mini| `openai:o4-mini`  
      
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
    });

### Anthropic#

Model| Specifier  
---|---  
Claude Opus 4.8| `anthropic:claude-opus-4-8`  
Claude Sonnet 4.6| `anthropic:claude-sonnet-4-6`  
Claude Haiku 4.5| `anthropic:claude-haiku-4-5`  
Claude Sonnet 4.5| `anthropic:claude-sonnet-4-5`  
      
    
    const agent = new BuiltInAgent({
      model: "anthropic:claude-sonnet-4-6",
    });

### Google#

Model| Specifier  
---|---  
Gemini 2.5 Pro| `google:gemini-2.5-pro`  
Gemini 2.5 Flash| `google:gemini-2.5-flash`  
Gemini 2.5 Flash Lite| `google:gemini-2.5-flash-lite`  
      
    
    const agent = new BuiltInAgent({
      model: "google:gemini-2.5-pro",
    });

### MiniMax#

Model| Specifier  
---|---  
MiniMax M3| `minimax:MiniMax-M3`  
MiniMax M2.7| `minimax:MiniMax-M2.7`  
      
    
    const agent = new BuiltInAgent({
      model: "minimax:MiniMax-M3",
    });

## Environment Variables#

Set the API key for your chosen provider:
    
    
    # OpenAI
    OPENAI_API_KEY=sk-...
    
    # Anthropic
    ANTHROPIC_API_KEY=sk-ant-...
    
    # Google
    GOOGLE_API_KEY=...
    
    # MiniMax
    MINIMAX_API_KEY=...
    
    # Optional: use the China endpoint
    MINIMAX_BASE_URL=https://api.minimaxi.com/v1

Alternatively, pass the API key directly in your configuration:
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      apiKey: process.env.MY_OPENAI_KEY, 
    });

## Custom Models (AI SDK)#

For models not in the built-in list, you can pass any Vercel AI SDK `LanguageModel` instance directly. First, install the provider package from its `ai-v6` release line:
    
    
    npm install @ai-sdk/openai@ai-v6

Install the ai-v6 version of each @ai-sdk provider

The Built-in Agent runs on AI SDK 6 (`ai@6`), which needs `@ai-sdk/*` provider packages from the 3.x line. Add `@ai-v6` to every provider you install, for example `npm install @ai-sdk/azure@ai-v6`.
    
    
    import { BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createOpenAI } from "@ai-sdk/openai"; 
    
    const customProvider = createOpenAI({
      apiKey: process.env.MY_API_KEY, 
      baseURL: "https://my-proxy.example.com/v1", 
    }); 
    
    const agent = new BuiltInAgent({
      model: customProvider("my-fine-tuned-model"), 
    });

This works with any AI SDK provider, including Azure OpenAI, AWS Bedrock, Ollama, or any OpenAI-compatible endpoint:
    
    
    import { createAzure } from "@ai-sdk/azure";
    
    const azure = createAzure({
      resourceName: "my-resource",
      apiKey: process.env.AZURE_API_KEY,
    });
    
    const agent = new BuiltInAgent({
      model: azure("my-deployment"),
    });

## OpenRouter, proxies, and bring-your-own LLM#

Anything that exposes an **OpenAI-compatible** API, including [OpenRouter](https://openrouter.ai), a self-hosted gateway, an internal LLM proxy, [Ollama](https://ollama.com), [Together](https://together.ai), [Groq](https://groq.com), [Novita](https://novita.ai), or your own fine-tuned endpoint, works through the same `createOpenAI({ baseURL })` pattern shown in Custom Models above. Point `baseURL` at the provider's OpenAI-compatible route and pass your key:

Novita: use provider.chat(model)

Novita only implements the Chat Completions endpoint, not Responses. Call it as `provider.chat("model")` (not `provider("model")`) — the bare call form used in the example below routes through Responses and returns an error on Novita.
    
    
    import { BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createOpenAI } from "@ai-sdk/openai"; 
    
    // OpenRouter: one key, hundreds of models behind an OpenAI-compatible API
    const openrouter = createOpenAI({
      apiKey: process.env.OPENROUTER_API_KEY, 
      baseURL: "https://openrouter.ai/api/v1", 
    }); 
    
    const agent = new BuiltInAgent({
      model: openrouter("anthropic/claude-sonnet-4-6"), 
    });

The same shape works for any OpenAI-compatible proxy. Swap the `baseURL` and key. There is no CopilotKit-specific provider to install. Install `@ai-sdk/openai@ai-v6` as shown in Custom Models. If the AI SDK can talk to it, the Built-in Agent can use it.

The model is set on the agent

CopilotKit does **not** expose a cloud-hosted endpoint for choosing or switching the model at request time. The model is configured **on the agent** , either as a `"provider:model"` string or an AI SDK `LanguageModel` instance:
    
    
    new BuiltInAgent({ model: "openai:gpt-5.4-mini" }); // built-in string
    new BuiltInAgent({ model: openrouter("...") }); // any LanguageModel

To switch models per user, request, or feature flag, construct the agent with the desired `model` on your own backend. For full control over the runtime you can also use a [Custom Agent](https://docs.copilotkit.ai/backend/custom-agent).

## How it works#

The Built-in Agent resolves model strings to AI SDK provider instances:

Model string| AI SDK provider| Resolved call  
---|---|---  
`"openai:gpt-5.4-mini"`| `@ai-sdk/openai`| `openai("gpt-5.4-mini")`  
`"anthropic:claude-sonnet-4-6"`| `@ai-sdk/anthropic`| `anthropic("claude-sonnet-4-6")`  
`"google:gemini-2.5-pro"`| `@ai-sdk/google`| `google("gemini-2.5-pro")`  
  
Both `"provider:model"` and `"provider/model"` separators are supported and work identically.

Need a different AI SDK or full control?

The [Custom Agent](https://docs.copilotkit.ai/backend/custom-agent) lets you bring your own AI SDK, TanStack AI, or any custom LLM backend while CopilotKit handles the rest.

### On this page

Supported ModelsOpenAIAnthropicGoogleMiniMaxEnvironment VariablesCustom Models (AI SDK)OpenRouter, proxies, and bring-your-own LLMHow it works
