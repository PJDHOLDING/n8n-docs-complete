# SIGNL4 credentials

**Source:** https://docs.n8n.io/integrations/builtin/credentials/signl4/

---

# SIGNL4 credentials

You can use these credentials to authenticate the following nodes:

- [SIGNL4](../../app-nodes/n8n-nodes-base.signl4/)

## Prerequisites

Create a [SIGNL4](https://www.signl4.com/) account.

## Supported authentication methods

- Webhook secret

## Related resources

Refer to [SIGNL4's Inbound Webhook documentation](https://connect.signl4.com/webhook/docs/index.html) for more information about the service.

## Using webhook secret

To configure this credential, you'll need:

- A **Team Secret**: SIGNL4 includes this secret in the "✅ Sign up complete" email as the last part of the webhook URL. If your webhook URL is `https://connect.signl4.com/webhook/helloworld`, your team secret would be `helloworld`.
