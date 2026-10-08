---
url: https://docs.copilotkit.ai/ag2/auth/
title: Authentication
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:43:27.136254+00:00
---

# Authentication

> Source: https://docs.copilotkit.ai/ag2/auth/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Authentication](https://docs.copilotkit.ai/ag2/auth)

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Authentication

Agent capabilitiesAG2

# Authentication

Secure your AG2 backend with user authentication on /chat

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

CopilotKit supports user authentication for AG2 backends in two deployment modes:

  * **LangGraph Platform equivalent** : cloud-hosted runtime forwarding to your AG2 `/chat` endpoint
  * **Self-hosted runtime** : your own CopilotKit runtime forwarding to your AG2 `/chat` endpoint



Both approaches let your AG2 backend access authenticated user context and enforce authorization.

This pattern enables your backend to:

  * Validate user tokens before dispatching the agent
  * Attach authenticated user context to agent state/tools
  * Enforce authorization decisions server-side



CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## How It Works#
    
    
    sequenceDiagram
        participant Frontend
        participant CopilotKit
        participant AG2Backend
        participant Agent
    
        Frontend->>CopilotKit: authorization: "user-token"
        CopilotKit->>AG2Backend: Forward auth token header
        AG2Backend->>AG2Backend: Validate token
        AG2Backend->>Agent: Dispatch with authenticated context
        Agent->>Agent: Access authenticated user context

## Frontend Setup#

Pass your authentication token via the `properties` prop:
    
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      properties={{
        authorization: userToken, // forwarded to AG2 /chat
      }}
    >
      <YourApp />
    </CopilotKit>

**Note** : The `authorization` property is forwarded to your AG2 `/chat` endpoint as a request header.

## LangGraph Platform Deployment#

**For cloud-hosted deployments** , protect your AG2 `/chat` endpoint with token-header validation.

### Setup Authentication Handler#
    
    
    from fastapi import FastAPI, Header, HTTPException
    from fastapi.responses import StreamingResponse
    
    from ag2 import Agent
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    agent = Agent(
        name="assistant",
        prompt="You are a helpful assistant.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    def validate_your_token(token: str) -> dict:
        # Replace this with your own validation logic.
        if token != "valid-token":
            raise HTTPException(status_code=401, detail="Unauthorized")
        return {
            "user_id": "user_123",
            "role": "member",
            # The scope `get_account_data` below checks against.
            "allowed_accounts": ["acct_456"],
        }
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
        accept: str | None = Header(None),
        authorization: str | None = Header(None),
    ) -> StreamingResponse:
        if not authorization:
            raise HTTPException(status_code=401, detail="Missing authorization header")
    
        token = authorization.replace("Bearer ", "")
        user_info = validate_your_token(token)
    
        # Pass the authenticated user into the run as a dependency, so tools
        # can scope data access to this user. Dependencies stay server-side —
        # unlike variables, they are never streamed to the client as state.
        return StreamingResponse(
            stream.dispatch(message, dependencies={"auth_user": user_info}, accept=accept),
            media_type=accept or "text/event-stream",
        )

### Access User in Agent#

Use validated user identity to scope tool calls and data access:
    
    
    from typing import Annotated
    
    from ag2 import Inject, tool
    
    @tool
    def get_account_data(
        account_id: str,
        auth_user: Annotated[dict, Inject("auth_user")],
    ) -> dict:
        """Return account data for the authenticated user."""
        if not auth_user:
            return {"error": "unauthorized"}
        # Example check: ensure user can access this account
        if account_id not in auth_user.get("allowed_accounts", []):
            return {"error": "forbidden"}
        return {"account_id": account_id, "owner": auth_user["user_id"]}

The `Inject("auth_user")` annotation pulls the dependency you passed to `stream.dispatch(...)` — it is invisible to the LLM and never leaves the server. Register the tool on the agent so the LLM can call it:
    
    
    agent = Agent(
        name="assistant",
        prompt="You are a helpful assistant.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[get_account_data], 
    )

## Self-hosted Deployment#

**For self-hosted deployments** , use the same `/chat` header-validation pattern in your own FastAPI service.

### Setup Dynamic Agent Configuration#
    
    
    from fastapi import FastAPI, Header, HTTPException
    from fastapi.responses import StreamingResponse
    
    from ag2 import Agent
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    agent = Agent(
        name="assistant",
        prompt="You are a helpful assistant.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[get_account_data], 
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
        accept: str | None = Header(None),
        authorization: str | None = Header(None),
    ) -> StreamingResponse:
        if not authorization:
            raise HTTPException(status_code=401, detail="Unauthorized")
    
        token = authorization.replace("Bearer ", "")
        user_info = validate_your_token(token)  # the same helper as above
    
        return StreamingResponse(
            stream.dispatch(message, dependencies={"auth_user": user_info}, accept=accept),
            media_type=accept or "text/event-stream",
        )

### Access User in Agent#

The identity travels as a request-scoped dependency, so the same `Inject("auth_user")` tools shown above work unchanged here — nothing about a tool has to know whether the deployment is managed or self-hosted.

## Universal Authentication Pattern#

For backends that run in both cloud-hosted and self-hosted modes, use this pattern:
    
    
    def extract_user_from_auth_header(authorization: str | None) -> dict | None:
        if not authorization:
            return None
        token = authorization.replace("Bearer ", "")
        return validate_your_token(token)

Then:

  * Read `authorization` on `/chat`
  * Validate token before `stream.dispatch(...)`
  * Attach the user as a dependency (`dependencies={"auth_user": ...}`) for tool authorization
  * Deny unauthorized or out-of-scope access
  * Apply the same check to the capabilities `GET` route if you expose one (`stream.capabilities()`), so it does not describe your agent to anonymous callers



## Security Notes#

### LangGraph Platform#

  * **Token Validation** : Validate tokens on your AG2 `/chat` endpoint
  * **User Scoping** : Scope data access by authenticated user identity



### Self-hosted#

  * **Manual Validation** : Implement and maintain your own validation logic
  * **Header Forwarding** : Ensure your runtime forwards `authorization` to AG2



### General Best Practices#

  * **Permission Checks** : Enforce role-based checks in AG2 tools
  * **Transport Security** : Serve `/chat` over HTTPS
  * **Least Privilege** : Return only data needed for the current user/task



## Troubleshooting#

### Common Issues#

**Token not reaching backend** :

  * Ensure you're passing `authorization` in `properties`
  * Confirm your runtime forwards headers to AG2 `/chat`



**Invalid token format** :

  * Handle both raw tokens and `Bearer <token>` formats consistently



**Unexpected anonymous access** :

  * Verify `authorization` checks happen before calling `stream.dispatch(...)`



## Next Steps#

  * [Configure chat UI with AG2 backend ->](https://docs.copilotkit.ai/ag2/prebuilt-components)
  * [Learn about shared state ->](https://docs.copilotkit.ai/ag2/shared-state)
  * [Implement human-in-the-loop workflows ->](https://docs.copilotkit.ai/ag2/human-in-the-loop)



### On this page

OverviewHow It WorksFrontend SetupLangGraph Platform DeploymentSetup Authentication HandlerAccess User in AgentSelf-hosted DeploymentSetup Dynamic Agent ConfigurationAccess User in AgentUniversal Authentication PatternSecurity NotesLangGraph PlatformSelf-hostedGeneral Best PracticesTroubleshootingCommon IssuesNext Steps
