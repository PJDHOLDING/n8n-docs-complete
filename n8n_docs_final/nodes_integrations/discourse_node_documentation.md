# Discourse node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discourse/

---

# Discourse node

Use the Discourse node to automate work in Discourse, and integrate Discourse with other applications. n8n has built-in support for a wide range of Discourse features, including creating, getting, updating, and removing categories, groups, posts, and users.

Credentials

Refer to [Discourse credentials](../../credentials/discourse/) for guidance on setting up authentication.

## Operations

- Category
  - Create a category
  - Get all categories
  - Update a category
- Group
  - Create a group
  - Get a group
  - Get all groups
  - Update a group
- Post
  - Create a post
  - Get a post
  - Get all posts
  - Update a post
- User
  - Create a user
  - Get a user
  - Get all users
- User Group
  - Create a user to group
  - Remove user from group

## Templates and examples

[Browse Discourse integration templates](https://n8n.io/integrations/discourse/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
