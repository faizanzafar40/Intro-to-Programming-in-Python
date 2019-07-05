"""
in this program I am trying to find out
if the number user provided is actually a prime number
or not
"""

number = int(input("Enter your number:"))

for n in range(2, number): #dividing by 0 or 1 doesn't make sense so we skip it
    if(number%n == 0): #if it's divisible by any number in range it's not prime
        print(number, "is not a prime number")
        break #we don't need to check furthur 
else: #note that I am using else with for-loop(it has nothing to do with if statement inside for), it will only execute if we don't break from for, for questions regarding this write me 
    print(number, "is a prime number")


