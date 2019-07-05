"""
here I am
using 'while' loop to simulate three password
attemps for logging into any system
"""


counter = 0

while(counter < 3):
    password = input("Please enter your Password:")
    if(password == 'bilal123'):
        print("Welcome, Bilal")
        break
    else:
        print("Wrong password, try again!!")

    counter = counter + 1 #this will increase the counter value by 1 for every loop iteration


