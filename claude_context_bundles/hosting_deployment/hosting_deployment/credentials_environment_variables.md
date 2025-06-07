# Credentials environment variables

**Source:** https://docs.n8n.io/hosting/configuration/environment-variables/credentials/

---

# Credentials environment variables

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](../../configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

Enable credential overwrites using the following environment variables. Refer to [Credential overwrites](../../../../embed/configuration/#credential-overwrites) for details.

| Variable | Type | Default | Description |
| `CREDENTIALS_OVERWRITE_DATA` /`_FILE` | * | - | Overwrites for credentials. |
| `CREDENTIALS_OVERWRITE_ENDPOINT` | String | - | The API endpoint to fetch credentials. |
| `CREDENTIALS_DEFAULT_NAME` | String | `My credentials` | The default name for credentials. |
