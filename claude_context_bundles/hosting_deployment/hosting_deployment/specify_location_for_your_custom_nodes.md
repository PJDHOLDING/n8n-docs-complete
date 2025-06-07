# Specify location for your custom nodes

**Source:** https://docs.n8n.io/hosting/configuration/configuration-examples/custom-nodes-location/

---

# Specify location for your custom nodes

Every user can add custom nodes that get loaded by n8n on startup. The default
location is in the subfolder `.n8n/custom` of the user who started n8n.

You can define more folders with an environment variable:

| ``` 1 ``` | ``` export N8N_CUSTOM_EXTENSIONS="/home/jim/n8n/custom-nodes;/data/n8n/nodes"  ``` |

Refer to [Environment variables reference](../../environment-variables/nodes/) for more information on this variable.
