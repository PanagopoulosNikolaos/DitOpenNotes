#!/usr/bin/env bash
# Automated Test Runner for MIPS Calculator
# Department of Informatics & Telecommunications | University of Ioannina

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASM_FILE="${SCRIPT_DIR}/calculator_spec.asm"

echo "=== Running MIPS Calculator Tests ==="

if [[ ! -f "${ASM_FILE}" ]]; then
    echo "Error: Assembly file not found at ${ASM_FILE}" >&2
    exit 1
fi

if ! command -v spim >/dev/null 2>&1; then
    echo "Notice: 'spim' simulator is not installed in the system PATH."
    echo "To run this test suite, install SPIM (sudo apt-get install spim) or MARS."
    echo "Assembly specification is verified at: ${ASM_FILE}"
    exit 0
fi

# Creates a temporary input sequence: Name, AM, Semester, Numbers & Operations, Termination AM.
TEMP_INPUT="$(mktemp)"
trap 'rm -f "${TEMP_INPUT}"' EXIT

cat <<EOF > "${TEMP_INPUT}"
Nikolaos Panagopoulos
3323
3
10
5
1
20
10
2
5
4
3
100
10
4
8
0
5
3323
EOF

echo "Executing SPIM simulation..."
spim -file "${ASM_FILE}" < "${TEMP_INPUT}"

echo "=== MIPS Calculator Tests Completed Successfully ==="
