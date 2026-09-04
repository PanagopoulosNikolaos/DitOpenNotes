# Term Project: Terminal Inventory & Warehouse Management System

## Project Overview
The Terminal Inventory Management System is a robust, modular, menu-driven command-line application implemented in ANSI/ISO C. It models an industrial warehouse tracking products, stock quantities, unit prices, supplier details, and restocking alerts. This capstone project synthesizes procedural design, multi-file modularity, pointer mechanics, custom data structures, and binary file serialization.

---

## 1. System Architecture and Component Structure

The application is structured into four distinct modules:

```text
inventory_system/
├── Makefile
├── include/
│   ├── inventory.h         # Core data definitions and function prototypes
│   ├── file_io.h           # Binary serialization and export interfaces
│   └── ui.h                # Terminal menu and input sanitization interfaces
└── src/
    ├── main.c              # Application lifecycle and main event loop
    ├── inventory.c         # Item manipulation, sorting, and search logic
    ├── file_io.c           # File reading and writing implementation
    └── ui.c                # Console interface and formatting logic
```

---

## 2. Data Schema and Domain Model

Define item and inventory registry structures:

```c
#define MAX_CODE_LEN 16
#define MAX_NAME_LEN 48
#define MAX_SUPPLIER_LEN 48
#define MAX_ITEMS 500

typedef struct {
    char product_code[MAX_CODE_LEN];  // Unique alphanumeric SKU
    char product_name[MAX_NAME_LEN];  // Item description
    int quantity_in_stock;            // Available warehouse units
    int minimum_threshold;            // Restock trigger level
    double unit_price;                // Wholesale cost in Euros
    char supplier_name[MAX_SUPPLIER_LEN];
} InventoryItem;

typedef struct {
    InventoryItem items[MAX_ITEMS];
    size_t total_items;
    char database_path[256];
} InventoryRegistry;
```

---

## 3. Core Functional Requirements

### 3.1 Item Lifecycle Operations (CRUD)
* **Create**: Prompt user for product code, name, quantity, minimum threshold, unit price, and supplier. Ensure product code is unique.
* **Read / Search**: Support lookup by exact product code, or substring lookup by product name.
* **Update**: Allow updating stock quantities (restock/dispatch) and modifying unit prices.
* **Delete**: Remove an item by code with confirmation prompt, shifting remaining elements leftward.

### 3.2 Inventory Analytics & Reports
* **Low Stock Warning**: Display all items where `quantity_in_stock <= minimum_threshold`.
* **Valuation Summary**: Compute total inventory asset value:
  $$\text{Total Valuation} = \sum_{i=0}^{N-1} \text{quantity}_i \times \text{unit\_price}_i$$
* **Sorting**: Sort inventory alphabetically by product name, or numerically by stock level or price.

### 3.3 Persistence & File I/O
* **Binary Database Persistence**: Automatically save state to `inventory.dat` on exit and reload upon startup using `fwrite` and `fread`.
* **CSV Report Export**: Export human-readable CSV ledger to `inventory_report.csv`.

---

## 4. Technical Constraints & Build Requirements
* **Compilation**: Build cleanly with `make` using `-Wall -Wextra -Werror -std=c11 -pedantic`.
* **Input Validation**: Never allow invalid numeric inputs or negative quantities/prices. Reject buffer overflow attempts during string entry.
* **Zero Leaks**: Ensure clean memory handling and closed file descriptors across all exit paths.

---

## 5. Evaluation Rubric

| Criterion | Evaluation Focus | Points |
|:---|:---|:---:|
| System Architecture | Proper modularization across `.h` and `.c` files with standard Makefile | 20 |
| Functional Correctness | Complete CRUD operations, stock alerts, and valuation calculation | 25 |
| Persistence & Serialization | Flawless binary read/write and CSV report generation | 20 |
| Defensive Input Handling | Rejects malformed strings, invalid numbers, and buffer overruns | 15 |
| Documentation & Standards | Adherence to Google-style docstrings, PascalCase, camelCase, snake_case | 20 |
| **Total** | | **100** |

