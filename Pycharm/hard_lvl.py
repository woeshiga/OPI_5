#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-10


def get_a(n, x):
    n_fact = 1
    for i in range(1, n + 1):
        n_fact *= i
    return (((-1) ** n) * (x ** (2 * n + 1))) / (2 * n + 1) * n_fact


def erf(x: float) -> float:
    res = 0
    n = 0
    a = get_a(n, x)
    while math.fabs(a) > EPS:
        res += a
        n += 1
        a *= get_a(n, x)
    res *= 2 / math.sqrt(math.pi)
    return res


if __name__ == '__main__':
    x = float(input("Enter x: "))

    while x < 0:
        x = float(input("x < 0! Enter x: "))

    print(erf(x))
