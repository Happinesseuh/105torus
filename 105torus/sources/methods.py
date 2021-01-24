##
## EPITECH PROJECT, 2021
## Untitled (Workspace)
## File description:
## methods
##

from math import *
from sys import *
from sources.class_create import *


def function_result(function, x):
    f = (
        (function.a4 * x ** 4)
        + (function.a3 * x ** 3)
        + (function.a2 * x ** 2)
        + (function.a1 * x)
        + (function.a0)
    )
    return f


def function_derived(function, x):
    f = (
        (4 * function.a4 * x ** 3)
        + (3 * function.a3 * x ** 2)
        + (2 * function.a2 * x)
        + (function.a1)
    )
    return f


def bisection_method(function):
    a = 0
    b = 1
    i = 1

    while round(float(a) * pow(10, function.n) + 1) < round(
        float(b) * pow(10, function.n)
    ):
        if i > 500:
            exit(84)
        c = (a + b) / 2
        if i < function.n:
            print(f"x = {c:.{i}f}")
        else:
            print(f"x = {c:.{function.n}f}")
        if function_result(function, a) * function_result(function, c) < 0:
            b = c
        else:
            a = c
        i += 1
    if c > 1 or c < 0:
        exit(84)


def newton_method(function):
    x = 0.5
    i = 1

    print(f"x = {x}")
    if pow(10, function.n) == 0:
        exit(84)
    while abs(function_result(function, x)) > 1 / 10 ** function.n:
        if i > 500 or function_derived(function, x) == 0:
            exit(84)
        x = x - (function_result(function, x) / function_derived(function, x))
        print(f"x = {x:.{function.n}f}")
        i += 1
    if x < 0 or x > 1:
        exit(84)


def secant_method(function):
    x = 0
    x1 = 1
    xn = 0
    i = 0

    if pow(10, function.n) == 0:
        exit(84)
    while abs(function_result(function, xn)) > (1 / 10 ** function.n):
        if i > 500 or (
            (function_result(function, x1) - function_result(function, x)) == 0
        ):
            exit(84)
        if (function_result(function, x1) - function_result(function, x)) == 0:
            exit(84)
        xn = x1 - (
            (function_result(function, x1) * (x1 - x))
            / (function_result(function, x1) - function_result(function, x))
        )
        if i == 0:
            print(f"x = {xn:0.1f}")
        else:
            print(f"x = {xn:.{function.n}f}")
        x = x1
        x1 = xn
        i += 1
    if xn < 0 or xn > 1:
        exit(84)
