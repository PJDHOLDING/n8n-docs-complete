# Date and time

**Source:** https://docs.n8n.io/code/builtin/date-time/

---

# Built-in date and time methods

Methods for working with date and time.

Python support

You can use Python in the Code node. It isn't available in expressions.

JavaScriptPython

| Method | Description | Available in Code node? |
| `$now` | A Luxon object containing the current timestamp. Equivalent to `DateTime.now()`. | ✅ |
| `$today` | A Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`. | ✅ |

| Method | Description |
| `_now` | A Luxon object containing the current timestamp. Equivalent to `DateTime.now()`. |
| `_today` | A Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`. |

n8n passes dates between nodes as strings, so you need to parse them. Luxon helps you do this. Refer to [Date and time with Luxon](../../cookbook/luxon/) for more information.

n8n provides built-in convenience functions to support data transformation in expressions for dates. Refer to [Data transformation functions | Dates](../data-transformation-functions/dates/) for more information.
