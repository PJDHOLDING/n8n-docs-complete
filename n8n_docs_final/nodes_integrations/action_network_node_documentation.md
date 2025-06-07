# Action Network node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.actionnetwork/

---

# Action Network node

Use the Action Network node to automate work in Action Network, and integrate Action Network with other applications. n8n has built-in support for a wide range of Action Network features, including creating, updating, and deleting events, people, tags, and signatures.

Credentials

Refer to [Action Network credentials](../../credentials/actionnetwork/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations

- Attendance
  - Create
  - Get
  - Get All
- Event
  - Create
  - Get
  - Get All
- Person
  - Create
  - Get
  - Get All
  - Update
- Person Tag
  - Add
  - Remove
- Petition
  - Create
  - Get
  - Get All
  - Update
- Signature
  - Create
  - Get
  - Get All
  - Update
- Tag
  - Create
  - Get
  - Get All

## Templates and examples

[Browse Action Network integration templates](https://n8n.io/integrations/action-network/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
