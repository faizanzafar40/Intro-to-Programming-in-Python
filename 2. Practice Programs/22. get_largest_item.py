'''
Given a list of strings(names), write a function(get_largest_item) that takes that list
and returns the item with more number of characters
'''

def f1(names):
    lenlist = []
    for i in names:
        a = len(i)
        lenlist.append(a)
    return lenlist

def get_largest_item(lenlist,names):
    maximum = 0
    namelist = names
    dic = dict(zip(lenlist,namelist))
    for i in lenlist:
        if (i > maximum):
            maximum = i
            s = dic.get(maximum)
    return s

names = ['bilal', 'andrew', 'sarah', 'anna', 'vanessa', 'john']
a = f1(names)
largest_item = get_largest_item(a,names)
print('Largest item in the list is', largest_item)