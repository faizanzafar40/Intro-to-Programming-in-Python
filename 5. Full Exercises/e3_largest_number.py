"""
Problem
-------
Write a function that takes a list as input and returns the largest number in it.
Don't use the built-in max function, write your own.

For example: if the input to the function is [2, 5, 9, 1, 3, 6, 10] the output should be 10
You can try with either/both positive or/and negative numbers.

Hint:
1. If you need to define a variable without setting its value, it can have a value of "None".
    i.e. my_var = None
"""


def get_maximum(numbers):
    result = numbers[0]
    for i in range(len(numbers)):
        if numbers[i]>result:
            result=numbers[i]

    return result


n = [2, 5, 9, 1, 3, 6, 10]
max_num = get_maximum(n)
print("The maximum number is ", max_num)
