#!/usr/bin/python3

def minOperations(n):
    ops = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            ops += divisor
            n //= divisor
        else:
            divisor += 1
    return ops

