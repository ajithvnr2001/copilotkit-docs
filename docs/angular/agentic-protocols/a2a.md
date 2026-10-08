---
url: https://docs.copilotkit.ai/angular/agentic-protocols/a2a/
title: A2A
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:16.041642+00:00
---

# A2A

> Source: https://docs.copilotkit.ai/angular/agentic-protocols/a2a/

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

[Architecture](https://docs.copilotkit.ai/angular/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/angular/concepts/generative-ui-overview)[Open source vs Intelligence](https://docs.copilotkit.ai/angular/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/angular/agentic-protocols)

[AG-UI](https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui)[AG-UI Middleware](https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui-middleware)[A2A](https://docs.copilotkit.ai/angular/agentic-protocols/a2a)

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

A2A

LearnConceptsAgentic Protocols

# A2A

Bring your A2A agents to your users through AG-UI and CopilotKit.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is the A2A Protocol?#

A2A, or the Agent2Agent protocol, is a protocol introduced by Google for AI agents to interact and collaborate securely in a framework agnostic manner.

CopilotKit fully supports the A2A protocol, connecting directly to A2A supporting agents or meshes with no modification of the agent needed.

![CopilotKit with Agentic Protocols](https://docs.copilotkit.ai/images/any-agentic-backend-light.png)![CopilotKit with Agentic Protocols](https://docs.copilotkit.ai/images/any-agentic-backend-dark.png)

A2A is one of three prominent [agentic protocols](https://docs.copilotkit.ai/angular/agentic-protocols) CopilotKit supports to connect agents to user-facing frontends

## How CopilotKit uses A2A agents#

CopilotKit uses a middleware to expose A2A agents to an AG-UI compatible coordinator. This allows you to expose your A2A agents to your users through the AG-UI protocol.

  * **Flexibility and Interoperability** : By making a2a agents available over the AG-UI standard, any A2A agents can work seamless with CopilotKit components.
  * **Unified Communication** : While A2A agents are enabled to communicate with each other over the A2A protocol, AG-UI adds the missing tooling to expose them cleanly to the front end.



To learn more, check out the [A2A](https://a2a-protocol.org/latest/) website.

## How to use A2A agents with CopilotKit#

To use A2A agents with CopilotKit, you need to first install the CopilotKit middleware.

### Run and Connect Your Agent to CopilotKit#

You'll need to run your agent and connect it to CopilotKit before proceeding.

#### I already have an AG-UI agent to use as a coordinator.

Excellent! You can move on to the next step.

#### I want to start from scratch

Run the following command to create a brand new project with a pre-configured AG-UI agent and some A2A agents:
    
    
    npx copilotkit@latest create -f a2a

This will create a new project with a pre-configured ADK AG-UI agent, but you can use any AG-UI agent you want.

### Install the A2A middleware This is already installed for you in the#

project, but if you're adding the middleware to an existing agent, you can install it with the following command: `bash npm install @ag-ui/a2a-middleware `

### Configure the A2A middleware#

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    import { HttpAgent } from "@ag-ui/client";
    import { A2AMiddlewareAgent } from "@ag-ui/a2a-middleware";
    
    // These first two are the urls to the a2a agents
    const researchAgentUrl = process.env.RESEARCH_AGENT_URL || "http://localhost:9001";
    const analysisAgentUrl = process.env.ANALYSIS_AGENT_URL || "http://localhost:9002";
    
    // And this is the url to the orchestrator agent that will be wrapped in the middleware
    const orchestratorUrl = process.env.ORCHESTRATOR_URL || "http://localhost:9000";
    
    // the orchestrator agent we pass to the middleware needs to be an instance of a derivative of an ag-ui `AbstractAgent`
    // In this case, we have access to the agent via url, so we can gain an instance using the `HttpAgent` class
    const orchestrationAgent = new HttpAgent({
      url: orchestratorUrl,
    });
    
    // A2A Middleware: Wraps orchestrator and injects send_message_to_a2a_agent tool
    // This allows orchestrator to communicate with A2A agents transparently
    const a2aMiddlewareAgent = new A2AMiddlewareAgent({
      description:
        "Research assistant with 2 specialized agents: Research (LangGraph) and Analysis (ADK)",
      // We pass the urls to the a2a agents, the middleware will handle the connections
      agentUrls: [
        researchAgentUrl,
        analysisAgentUrl,
      ],
      // Pass the agent instance
      orchestrationAgent,
      // These are domain specific instructions for the agent. They will be added to the generic instructions on how to
      // connect to a2a agents that will be automatically generated by the middleware
      instructions: `
        You are a research assistant that orchestrates between 2 specialized agents.
    
        AVAILABLE AGENTS:
    
        - Research Agent (LangGraph): Gathers and summarizes information about a topic
        - Analysis Agent (ADK): Analyzes research findings and provides insights
    
        WORKFLOW STRATEGY (SEQUENTIAL - ONE AT A TIME):
    
        When the user asks to research a topic:
    
        1. Research Agent - First, gather information about the topic
          - Pass: The user's research query or topic
          - The agent will return structured JSON with research findings
    
        2. Analysis Agent - Then, analyze the research results
          - Pass: The research results from step 1
          - The agent will return structured JSON with analysis and insights
    
        3. Present the complete research and analysis to the user
    
        CRITICAL RULES:
        - Call agents ONE AT A TIME, wait for results before making next call
        - Pass information from earlier agents to later agents
        - Synthesize all gathered information in final response
      `,
    });
    
    // CopilotKit runtime connects frontend to agent system
    const runtime = new CopilotRuntime({
      agents: {
        a2a_chat: a2aMiddlewareAgent, // Use this same id in the frontend.
      },
      runner: new InMemoryAgentRunner(),
    });
    
    // Standard Next.js App Router handler that hands requests to the runtime.
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

### Render A2A handoffs in Angular#

The middleware emits the `send_message_to_a2a_agent` tool call. Register an Angular renderer for that name so the chat can show the destination, request, and completion state:

src/app/a2a-message.component.ts
    
    
    import { Component, input } from "@angular/core";
    import {
      AngularToolCall,
      ToolRenderer,
      registerRenderToolCall,
    } from "@copilotkit/angular";
    import { z } from "zod";
    
    type A2AMessageArgs = {
      agentName: string;
      task: string;
    };
    
    @Component({
      selector: "app-a2a-message",
      template: `
        <strong>Orchestrator → {{ toolCall().args.agentName }}</strong>
        <p>{{ toolCall().args.task }}</p>
        <small>{{ toolCall().status }}</small>
      `,
    })
    export class A2AMessageComponent
      implements ToolRenderer<A2AMessageArgs>
    {
      readonly toolCall =
        input.required<AngularToolCall<A2AMessageArgs>>();
    }
    
    @Component({ selector: "app-chat", template: `` })
    export class ChatComponent {
      constructor() {
        registerRenderToolCall({
          name: "send_message_to_a2a_agent",
          args: z.object({
            agentName: z.string(),
            task: z.string(),
          }),
          component: A2AMessageComponent,
        });
      }
    }

Registration follows the current injector and cleans itself up when that injector is destroyed. See the [renderer API](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall) for agent scoping and streaming argument details.

### Give it a try!#

Try asking your agent to research a topic, like "Please research quantum computing". You'll see that it will send messages to the research agent and the analysis agent. Then, it will present the complete research and analysis to the user.

### On this page

What is the A2A Protocol?How CopilotKit uses A2A agentsHow to use A2A agents with CopilotKit
