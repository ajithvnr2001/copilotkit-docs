---
url: https://docs.copilotkit.ai/langgraph-fastapi/configurable/
title: Configurable
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:41.754622+00:00
---

# Configurable

> Source: https://docs.copilotkit.ai/langgraph-fastapi/configurable/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Readables](https://docs.copilotkit.ai/langgraph-fastapi/agent-app-context)[Configurable](https://docs.copilotkit.ai/langgraph-fastapi/configurable)[Subgraphs](https://docs.copilotkit.ai/langgraph-fastapi/subgraphs)[Guardrails & DLP](https://docs.copilotkit.ai/langgraph-fastapi/guardrails)[AWS AgentCore](https://docs.copilotkit.ai/langgraph-fastapi/deploy-agentcore)[LangSmith Platform](https://docs.copilotkit.ai/langgraph-fastapi/deploy-langsmith)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Configurable

Agent capabilitiesLangGraph (FastAPI)

# Configurable

Choose the supported channel for LangGraph runtime values and execution settings.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Choose the right channel#

Some LangGraph adapters merge browser-supplied `forwardedProps.config` into LangGraph's `RunnableConfig`. Those values remain browser-controlled and untrusted, even when a LangGraph config schema accepts them. Never use them for credentials, tenant identity, authorization, or server execution controls. Keep the trust boundary explicit and use the channel that matches the value:

Value| Supported channel  
---|---  
UI preferences the model should see| Publish them with your frontend's agent-context API; see [Agent Config](https://docs.copilotkit.ai/langgraph-fastapi/agent-config).  
Authentication and authorization| Send an `Authorization` header and validate it for every request; see [Authentication](https://docs.copilotkit.ai/langgraph-fastapi/auth).  
Graph execution settings| Set them in the trusted backend that invokes or serves the graph.  
  
Do not send credentials as run properties

Run properties are application payload, not an authentication or LangGraph configuration channel. Validate credentials at the server boundary and pass only the resolved identity to the graph.

## Model-visible UI preferences#

For tone, expertise level, response length, selected records, or other non-secret values that should influence the model, publish them as agent context. The [Agent Config guide](https://docs.copilotkit.ai/langgraph-fastapi/agent-config) shows the complete pattern and how CopilotKit middleware exposes the latest values on every turn.

In React, publish the values with [`useAgentContext`](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext).

## Authentication#

Authentication belongs in request headers, not graph state or runtime properties. The [Authentication guide](https://docs.copilotkit.ai/langgraph-fastapi/auth) covers both LangGraph Platform and self-hosted AG-UI endpoints. In both cases, validate the current request before the graph runs and inject only a resolved user or tenant identifier.

## Trusted graph execution settings#

Set graph configuration in backend code after validating any input that influences it. Do not accept a browser-supplied configuration object wholesale.

PythonTypeScript

For a self-hosted AG-UI endpoint, construct a request-local `LangGraphAGUIAgent` with backend-owned configuration:

main.py
    
    
    from copilotkit import LangGraphAGUIAgent
    
    def build_agent(tenant_id: str) -> LangGraphAGUIAgent:
        return LangGraphAGUIAgent(
            name="sample_agent",
            description="Tenant-scoped agent",
            graph=graph,
            config={
                "configurable": {"tenant_id": tenant_id},
                "recursion_limit": 50,
            },
        )

A node can then read the validated value from the configuration supplied by the server:
    
    
    from langchain_core.runnables import RunnableConfig
    
    async def agent_node(state: AgentState, config: RunnableConfig):
        tenant_id = config["configurable"]["tenant_id"]
        return state

Create the agent after authentication for each request, as shown in the [self-hosted authentication guide](https://docs.copilotkit.ai/langgraph-fastapi/auth).

Set runtime context and execution controls where your trusted backend invokes the graph. `recursionLimit` is a top-level execution setting; your application values belong in `context`:

agent.ts
    
    
    const result = await graph.invoke(input, {
      context: { tenantId: verifiedTenantId },
      recursionLimit: 50,
    });

Read the validated context through the node's LangGraph runtime. See [LangGraph's runtime configuration guide](https://docs.langchain.com/oss/javascript/langgraph/use-graph-api#add-runtime-configuration) for the matching context schema and node signature.

## What not to do#

  * Do not put raw credentials in model-visible context or graph state.
  * Do not persist credentials merely to make them available on later turns.
  * Do not trust a value merely because an adapter placed it in `RunnableConfig`.
  * Do not let a browser choose recursion limits, callbacks, metadata, or other server execution controls.
  * Do not reuse request-scoped identity between runs. Validate every request.



### On this page

Choose the right channelModel-visible UI preferencesAuthenticationTrusted graph execution settingsWhat not to do
