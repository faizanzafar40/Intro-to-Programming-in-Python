"""Write a program that let the user maintain a todo list with following features:

- Insert new items to the end of list
- Remove specific item
- Clear the list
- Save the list in a file
"""


# STEP 1: generate todo list from the file "data.txt"
todo = []
file = None
try:
    file = open('data.txt', 'r+')
    # todo = file.readlines()   <--- I am not using this, because readlines() are returning with '\n' characters, try it to see
    todo = file.read().splitlines()
except FileNotFoundError as fnf:
    print("File doesn't exist yet!")
except Exception as e:
    pass
finally:
    if(file != None):
        file.close()


# STEP 2: Display todo list and options to the user and run until user exits
option = -1

print("")
print("<<<<<<<<< TODO LIST APP >>>>>>>>>>>")
while(option != '0'):
    print("")
    print("TODO List: ", todo)
    print("1. Insert Item")
    print("2. Remove Item")
    print("3. Clear List")
    print("0. Exit")
    option = input("Enter your option:")

    if(option == '1'):
        item_to_insert = input("Enter a new Item:")
        todo.append(item_to_insert)

    elif(option == '2'):
        item_to_remove = input("Which item to remove:")
        todo.remove(item_to_remove)
    elif(option == '3'):
        todo.clear()
    elif(option == '0'):
        continue


# STEP 3: Save todo list back to file as it is, note: I aim to overwrite the file to compensate changes done to list
# Same procedure as Step1 except now we are writing to file
# I am using for loop on our latest todo list and saving each item on a separate line in file

file = None
try:
    file = open('data.txt', 'w+')
    for item in todo:
        file.write(item)
        file.write('\n')

except FileNotFoundError as fnf:
    print("File doesn't exist yet!")
except Exception as e:
    pass
finally:
    if(file != None):
        file.close()
