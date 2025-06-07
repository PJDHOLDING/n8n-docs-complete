# Azure Cosmos DB node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb/

---

# Azure Cosmos DB node

Use the Azure Cosmos DB node to automate work in Azure Cosmos DB and integrate Azure Cosmos DB with other applications. n8n has built-in support for a wide range of Azure Cosmos DB features, which includes creating, getting, updating, and deleting containers and items.

Credentials

You can find authentication information for this node [here](../../credentials/azurecosmosdb/).

## Operations

- **Container**:
  - **Create**
  - **Delete**
  - **Get**
  - **Get Many**
- **Item**:
  - **Create**
  - **Delete**
  - **Get**
  - **Get Many**
  - **Execute Query**
  - **Update**

## Templates and examples

**Build Your Own Counseling Chatbot on LINE to Support Mental Health Conversations**

by lin@davoy.tech

[View template details](https://n8n.io/workflows/2975-build-your-own-counseling-chatbot-on-line-to-support-mental-health-conversations/)

**CallForge - 05 - Gong.io Call Analysis with Azure AI & CRM Sync**

by Angel Menendez

[View template details](https://n8n.io/workflows/3035-callforge-05-gongio-call-analysis-with-azure-ai-and-crm-sync/)

**Get Daily Exercise Plan with Flex Message via LINE**

by lin@davoy.tech

[View template details](https://n8n.io/workflows/2988-get-daily-exercise-plan-with-flex-message-via-line/)

[Browse Azure Cosmos DB integration templates](https://n8n.io/integrations/azure-cosmos-db/), or [search all templates](https://n8n.io/workflows/)

## Related resources

Refer to [Azure Cosmos DB's documentation](https://learn.microsoft.com/en-us/rest/api/cosmos-db/) for more information about the service.

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
