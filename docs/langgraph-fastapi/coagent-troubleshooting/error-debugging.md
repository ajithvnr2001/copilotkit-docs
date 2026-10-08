---
url: https://docs.copilotkit.ai/langgraph-fastapi/coagent-troubleshooting/error-debugging/
title: Error Debugging & Observability
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:39.377981+00:00
---

# Error Debugging & Observability

> Source: https://docs.copilotkit.ai/langgraph-fastapi/coagent-troubleshooting/error-debugging/

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

On this page

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)Coagent Troubleshooting

# Error Debugging & Observability

Learn how to debug errors in CopilotKit with dev console and set up error observability for monitoring services.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit provides comprehensive error handling capabilities to help you debug issues and monitor your application's behavior. Whether you're developing locally or running in production, CopilotKit offers tools to capture, understand, and resolve errors effectively.

## Quick Start#

### Local Development with Dev Console#

For local development, enable the dev console to see errors directly in your UI:
    
    
    export default function App() {
      return (
        <CopilotKit
          runtimeUrl="<your-runtime-url>"
          showDevConsole={true} 
        >
          {/* Your app */}
        </CopilotKit>
      );
    }

The dev console shows error banner directly in your UI, making it easy to spot issues during development. **No API key required** for this feature.

### Production Error Observability#

For production applications, use error observability hooks to send errors to monitoring services (requires `publicApiKey`):
    
    
    export default function App() {
      return (
        <CopilotKit
          runtimeUrl="<your-runtime-url>"
          publicApiKey="ck_pub_your_key"
          onError={(errorEvent) => {
            // Send to your monitoring service
            console.error("CopilotKit Error:", errorEvent);
    
            // Example: Send to analytics
            analytics.track("copilotkit_error", {
              type: errorEvent.type,
              source: errorEvent.context.source,
              timestamp: errorEvent.timestamp,
            });
          }} 
          showDevConsole={false} // Hide dev console in production
        >
          {/* Your app */}
        </CopilotKit>
      );
    }

**Need a publicApiKey?** Go to <https://dashboard.operations.copilotkit.ai> and get one for free!

## Error Handling Options#

### Dev Console (`showDevConsole`)#

The dev console provides immediate visual feedback during development:
    
    
    <CopilotKit runtimeUrl="<your-runtime-url>" showDevConsole={true}>
      {/* Your app */}
    </CopilotKit>

**Features:**

  * ✅ **No API key required** \- works with any setup
  * ✅ **Visual error banner** \- errors appear as banner in your UI
  * ✅ **Real-time feedback** \- see errors immediately as they occur
  * ✅ **Development-focused** \- detailed error information for debugging



**Best for:**

  * Local development
  * Testing and debugging
  * Understanding error flows



Set `showDevConsole={false}` in production to avoid showing error details to end users.

### Error Observability (`onError`)#

The error observability hooks provide programmatic access to detailed error information for monitoring and analytics:
    
    
    <CopilotKit
      publicApiKey="ck_pub_your_key"
      onError={(errorEvent: CopilotErrorEvent) => {
        // Send error data to monitoring services
        switch (errorEvent.type) {
          case "error":
            logToService("Critical error", errorEvent);
            break;
          case "request":
            logToService("Request started", errorEvent);
            break;
          case "response":
            logToService("Response received", errorEvent);
            break;
          case "agent_state":
            logToService("Agent state change", errorEvent);
            break;
        }
      }}
    >
      {/* Your app */}
    </CopilotKit>

**Features:**

  * ✅ **Rich error context** \- detailed information about what went wrong
  * ✅ **Request/response tracking** \- monitor the full conversation flow
  * ✅ **Agent state monitoring** \- track agent interactions and state changes
  * ✅ **Production-ready** \- structured data perfect for monitoring services



