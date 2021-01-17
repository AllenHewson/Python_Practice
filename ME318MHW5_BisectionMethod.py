# Problem 1
import numpy as np
import math
print('Problem 1')
# Write a function that takes in a matrix as an input and outputs the number of rows and columns.
# It will also output the transverse of the matrix multiplied by the inverse of the matrix multiplied by its transpose
def matrix_info(m):
    num_rows, num_cols = m.shape
    r = np.matmul(np.linalg.inv(np.matmul(m.T, m)), m.T)
    print(f"Number of rows is {num_rows}.")
    print(f"Number of cols is {num_cols}.")
    print(f"Matrix R is \n {r}")
matrix = np.array([[2, 1, 7], [5, 4, 1], [3, 1, 5]])
matrix_info(matrix)

# Problem 3
print("\n Problem 2")
# Use The bisection method to find a root of the polynomial f(x) = x^3 - 4 between 1 and 2 to within 0.0005 accuracy
# Create a bisection method function
def bisection_method(func, lowerbound, upperbound, error_margin):
    while abs(upperbound - lowerbound) >= abs(error_margin):
        middle = (upperbound + lowerbound)/2
        if func(lowerbound)*func(middle) < 0:
            upperbound = middle
        else:
            lowerbound = middle
    # display which bound evaluates closer to 0
    root = 0
    if abs(func(lowerbound)) < abs(func(upperbound)):
        root = lowerbound
    else:
        root = upperbound
    return root
# Now define the function
def func(x):
    return math.pow(x, 3) - 4
# Call the bisection method function with the given parameters
print(f"The root is {bisection_method(func, 1, 2, 0.0005)}")
