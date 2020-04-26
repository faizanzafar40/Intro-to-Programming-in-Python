"""
Problem
-------

Take a numeric pin code as input and let your program crack it by checking different combinations.
print it as you match the combinations
Start with a pin length of 4 and experiment with larger pin codes when done.

Example:
Enter your pincode: 1025

checking combination:  1000
checking combination:  1001
checking combination:  1002
.
.
checking combination:  1024
checking combination:  1025
cracked:  1025


"""
import random

def check_pincode(pin):
    l=list(pin)
    """l=[]
    for i in a:
        x=int(i)
        l.append(x)"""
    pin_length=len(l)
    cracked_code="Random"
    while(pin!=cracked_code):
        cracked_code="".join(random.sample(l,pin_length))
        print("checking combination: ",cracked_code)
    print("cracked: ",cracked_code)

pin=input("Enter the pin: ")
check_pincode(pin)


