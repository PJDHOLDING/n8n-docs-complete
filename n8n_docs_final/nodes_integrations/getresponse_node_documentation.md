# GetResponse node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.getresponse/

---

# GetResponse node

Use the GetResponse node to automate work in GetResponse, and integrate GetResponse with other applications. n8n has built-in support for a wide range of GetResponse features, including creating, updating, deleting, and getting contacts.

Credentials

Refer to [GetResponse credentials](../../credentials/getresponse/) for guidance on setting up authentication.

## Operations

- Contact
  - Create a new contact
  - Delete a contact
  - Get a contact
  - Get all contacts
  - Update contact properties

## Templates and examples

[Browse GetResponse integration templates](https://n8n.io/integrations/getresponse/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
