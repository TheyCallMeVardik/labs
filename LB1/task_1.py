#!/usr/bin/env python3
import random
import sys

try:
    A = random.randint(-10, 10)
    print(A)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
