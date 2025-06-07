# Home Assistant node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant/

---

# Home Assistant node

Use the Home Assistant node to automate work in Home Assistant, and integrate Home Assistant with other applications. n8n has built-in support for a wide range of Home Assistant features, including getting, creating, and checking camera proxies, configurations, logs, services, and templates.

Credentials

Refer to [Home Assistant credentials](../../credentials/homeassistant/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

## Operations

- Camera Proxy
  - Get the camera screenshot
- Config
  - Get the configuration
  - Check the configuration
- Event
  - Create an event
  - Get all events
- Log
  - Get a log for a specific entity
  - Get all logs
- Service
  - Call a service within a specific domain
  - Get all services
- State
  - Create a new record, or update the current one if it already exists (upsert)
  - Get a state for a specific entity
  - Get all states
- Template
  - Create a template

## Templates and examples

**Turn on a light to a specific color on any update in GitHub repository**

by n8n Team

[View template details](https://n8n.io/workflows/1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github-repository/)

**Birthday and Ephemeris Notification (Google Contact, Telegram & Home Assistant)**

by Thibaud

[View template details](https://n8n.io/workflows/4462-birthday-and-ephemeris-notification-google-contact-telegram-and-home-assistant/)

**📍 Daily Nearby Garage Sales Alerts via Telegram**

by Thibaud

[View template details](https://n8n.io/workflows/4649-daily-nearby-garage-sales-alerts-via-telegram/)

[Browse Home Assistant integration templates](https://n8n.io/integrations/home-assistant/), or [search all templates](https://n8n.io/workflows/)

## Related resources

Refer to [Home Assistant's documentation](https://developers.home-assistant.io/docs/api/rest/) for more information about the service.
