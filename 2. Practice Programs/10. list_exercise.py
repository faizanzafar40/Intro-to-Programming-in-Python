'''
Take a list and write a program that prints out all the 
elements of the list that are less than 13.
'''

test_list = [1, 1, 2, 3, 5, 8, 13, 21, 4, 55, 9]

for i in test_list:
    if(i < 13):
        print("Values from list less than 13: ", i)
