# Assignment 02: Complex SQL Analytics and Query Optimization

This assignment evaluates practical SQL capabilities including multi-table joining, recursive common table expressions, window functions, and query execution plan analysis.

---

## 1. Schema Description: E-Commerce Storefront

Consider the following relational schema for an online retail platform:
- $\text{Customers}(\underline{\text{customer\_id}}, \text{full\_name}, \text{country}, \text{joined\_date})$
- $\text{Categories}(\underline{\text{category\_id}}, \text{category\_name}, \text{parent\_category\_id} \uparrow \text{Categories})$
- $\text{Products}(\underline{\text{product\_id}}, \text{title}, \text{unit\_price}, \text{category\_id} \uparrow \text{Categories})$
- $\text{Orders}(\underline{\text{order\_id}}, \text{customer\_id} \uparrow \text{Customers}, \text{order\_timestamp}, \text{order\_status})$
- $\text{OrderItems}(\underline{\text{order\_id} \uparrow \text{Orders}, \text{product\_id} \uparrow \text{Products}}, \text{quantity}, \text{item\_price})$

---

## 2. Query Formulation Tasks

### Task 1: Recursive Category Hierarchy Traversal (25 Points)
Categories form an arbitrary tree hierarchy via self-referencing `parent_category_id`.
Write an ANSI SQL recursive Common Table Expression (CTE) that outputs every category alongside its absolute root ancestor category name and tree depth level.

### Task 2: Dense Ranking and Running Aggregates (25 Points)
Using SQL Window Functions (`DENSE_RANK()`, `SUM() OVER (...)`):
1. For each product category, rank products by unit price in descending order.
2. For each customer, list all their orders with a running cumulative total of amounts spent over time.

### Task 3: Customer Retention and Inactivity Analysis (25 Points)
Write a query to identify all customers who placed an order in calendar year 2025, but have placed zero orders in 2026. Implement this using:
- Method A: Correlated `NOT EXISTS` subquery.
- Method B: `LEFT OUTER JOIN` with `IS NULL` filter.

### Task 4: Query Optimization with EXPLAIN QUERY PLAN (25 Points)
Execute an `EXPLAIN QUERY PLAN` on a query joining $\text{Orders}$ and $\text{OrderItems}$ over a date range. Propose and implement appropriate B-Tree indexes on foreign keys and timestamps to eliminate full table scans (`SCAN TABLE`) and achieve index lookups (`SEARCH TABLE`).

