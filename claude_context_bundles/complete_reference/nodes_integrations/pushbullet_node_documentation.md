# Pushbullet node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pushbullet/

---

# Pushbullet node

Use the Pushbullet node to automate work in Pushbullet, and integrate Pushbullet with other applications. n8n has built-in support for a wide range of Pushbullet features, including creating, updating, deleting, and getting a push.

Credentials

Refer to [Pushbullet credentials](../../credentials/pushbullet/) for guidance on setting up authentication.

## Operations

- Push
  - Create a push
  - Delete a push
  - Get all pushes
  - Update a push

## Templates and examples

[Browse Pushbullet integration templates](https://n8n.io/integrations/pushbullet/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
