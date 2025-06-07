# QuestDB node documentation

**Source:** https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb/

---

# QuestDB node

Use the QuestDB node to automate work in QuestDB, and integrate QuestDB with other applications. n8n supports executing an SQL query and inserting rows in a database with QuestDB.

Credentials

Refer to [QuestDB credentials](../../credentials/questdb/) for guidance on setting up authentication.

## Operations

- Executes a SQL query.
- Insert rows in database.

## Templates and examples

[Browse QuestDB integration templates](https://n8n.io/integrations/questdb/), or [search all templates](https://n8n.io/workflows/)

## Node reference

### Specify a column's data type

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.
