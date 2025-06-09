# No Title

**Source:** https://docs.n8n.io/_workflows//courses/level-one/chapter-5/chapter-5.1.json

---

{
"nodes": [
{
"parameters": {
"url": "https://internal.users.n8n.cloud/webhook/custom-erp",
"authentication": "genericCredentialType",
"genericAuthType": "httpHeaderAuth",
"sendHeaders": true,
"headerParameters": {
"parameters": [
{
"name": "unique_id",
"value": ""
}
]
},
"options": {}
},
"type": "n8n-nodes-base.httpRequest",
"typeVersion": 4.2,
"position": [
340,
-680
],
"id": "ada6becf-c320-41a7-bdca-a842ea3ee769",
"name": "HTTP Request1",
"credentials": {
"httpHeaderAuth": {
"id": "sMuanZ4xGobAurzY",
"name": "Nathan's ABCorp data warehouse account"
}
}
},
{
"parameters": {},
"type": "n8n-nodes-base.manualTrigger",
"typeVersion": 1,
"position": [
140,
-680
],
"id": "ffa1a8ce-1a1e-48c4-8a0d-6af28c0447a5",
"name": "When clicking ‘Execute workflow’"
}
],
"connections": {
"HTTP Request1": {
"main": [
[]
]
},
"When clicking ‘Execute workflow’": {
"main": [
[
{
"node": "HTTP Request1",
"type": "main",
"index": 0
}
]
]
}
},
"pinData": {},
"meta": {
"templateCredsSetupCompleted": true,
"instanceId": "24789c4d5aa56ca018d140332e7a43fd37dd7af0409453314fff12dc1aeebfa8"
}
}
