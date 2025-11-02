#!/usr/bin/env python3
# Runner that executes each demo module in a separate subprocess with timeout
# to avoid hangs (e.g., a stuck Ford-Fulkerson demo). Prints results and exits
# with non-zero code if any failures/timeouts occur.

import os
import sys
import subprocess

BASE_DIR = os.path.dirname(__file__)
files = [
    os.path.join(BASE_DIR, "algorithms", "searching.py"),
    os.path.join(BASE_DIR, "algorithms", "sorting.py"),
    os.path.join(BASE_DIR, "algorithms", "graph_algorithms.py"),
    os.path.join(BASE_DIR, "data_structures", "arrays.py"),
    os.path.join(BASE_DIR, "data_structures", "linked_lists.py"),
    os.path.join(BASE_DIR, "data_structures", "stacks.py"),
    os.path.join(BASE_DIR, "data_structures", "queues.py"),
    os.path.join(BASE_DIR, "data_structures", "trees.py"),
    os.path.join(BASE_DIR, "data_structures", "graphs.py"),
    os.path.join(BASE_DIR, "data_structures", "hash_tables.py"),
]

TIMEOUT_SECONDS = 8
failures = 0

for path in files:
    print("\n" + "=" * 70)
    print(f"=== Running: {os.path.relpath(path, BASE_DIR)} (timeout={TIMEOUT_SECONDS}s) ===")
    print("=" * 70)
    if not os.path.exists(path):
        print(f"SKIP: {path} not found")
        failures += 1
        continue
    try:
        completed = subprocess.run(
            [sys.executable, path],
            check=False,
            timeout=TIMEOUT_SECONDS
        )
        if completed.returncode == 0:
            print(f"OK: {path}")
        else:
            print(f"FAIL (exit {completed.returncode}): {path}")
            failures += 1
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {path} after {TIMEOUT_SECONDS}s")
        failures += 1
    except Exception as e:
        print(f"ERROR running {path}: {e}")
        failures += 1

print("\n" + "=" * 70)
print(f"SUMMARY: failures={failures}")
print("=" * 70)
sys.exit(failures)
