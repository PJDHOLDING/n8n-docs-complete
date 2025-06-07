# Gotify credentials

**Source:** https://docs.n8n.io/integrations/builtin/credentials/gotify/

---

# Gotify credentials

You can use these credentials to authenticate the following nodes:

- [Gotify](../../app-nodes/n8n-nodes-base.gotify/)

## Prerequisites

Install [Gotify](https://gotify.net/docs/install) on your server.

## Supported authentication methods

- API token

## Related resources

Refer to [Gotify's API documentation](https://gotify.net/api-docs) for more information about the service.

## Using API token

To configure this credential, you'll need:

- An **App API Token**: Only required if you'll use this credential to create messages. To generate an App API token, create an application from the **Apps** menu. Refer to [Gotify's Push messages documentation](https://gotify.net/docs/pushmsg) for more information.
- A **Client API Token**: Required for all actions other than creating messages (such as deleting or retrieving messages). To generate a Client API token, create a client from the **Clients** menu.
- The **URL** of the Gotify host
