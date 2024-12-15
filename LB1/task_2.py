#!/usr/bin/env python3
import random
import sys

try:
    A = int(input().strip())
    B = random.randint(-10, 10)
    if B == 0:
        raise ValueError("Division by zero is not allowed.")
    print(f'"B" = {B}') 
    result = A / B
    print(result)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
