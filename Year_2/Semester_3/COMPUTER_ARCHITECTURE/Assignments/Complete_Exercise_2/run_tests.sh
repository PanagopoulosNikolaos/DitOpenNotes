#!/bin/bash


echo "Running MIPS Calculator Tests..."

# Create a temporary input file
TEMP_INPUT=$(mktemp)


# Format: Name, AM, Semester, Num1, Num2, Op, ...
cat <<EOF > "$TEMP_INPUT"
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


spim -file calculator_spec.asm < "$TEMP_INPUT"

# Clean up the temporary file
rm "$TEMP_INPUT"

echo "Tests completed."
