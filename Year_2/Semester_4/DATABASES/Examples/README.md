# Database Systems: Code Examples

This directory provides practical, executable SQL implementations and relational schema definitions for SQLite and PostgreSQL.

---

## Directory Contents

| File | Language / Format | Description |
|:---|:---|:---|
| [`examples_sql_schema_and_queries.sql`](examples_sql_schema_and_queries.sql) | SQL (DDL + DML) | Relational schema creation, referential integrity foreign keys, table seeding, and complex analytical multi-join queries |
| [`examples_sql_walkthrough.md`](examples_sql_walkthrough.md) | Markdown | Comprehensive walkthrough guide explaining schema design, normalization, join mechanics, and command-line execution |

---

## Execution Instructions

```bash
# Execute against SQLite CLI
sqlite3 :memory: < examples_sql_schema_and_queries.sql
```

