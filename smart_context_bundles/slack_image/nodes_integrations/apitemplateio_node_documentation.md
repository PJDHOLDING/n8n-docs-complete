# APITemplate.io node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.apitemplateio/

---

# APITemplate.io node

Use the APITemplate.io node to automate work in APITemplate.io, and integrate APITemplate.io with other applications. n8n has built-in support for a wide range of APITemplate.io features, including getting and creating accounts and PDF.

Credentials

Refer to [APITemplate.io credentials](../../credentials/apitemplateio/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations

- Account
  - Get
- Image
  - Create
- PDF
  - Create

## Templates and examples

**Create an invoice based on the Typeform submission**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/989-create-an-invoice-based-on-the-typeform-submission/)

**🤖 AI content generation for Auto Service 🚘 Automate your social media📲!**

by N8ner

[View template details](https://n8n.io/workflows/4600-ai-content-generation-for-auto-service-automate-your-social-media/)

**Generate Dynamic Images with Text & Templates using ImageKit.**

by Ahmed Alnaqa

[View template details](https://n8n.io/workflows/3519-generate-dynamic-images-with-text-and-templates-using-imagekit/)

[Browse APITemplate.io integration templates](https://n8n.io/integrations/apitemplateio/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
