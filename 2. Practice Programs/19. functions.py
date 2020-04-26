# loop runs for one particular time
# function can run multiple places in program

def add(a, b):
    return (a+b)

a = int(input("a: "))
b = int(input("b: "))
c = add(a, b)
print(c)

n = int(input("Enter result: "))
if(n > 50):
    print("result > 50")
elif(n > 90):
    print("result > 90")
else:
    print(n, "is the result")     


'''
Built-in functions

print
input
len (len also counts the spaces in strings along with characters)
type
range 
sum
sort (spaces come first, then caps, then small chars in the default sort method)
'''


password = str(input("Enter password: "))
if(len(password) < 8):
    print("password must be 8 chars long")


name = "55"
print(type(name))


number_list=list(range(0,101))
print(number_list)
print(len(number_list))


text="The quick brown fox jumps over the lazy dog"
a=sorted(list(text),reverse=True)
print(a)


colors = ['red','green','blue','white']
colors.append('pink')
colors.insert(colors.index('blue'),'yellow')
colors.sort()
print(colors)

for x in sorted(colors):
    print (x)


from math import sqrt

a = float(sqrt(81))
print(a)

import math
a = float(math.sqrt(81))
print(a)

    


























