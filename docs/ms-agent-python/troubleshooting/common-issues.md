---
url: https://docs.copilotkit.ai/ms-agent-python/troubleshooting/common-issues/
title: Common Copilot Issues
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:45.012122+00:00
---

# Common Copilot Issues

> Source: https://docs.copilotkit.ai/ms-agent-python/troubleshooting/common-issues/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

Troubleshooting Copilots

[Migrate to V2](https://docs.copilotkit.ai/ms-agent-python/troubleshooting/migrate-to-v2)[Common Copilot Issues](https://docs.copilotkit.ai/ms-agent-python/troubleshooting/common-issues)

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Common Copilot Issues

OtherTroubleshootingTroubleshooting Copilots

# Common Copilot Issues

Common issues you may encounter when using Copilots.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Welcome to the CopilotKit Troubleshooting Guide! Here, you can find answers to common issues

Have an issue not listed here? Open a ticket on [GitHub](https://github.com/CopilotKit/CopilotKit/issues) or reach out on [Discord](https://discord.com/invite/6dffbvGU3D) and we'll be happy to help.

We also highly encourage any open-source contributors that want to add their own troubleshooting issues to [GitHub as a pull request](https://github.com/CopilotKit/CopilotKit/blob/main/CONTRIBUTING.md).

## I am getting network errors / API not found error#

If you're encountering network or API errors, here's how to troubleshoot:

Check your endpoint configuration

Verify your endpoint configuration in your CopilotKit setup:
    
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
    >
      {/* Your app */}
    </CopilotKit>

or, if using CopilotCloud
    
    
    <CopilotKit
        publicApiKey="<your-copilot-cloud-public-api-key>"
    >
        {/* Your app */}
    </CopilotKit>

Common issues:

  * Missing leading slash in endpoint path
  * Incorrect path relative to your app's base URL, or, if using absolute paths, incorrect full URL
  * Typos in the endpoint path


  * If using CopilotCloud, make sure to omit the `runtimeUrl` property and provide a valid API key



localhost vs 127.0.0.1

If you're running locally and getting connection errors, try using `127.0.0.1` instead of `localhost`:
    
    
    # If this doesn't work:
    http://localhost:3000/api/copilotkit
    
    # Try this instead:
    http://127.0.0.1:3000/api/copilotkit

This is often due to local DNS resolution issues in `/etc/hosts` or network configuration.

Verify your backend is running

Make sure your backend server is:

  * Running on the expected port
  * Accessible from your frontend
  * Not blocked by CORS or firewalls



Check the [quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart) to see how to set it up

## I am getting "CopilotKit's Remote Endpoint" not found error#

If you're getting a "CopilotKit's Remote Endpoint not found" error, it usually means the server serving `/info` endpoint isn't accessible. Here's how to fix it:

Check your FastAPI setup (if using python's FastAPI)

Make sure your FastAPI app has the CopilotKitSDK properly set up.  
Refer to [Remote Python Endpoint](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint) to see how to set it up

Test your endpoint

The `/info` endpoint should return agent or action information. Test it directly:
    
    
    curl -v -d '{}' http://localhost:8000/copilotkit/info

The response looks something like this:
    
    
    * Host localhost:8000 was resolved.
    * IPv6: ::1
    * IPv4: 127.0.0.1
    *   Trying [::1]:8000...
    * connect to ::1 port 8000 from ::1 port 55049 failed: Connection refused
    *   Trying 127.0.0.1:8000...
    * Connected to localhost (127.0.0.1) port 8000
    > POST /copilotkit/info HTTP/1.1
    > Host: localhost:8000
    > User-Agent: curl/8.7.1
    > Accept: */*
    > Content-Length: 2
    > Content-Type: application/x-www-form-urlencoded
    >
    * upload completely sent off: 2 bytes
    < HTTP/1.1 200 OK
    < date: Thu, 16 Jan 2025 17:45:05 GMT
    < server: uvicorn
    < content-length: 214
    < content-type: application/json
    <
    * Connection #0 to host localhost left intact
    {"actions":[],"agents":[{"name":"my_agent","description":"A helpful agent.","type":"langgraph"},],"sdkVersion":"0.1.32"}%

As you can see, it's a JSON response with your registered agents and actions, as well as the `200 OK` HTTP response status. If you see a different response, check your FastAPI logs for errors.

## Connection issues with tunnel creation#

If you notice the tunnel creation process spinning indefinitely, your router or ISP might be blocking the connection to CopilotKit's tunnel service.

Router or ISP blocking tunnel connections

To verify connectivity to the tunnel service, try these commands:
    
    
    ping tunnels.devcopilotkit.com
    curl -I https://tunnels.devcopilotkit.com
    telnet tunnels.devcopilotkit.com 443

If these fail, your router's security features or ISP might be blocking the connection. Common solutions:

  * Check router security settings
  * Contact your ISP to verify if they're blocking the connection
  * Try a different network to confirm the issue



### On this page

I am getting network errors / API not found errorI am getting "CopilotKit's Remote Endpoint" not found errorConnection issues with tunnel creation
