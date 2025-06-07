# Adalo node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.adalo/

---

# Adalo node

Use the Adalo node to automate work in Adalo, and integrate Adalo with other applications. n8n has built-in support for a wide range of Adalo features, including like creating, getting, updating and deleting databases, records, and collections.

Credentials

Refer to [Adalo credentials](../../credentials/adalo/) for guidance on setting up authentication.

## Operations

- Collection
  - Create
  - Delete
  - Get
  - Get Many
  - Update

## Templates and examples

[Browse Adalo integration templates](https://n8n.io/integrations/adalo/), or [search all templates](https://n8n.io/workflows/)

## Related resources

Refer to [Adalo's documentation](https://help.adalo.com/) for more information on using Adalo. Their [External Collections with APIs](https://help.adalo.com/integrations/external-collections-with-apis) page gives more detail about what you can do with Adalo collections.

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
