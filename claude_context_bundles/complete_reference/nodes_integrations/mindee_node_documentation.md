# Mindee node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mindee/

---

# Mindee node

Use the Mindee node to automate work in Mindee, and integrate Mindee with other applications. n8n has built-in support for a wide range of Mindee features, including predicting invoices.

Credentials

Refer to [Mindee credentials](../../credentials/mindee/) for guidance on setting up authentication.

## Operations

- **Invoice**
  - Predict
- **Receipt**
  - Predict

## Templates and examples

**Extract expenses from emails and add to Google Sheets**

by Jonathan

[View template details](https://n8n.io/workflows/1466-extract-expenses-from-emails-and-add-to-google-sheets/)

**Notify on new emails with invoices in Slack**

by Jonathan

[View template details](https://n8n.io/workflows/1467-notify-on-new-emails-with-invoices-in-slack/)

**Extract information from an image of a receipt**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/702-extract-information-from-an-image-of-a-receipt/)

[Browse Mindee integration templates](https://n8n.io/integrations/mindee/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
