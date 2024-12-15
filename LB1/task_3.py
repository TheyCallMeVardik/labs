#!/usr/bin/env python3
import sys
import math

try:
    number = float(input().strip())
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    result = math.sqrt(number)
    with open("LB1/output.txt", "w") as f:
        f.write(f"{result}\n")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
