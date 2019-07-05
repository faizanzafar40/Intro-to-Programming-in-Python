

"""Write a program that let the user maintain a listof colors with following features:
- Insert new colors to the end of list
- Remove colors
- Clear the list of colors
- Use filing throughout
"""

i=1

print("<<<ADD COLORS>>>")
f= open("colors.txt","r+")
a = f.read()

print("COLORS List:", a)
print("1. Insert item:")
print("2. Remove item: ") 
print("3. Clear list: ")
print("0. Exit")

f.close()

while(i!=0):

    b = int(input("Enter your option: "))

    if(b==1):

        f= open("colors.txt","a+")
        c=str(input("Enter a new item: "))
        f.write(c+"\n")
        f.close()
        f= open("colors.txt","r+")
        d = f.read()
        print("COLORS List:", d)
        print("1. Insert item:")
        print("2. Remove item: ") 
        print("3. Clear list: ")
        print("0. Exit")
        f.close()
        
    elif(b==2):

        m=str(input("Which item to remove: "))
        f= open("colors.txt","r")
        lines = f.readlines()
        f= open("colors.txt","w")
        for i in lines:
            if i.strip("\n") != m:
                f.write(i)
        f.close()
        f= open("colors.txt","r+")
        g = f.read()
        print("COLORS List:", g)
        print("1. Insert item:")
        print("2. Remove item: ") 
        print("3. Clear list: ")
        print("0. Exit")

    elif(b==3):

        f= open("colors.txt","w+")
        z=f.write("")
        print("COLORS List:", z)
        print("1. Insert item:")
        print("2. Remove item: ") 
        print("3. Clear list: ")
        print("0. Exit")
        f.close()

    elif(b==0):

        i=0  
        print("Goodbye!")
i=i+1
