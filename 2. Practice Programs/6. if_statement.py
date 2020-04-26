"""
here I am
using 'if' statement to make decisions based
on user age
"""

age = int(input("Enter your age:"))

if(age >= 18):
    print("You can watch R-Rated movies!")
elif(age > 13 and age <= 17):
    print("You can watch PG-13 movies!")
else:
    print("You should only watch Cartoon Network")