# Google Cloud Natural Language node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage/

---

# Google Cloud Natural Language node

Use the Google Cloud Natural Language node to automate work in Google Cloud Natural Language, and integrate Google Cloud Natural Language with other applications. n8n has built-in support for a wide range of Google Cloud Natural Language features, including analyzing documents.

Credentials

Refer to [Google Cloud Natural Language credentials](../../credentials/google/) for guidance on setting up authentication.

## Operations

- Document
  - Analyze Sentiment

## Templates and examples

**ETL pipeline for text processing**

by Lorena

[View template details](https://n8n.io/workflows/1045-etl-pipeline-for-text-processing/)

**Automate testimonials in Strapi with n8n**

by Tom

[View template details](https://n8n.io/workflows/1535-automate-testimonials-in-strapi-with-n8n/)

**Add positive feedback messages to a table in Notion**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/1109-add-positive-feedback-messages-to-a-table-in-notion/)

[Browse Google Cloud Natural Language integration templates](https://n8n.io/integrations/google-cloud-natural-language/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
