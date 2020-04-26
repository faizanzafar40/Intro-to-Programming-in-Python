'''
Write a function(is_palindrome) that checks if a word/string is palindrome or not

A palindrome is a word which spells the same backwards
'''

def is_palindrome(word):
    a = list(word)
    b = a[::-1] #reverse list
    if(a==b):
        return True
    else:
        return False

word = str(input("Enter a word: "))

if(is_palindrome(word)):
    print("Yes", word, "is a palindrome!")
else:
    print("No", word, "is not a palindrome!")