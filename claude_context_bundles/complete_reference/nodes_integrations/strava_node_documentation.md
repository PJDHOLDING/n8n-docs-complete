# Strava node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.strava/

---

# Strava node

Use the Strava node to automate work in Strava, and integrate Strava with other applications. n8n has built-in support for a wide range of Strava features, including creating new activities, and getting activity information.

Credentials

Refer to [Strava credentials](../../credentials/strava/) for guidance on setting up authentication.

## Operations

- Activity
  - Create a new activity
  - Get an activity
  - Get all activities
  - Get all activity comments
  - Get all activity kudos
  - Get all activity laps
  - Get all activity zones
  - Update an activity

## Templates and examples

**AI Fitness Coach Strava Data Analysis and Personalized Training Insights**

by Amjid Ali

[View template details](https://n8n.io/workflows/2790-ai-fitness-coach-strava-data-analysis-and-personalized-training-insights/)

**Receive updates when a new activity gets created and tweet about it**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/745-receive-updates-when-a-new-activity-gets-created-and-tweet-about-it/)

**Export all Strava Activity Data to Google Sheets**

by Sherlockes

[View template details](https://n8n.io/workflows/2678-export-all-strava-activity-data-to-google-sheets/)

[Browse Strava integration templates](https://n8n.io/integrations/strava/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](../../core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](../../../custom-operations/) for more information.
