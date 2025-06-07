# Microsoft To Do node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo/

---

# Microsoft To Do node

Use the Microsoft To Do node to automate work in Microsoft To Do, and integrate Microsoft To Do with other applications. n8n has built-in support for a wide range of Microsoft To Do features, including creating, updating, deleting, and getting linked resources, lists, and tasks.

Credentials

Refer to [Microsoft credentials](../../credentials/microsoft/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations

- Linked Resource
  - Create
  - Delete
  - Get
  - Get All
  - Update
- List
  - Create
  - Delete
  - Get
  - Get All
  - Update
- Task
  - Create
  - Delete
  - Get
  - Get All
  - Update

## Templates and examples

**📂 Automatically Update Stock Portfolio from OneDrive to Excel**

by Louis

[View template details](https://n8n.io/workflows/2507-automatically-update-stock-portfolio-from-onedrive-to-excel/)

**Create, update and get a task in Microsoft To Do**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/1114-create-update-and-get-a-task-in-microsoft-to-do/)

**Analyze Email Headers for IP Reputation and Spoofing Detection - Outlook**

by Angel Menendez

[View template details](https://n8n.io/workflows/2676-analyze-email-headers-for-ip-reputation-and-spoofing-detection-outlook/)

[Browse Microsoft To Do integration templates](https://n8n.io/integrations/microsoft-to-do/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
