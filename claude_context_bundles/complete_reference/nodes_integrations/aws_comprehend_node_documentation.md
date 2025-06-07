# AWS Comprehend node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend/

---

# AWS Comprehend node

Use the AWS Comprehend node to automate work in AWS Comprehend, and integrate AWS Comprehend with other applications. n8n has built-in support for a wide range of AWS Comprehend features, including identifying and analyzing texts.

Credentials

Refer to [AWS Comprehend credentials](../../credentials/aws/) for guidance on setting up authentication.

## Operations

**Text**

- Identify the dominant language
- Analyse the sentiment of the text

## Templates and examples

[Browse AWS Comprehend integration templates](https://n8n.io/integrations/aws-comprehend/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
