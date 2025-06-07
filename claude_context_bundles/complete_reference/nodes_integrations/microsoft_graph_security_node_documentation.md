# Microsoft Graph Security node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity/

---

# Microsoft Graph Security node

Use the Microsoft Graph Security node to automate work in Microsoft Graph Security, and integrate Microsoft Graph Security with other applications. n8n has built-in support for a wide range of Microsoft Graph Security features, including getting, and updating scores, and profiles.

Credentials

Refer to [Microsoft credentials](../../credentials/microsoft/) for guidance on setting up authentication.

## Operations

- Secure Score
  - Get
  - Get All
- Secure Score Control Profile
  - Get
  - Get All
  - Update

## Templates and examples

[Browse Microsoft Graph Security integration templates](https://n8n.io/integrations/microsoft-graph-security/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
