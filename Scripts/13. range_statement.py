"""
here I am
using range statement with for loop 
to print only even numbers upto user specified limit
"""

limit = int(input("Please provide a limit for even numbers:"))

for n in range(0,limit):
    if(n%2==0):
        print(n)