**Requirements:**

  * Requires `publicApiKey` from [Copilot Cloud](https://dashboard.operations.copilotkit.ai)
  * Part of CopilotKit's enterprise observability offering



**Note:** Basic error handling works without Cloud. The `onError` hook is specifically for **error observability** \- sending error data to monitoring services like Sentry, DataDog, etc.

## Error Event Structure#

The `onError` handler receives detailed error events with rich context:
    
    
    interface CopilotErrorEvent {
      type:
        | "error"
        | "request"
        | "response"
        | "agent_state"
        | "action"
        | "message"
        | "performance";
      timestamp: number;
      context: {
        source: "ui" | "runtime" | "agent";
        request?: {
          operation: string;
          method?: string;
          url?: string;
          startTime: number;
        };
        response?: {
          endTime: number;
          latency: number;
        };
        agent?: {
          name: string;
          nodeName?: string;
        };
        messages?: {
          input: any[];
          messageCount: number;
        };
        technical?: {
          environment: string;
          stackTrace?: string;
        };
      };
      error?: any; // Present for error events
    }

## Common Error Observability Patterns#

### Basic Error Logging#
    
    
    <CopilotKit
      publicApiKey="ck_pub_your_key"
      onError={(errorEvent) => {
        console.error("[CopilotKit Error]", {
          type: errorEvent.type,
          timestamp: new Date(errorEvent.timestamp).toISOString(),
          context: errorEvent.context,
          error: errorEvent.error,
        });
      }}
    >
      {/* Your app */}
    </CopilotKit>

### Integration with Monitoring Services#
    
    
    // Example with Sentry
    
    <CopilotKit
      publicApiKey="ck_pub_your_key"
      onError={(errorEvent) => {
        if (errorEvent.type === "error") {
          Sentry.captureException(errorEvent.error, {
            tags: {
              source: errorEvent.context.source,
              operation: errorEvent.context.request?.operation,
            },
            extra: {
              context: errorEvent.context,
              timestamp: errorEvent.timestamp,
            },
          });
        }
      }}
    >
      {/* Your app */}
    </CopilotKit>

### Custom Error Analytics#
    
    
    <CopilotKit
      publicApiKey="ck_pub_your_key"
      onError={(errorEvent) => {
        // Track different error types
        analytics.track("copilotkit_event", {
          event_type: errorEvent.type,
          source: errorEvent.context.source,
          agent_name: errorEvent.context.agent?.name,
          latency: errorEvent.context.response?.latency,
          error_message: errorEvent.error?.message,
          timestamp: errorEvent.timestamp,
        });
      }}
    >
      {/* Your app */}
    </CopilotKit>

## Development vs Production Setup#

### Development Environment#
    
    
    <CopilotKit
      runtimeUrl="http://localhost:3000/api/copilotkit"
      showDevConsole={true} // Show visual errors
      onError={(errorEvent) => {
        // Simple console logging for development
        console.log("CopilotKit Event:", errorEvent);
      }}
    >
      {/* Your app */}
    </CopilotKit>

### Production Environment#
    
    
    <CopilotKit
      runtimeUrl="https://your-app.com/api/copilotkit"
      publicApiKey={process.env.NEXT_PUBLIC_COPILOTKIT_API_KEY}
      showDevConsole={false} // Hide from users
      onError={(errorEvent) => {
        // Production error observability
        if (errorEvent.type === "error") {
          // Log critical errors
          logger.error("CopilotKit Error", {
            error: errorEvent.error,
            context: errorEvent.context,
            timestamp: errorEvent.timestamp,
          });
    
          // Send to monitoring service
          monitoring.captureError(errorEvent.error, {
            extra: errorEvent.context,
          });
        }
      }}
    >
      {/* Your app */}
    </CopilotKit>

## Getting Started with Copilot Cloud#

To use error observability hooks, you'll need a Copilot Cloud account:

  1. **Sign up for free** at <https://dashboard.operations.copilotkit.ai>
  2. **Get your public API key** from the dashboard
  3. **Add it to your environment variables** : 
         
         NEXT_PUBLIC_COPILOTKIT_API_KEY=ck_pub_your_key_here

  4. **Use it in your CopilotKit provider** : 
         
         <CopilotKit publicApiKey={process.env.NEXT_PUBLIC_COPILOTKIT_API_KEY}>
           {/* Your app */}
         </CopilotKit>




Copilot Cloud is free to get started and provides production-ready infrastructure for your AI copilots, including comprehensive error observability and monitoring capabilities.

## Best Practices#

### ✅ Do#

  * **Use`showDevConsole={true}` during development** for immediate feedback
  * **Set`showDevConsole={false}` in production** to hide errors from users
  * **Implement proper error observability** with the `onError` hook for monitoring
  * **Monitor error patterns** to identify and fix issues proactively
  * **Use structured logging** to make error analysis easier



### ❌ Don't#

  * **Don't expose detailed errors to end users** in production
  * **Don't ignore error events** \- they provide valuable debugging information
  * **Don't log sensitive data** in error observability hooks
  * **Don't block the UI** with error handling logic



## Troubleshooting#

### Error Observability Not Working#

If your `onError` hook isn't being called:

  1. **Check your publicApiKey** \- error observability requires a valid API key
  2. **Verify the key format** \- should start with `ck_pub_`
  3. **Ensure the key is set** \- check your environment variables
  4. **Test with dev console** \- use `showDevConsole={true}` to see if errors are occurring



### Dev Console Not Showing#

If the dev console isn't displaying errors:

  1. **Check showDevConsole setting** \- ensure it's set to `true`
  2. **Look for console errors** \- check browser dev tools for JavaScript errors
  3. **Verify error occurrence** \- make sure errors are actually happening



## Next Steps#

  * Learn about [Copilot Cloud features](https://dashboard.operations.copilotkit.ai)
  * Explore the [CopilotKit reference documentation](https://docs.copilotkit.ai/reference/v1/components/CopilotKit)
  * Check out [troubleshooting guides](https://docs.copilotkit.ai/langgraph-fastapi/troubleshooting/common-issues) for common issues



### On this page

Quick StartLocal Development with Dev ConsoleProduction Error ObservabilityError Handling OptionsDev Console (showDevConsole)Error Observability (onError)Error Event StructureCommon Error Observability PatternsBasic Error LoggingIntegration with Monitoring ServicesCustom Error AnalyticsDevelopment vs Production SetupDevelopment EnvironmentProduction EnvironmentGetting Started with Copilot CloudBest Practices✅ Do❌ Don'tTroubleshootingError Observability Not WorkingDev Console Not ShowingNext Steps
