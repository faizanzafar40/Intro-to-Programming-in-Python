"""
Problem
-------
Write a function that takes a list as an input and returns a shuffled list.
You can use the randint function from random module but not the shuffle function.

For example: if the input is [1, 2, 3, 4], the output can be [3,2,4,1] etc.
"""

import random
def shuffle(numbers):
    a=[]
    while len(a)!=len(numbers):
        x=random.randint(0,(len(numbers)-1))
        if numbers[x] not in a:
            a.append(numbers[x])
    return a
        

list_at_the_beginning = [1, 2, 3, 4, 5]
print("Shuffled list: ", shuffle(list_at_the_beginning))
