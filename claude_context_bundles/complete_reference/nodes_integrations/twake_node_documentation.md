# Twake node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twake/

---

# Twake node

Use the Twake node to automate work in Twake, and integrate Twake with other applications. n8n supports sending messages with Twake.

Credentials

Refer to [Twake credentials](../../credentials/twake/) for guidance on setting up authentication.

## Operations

- Message
  - Send a message

## Templates and examples

[Browse Twake integration templates](https://n8n.io/integrations/twake/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
