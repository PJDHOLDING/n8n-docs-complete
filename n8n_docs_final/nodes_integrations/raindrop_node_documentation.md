# Raindrop node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.raindrop/

---

# Raindrop node

Use the Raindrop node to automate work in Raindrop, and integrate Raindrop with other applications. n8n has built-in support for a wide range of Raindrop features, including getting users, deleting tags, and creating, updating, deleting and getting collections and bookmarks.

Credentials

Refer to [Raindrop credentials](../../credentials/raindrop/) for guidance on setting up authentication.

## Operations

- Bookmark
  - Create
  - Delete
  - Get
  - Get All
  - Update
- Collection
  - Create
  - Delete
  - Get
  - Get All
  - Update
- Tag
  - Delete
  - Get All
- User
  - Get

## Templates and examples

[Browse Raindrop integration templates](https://n8n.io/integrations/raindrop/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
