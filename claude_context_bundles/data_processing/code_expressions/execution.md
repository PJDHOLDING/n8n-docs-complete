# execution

**Source:** https://docs.n8n.io/code/cookbook/builtin/execution/

---

# `execution`

## `execution.id`

Contains the unique ID of the current workflow execution.

JavaScriptPython

| ``` 1 ``` | ``` let executionId = $execution.id;  ``` |

| ``` 1 ``` | ``` executionId = _execution.id  ``` |

## `execution.resumeUrl`

The webhook URL to call to resume a [waiting](../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait/) workflow.

See the [Wait > On webhook call](../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait/#on-webhook-call) documentation to learn more.

## `execution.customData`

This is only available in the Code node.

JavaScriptPython

| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` // Set a single piece of custom execution data $execution.customData.set("key", "value");  // Set the custom execution data object $execution.customData.setAll({"key1": "value1", "key2": "value2"})  // Access the current state of the object during the execution var customData = $execution.customData.getAll()  // Access a specific value set during this execution var customData = $execution.customData.get("key")  ``` |

| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` # Set a single piece of custom execution data _execution.customData.set("key", "value");  # Set the custom execution data object _execution.customData.setAll({"key1": "value1", "key2": "value2"})  # Access the current state of the object during the execution customData = _execution.customData.getAll()  # Access a specific value set during this execution customData = _execution.customData.get("key")  ``` |

Refer to [Custom executions data](../../../../workflows/executions/custom-executions-data/) for more information.
