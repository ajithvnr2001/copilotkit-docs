---
url: https://docs.copilotkit.ai/langgraph-python/build-with-agents/
title: Build with agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:07:31.616961+00:00
---

# Build with agents

> Source: https://docs.copilotkit.ai/langgraph-python/build-with-agents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Build with agents

# Build with agents

Give your AI coding agent up-to-date knowledge of CopilotKit's APIs, patterns, and best practices.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

AI coding agents may not have up-to-date knowledge of CopilotKit's APIs, patterns, and best practices. The resources on this page give them accurate, current knowledge directly in their context.

## CopilotKit Skills#

Skills are folders of instructions that coding agents discover and use automatically. The CopilotKit skills are deliberately thin: rather than restating the API, they teach your agent to look the current answer up — in these docs, in the source, and in the CLI. A copy of an API goes stale; a search does not.

Skills are the recommended way to give your agent CopilotKit knowledge. They work natively in Claude Code, Cursor, Codex, Gemini CLI, and any tool supporting the [agentskills.io](https://agentskills.io) standard.

There are two:

Skill| Use it to  
---|---  
`copilotkit`| Answer any CopilotKit question from current docs and source. It fetches the docs as Markdown, and uses the `copilotkit-docs` MCP server when the plugin provides it  
`copilotkit-cli`| Drive the CLI — scaffold a project, connect Intelligence, and prove a project's wiring with `copilotkit verify` before debugging by hand  
  
You don't need to pick between them — your agent loads whichever fits the task. The [skills directory](https://github.com/CopilotKit/CopilotKit/tree/main/skills) also holds a few procedure skills, such as setting up a Slack Channel, which walk through steps that span several systems.

### Install the skills#

Run this from the root of the project you're building in:
    
    
    npx skills add CopilotKit/CopilotKit/skills -y

This installs the skills into your project, where any coding agent working there (Claude Code, Codex, Cursor, or Gemini CLI) discovers them automatically. There's no per-agent configuration to do.

Want to choose what gets installed? Run `npx skills add CopilotKit/CopilotKit/skills` without `-y` to pick specific skills, target agents, and scope interactively — or add `-g` to install globally for every project.

### Start building#

Open a new agent session and use a starter prompt to put the skills to work:
    
    
    Help me add CopilotKit to this app. Look up the current setup in the CopilotKit docs first.

Your agent searches the documentation rather than working from memory, and reaches for `copilotkit verify` when something doesn't work.

## MCP Docs Server#

The CopilotKit MCP server equips AI coding agents with deep knowledge about CopilotKit's APIs, patterns, and best practices. When connected to your development environment, it enables AI assistants to:

  * Provide expert guidance
  * Generate accurate code
  * Give your AI agents a user interface
  * Help you implement CopilotKit features correctly



### Cursor#

[Cursor](https://cursor.sh/) is an AI-powered code editor built for productivity. It features built-in AI assistance and supports MCP for extending AI capabilities with external tools.

### Open MCP Settings in Cursor#

  1. Press `Shift+Command+J` (Mac) or `Shift+Ctrl+J` (Windows/Linux) to open Cursor's settings.
  2. Look for "MCP Tools" in the left sidebar categories.
  3. Click "Add Custom MCP". This will open the mcp.json file in the editor, which you need to edit.



This screen opens the global `~/.cursor/mcp.json`, which registers the server for every project you open. To register it for this project alone, create `.cursor/mcp.json` at the project root instead and put the same configuration there.

### Add MCP Server to Cursor#

Copy CopilotKit MCP's configuration and paste it under the mcpServers key in the mcp.json file.

HTTPSSE
    
    
    {
      "mcpServers": {
        "CopilotKit MCP": {
          "command": "npx",
          "args": [
            "-y",
            "mcp-remote",
            "https://mcp.copilotkit.ai/mcp"
          ]
        }
      }
    }
    
    
    {
      "mcpServers": {
        "CopilotKit MCP": {
          "url": "https://mcp.copilotkit.ai/sse"
        }
      }
    }

### Claude Web#

[Claude](https://claude.ai/) is Anthropic's AI assistant accessible through a web interface. It supports MCP integrations, called Connectors, to connect with external tools and services.

Navigate to the [Connectors](https://claude.ai/settings/connectors) settings page in Claude. 1. Click on your user in the bottom left of the chat box and then select "Settings" from the menu options that appear. 2. In the menu along the left side of the Settings page, select "Connectors"

Click "Add custom connector"

  1. In the Name field, enter a memorable name for the CopilotKit connector, like `CopilotKit` 2\. In the URL field, enter the following: ` https://mcp.copilotkit.ai/sse`



Click "Add"

### Claude Desktop#

[Claude Desktop](https://claude.ai/download) is the desktop application version of Claude, offering the same AI capabilities with local system integration and MCP support.

These steps are the same as those for Claude Web, above. The only difference is that the Connectors link below navigates to the Connectors settings in the Claude desktop app, instead of the Claude web app.

Navigate to the [Connectors](claude://claude.ai/settings/connectors) settings page in Claude. 1. Click on your user in the bottom left of the chat box and then select "Settings" from the menu options that appear. 2. In the menu along the left side of the Settings page, select "Connectors"

Click "Add custom connector"

  1. In the Name field, enter a memorable name for the CopilotKit connector, like `CopilotKit` 2\. In the URL field, enter the following: ` https://mcp.copilotkit.ai/sse`



Click "Add"

### Claude Code#

[Claude Code](https://docs.claude.com/en/docs/claude-code) is Anthropic's official CLI for Claude. It supports MCP integrations to connect with external tools and services, enhancing AI capabilities with specialized knowledge.

### Add MCP Server to Claude Code#

Use the Claude Code CLI to add the CopilotKit MCP server:
    
    
    claude mcp add --transport sse copilotkit-mcp https://mcp.copilotkit.ai/sse --scope project

**Expected Output:**
    
    
     Added SSE MCP server copilotkit-mcp with URL: https://mcp.copilotkit.ai/sse to project config
    File modified: /path/to/your/project/.mcp.json

`--scope project` writes `.mcp.json` at the root of your project, so the server is registered for everyone who checks the repository out. Without the flag the command falls back to `local` scope, which writes `~/.claude.json` in your home directory: that keeps the registration private to you, and it puts the change outside the project, which a coding agent running unattended is generally not permitted to do.

### Verify Connection#

Check that the server is properly connected:
    
    
    claude mcp list

**Expected Output:**
    
    
     Checking MCP server health...
    
    copilotkit-mcp: https://mcp.copilotkit.ai/sse (SSE) - ✓ Connected

💡 Server Name Requirements

Server names can only contain letters, numbers, hyphens, and underscores. Avoid spaces in server names.

### Using MCP Tools in Claude Code#

Once configured, the CopilotKit MCP server tools are automatically available when you interact with Claude Code for CopilotKit-related development tasks. The AI will intelligently use these tools when relevant to your queries.

**What the MCP Server Provides:**

  * Expert guidance for CopilotKit development
  * Accurate code generation for CopilotKit features
  * Best practices and implementation patterns
  * Deep understanding of CopilotKit APIs



**Management Commands:**
    
    
     # View server details
    claude mcp get copilotkit-mcp
    
    # Remove server if needed
    claude mcp remove copilotkit-mcp -s project

### Windsurf#

[Windsurf](https://codeium.com/windsurf) is Codeium's agentic IDE that combines AI-powered coding assistance with traditional development tools. It features the Cascade AI assistant with MCP integration.

### Access Windsurf MCP Settings#

  1. Open Windsurf Settings (click the settings button in the bottom right)
  2. Navigate to the "Cascade" section
  3. Look for "Model Context Protocol" or "MCP" settings
  4. Enable MCP support if not already enabled



### Add MCP Server to Windsurf#

You can add CopilotKit MCP in several ways:

Using the Built-in Server BrowserManual Configuration

  1. In the Cascade section, click "Add Server"
  2. Select "Add custom server"
  3. Choose the transport type: 
     * **SSE/HTTP** for remote servers
     * **stdio** for local command-based servers



Add the server configuration to your mcp_config.json file:

HTTP TransportSSE Transportstdio Transport (Local)
    
    
    {
      "mcpServers": {
        "CopilotKit MCP": {
          "url": "https://mcp.copilotkit.ai/mcp",
          "disabled": false,
          "timeout": 30
        }
      }
    }
    
    
    {
      "mcpServers": {
        "CopilotKit MCP": {
          "url": "https://mcp.copilotkit.ai/sse",
          "disabled": false,
          "timeout": 30
        }
      }
    }
    
    
    {
      "mcpServers": {
        "CopilotKit MCP": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://mcp.copilotkit.ai/mcp"]
        }
      }
    }

### Configuration File Location#

The MCP configuration is typically stored at:

macOSWindowsLinux
    
    
    ~/.codeium/windsurf/mcp_config.json
    
    
    %APPDATA%\.codeium\windsurf\mcp_config.json
    
    
    ~/.config/codeium/windsurf/mcp_config.json

### Using MCP Tools in Windsurf#

Once configured, CopilotKit MCP tools will be available in Windsurf's Cascade AI assistant:

  * Open the Cascade panel (AI chat interface)
  * The MCP tools are automatically available to the AI
  * You can reference specific tools using `@CopilotKit MCP` in your conversations
  * Windsurf will intelligently choose which tools to use based on your requests



### Managing Your MCP Servers#

In the Windsurf MCP settings, you can:

  * Enable/Disable individual servers
  * View server status and connection health
  * Configure tool permissions and auto-approval settings
  * Monitor server logs for debugging
  * Restart servers if they become unresponsive



The AI will seamlessly integrate CopilotKit MCP functionality into your development workflow!

### Cline#

[Cline](https://github.com/cline/cline) is a VS Code extension that provides autonomous AI coding assistance. It can perform complex tasks using MCP tools to interact with external systems.

### Open Cline MCP Settings#

  1. Open the Cline extension panel in VS Code
  2. Click the menu (⋮) in the top right corner of the Cline panel
  3. Select "MCP Servers" from the dropdown menu



This will open the MCP Servers interface where you can manage your server connections.

### Add MCP Server to Cline#

In the MCP Servers interface, you have three main options:

Remote Server SetupConfiguration File Setup

  1. Click on the "Remote Servers" tab
  2. Enter a Server Name (e.g., "CopilotKit MCP")
  3. Enter the Server URL:


    
    
    https://mcp.copilotkit.ai/sse

  4. Click "Add Server" to connect



Alternatively, you can configure via the advanced settings:

  1. In the "Installed" tab, click "Configure MCP Servers"
  2. Add the following configuration to your settings file:


    
    
    {
      "mcpServers": {
        "CopilotKit MCP": {
          "url": "https://mcp.copilotkit.ai/sse",
          "disabled": false,
          "timeout": 30
        }
      }
    }

### Using MCP Tools in Cline#

Once connected, Cline can automatically use the tools provided by CopilotKit MCP when you interact with the AI assistant. The MCP tools will be available without requiring manual selection - Cline's AI will intelligently choose which tools to use based on your requests.

**Server Status Indicators:**

  * Green dot: Connected and ready to use
  * Yellow dot: Connecting in progress
  * Red dot: Connection error



You can manage server settings, restart connections, or disable servers from the "Installed" tab in the MCP Servers interface.

### GitHub Copilot#

[GitHub Copilot](https://github.com/features/copilot) is Microsoft's AI pair programmer integrated into VS Code and other editors. It supports MCP to extend its capabilities with external tools and services.

### Enable MCP Support in VS Code#

  1. Open VS Code Settings (`Cmd+,` on Mac or `Ctrl+,` on Windows/Linux)
  2. Search for "MCP" in the settings search bar
  3. Enable the `chat.mcp.enabled` setting



### Add MCP Server to GitHub Copilot#

You can configure MCP servers for GitHub Copilot in several ways:

Workspace Configuration (Recommended)User Settings ConfigurationCommand Palette

Create a `.vscode/mcp.json` file in your project root:
    
    
    {
      "servers": {
        "CopilotKit MCP": {
          "url": "https://mcp.copilotkit.ai/sse"
        }
      }
    }

Add to your VS Code `settings.json`:
    
    
    {
      "mcp": {
        "servers": {
          "CopilotKit MCP": {
            "url": "https://mcp.copilotkit.ai/sse"
          }
        }
      }
    }

  1. Open the Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`)
  2. Type "MCP: Add Server" and select the command
  3. Choose "HTTP (sse)" as the server type
  4. Enter the server URL: `https://mcp.copilotkit.ai/sse`
  5. Provide a name for the server: `CopilotKit MCP`



### Using MCP Tools with GitHub Copilot#

  1. Open Copilot Chat in VS Code (click the Copilot icon in the activity bar)
  2. Switch to Agent mode from the chat dropdown menu
  3. Click the Tools (🔧) button to view available MCP tools
  4. Your CopilotKit MCP tools will be listed and can be used automatically



GitHub Copilot will intelligently use the MCP tools when relevant to your queries. You can also reference tools directly using `#` followed by the tool name.

### Managing MCP Servers#

Use the "MCP: List Servers" command to view and manage your configured servers:

  * Start/Stop/Restart servers
  * View server logs for debugging
  * Browse available tools and resources



### Codex#

[Codex](https://developers.openai.com/codex/mcp) supports Streamable HTTP MCP servers directly.

### Add MCP Server to Codex#

Run this command:
    
    
    codex mcp add copilotkit --url https://mcp.copilotkit.ai/mcp

Alternatively, add this table to `~/.codex/config.toml`:

~/.codex/config.toml
    
    
    [mcp_servers.copilotkit]
    url = "https://mcp.copilotkit.ai/mcp"

If you used the previous `mcp-remote` configuration, replace its `command` and `args` entries with `url`. Use `/mcp` for Streamable HTTP. The root URL (`https://mcp.copilotkit.ai`) returns 404.

### Verify Connection#

List the configured MCP servers:
    
    
    codex mcp list

This command verifies registration only. Start a new Codex session and run `/mcp` to check the connection and available tools.

Ask Codex to test a documentation search:
    
    
    Use CopilotKit's search-docs tool to find documentation for useFrontendTool.

A successful tool call returns documentation results. If the server fails to connect, verify that its URL ends with `/mcp`.

### Other#

For MCP-compatible applications not listed above, use these universal integration patterns. MCP (Model Context Protocol) is an open standard that allows AI applications to connect with external tools and data sources.

#### Connection Methods

Most MCP-compatible applications support one or both of these connection methods:

SSEstdio

For web-based or remote integrations:
    
    
    https://mcp.copilotkit.ai/sse

For local command-line integrations:
    
    
    {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.copilotkit.ai/mcp"]
    }

#### Integration Steps

  1. **Find MCP Settings** \- Look for "MCP," "Model Context Protocol," or "Tools" in your application settings
  2. **Add Server** \- Use the SSE URL: `https://mcp.copilotkit.ai/sse`
  3. **Test Connection** \- Restart your application and verify the server appears in available tools



#### Common Configuration Patterns

JSON Configuration FileApplication Settings

Many applications use a configuration file (locations vary by app):
    
    
    {
      "servers": {
        "CopilotKit MCP": {
          "url": "https://mcp.copilotkit.ai/sse"
        }
      }
    }

Some apps integrate MCP into their main settings:
    
    
    {
      "mcp": {
        "enabled": true,
        "servers": {
          "CopilotKit MCP": {
            "url": "https://mcp.copilotkit.ai/sse"
          }
        }
      }
    }

### On this page

CopilotKit SkillsMCP Docs ServerCursorClaude WebClaude DesktopClaude CodeWindsurfClineGitHub CopilotCodexOther
