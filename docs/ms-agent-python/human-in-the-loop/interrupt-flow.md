---
url: https://docs.copilotkit.ai/ms-agent-python/human-in-the-loop/interrupt-flow/
title: Interrupt-based
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:16.940027+00:00
---

# Interrupt-based

> Source: https://docs.copilotkit.ai/ms-agent-python/human-in-the-loop/interrupt-flow/

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)[Human-in-the-Loop](https://docs.copilotkit.ai/ms-agent-python/human-in-the-loop)

# Interrupt-based

Gate a backend tool behind an approval that the agent raises itself, and render it with useInterrupt.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Microsoft Agent Framework can mark a backend tool as approval-gated. When the agent decides to call that tool, it does not run it. It ends the run with an AG-UI interrupt, which carries the pending tool call to your frontend. Your UI asks the user, and your answer resumes the agent.

The backend owns the decision, so the frontend does not register a tool with the same name as the backend tool. Any agent that raises AG-UI interrupts uses this same path.

## When should I use this?#

Use this when the action lives on the server and the approval is a property of that action:

  * Destructive or irreversible operations, such as deleting a record
  * Spending money, sending mail, or calling a third-party API
  * Anything where the approval rule must hold no matter which frontend is attached



Use [tool-based HITL](https://docs.copilotkit.ai/microsoft-agent-framework/human-in-the-loop/tool-based) instead when the work itself runs in the browser.

## Requirements#

Package| Version  
---|---  
`@copilotkit/react-core`| 1.61.2 or later  
`agent-framework-ag-ui` (Python)| 1.2.0 or later  
`AGUI.Server` (.NET)| 0.0.6 or later  
  
## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Mark the backend tool as approval-gated#

Nothing else about the tool changes. The framework holds the call and raises the approval for you.

.NETPython

agent/src/agent.py
    
    
    from agent_framework import tool
    
    @tool(
        name="delete_file",
        description="Delete a file",
        approval_mode="always_require", 
    )
    def delete_file(filename: str) -> str:
        return f"Deleted {filename}."

Program.cs
    
    
    // Wrap the function so the framework requests approval before it runs.
    var deleteFileTool = new ApprovalRequiredAIFunction( 
        AIFunctionFactory.Create(DeleteFile, "delete_file", "Deletes a file"));
    
    builder.Services.AddChatClient(/* ... */)
        .ConfigureOptions(options =>
        {
            options.Tools ??= [];
            options.Tools.Add(deleteFileTool);
        })
        .UseFunctionInvocation();

### Render the approval with `useInterrupt`#

`useInterrupt` receives every AG-UI interrupt the agent raises. Call `resolve` to approve and resume, or `cancel` to decline.

page.tsx
    
    
    import { useInterrupt } from "@copilotkit/react-core/v2"; 
    
    export function ApprovalPanel() {
      // renderInChat: false makes useInterrupt return the element, so render it yourself.
      const approval = useInterrupt({
        renderInChat: false,
        render: ({ interrupt, resolve, cancel }) => {
          if (!interrupt) return <></>;
          return (
            <div>
              <p>{interrupt.message}</p>
              <button onClick={() => resolve({ approved: true })}>Approve</button>
              <button onClick={() => cancel()}>Deny</button>
            </div>
          );
        },
      });
    
      return <div>{approval}</div>;
    }

`renderInChat` defaults to `true`, which draws your UI inside the chat. If no `<CopilotChat />` is mounted, nothing appears and there is no warning. Pass `renderInChat: false`, as above, and place the returned element yourself.

### Give it a try!#

Ask the agent to delete a file. The run stops, your approval UI appears, and the tool only runs after you approve.

## What the interrupt contains#

An approval-gated call arrives with `reason` set to `"tool_call"`. These fields are the same for both backends:

Field| Description  
---|---  
`id`| The interrupt's identity. Pass it to `resolve` or `cancel` when several are open.  
`reason`| `"tool_call"` for an approval-gated call.  
`message`| A human-readable summary, such as `Approve running delete_file?`  
`toolCallId`| The pending call's id. It matches the `TOOL_CALL_START` event both backends emit, so you can correlate the two.  
`responseSchema`| JSON Schema for the payload the agent expects. Both backends ask for a boolean `approved`.  
  
The Python adapter also puts the whole request under `interrupt.metadata.agent_framework.function_call`, which gives you the tool `name` and its `arguments`. The .NET server does not send that field, so read the tool name from `message` if you support both.

## Approving, denying, and cancelling#

`cancel()` and `resolve({ approved: false })` both leave the tool unrun, but they end the turn differently:

  * `resolve({ approved: true })` resumes the agent and the tool runs.
  * `resolve({ approved: false })` hands the refusal to the agent, which continues and can reply to the user.
  * `cancel()` ends the run immediately.



Do not register a frontend tool with the same name as a backend tool. Tool names must be unique across both, and a collision fails the run with `Duplicate tool name`.

### On this page

What is this?When should I use this?RequirementsImplementationWhat the interrupt containsApproving, denying, and cancelling
