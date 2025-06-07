# Dropcontact node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropcontact/

---

# Dropcontact node

Use the Dropcontact node to automate work in Dropcontact, and integrate Dropcontact with other applications. n8n has built-in support for a wide range of Dropcontact features, including fetching contacts.

Credentials

Refer to [Dropcontact credentials](../../credentials/dropcontact/) for guidance on setting up authentication.

## Operations

**Contact**
- Enrich
- Fetch Request

## Templates and examples

**Create HubSpot contacts from LinkedIn post interactions**

by Pauline

[View template details](https://n8n.io/workflows/1323-create-hubspot-contacts-from-linkedin-post-interactions/)

**Enrich up to 1500 emails per hour with Dropcontact batch requests**

by victor de coster

[View template details](https://n8n.io/workflows/2272-enrich-up-to-1500-emails-per-hour-with-dropcontact-batch-requests/)

**Enrich Google Sheet contacts with Dropcontact**

by Pauline

[View template details](https://n8n.io/workflows/1304-enrich-google-sheet-contacts-with-dropcontact/)

[Browse Dropcontact integration templates](https://n8n.io/integrations/dropcontact/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
