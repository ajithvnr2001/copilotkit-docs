---
url: https://docs.copilotkit.ai/angular/advanced-configuration/
title: Advanced Configuration
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:11.765835+00:00
---

# Advanced Configuration

> Source: https://docs.copilotkit.ai/angular/advanced-configuration/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Server Tools](https://docs.copilotkit.ai/angular/server-tools)[MCP Servers](https://docs.copilotkit.ai/angular/mcp-servers)[Model Selection](https://docs.copilotkit.ai/angular/model-selection)[Advanced Configuration](https://docs.copilotkit.ai/angular/advanced-configuration)

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Advanced Configuration

Agent capabilitiesBuilt-in Agent

# Advanced Configuration

Fine-tune your Built-in Agent's behavior with advanced options.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The `BuiltInAgent` accepts a full set of configuration options to control model behavior, tool calling, and more.

## Multi-step tool calling#

By default, the agent performs a single generation step. Set `maxSteps` to allow the agent to call tools and then continue reasoning:

src/copilotkit.ts
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      maxSteps: 5, 
      tools: [searchDocs, createTicket],
    });

With `maxSteps: 5`, the agent can call a tool, process the result, call another tool, and so on — up to 5 iterations. This is essential for workflows where the agent needs to chain multiple tool calls.

## Tool choice#

Control how the agent selects tools:
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      toolChoice: "auto",       // Let the model decide (default)
      // toolChoice: "required", // Force the model to call a tool
      // toolChoice: "none",     // Disable tool calling
      // toolChoice: { type: "tool", toolName: "searchDocs" }, // Force a specific tool
    });

## System prompt#

Customize the agent's system prompt:
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      prompt: "You are a customer support agent for Acme Corp. Be concise and helpful. Always check the knowledge base before answering.", 
    });

## Generation parameters#

Fine-tune the model's output:
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      temperature: 0.7,        // Creativity (0 = deterministic, 1+ = creative)
      topP: 0.9,               // Nucleus sampling
      topK: 40,                // Top-K sampling (provider-dependent)
      maxOutputTokens: 4096,   // Maximum tokens in the response
      presencePenalty: 0.1,    // Penalize repeated topics
      frequencyPenalty: 0.1,   // Penalize repeated tokens
      stopSequences: ["END"],  // Stop generation at these sequences
      seed: 42,                // Deterministic output (provider-dependent)
      maxRetries: 3,           // Retry on transient failures
    });

Not all parameters are supported by every provider. For example, `topK` is supported by Google but not OpenAI. Unsupported parameters are ignored.

## Provider-specific options#

Pass options specific to a model provider using `providerOptions`:
    
    
    // OpenAI reasoning models (o3, o4-mini) with reasoning effort
    const agent = new BuiltInAgent({
      model: "openai:o3",
      providerOptions: { 
        openai: { reasoningEffort: "high" },
      },
    });
    
    
    // Anthropic with adaptive thinking
    const agent = new BuiltInAgent({
      model: "anthropic:claude-sonnet-4-6",
      providerOptions: { 
        anthropic: { thinking: { type: "adaptive" }, effort: "high" },
      },
    });

## Overridable properties#

Allow the frontend to override specific configuration at runtime. This is useful when you want users to switch models or adjust behavior without redeploying:
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      temperature: 0.5,
      overridableProperties: ["model", "temperature", "prompt"], 
    });

The full list of overridable properties: `model`, `toolChoice`, `maxOutputTokens`, `temperature`, `topP`, `topK`, `presencePenalty`, `frequencyPenalty`, `stopSequences`, `seed`, `maxRetries`, `prompt`, `providerOptions`

## Message forwarding#

Control whether system and developer messages from the conversation are forwarded to the LLM:
    
    
    const agent = new BuiltInAgent({
      model: "openai:gpt-5.4-mini",
      forwardSystemMessages: true,    // Forward system-role messages
      forwardDeveloperMessages: true, // Forward developer-role messages (as system messages)
    });

## Full configuration reference#

Property| Type| Default| Description  
---|---|---|---  
`model`| `string | LanguageModel`| —| Model specifier or AI SDK instance  
`apiKey`| `string`| env var| API key for the provider  
`maxSteps`| `number`| `1`| Max tool-calling iterations  
`toolChoice`| `"auto" | "required" | "none" | { type: "tool", toolName: string }`| `"auto"`| How tools are selected  
`maxOutputTokens`| `number`| —| Max tokens in response  
`temperature`| `number`| —| Sampling temperature  
`topP`| `number`| —| Nucleus sampling  
`topK`| `number`| —| Top-K sampling  
`presencePenalty`| `number`| —| Presence penalty  
`frequencyPenalty`| `number`| —| Frequency penalty  
`stopSequences`| `string[]`| —| Stop sequences  
`seed`| `number`| —| Random seed  
`maxRetries`| `number`| —| Retry count  
`prompt`| `string`| —| System prompt  
`tools`| `ToolDefinition[]`| `[]`| Server-side tools  
`mcpServers`| `MCPClientConfig[]`| `[]`| MCP server connections (agent-managed, per-request)  
`mcpClients`| `MCPClientProvider[]`| `[]`| User-managed MCP clients (persistent, user controls lifecycle)  
`overridableProperties`| `string[]`| `[]`| Properties the frontend can override  
`providerOptions`| `Record<string, any>`| —| Provider-specific options  
`forwardSystemMessages`| `boolean`| `false`| Forward system messages  
`forwardDeveloperMessages`| `boolean`| `false`| Forward developer messages  
  
Need even more control?

If `BuiltInAgent`'s configuration options don't cover your needs — for example, if you want to use TanStack AI, a custom LLM backend, or async initialization — see [Custom Agent](https://docs.copilotkit.ai/angular/backend/custom-agent).

### On this page

Multi-step tool callingTool choiceSystem promptGeneration parametersProvider-specific optionsOverridable propertiesMessage forwardingFull configuration reference
