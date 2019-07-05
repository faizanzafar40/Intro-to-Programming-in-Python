"""
Problem
-------
Write a function that takes a string as an input and shuffles it.
Every time it shuffles the characters, it prints the new string.
It won't stop until the shuffled string is the same with the original one.

Try with a small string e.g. 4-7 characters

For example: given the input abcd, the function prints different shuffles like:
 acbd
 dbca
 bdca
 ...
 ...
 abcd

 Notice the function stops printing since the original string is found again

 Hints:
 1. String can be converted to list with list()
 2. Use the shuffle function from module "random"
 3. You can join a list of characters into a string like this- "".join(["a", "b", "c", "d")
    This produces the string "abcd" again from list
"""

import random
def shuffle_game(text):
    l=list(text)
    m=None
    while(text!=m):
        a=random.sample(l,4)
        m="".join(a)
        print(m)

input_text = input("Enter a text (4-8 characters long): ")
shuffle_game(input_text)
