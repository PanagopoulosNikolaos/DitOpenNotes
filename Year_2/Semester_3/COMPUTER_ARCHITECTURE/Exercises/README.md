# Computer Architecture: Exercises & Problem Sets

Quantitative problem sets, pipelined timing diagrams, hazard forwarding equations, and cache memory calculations for **Computer Architecture (Course Code: 301)**.

---

## Solved Drills and Problem Sets

| Problem Set | Topics Covered | Key Concepts |
|:---|:---|:---|
| [`exercises_pipelining_hazards_and_forwarding.md`](exercises_pipelining_hazards_and_forwarding.md) | Classic 5-stage RISC pipeline execution, RAW data hazard detection, forwarding multiplexer control equations, load-use interlock stalls, and branch penalties. | Clock cycle execution tables ($C_1$ to $C_N$), EX-to-EX bypass, MEM-to-EX bypass, stall bubble insertion, and branch resolution timing. |
| [`exercises_cache_mapping_and_performance.md`](exercises_cache_mapping_and_performance.md) | Direct-mapped, set-associative, and fully associative cache memory mapping, address bitfield decomposition, sequential reference tracing, and AMAT modeling. | Tag/Index/Offset bit calculations, Least Recently Used (LRU) eviction tracking, multilevel cache penalties (L1, L2, DRAM), and write-back versus write-through policies. |

---

## Pedagogical Objectives

1. **Cycle-by-Cycle Execution Modeling:** Construct rigorous pipeline timing charts demonstrating how instructions progress through IF, ID, EX, MEM, and WB stages in the presence of hazards.
2. **Hazard Control Logic Synthesis:** Formulate boolean conditions used by the forwarding and hazard detection units to bypass data or insert bubbles dynamically.
3. **Memory Organization Optimization:** Calculate physical bit allocation in cache arrays and quantify memory system performance using Average Memory Access Time (AMAT).

