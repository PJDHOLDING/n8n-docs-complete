# AWS SNS node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awssns/

---

# AWS SNS node

Use the AWS SNS node to automate work in AWS SNS, and integrate AWS SNS with other applications. n8n has built-in support for a wide range of AWS SNS features, including publishing messages.

Credentials

Refer to [AWS SNS credentials](../../credentials/aws/) for guidance on setting up authentication.

## Operations

- Publish a message to a topic

## Templates and examples

[Browse AWS SNS integration templates](https://n8n.io/integrations/aws-sns/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
