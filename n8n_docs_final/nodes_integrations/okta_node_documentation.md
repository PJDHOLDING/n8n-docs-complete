# Okta node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.okta/

---

# Okta node

Use the Okta node to automate work in Okta and integrate Okta with other applications. n8n has built-in support for a wide range of Okta features, which includes creating, updating, and deleting users.

Credentials

You can find authentication information for this node [here](../../credentials/okta/).

## Operations

- User
  - Create a new user
  - Delete an existing user
  - Get details of a user
  - Get many users
  - Update an existing user

## Templates and examples

[Browse Okta integration templates](https://n8n.io/integrations/{{ okta }}/), or [search all templates](https://n8n.io/workflows/)

## Related resources

Refer to [Okta's documentation](https://developer.okta.com/docs/guides/) for more information about the service.

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
