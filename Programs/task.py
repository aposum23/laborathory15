#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def console_message(func):
    def print_message(*args):
        square = func(*args)
        print('Площадь круга равна = %.2f' %square)
    return print_message


@console_message
def calculate_square(radius):
    return math.pi * radius**2


if __name__ == '__main__':
    radius = int(input('Введите значение радуиса: '))
    calculate_square(radius)
