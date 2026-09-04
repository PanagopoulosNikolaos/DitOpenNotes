# Project 01: High-Performance Inverted Index & Text Retrieval Engine

## Project Overview
Design and implement an in-memory inverted text index and ranked search engine in modern C++. The project reinforces custom data structure implementations by combining Hash Tables, self-balancing AVL Trees, Tries, and Max-Heaps without relying on high-level search libraries.

---

## Architecture and Technical Requirements

### 1. Inverted Index Data Structures
- **Lexicon / Dictionary:** Implement a custom Hash Table with open addressing (double hashing) or a Prefix Trie mapping unique query terms to posting lists.
- **Posting Lists:** Maintain sorted linked lists or dynamic arrays storing document IDs and term frequencies:
  $$\text{Posting}(t) = [(\text{docID}_1, f_{1, t}), (\text{docID}_2, f_{2, t}), \dots]$$

### 2. Query Processing and Ranked Retrieval
- **Boolean Queries:** Support `AND`, `OR`, and `NOT` operations by performing two-pointer linear intersections of sorted posting lists in $O(L_1 + L_2)$ time.
- **Ranked Retrieval (TF-IDF Scoring):**
  Score documents using Term Frequency-Inverse Document Frequency:
  $$\text{Score}(q, d) = \sum_{t \in q} \left(1 + \log_{10} f_{t, d}\right) \cdot \log_{10}\left(\frac{N}{\text{DF}_t}\right)$$
- **Top-$K$ Results Extraction:** Maintain a bounded Min-Heap of size $K$ to extract the highest-scoring documents in $O(D \log K)$ time.

---

## Project Milestones

| Milestone | Target Objective | Deliverables |
|---|---|---|
| **Phase 1** | Tokenization and Lexicon Structure | Custom tokenizer, case normalization, and Trie/Hash dictionary implementation |
| **Phase 2** | Inverted Index and Intersections | Posting list construction and Boolean query evaluation engine |
| **Phase 3** | TF-IDF Scoring and Heap Ranking | Top-$K$ query processing using bounded priority queue |
| **Phase 4** | Benchmark Profiling and Documentation | Throughput benchmarks (queries/sec), memory footprint analysis, and final report |

---

## Grading Rubric

| Assessment Criteria | Description | Weight |
|---|---|---|
| **Custom Data Structure Integrity** | Zero memory leaks, correct pointer management, and custom implementations | 30% |
| **Query Engine Correctness** | Accurate Boolean query evaluation and valid TF-IDF score computation | 30% |
| **Algorithmic Efficiency** | Linear posting intersections, $O(D \log K)$ heap ranking, efficient tokenization | 20% |
| **Testing and Benchmarking** | Automated test suite verifying edge cases, large corpus ingestion benchmarks | 20% |

