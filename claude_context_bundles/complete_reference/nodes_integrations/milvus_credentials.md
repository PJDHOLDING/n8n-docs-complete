# Milvus credentials

**Source:** https://docs.n8n.io/integrations/builtin/credentials/milvus/

---

# Milvus credentials

You can use these credentials to authenticate the following nodes:

- [Milvus Vector Store](../../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus/)

## Prerequisites

Create and run an [Milvus](https://milvus.io/) instance. Refer to the [Install Milvus](https://milvus.io/docs/install-overview.md) for more information.

## Supported authentication methods

- Basic auth

## Related resources

Refer to [Milvus's Authentication documentation](https://milvus.io/docs/authenticate.md?tab=docker#Authenticate-User-Access) for more information about setting up authentication.

View n8n's [Advanced AI](../../../../advanced-ai/) documentation.

## Using basic auth

To configure this credential, you'll need:

- **Base URL**: The base URL of your Milvus instance. The default is `http://localhost:19530`.
- **Username**: The username to authenticate to your Milvus instance. The default value is `root`.
- **Password**: The password to authenticate to your Milvus instance. The default value is `Milvus`.
