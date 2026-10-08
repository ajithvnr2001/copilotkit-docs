---
url: https://docs.copilotkit.ai/ms-agent-dotnet/auth/
title: Authentication
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:52.150682+00:00
---

# Authentication

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/auth/

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

[Authentication](https://docs.copilotkit.ai/ms-agent-dotnet/auth)

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

Authentication

Agent capabilitiesMicrosoft Agent Framework

# Authentication

Secure your Microsoft Agent Framework agents with user authentication

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

Forward user authentication from your frontend to your AG-UI server:

  * **Frontend** : Pass tokens via `<CopilotKit headers={{ Authorization: token }}>`
  * **Backend** : Validate tokens using ASP.NET Core authentication middleware



## Frontend Setup#

Pass your authentication token via the `headers` prop:
    
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      headers={{
        Authorization: `Bearer ${userToken}`,
      }}
    >
      <YourApp />
    </CopilotKit>

## Backend Setup#

Configure authentication in your AG-UI server:

.NETPython

Program.cs
    
    
    using Microsoft.Agents.AI;
    using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;
    using Microsoft.AspNetCore.Authentication.JwtBearer;
    using OpenAI;
    using OpenAI.Chat;
    
    var builder = WebApplication.CreateBuilder(args);
    
    // Configure JWT authentication
    builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
        .AddJwtBearer(options =>
        {
            options.Authority = builder.Configuration["JwtAuthority"];
            options.Audience = builder.Configuration["JwtAudience"];
            options.TokenValidationParameters = new Microsoft.IdentityModel.Tokens.TokenValidationParameters
            {
                ValidateIssuer = true,
                ValidateAudience = true,
                ValidateLifetime = true,
                ValidateIssuerSigningKey = true
            };
        });
    
    builder.Services.AddAuthorization();
    builder.Services.AddAGUIServer();
    
    var app = builder.Build();
    
    app.UseAuthentication();
    app.UseAuthorization();
    
    // Create and map your agent
    string openAiApiKey = builder.Configuration["OPENAI_API_KEY"]
        ?? throw new InvalidOperationException("Set OPENAI_API_KEY");
    var openAI = new OpenAIClient(openAiApiKey);
    var agent = openAI.GetChatClient("gpt-5.4-mini")
        .AsAIAgent(name: "AGUIAssistant", instructions: "You are a helpful assistant.");
    
    app.MapAGUIServer("/", agent).RequireAuthorization();
    
    await app.RunAsync();

agent/src/main.py (excerpt)
    
    
    from __future__ import annotations
    import os
    from fastapi import FastAPI, HTTPException, Request, status
    from fastapi.middleware.cors import CORSMiddleware
    from agent_framework import SupportsChatGetResponse
    from agent_framework.openai import OpenAIChatClient
    from agent_framework.ag_ui import add_agent_framework_fastapi_endpoint
    from azure.identity import DefaultAzureCredential
    from agent import create_agent
    
    app = FastAPI(title="CopilotKit + Microsoft Agent Framework (Python)")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    REQUIRED_BEARER_TOKEN = os.getenv("AUTH_BEARER_TOKEN")
    
    @app.middleware("http")
    async def auth_middleware(request: Request, call_next):
        # Protect the AG-UI endpoint if a token is configured
        if REQUIRED_BEARER_TOKEN and request.url.path == "/":
            auth_header = request.headers.get("Authorization", "")
            if not auth_header.startswith("Bearer "):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
            token = auth_header.split(" ", 1)[1].strip()
            if token != REQUIRED_BEARER_TOKEN:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return await call_next(request)
    
    # Build a chat client (same pattern as the Quickstart)
    def _build_chat_client() -> SupportsChatGetResponse:
        if bool(os.getenv("AZURE_OPENAI_ENDPOINT")):
            deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-5.4-mini")
            azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
            return OpenAIChatClient(
                model=deployment_name,
                api_key=azure_api_key,
                credential=None if azure_api_key else DefaultAzureCredential(),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )
        if bool(os.getenv("OPENAI_API_KEY")):
            return OpenAIChatClient(
                model=os.getenv("OPENAI_CHAT_MODEL_ID", "gpt-5.4-mini"),
                api_key=os.getenv("OPENAI_API_KEY"),
            )
        raise RuntimeError("Set AZURE_OPENAI_ENDPOINT (uses az login unless AZURE_OPENAI_API_KEY is set) or OPENAI_API_KEY")
    
    chat_client = _build_chat_client()
    my_agent = create_agent(chat_client)
    add_agent_framework_fastapi_endpoint(app=app, agent=my_agent, path="/")

### Configuration#

Add settings to your server configuration:

.NETPython

appsettings.json
    
    
    {
      "JwtAuthority": "https://login.microsoftonline.com/{your-tenant-id}/v2.0",
      "JwtAudience": "api://{your-client-id}"
    }

Save the model key outside `appsettings.json`:
    
    
    dotnet user-secrets init
    dotnet user-secrets set OPENAI_API_KEY "<your-openai-api-key>"

agent/.env
    
    
    # Simple shared-secret example for demo purposes
    AUTH_BEARER_TOKEN=super-secret-demo-token

### CORS (if needed)#

If your frontend and backend are on different origins:

Program.cs
    
    
    builder.Services.AddCors(options =>
    {
        options.AddDefaultPolicy(policy =>
        {
            policy.WithOrigins("http://localhost:3000")
                  .AllowAnyHeader()
                  .AllowAnyMethod()
                  .AllowCredentials();
        });
    });
    
    // ...
    
    app.UseCors();
    app.UseAuthentication();
    app.UseAuthorization();

## Security Best Practices#

  * Validate tokens on every request
  * Scope data access to authenticated users
  * Implement role-based access control in your agents
  * Use HTTPS in production



Avoid shared-secret bearer tokens in production

Examples that validate a bearer token against a single shared secret (e.g., an environment variable) are for local demos only. For production, use proper authentication:

  * .NET: Validate JWTs with `Microsoft.AspNetCore.Authentication.JwtBearer` (as shown above), backed by your IdP (e.g., Entra ID).
  * Python: Use OAuth 2.0 / OpenID Connect JWT validation or an API gateway that validates tokens before requests reach your AG‑UI server.



## Troubleshooting#

**Token not reaching server** : Verify the `Authorization` header is set in `<CopilotKit>` and forwarded through any proxies.

**Invalid token** : Ensure the token includes the `Bearer ` prefix.

**CORS errors** : Configure CORS if frontend and backend are on different origins (see CORS section).

For more details, see [Microsoft's JWT authentication guide](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-jwt-bearer-authentication).

### On this page

OverviewFrontend SetupBackend SetupConfigurationCORS (if needed)Security Best PracticesTroubleshooting
