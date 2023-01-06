#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for x in range(10, 1000):
        summ = x // 10 + x % 10
        if x == summ + summ**2:
            print(f"Полученные числа: {x}")
            