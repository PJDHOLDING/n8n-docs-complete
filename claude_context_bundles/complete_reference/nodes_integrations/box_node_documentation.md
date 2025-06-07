# Box node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.box/

---

# Box node

Use the Box node to automate work in Box, and integrate Box with other applications. n8n has built-in support for a wide range of Box features, including creating, copying, deleting, searching, uploading, and downloading files and folders.

Credentials

Refer to [Box credentials](../../credentials/box/) for guidance on setting up authentication.

## Operations

- File
  - Copy a file
  - Delete a file
  - Download a file
  - Get a file
  - Search files
  - Share a file
  - Upload a file
- Folder
  - Create a folder
  - Get a folder
  - Delete a folder
  - Search files
  - Share a folder
  - Update folder

## Templates and examples

[Browse Box integration templates](https://n8n.io/integrations/box/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
