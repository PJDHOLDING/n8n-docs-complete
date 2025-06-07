# TimescaleDB node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/

---

# TimescaleDB node

Use the TimescaleDB node to automate work in TimescaleDB, and integrate TimescaleDB with other applications. n8n has built-in support for a wide range of TimescaleDB features, including executing an SQL query, as well as inserting and updating rows in a database.

Credentials

Refer to [TimescaleDB credentials](../../credentials/timescaledb/) for guidance on setting up authentication.

## Operations

- Execute an SQL query
- Insert rows in database
- Update rows in database

## Templates and examples

[Browse TimescaleDB integration templates](https://n8n.io/integrations/timescaledb/), or [search all templates](https://n8n.io/workflows/)

## Specify a column's data type

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for the column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.
