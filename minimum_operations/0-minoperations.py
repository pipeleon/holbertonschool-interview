#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Principal funtion"""
    if n < 2:
        return 0

    common_mul = []
    divisor = 2

    while n != 1:
        if n % divisor == 0:
            common_mul.append(divisor)
            n /= divisor
            divisor = 1
        divisor += 1

    return sum(common_mul)
