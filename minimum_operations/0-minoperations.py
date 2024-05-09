#!/usr/bin/python3

def min_operations(n):
    """
    Calculates the minimum number of operations needed to result in exactly n H characters
    """
    # If n is less than 2, no operations are needed
    if n < 2:
        return 0

    ops, root = 0, 2  # Initialize variables: ops to count operations, root for divisor
    while root <= n:
        # Check if n is divisible by root
        if n % root == 0:
            # Add root to ops as it represents one operation
            ops += root
            # Divide n by root to reduce it for further operations
            n //= root
            # Decrement root to find remaining smaller values that evenly divide n
            root -= 1
        # Increment root to check the next possible divisor
        root += 1
    return ops
