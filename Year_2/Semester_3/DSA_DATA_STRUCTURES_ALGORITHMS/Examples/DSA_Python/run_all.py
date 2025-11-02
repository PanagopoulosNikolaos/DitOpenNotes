#!/usr/bin/env python3
# Runner to execute demo __main__ blocks for all modules in this package.
# Executes each script with runpy.run_path(run_name="__main__") so their
# if __name__ == "__main__" sections run and outputs/errors are captured.

import runpy
import os
import sys
import traceback

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

failures = 0

for path in files:
    print("\n" + "=" * 70)
    print(f"=== Running: {os.path.relpath(path, BASE_DIR)} ===")
    print("=" * 70)
    if not os.path.exists(path):
        print(f"SKIP: {path} not found")
        failures += 1
        continue
    try:
        # run_path with run_name="__main__" executes the file as a script
        runpy.run_path(path, run_name="__main__")
        print(f"OK: {path}")
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else 1
        print(f"FAIL (SystemExit {code}): {path}")
        failures += 1
    except Exception:
        print(f"FAIL: {path}")
        traceback.print_exc()
        failures += 1

print("\n" + "=" * 70)
print(f"SUMMARY: failures={failures}")
print("=" * 70)
sys.exit(failures)
