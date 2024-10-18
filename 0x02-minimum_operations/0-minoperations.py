#!/usr/bin/python3
"""
Module for minimum operations problem.
"""

def min_operations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters.
    
    Args:
        n (int): The number of H characters to achieve.
    
    Returns:
        int: The minimum number of operations required.
    """
    if not isinstance(n, int) or n <= 0:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} chars: {}".format(n, min_operations(n)))

    n = 12
    print("Min # of operations to reach {} chars: {}".format(n, min_operations(n)))