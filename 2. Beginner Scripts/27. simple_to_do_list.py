
"""Write a program that let the user maintain a todo list with following features:

- Insert new items to the end of list
- Remove specific item
- Clear the list
"""

i=1
print("<<<TODO LIST APP>>>")
a = []
print("TODO List:", a)
print("1. Insert item:")
print("2. Remove item: ") 
print("3. Clear list: ")
print("0. Exit")

while(i!=0):

    b = int(input("Enter your option: "))

    if(b==1):

        c=str(input("Enter a new item: "))
        a.append(c)
        print("TODO List:", a)
        print("1. Insert item:")
        print("2. Remove item: ") 
        print("3. Clear list: ")
        print("0. Exit")

    elif(b==2):

        m=str(input("Which item to remove: "))
        a.remove(m)
        print("TODO List:", a)
        print("1. Insert item:")
        print("2. Remove item: ") 
        print("3. Clear list: ")
        print("0. Exit")

    elif(b==3):

        a.clear()
        print("TODO List:", a)
        print("1. Insert item:")
        print("2. Remove item: ") 
        print("3. Clear list: ")
        print("0. Exit")

    elif(b==0):
        i=0  

i=i+1