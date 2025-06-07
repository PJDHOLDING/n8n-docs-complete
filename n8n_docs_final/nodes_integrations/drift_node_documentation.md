# Drift node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.drift/

---

# Drift node

Use the Drift node to automate work in Drift, and integrate Drift with other applications. n8n has built-in support for a wide range of Drift features, including creating, updating, deleting, and getting contacts.

Credentials

Refer to [Drift credentials](../../credentials/drift/) for guidance on setting up authentication.

## Operations

- Contact
  - Create a contact
  - Get custom attributes
  - Delete a contact
  - Get a contact
  - Update a contact

## Templates and examples

[Browse Drift integration templates](https://n8n.io/integrations/drift/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
