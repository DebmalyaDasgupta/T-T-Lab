import numpy
import numpy as np
a = np.array([1,2,3])

a = np.array([[1, 2], [3, 4]])

a = np.array([1, 2, 3,4,5], ndmin = 2)

a = np.array([1, 2, 3], dtype = complex)
a = np.array([[1,2,3],[4,5,6]])

a.shape
#dimensions
a.ndim

#Resizing an Array

a = np.array([[1,2,3],[4,5,6]])

a.shape = (3,2)

a = np.array([[1,2,3],[4,5,6]])

b = a.reshape(3,2)

a = np.arange(24)

x = np.arange(10,20,2)

b = a.reshape(2,4,3)

#Returns the length of each element of array in bytes.

x = np.array([1,2,3,4,5], dtype = np.int8)

print (x.itemsize)

x = np.array([1,2,3,4,5])

print (x.flags)

#Array Creation

#numpy.empty(shape, dtype = float, order = 'C')

#C' for C-style row-major array 'F' for FORTRAN
#style column-major array

x = np.empty([3,2], dtype = int)

#Array with Zero

x = np.zeros(5)

x = np.zeros((5,), dtype = rint)

#Array with Ones

x = np.ones([2,2], dtype = int)

#Array from Existing Data

x = [1,2,3]

a = np.asarray(x)

list = range(5)

it = iter(list) #iter function returns iterator

x = np.fromiter(it, dtype = float)

print (x)

#Extraction by Slicing.

for x in np.nditer(a):
    print (x)

a = np.arange(10)

s = slice(2,7,2) # slice (start ,stop , step)

print (a[s])

b = a[2:7:2]

print (b)

a = np.array([[1,2,3],[3,4,5],[4,5,6]])

print (a)

print ('The items in the second column are:')

print (a[...,1])

print ('The items in the second row are:')

print (a[1,...])

# Now we will slice all items from column 1 onwards

print ('The items column 1 onwards are:')

print (a[...,1:])

a = np.array([0,30,45,60,90])

print ('Array containing sine values:')

sin = np.sin(a*np.pi/180)

print (sin)

print ('\n')

print ('Compute sine inverse of angles. Returned values are in radians.')

inv = np.arcsin(sin)

print (inv)

print ('\n')

print ('Check result by converting to degrees:')

print (np.degrees(inv))

print ('\n')

print ('arccos and arctan functions behave similarly:')

cos = np.cos(a*np.pi/180)

print (cos)

print ()

print ('Inverse of cos:')

inv = np.arccos(cos)

print (inv)

print ('\n')

print ('Tan function:')

tan = np.tan(a*np.pi/180)

print (tan)

print ('Inverse of tan:')

inv = np.arctan(tan)

print (inv)

print ('In degrees:')

print (np.degrees(inv))