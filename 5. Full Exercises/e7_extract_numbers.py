"""
Problem
-------
Write a function that takes a number as input and return all the individual numbers in it as a list

For example: if the input is 18382109, the output should be [1, 8, 2, 8, 2, 1, 0, 9]
"""

def extract_numbers(number):
    n=list(number)
    l=[]
    for i in n:
        a=int(i)
        l.append(a)
    return l

number=input("Enter the number: ")
l = extract_numbers(number)
print(l)
