# Philips Hue node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.philipshue/

---

# Philips Hue node

Use the Philips Hue node to automate work in Philips Hue, and integrate Philips Hue with other applications. n8n has built-in support for a wide range of Philips Hue features, including deleting, retrieving, and updating lights.

Credentials

Refer to [Philips Hue credentials](../../credentials/philipshue/) for guidance on setting up authentication.

## Operations

- Light
  - Delete a light
  - Retrieve a light
  - Retrieve all lights
  - Update a light

## Templates and examples

[Browse Philips Hue integration templates](https://n8n.io/integrations/philips-hue/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
