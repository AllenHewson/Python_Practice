# https://www.youtube.com/watch?v=GB9ByFAIAH4
import numpy as np

# CREATING ARRAYS AND ARRAY INFORMATION
print('CREATING ARRAYS AND ARRAY INFORMATION')
# One dimensional array
a = np.array([1, 2, 3], dtype='int32')
print(a)
# Two Dimensional Array
b = np.array([[1.2, 2.3, 3.1], [6.9, 4.3, 6.4]])
print(b)
# Get Dimension
print(b.ndim)
# Get Shape
print(a.shape)
# Get Type
print(a.dtype)
# Get Size
print(a.itemsize)
# Get Total Size (Number of elements)
print(a.size)
# Get total number of bites(a.size*a.itemsize)
print(a.nbytes)

# ACCESSING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC.
print('ACCESSING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC.')
# (Indexing starts at 0)
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
# Get a specific element [r, c]
print(a[1, 5])
print(a[1, -2])
# Get a specific row
print(a[0, :])
# Get a specific column
print(a[:, 2])
# Getting a little more fancy [startindex:endindexx:stepsize]
print(a[0, 1:6:2])
#Changing elements
a[1,5]=20
print(a)
a[:, 2] = [5]
print(a)
a[:, 2] = [1,2]
print(a)
# 3-D Example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
#Get specific element in 3-D (work outside in)
#To get the number 4 (group, row, column)
print(b[0,1,1])
print(b[:,1,:])
# Replace in 3-D
b[:,1,:] = [[9,9],[8,8]]
print(b)

# INITIALIZING DIFFERENT TYPES OF ARRAYS
print('INITIALIZING DIFFERENT TYPES OF ARRAYS')
# All 0's Matrix
print(np.zeros((2, 3)))
# All 1's Matrix
print(np.ones((4,2,4)))
# Any other number
print(np.full((2,2), 99, dtype='float32'))
# Any other number (full_like) same size but a single number
print(np.full_like(a, 4))
# Random Decimal Numbers Matrix
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))
# Random Integer Values Matrix
print(np.random.randint(5, 8, size=(3, 3)))\
# Identity matrix
print(np.identity(3))
# Repeat an array
arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 3)
print(r1)
# To change axis, make arr multidimensional then specify axis
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)
# Be careful when copying arrays
a = np.array([1, 2, 3])
b = a
print(b)
b[0] = 100
print(a)
# b and a are linked, so changing the value of one changes the value of the other
# To prevent this use the .copy
a = np.array([1, 2, 3])
b = a.copy()
print(b)
b[0] = 100
print(a)

# BASIC MATHEMATICS
print('BASIC MATHEMATICS')
a = np.array([1, 2, 3, 4])
print(a)
# Element wise addition
print(a + 2)
# Element wise subtraction
print(a - 2)
# Element wise multiplication
print(a * 2)
# Element wise division
print(a / 2)
# Element wise power
print(a ** 2)
# Math with another array element wise
b = np.array([1, 0, 1, 0])
c = a + b
print(c)
c = a * b
print(c)
# Take the sin element wise
print(np.sin(a))

# LINEAR ALGEBRA
print('LINEAR ALGEBRA')
a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)
# Matrix Multiplication
c = np.matmul(a, b)
print(c)
# Find the Determinant
i = np.identity(3)
print(np.linalg.det(i))
# Find the inverse
b = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
binv = np.linalg.inv(b)
print(binv)
# So many more linear algebra functions can be found in numpy documentation

# STATISTICS
print('STATISTICS')
data = np.array([[1, 2, 3],[4, 5, 6]])
# Find min and max
print(np.min(data))
print(np.max(data))
# Doing this on an axis basis
print(np.min(data, axis=1))
# Sum the elements
print(np.sum(data))
# You can also do this by axis
print(np.sum(data, axis=0))

# REORGANIZING ARRAYS
before = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(before)
# Reorganize the shape
after = before.reshape((8,1))
print(after)
# Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
v3 = np.vstack([v1, v2])
print(v3)
# Horizontal Stack
h1 = np.array([[1, 2, 3, 4],[1, 2, 3, 4]])
h2 = np.array([[5, 6, 7, 8],[5, 6, 7, 8]])
h3 = np.hstack([h1, h2])
print(h3)

# BOOLEAN MASKING AND ADVANCED INDEXING
data = np.array([[1, 123, 412, 23, 32, 53, 321, 46, 54],[3, 123, 412, 53, 32, 112, 55, 32, 43]])
print(data)
# Greater than, less than boolean
datagreaterthan50 = data > 50
print(datagreaterthan50)
# Indexing by <, >, =
print(data[data > 50])
# Indexing with a list in Numpy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 5]])
# If any data in each column is greater than 50
print(np.any(data > 50, axis=0))
# If all data in each column is greater than 50
print(np.all(data > 50, axis=0))
# More conditions
a = ((data > 50) & (data < 100))
print(a)