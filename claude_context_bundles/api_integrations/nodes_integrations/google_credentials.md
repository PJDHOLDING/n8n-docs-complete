# Google credentials

**Source:** https://docs.n8n.io/integrations/builtin/credentials/google/

---

# Google credentials

This section contains:

- [OAuth2 single service](oauth-single-service/): Create an OAuth2 credential for a specific service node, such as the Gmail node.
- [OAuth2 generic](oauth-generic/): Create an OAuth2 credential for use with [custom operations](../../../custom-operations/).
- [Service Account](service-account/): Create a [Service Account](https://cloud.google.com/iam/docs/service-account-overview) credential for some specific service nodes.
- [Google PaLM and Gemini](../googleai/): Get a Google Gemini/Google PaLM API key.

## OAuth2 and Service Account

There are two authentication methods available for Google services nodes:

- [OAuth2](https://developers.google.com/identity/protocols/oauth2): Recommended because it's more widely available and easier to set up.
- [Service Account](https://cloud.google.com/iam/docs/understanding-service-accounts): Refer to the [Google documentation: Understanding service accounts](https://cloud.google.com/iam/docs/understanding-service-accounts) for guidance on when you need a service account.

Note for n8n Cloud users

For the following nodes, you can authenticate by selecting **Sign in with Google** in the OAuth section:

- [Google Calendar](../../app-nodes/n8n-nodes-base.googlecalendar/)
- [Google Contacts](../../app-nodes/n8n-nodes-base.googlecontacts/)
- [Google Drive](../../app-nodes/n8n-nodes-base.googledrive/)
- [Google Mail](../../app-nodes/n8n-nodes-base.gmail/)
- [Google Sheets](../../app-nodes/n8n-nodes-base.googlesheets/)
- [Google Sheets Trigger](../../trigger-nodes/n8n-nodes-base.googlesheetstrigger/)
- [Google Tasks](../../app-nodes/n8n-nodes-base.googletasks/)

## Compatible nodes

Once configured, you can use your credentials to authenticate the following nodes. Most nodes are compatible with OAuth2 authentication. Support for Service Account authentication is limited.

| Node | OAuth | Service Account |
| [Google Ads](../../app-nodes/n8n-nodes-base.googleads/) | ✅ | ❌ |
| [Gmail](../../app-nodes/n8n-nodes-base.gmail/) | ✅ | ⚠ |
| [Google Analytics](../../app-nodes/n8n-nodes-base.googleanalytics/) | ✅ | ❌ |
| [Google BigQuery](../../app-nodes/n8n-nodes-base.googlebigquery/) | ✅ | ✅ |
| [Google Books](../../app-nodes/n8n-nodes-base.googlebooks/) | ✅ | ✅ |
| [Google Calendar](../../app-nodes/n8n-nodes-base.googlecalendar/) | ✅ | ❌ |
| [Google Chat](../../app-nodes/n8n-nodes-base.googlechat/) | ❌ | ✅ |
| [Google Cloud Storage](../../app-nodes/n8n-nodes-base.googlecloudstorage/) | ✅ | ❌ |
| [Google Contacts](../../app-nodes/n8n-nodes-base.googlecontacts/) | ✅ | ❌ |
| [Google Cloud Firestore](../../app-nodes/n8n-nodes-base.googlecloudfirestore/) | ✅ | ✅ |
| [Google Cloud Natural Language](../../app-nodes/n8n-nodes-base.googlecloudnaturallanguage/) | ✅ | ❌ |
| [Google Cloud Realtime Database](../../app-nodes/n8n-nodes-base.googlecloudrealtimedatabase/) | ✅ | ❌ |
| [Google Docs](../../app-nodes/n8n-nodes-base.googledocs/) | ✅ | ✅ |
| [Google Drive](../../app-nodes/n8n-nodes-base.googledrive/) | ✅ | ✅ |
| [Google Drive Trigger](../../trigger-nodes/n8n-nodes-base.googledrivetrigger/) | ✅ | ✅ |
| [Google Perspective](../../app-nodes/n8n-nodes-base.googleperspective/) | ✅ | ❌ |
| [Google Sheets](../../app-nodes/n8n-nodes-base.googlesheets/) | ✅ | ✅ |
| [Google Slides](../../app-nodes/n8n-nodes-base.googleslides/) | ✅ | ✅ |
| [Google Tasks](../../app-nodes/n8n-nodes-base.googletasks/) | ✅ | ❌ |
| [Google Translate](../../app-nodes/n8n-nodes-base.googletranslate/) | ✅ | ✅ |
| [Google Workspace Admin](../../app-nodes/n8n-nodes-base.gsuiteadmin/) | ✅ | ❌ |
| [YouTube](../../app-nodes/n8n-nodes-base.youtube/) | ✅ | ❌ |

Gmail and Service Accounts

Google technically supports Service Accounts for use with Gmail, but it requires enabling domain-wide delegation, which Google discourages, and its behavior can be inconsistent.

n8n recommends using OAuth2 with the Gmail node.
