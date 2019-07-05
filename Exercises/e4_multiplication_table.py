"""
Problem
-------
Write a function that takes a number as input and prints the multiplication table for that number.

For example, if the input is 8, the function should print:

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64

"""


def print_multiplication_table(number):
    for i in range(1,9):
        print(number,"X",i,"=",number*i)



print_multiplication_table(20)
