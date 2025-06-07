# Mailjet node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailjet/

---

# Mailjet node

Use the Mailjet node to automate work in Mailjet, and integrate Mailjet with other applications. n8n has built-in support for a wide range of Mailjet features, including sending emails, and SMS.

Credentials

Refer to [Mailjet credentials](../../credentials/mailjet/) for guidance on setting up authentication.

## Operations

- Email
  - Send an email
  - Send an email template
- SMS
  - Send an SMS

## Templates and examples

**Forward Netflix emails to multiple email addresses with GMail and Mailjet**

by Manuel

[View template details](https://n8n.io/workflows/2279-forward-netflix-emails-to-multiple-email-addresses-with-gmail-and-mailjet/)

**Send an email using Mailjet**

by amudhan

[View template details](https://n8n.io/workflows/520-send-an-email-using-mailjet/)

**Receive updates on emails sent via Mailjet**

by amudhan

[View template details](https://n8n.io/workflows/521-receive-updates-on-emails-sent-via-mailjet/)

[Browse Mailjet integration templates](https://n8n.io/integrations/mailjet/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
