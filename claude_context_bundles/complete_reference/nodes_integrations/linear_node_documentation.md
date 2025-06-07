# Linear node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linear/

---

# Linear node

Use the Linear node to automate work in Linear, and integrate Linear with other applications. n8n has built-in support for a wide range of Linear features, including creating, updating, deleting, and getting issues.

Credentials

Refer to [Linear credentials](../../credentials/linear/) for guidance on setting up authentication.

## Operations

- Issue
  - Create
  - Delete
  - Get
  - Get All
  - Update

## Templates and examples

**Customer Support Channel and Ticketing System with Slack and Linear**

by Jimleuk

[View template details](https://n8n.io/workflows/2323-customer-support-channel-and-ticketing-system-with-slack-and-linear/)

**Visual Regression Testing with Apify and AI Vision Model**

by Jimleuk

[View template details](https://n8n.io/workflows/2419-visual-regression-testing-with-apify-and-ai-vision-model/)

**Send alert when data is created in app/database**

by n8n Team

[View template details](https://n8n.io/workflows/1932-send-alert-when-data-is-created-in-appdatabase/)

[Browse Linear integration templates](https://n8n.io/integrations/linear/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
