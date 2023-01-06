#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    N = int(input('Value of N? '))
    if 20 >= N >= 0:
        if N == 1:
            print(f'Мы успешно сдали {N} экзамен')
        if N == 2:
            print(f'Мы успешно сдали {N} экзамена')
        else:
            print(f'Мы успешно сдали {N} экзаменов')
    else:
        print('Ошибка!', file=sys.stderr)
        exit(1)
        