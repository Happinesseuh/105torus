#!/usr/bin/env python3

##
## EPITECH PROJECT, 2021
## 105 torus
## File description:
## main
##

from math import *
from sys import *
from sources.methods import *
from sources.class_create import *


def print_help():
    print("USAGE")
    print("\t./105torus opt a0 a1 a2 a3 a4 n\n")
    print("DESCRIPTION")
    print("\topt\tmethod option:")
    print("\t\t\t1 for the bisection method")
    print("\t\t\t2 for Newton’s method")
    print("\t\t\t3 for the secant method")
    print("\ta[0-4]\tcoefficients of the equation")
    print(
        "\tn\tprecision (the application of the polynomial to the solution shouldbe smaller than 10ˆ-n)"
    )


def error_check():
    i = 1
    ac = len(argv)
    if ac < 8 or ac > 8:
        return 1
    if argv[1] != "1" and argv[1] != "2" and argv[1] != "3":
        print("bad option")
        return 1
    if int(argv[7]) <= 0:
        return 1
    while i < 8:
        for j in range(len(argv[i])):
            if (argv[i][j] != "-") and (argv[i][j] < "0" or argv[i][j] > "9"):
                return 1
        i += 1


def main():
    ac = len(argv)
    if ac == 2 and argv[1] == "-h":
        print_help()
    if error_check() == 1:
        exit(84)
    create_function(function, argv)
    if argv[1] == "1":
        bisection_method(function)
    if argv[1] == "2":
        newton_method(function)
    if argv[1] == "3":
        secant_method(function)


main()
