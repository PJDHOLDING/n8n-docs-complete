# Specify user folder path

**Source:** https://docs.n8n.io/hosting/configuration/configuration-examples/user-folder/

---

# Specify user folder path

n8n saves user-specific data like the encryption key, SQLite database file, and
the ID of the tunnel (if used) in the subfolder `.n8n` of the user who started n8n. It's possible to overwrite the user-folder using an environment variable.

| ``` 1 ``` | ``` export N8N_USER_FOLDER=/home/jim/n8n  ``` |

Refer to [Environment variables reference](../../environment-variables/deployment/) for more information on this variable.
