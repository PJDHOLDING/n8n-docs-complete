# Mailchimp credentials

**Source:** https://docs.n8n.io/integrations/builtin/credentials/mailchimp/

---

# Mailchimp credentials

You can use these credentials to authenticate the following nodes:

- [Mailchimp](../../app-nodes/n8n-nodes-base.mailchimp/)
- [Mailchimp Trigger](../../trigger-nodes/n8n-nodes-base.mailchimptrigger/)

## Prerequisites

Create a [Mailchimp](https://www.mailchimp.com/) account.

## Supported authentication methods

- API key
- OAuth2

Refer to [Selecting an authentication method](#selecting-an-authentication-method) for guidance on which method to use.

## Related resources

Refer to [Mailchimp's API documentation](https://mailchimp.com/developer/marketing/api/) for more information about the service.

## Using API key

To configure this credential, you'll need:

- An **API Key**: Generate an API key in the [API keys section](https://us1.admin.mailchimp.com/account/api/) of your Mailchimp account. Refer to [Mailchimp's Generate your API key documentation](https://mailchimp.com/developer/marketing/guides/quick-start/#generate-your-api-key) for more detailed instructions.

## Using OAuth2

Note for n8n Cloud users

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you need to configure OAuth2 from scratch, [register an application](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#register-your-application). Refer to the [Mailchimp OAuth2 documentation](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/) for more information.

## Selecting an authentication method

Mailchimp suggests using an API key if you're only accessing your own Mailchimp account's data:

> Use an API key if you're writing code that tightly couples *your* application's data to *your* Mailchimp account's data. If you ever need to access *someone else's* Mailchimp account's data, you should be using OAuth 2 ([source](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#when-not-to-use-oauth-2))
