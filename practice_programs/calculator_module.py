"""A tiny calculator module.

I keep the arithmetic here so 20_calculator_main.py can import it and call
these functions. It shows how to split a program across files with import.
"""


def add(a, b):
    s = a + b
    return s


def sub(a, b):
    s = a - b
    return s


def mult(a, b):
    s = a * b
    return s


def div(a, b):
    s = a / b
    return s


def power(a, b):
    s = a**b
    return s


def mod(a, b):
    s = a % b
    return s
