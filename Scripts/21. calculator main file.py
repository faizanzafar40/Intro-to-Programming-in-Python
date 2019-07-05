'''
Main file for calculator_module
'''

import calculator_module

a=float(input("first num: "))

b=float(input("sec num: "))

inp = int(input("Enter 1 for add\nEnter 2 for sub\nEnter 3 for mult\nEnter 4 for div\nEnter 5 for power\nEnter 6 for mod\n"))

if(inp==1):
    q=float(calculator_module.add(a, b))
    print(q)
elif(inp==2):
    w=float(calculator_module.sub(a, b))
    print(w)
elif(inp==3):
    e=float(calculator_module.mult(a, b))
    print(e)
elif(inp==4):
    r=float(calculator_module.div(a, b))
    print(r)
elif(inp==5):
    t=float(calculator_module.power(a, b))
    print(t)
elif(inp==6):
    y=float(calculator_module.mod(a, b))
    print(y)
else:
    print("exit")
