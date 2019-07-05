"""
here I am
using continue statement with for loop 
to skip any even numbers in the list
"""

numbers = [1,2,3,4,5,6,7,8,12,14,13,23,22,76,55]

for n in numbers:
    if(n%2==0):
        continue #loop will reset from here with next iteration
    print(n)