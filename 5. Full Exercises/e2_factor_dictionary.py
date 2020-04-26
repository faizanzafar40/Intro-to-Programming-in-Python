"""
Problem
-------
This is an easy one. Take a number as input (say number 10)
For each number between 2 and the given number (i.e. 10) generate a dictionary of factors for non-prime numbers.
Put the code in a function and return the dictionary.
Note: dictionary is a container like list but with key value pair and we use curly brackets instead of square e.g
names_list = ['john', 'tom', 'sam']
names_dict = { 'name':'john', 'name':'tom', 'name':'sam' }

You can import the factors function, created previously.

For example, if the given input is 10, the output should be:
{
    4: [2, 2],
    6: [2, 3],
    8: [2, 2, 2],
    9: [3, 3],
    10: [2, 5]
}
Notice that each number in the keys is a non-prime number, and it is associated with a list of its factors.

Hints:
1. A number is a prime number if it has only one factor, i.e. itself.

"""

def isPrime(number):
    for i in range(2,number):
        if number%i==0:
            return False
            break
    else:
        return True

def get_factors(number):
    factors=[]
    for i in range(2,number+1):
        while(number%i==0):
            number=number//i
            factors.append(i)            
    return factors

def get_non_prime_factors(number):
    a={}
    for i in range(2,number+1):
        if not isPrime(i):
            a.update({i:get_factors(i)})
    return a


limitRange=int(input("Enter the range: "))
res=get_non_prime_factors(limitRange)
print(res)
