# Exam 5: Advanced Database Administration (Level: Advanced)

Multiple Choice Question 1: What does the creation of an Index on a table mainly provide?
[✓] 1. Increase in the speed of retrieval queries (SELECT).
[ ] 2. Increase in the speed of insertion commands (INSERT).
[ ] 3. Reduction of the required storage space.
[ ] 4. Encryption of the table data.
---
*solution:*
Indexes dramatically improve the speed of searching and retrieving records, but they add a small delay to INSERT/UPDATE/DELETE commands and occupy additional storage space.
---

Multiple Choice Question 2: In the conceptual ER model, how are "weak entities" handled during the transition to the relational model?
[✓] 1. They obtain a primary key composed of the strong entity's key plus their own partial key.
[ ] 2. They are incorporated as simple attributes in the strong entity's table.
[ ] 3. They are ignored during the conversion to tables.
[ ] 4. A table is created only if they have a many-to-many relationship.
---
*solution:*
In weak entities, the primary key is created by combining the foreign key of the strong (owner) entity and their own partial key.
---

Exercise 3: How would you convert the following requirement into tables: An order (Order) involves many products (Product) and a product can be in many orders. In each order, the quantity of the respective product is also recorded. Provide the CREATE TABLE commands with the keys.
---
*solution:*
The relationship is M:N. A third junction table must be created that holds the "quantity".
```sql
CREATE TABLE OrderTbl (
    order_id INT PRIMARY KEY,
    order_date DATE
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);

CREATE TABLE Order_Details (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES OrderTbl(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);
```
---

Exercise 4: Write an SQL command using CASCADE that ensures that if a product is deleted, the corresponding records of the Order_Details table are deleted automatically.
---
*solution:*
ON DELETE CASCADE is defined during the creation of the Foreign Key. If we want to add it afterwards to an existing table:
```sql
ALTER TABLE Order_Details
ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE;
```
---
