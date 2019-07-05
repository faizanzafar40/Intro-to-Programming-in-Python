"""
Problem
-------
Take an integer number as input and return a list of its factors.
Make a function out of this code and name the function "get_factors".
For example, if the user gives an input 12, the function should return [2, 2, 3]
Therefore, if we multiply all the elements of the result list, we should get back the original number.

If this seems a bit hard, at first return a list of numbers that divide the input
and then try to get to the final answer.

Hint: 
1. You can call the function "get_factors" from inside itself.
2. The input function returns string, not a number. You need to convert it to a proper type.
3. You can join two lists simply with the "+" sign.
4. // is integer division, i.e. 5 / 2 = 2.5 but 5 // 2 = 2
"""


def get_factors(number):
    factors=[]
    for i in range(2,number+1):
        while(number%i==0):
            number=number//i
            factors.append(i)            
    return factors

input_number = int(input("Enter a number: "))
all_factors = get_factors(input_number)

print("The factors are", all_factors)
