"""Slicing syntax

any container can use slicing syntax in python

e.g

name = "hello"

is internally stored in memory as:

|   h	|   e	|   l	|  l 	|   o	|   	|
|---	|---	|---	|---	|---	|---	|
|  0 	|   1	|   2	|   3	|   4	|   5	|
|  -6 	|   -5	|   -4	|   -3	|   -2	|  -1	|
|   	|   	|   	|   	|   	|   	|
|   	|   	|   	|   	|   	|   	|


"""


name = "arnold"

print(name[1:3])
