import numpy as np
from numpy import random
import matplotlib as plt
import matplotlib.pyplot as pyplot


def separator_line():
    print(20*"-")


print("######## Array Creation #########")


# TODO: Create a numpy array with elements 2, 3 and 4 and retrieve the data type

numpy_array_1 = np.array([2, 3, 4])
print(numpy_array_1)
print(type(numpy_array_1))
print(numpy_array_1.dtype)

separator_line()

# TODO: Create a numpy array with elements 1.2, 3.5 and 5.1 and retrieve data type

numpy_array_2 = np.array([1.2, 3.5, 5.1])
print(numpy_array_2)
print(type(numpy_array_2))
print(numpy_array_2.dtype)

separator_line()

# This is how not to do it

try:
    a = np.array(1, 2, 3, 4)
except Exception:
    print("Sorry, this isn't how numpy creates arrays")

separator_line()

# TODO: Create a two dimensional numpy array with the following elements:
# 1.row: 1.5, 2, 3
# 2.row: 4, 5, 6

array_2d = np.array([[1.5, 2, 3], [4, 5, 6]])
print(array_2d)

separator_line()

# TODO: Create a 3x4 matrix which contains zeros

zero_matrix = np.zeros((3,4))
print(zero_matrix)

separator_line()

# TODO: Create a 2x3x4 matrix which contains ones

one_matrix = np.ones((2,3,4))
print(one_matrix)

separator_line()

# TODO: Create a random 2x3 matrix with values in the rang of [0, 1)

rand_matrix = random.random((2,3))
print(rand_matrix)

separator_line()

# TODO: Create an uninitialized 2x3 matrix

empty_matrix = np.empty((2,3))
print(empty_matrix)

separator_line()

# TODO: Create a numpy array by using the arange() function

new_array = np.arange(10, 30, 5) # excludes last number from range
print(new_array)

separator_line()

# TODO: Create a numpy array by using the linspace() function

lin_array = np.linspace(0, 2, 9) # includes last number in range
print(lin_array)

separator_line()

# TODO: Get 100 points of sin(x) on the interval [0, 2*pi]

x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x) # sin can take vector or matrix as an argument
print(f)

# TODO: Plot sin-function with matplotlib

pyplot.plot(x, f)
pyplot.show()

separator_line()

# TODO: Use the reshape() function to convert an array with 12 elements to a 3x4 matrix

new_array_1 = np.arange(0, 12)
new_matrix = new_array_1.reshape(3,4)
print(new_matrix)

print("######## Basic Operations #########")

# TODO: Apply basic numerical operations, numpy functions and boolean expressions

test_array_1 = np.array([20, 30, 40, 50])
test_array_2 = np.array(4)

separator_line()

result = test_array_1+test_array_2
print(result)

separator_line()

result = test_array_1-test_array_2
print(result)

separator_line()

result = test_array_1*test_array_2
print(result)

separator_line()

result = test_array_1**2
print(result)

separator_line()

print(test_array_1 < 35) # prints bool array indicating where conditions are satisfied or not

separator_line()

# TODO: Create two matrices with 2x2 dimension

A = np.array([[1.5, 2], [4, 5]])
B = np.array([[3, 7], [6, 9.4]])

separator_line()

# TODO: Print number of dimensions of matrix A and its shape

print(A)
print(A.ndim)
print(A.shape)

separator_line()

# TODO: Calculate elementwise product

print(A*B)

separator_line()

# TODO: Calculate matrix product

print(A @ B)

print(A.dot(B))

separator_line()

print("######## Indexing, Slicing, Iterating #########")

# TODO: Create array by np.arange(10)**3

n = np.arange(10)**3

separator_line()

# TODO: Retrieve element at index 2

print(n[2])

separator_line()

# TODO: Get elements at indices 2, 3, and 4 from array 'n' by a slicing operation

print(n[2:5])

separator_line()

# TODO: Create a 3x4 matrix M with numbers from 0-11

M = np.arange(12).reshape(3, 4)

separator_line()

# TODO: Get the row with index 1

print(A[1])
print(A[1, :])
print(A[1, ...])

separator_line()

# TODO: Get the last two rows

print(A[1])
print(A[1, :])
print(A[1, ...])

separator_line()

# TODO: Iterate through M's rows and print them out one by one

for row in M:
    print(row)

separator_line()

# TODO: Iterate through M's elements and print them out one by one

for x in M.flat: # where M.flat is a numpy array
    print(x)

print("######## Shape manipulation #########")

# TODO: Create a 3x4 matrix N with numbers from 0-11

N = np.arange(12).reshape(3,4)

separator_line()

# TODO: Reshape A such that we get a 6x2 matrix

print(N.reshape(6,2))

separator_line()

# reshape creates new matrix
# resize modifies original matrix

# TODO: Use the resize() method to resize A to a 6x2 matrix

print(N.resize(6,2))

separator_line()

# TODO: Transpose A

print(N.T)

print("######## Stacking together different arrays #########")

# TODO: Create two matrices with 2x2 dimension

M1 = np.array([[1, 2], [2, 4]])
M2 = np.array([[5, 6], [0, 7]])

# TODO: Stack A and B together horizontally

print(np.hstack((M1,M2)))

separator_line()

# TODO: Stack A and B together vertically

print(np.vstack((M1,M2)))

separator_line()

print("######## Copies and Views #########")

# TODO: Create array 'original' with first 11 natural numbers

original = np.arange(1, 12, 1)

# TODO: Create a new variable 'copy' and assign array 'original' to it

copy = original

# TODO: Show that 'original' and 'copy' are the same objects

if(id(original)==id(copy)):
    print("Original and copy have same ID")
else:
    print("Original and copy are different")

separator_line()

# TODO: Create a shallow copy of array 'original'

s_copy = original.view()

# TODO: Check if 's_copy' is the same object as 'original'

if(id(original)==id(s_copy)):
    print("Original and shallow copy have same ID")
else:
    print("Original and shallow copy are different")

separator_line()

# TODO: Check if 'original' and 's_copy' share the same data

if(original.data==s_copy.data):
    print("Original and shallow share same data")
else:
    print("Original and shallow have different data")

separator_line()

# TODO: Prove that 'original' and 's_copy' share the same data by changing 1 value of 's_copy' and showing that it changes in 'original'

s_copy[2]= 85

if(original.data==s_copy.data):
    print("Original and shallow share same data")
else:
    print("Original and shallow have different data")

separator_line()

# TODO: Reset 'original'

original = np.arange(1, 12, 1)

# TODO: Create a deep copy of 'original' such that the new object does not share data with 'original'

d_copy = original.copy() 

d_copy[5] = 176 

if(original.data==d_copy.data):
    print("Original and shallow share same data")
else:
    print("Original and shallow have different data")

separator_line()
