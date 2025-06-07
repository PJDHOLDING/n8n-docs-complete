# CrateDB node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb/

---

# CrateDB node

Use the CrateDB node to automate work in CrateDB, and integrate CrateDB with other applications. n8n has built-in support for a wide range of CrateDB features, including executing, inserting, and updating rows in the database.

Credentials

Refer to [CrateDB credentials](../../credentials/cratedb/) for guidance on setting up authentication.

## Operations

- Execute an SQL query
- Insert rows in database
- Update rows in database

## Templates and examples

[Browse CrateDB integration templates](https://n8n.io/integrations/cratedb/), or [search all templates](https://n8n.io/workflows/)

## Node reference

### Specify a column's data type

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for the column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.
