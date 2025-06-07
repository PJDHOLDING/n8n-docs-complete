# Beeminder node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.beeminder/

---

# Beeminder node

Use the Beeminder node to automate work in Beeminder, and integrate Beeminder with other applications. n8n has built-in support for a wide range of Beeminder features, including creating, deleting, and updating data points.

Credentials

Refer to [Beeminder credentials](../../credentials/beeminder/) for guidance on setting up authentication.

## Operations

**data point**
- Create data point for a goal
- Delete a data point
- Get all data points for a goal
- Update a data point

## Templates and examples

[Browse Beeminder integration templates](https://n8n.io/integrations/beeminder/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
