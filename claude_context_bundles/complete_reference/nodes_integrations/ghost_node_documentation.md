# Ghost node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/

---

# Ghost node

Use the Ghost node to automate work in Ghost, and integrate Ghost with other applications. n8n has built-in support for a wide range of Ghost features, including creating, updating, deleting, and getting posts for the Admin and content API.

Credentials

Refer to [Ghost credentials](../../credentials/ghost/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations

### Admin API

- **Post**
  - Create a post
  - Delete a post
  - Get a post
  - Get all posts
  - Update a post

### Content API

- **Post**
  - Get a post
  - Get all posts

## Templates and examples

**Multi-Agent PDF-to-Blog Content Generation**

by Derek Cheung

[View template details](https://n8n.io/workflows/2457-multi-agent-pdf-to-blog-content-generation/)

**📄🌐PDF2Blog - Create Blog Post on Ghost CRM from PDF Document**

by Joseph LePage

[View template details](https://n8n.io/workflows/2522-pdf2blog-create-blog-post-on-ghost-crm-from-pdf-document/)

**Research AI Agent Team with auto citations using OpenRouter and Perplexity**

by Derek Cheung

[View template details](https://n8n.io/workflows/2607-research-ai-agent-team-with-auto-citations-using-openrouter-and-perplexity/)

[Browse Ghost integration templates](https://n8n.io/integrations/ghost/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
