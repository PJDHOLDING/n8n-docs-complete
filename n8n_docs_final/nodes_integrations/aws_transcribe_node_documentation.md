# AWS Transcribe node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awstranscribe/

---

# AWS Transcribe node

Use the AWS Transcribe node to automate work in AWS Transcribe, and integrate AWS Transcribe with other applications. n8n has built-in support for a wide range of AWS Transcribe features, including creating, deleting, and getting transcription jobs.

Credentials

Refer to [AWS Transcribe credentials](../../credentials/aws/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations

**Transcription Job**

- Create a transcription job
- Delete a transcription job
- Get a transcription job
- Get all transcriptions job

## Templates and examples

[Browse AWS Transcribe integration templates](https://n8n.io/integrations/aws-transcribe/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
