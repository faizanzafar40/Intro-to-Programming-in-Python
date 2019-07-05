"""
You also use for loop inside for loop
here I am printing list of tables from 2 to the limit
provided by the user

"""

limit = int(input("Enter your limit for tables:"))

for i in range(2, limit):
    print("<<<< Table for", i,">>>>")
    for j in range(1, 11): #table of this number 'i' from 1 until 10
        print(i,"x", j,"=", i*j)


