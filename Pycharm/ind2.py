#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a1, b1, c1 = map(int, input("Введите координаты первой прямой: ").split(' '))
    a2, b2, c2 = map(int, input("Введите координаты второй прямой ").split(' '))

    if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
        if a1 == 0 and b1 == 0 and a2 == 0 and b2 == 0:
            print("Обе прямые не существуют")
        else:
            print("Одна из прямых не существует")
    else:
        if a1 == a2 and b1 == b2 and c1 == c2:
            print("Прямые совпадают")
        elif a1 * b2 - b1 * a2 == 0:
            print("Прямые параллельны")
        else:
            x = (b1 * c2 - b2 * c1) / (a1 * b2 - b1 * a2)
            y = (a2 * c1 - a1 * c2) / (a1 * b2 - b1 * a2)
            print(f"Координаты точки пересечения: x = {x}, y = {y}")
