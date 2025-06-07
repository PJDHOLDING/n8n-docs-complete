# Brevo node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.brevo/

---

# Brevo node

Use the Brevo node to automate work in Brevo, and integrate Brevo with other applications. n8n has built-in support for a wide range of Brevo features, including creating, updating, deleting, and getting contacts, attributes, as well as sending emails.

Credentials

Refer to [Brevo credentials](../../credentials/brevo/) for guidance on setting up authentication.

## Operations

- Contact
  - Create
  - Create or Update
  - Delete
  - Get
  - Get All
  - Update
- Contact Attribute
  - Create
  - Delete
  - Get All
  - Update
- Email
  - Send
  - Send Template
- Sender
  - Create
  - Delete
  - Get All

## Templates and examples

**Smart Email Auto-Responder Template using AI**

by Amjid Ali

[View template details](https://n8n.io/workflows/3277-smart-email-auto-responder-template-using-ai/)

**Create Leads in SuiteCRM, synchronize with Brevo and notify in NextCloud**

by algopi.io

[View template details](https://n8n.io/workflows/2291-create-leads-in-suitecrm-synchronize-with-brevo-and-notify-in-nextcloud/)

**Automate B2B Lead Generation with Apollo, GPT-4o Scoring, and Brevo Email Outreach**

by Luka Zivkovic

[View template details](https://n8n.io/workflows/4539-automate-b2b-lead-generation-with-apollo-gpt-4o-scoring-and-brevo-email-outreach/)

[Browse Brevo integration templates](https://n8n.io/integrations/brevo/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
