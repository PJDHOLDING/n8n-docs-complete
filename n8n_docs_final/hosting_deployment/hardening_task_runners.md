# Hardening task runners

**Source:** https://docs.n8n.io/hosting/securing/hardening-task-runners/

---

# Hardening task runners

[Task runners](../../configuration/task-runners/) are responsible for executing code from the [Code node](../../../integrations/builtin/core-nodes/n8n-nodes-base.code/). While Code node executions are secure, you can follow these recommendations to further harden your task runners.

## Run task runners as sidecars in external mode

To increase the isolation between the core n8n process and code in the Code node, run task runners in [external mode](../../configuration/task-runners/#setting-up-external-mode). External task runners launch as separate containers, providing a fully isolated environment to execute the JavaScript defined in the Code node.
