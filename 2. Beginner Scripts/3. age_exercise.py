'''

Write a program that asks user name and age and tell them when are they going to be 100 years old?

'''

name = str(input("Enter your name: "))
print("Welcome,", name)
age = int(input("Enter your age: "))
new_age = 2019 - age + 100
print(name, "you will be 100 years old in", new_age)
