'''
Write a program that asks user the range 
upto which the program will print the prime numbers
'''

n = int(input("Enter your number: "))
i=2
for a in range(i,n):
        for b in range(2,a):
                if(a%b==0):
                        break
        else:
                print(a)               