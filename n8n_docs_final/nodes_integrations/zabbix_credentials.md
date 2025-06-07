# Zabbix credentials

**Source:** https://docs.n8n.io/integrations/builtin/credentials/zabbix/

---

# Zabbix credentials

You can use these credentials to authenticate when using the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to make a [Custom API call](../../../custom-operations/).

## Prerequisites

Create a [Zabbix Cloud](https://www.zabbix.com/) account or self-host your own Zabbix server.

## Supported authentication methods

- API key

## Related resources

Refer to [Zabbix's API documentation](https://www.zabbix.com/documentation/current/en/manual/api) for more information about the service.

This is a credential-only node. Refer to [Custom API operations](../../../custom-operations/) to learn more. View [example workflows and related content](https://n8n.io/integrations/zabbix/) on n8n's website.

## Using API key

To configure this credential, you'll need:

- an **API Token**: An API key for your Zabbix user.
- the **URL**: The URL of your Zabbix server. Don't include `/zabbix` as part of the URL.

Refer to [Zabbix's API documentation](https://www.zabbix.com/documentation/current/en/manual/api#authentication) for more information about authenticating to the service.
