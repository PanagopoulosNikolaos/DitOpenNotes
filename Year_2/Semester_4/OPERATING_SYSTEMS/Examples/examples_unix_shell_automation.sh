#!/usr/bin/env bash
# ==============================================================================
# Script: examples_unix_shell_automation.sh
# Purpose: Demonstrates POSIX Shell Automation, Pipeline Filtering, and Exit Codes
# ==============================================================================

set -euo pipefail # Enforces strict execution: fail on error, unbound vars, or broken pipes

# Print execution banner
echo "=== System Health and Metric Aggregator ==="

# Check if required commands exist in system PATH
for cmd in ps awk sort uniq wc; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Error: Required utility '$cmd' is not installed." >&2
        exit 1
    fi
done

echo "Analyzing active process table..."

# 1. Pipeline: Count total running processes
total_procs=$(ps -e --no-headers | wc -l)
echo "Total active processes: $total_procs"

# 2. Pipeline: Find top 3 users consuming the most processes
echo "Top 3 active users by process count:"
ps -eo user --no-headers \
    | sort \
    | uniq -c \
    | sort -rn \
    | head -n 3 \
    | awk '{printf "  User: %-12s | Process Count: %d\n", $2, $1}'

# 3. Memory metric calculation from virtual /proc filesystem
if [[ -f /proc/meminfo ]]; then
    echo "Memory Utilization Overview:"
    mem_total=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
    mem_free=$(awk '/MemAvailable/ {print $2}' /proc/meminfo)
    mem_used=$((mem_total - mem_free))
    mem_pct=$((mem_used * 100 / mem_total))
    echo "  Total: $((mem_total / 1024)) MB | Used: $((mem_used / 1024)) MB (${mem_pct}%)"
fi

echo "Execution completed successfully."
exit 0

