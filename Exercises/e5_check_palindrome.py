"""
Problem
-------

A palindrome is a text which is the same when reversed e.g. hannah, ada, anna, bob, nitin
Write a function that takes a string as an input and
returns True if the string is a palindrome and False otherwise

For example, if the input is "hannah" it should return True, but if the input is "trump" it should return False
"""


def check_palindrome(text):
    a=list(text)
    b=list(text)
    b.reverse()
    l=int(len(a)/2)
    count=0
    for i in range(l):
        if a[i]!=b[i]:
            count=1
            break
    if count==0:
        return True
    else:
        return False


text = input("Enter a string: ")
print("Palindrome: " + str(check_palindrome(text)))
