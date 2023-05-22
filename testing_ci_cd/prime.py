from sympy import ceiling


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, ceiling(n ** .5) + 1):
        if n % i == 0:
            return False
    return True
