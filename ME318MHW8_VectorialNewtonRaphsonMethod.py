import numpy as np
import math

# Problem 1
print("Problem 1")
# Find intersection of two curves give close to (4,-4) using the vectorial-newton-raphsons method
# x^2 + y^2 = 16
# e^(x/3) +y/3 = 1
# Define the functions
def f(x,y):
    return math.pow(x, 2) + math.pow(y, 2) - 16
def g(x, y):
    return math.exp(x/3) + (1/3)*y -1
# Define the Jacobian
def jacobian(x,y):
    return np.array([[2*x, 2*y], [1/3*math.exp(x/3), 1/3]])
# Use the Vectorial Newton Raphson's Method to find the intersection.
# Perform until approximation accuracy of 10^-6 and approximation evaluates less than 10^-7
initial_guess = np.array([[4, -4]])
x = np.array([0, initial_guess[0,0]])
y = np.array([0, initial_guess[0,1]])
while (math.sqrt(math.pow(x[-1] - x[-2], 2) + math.pow(y[-1] - y[-2], 2)) > math.pow(10, -6)) and (math.sqrt(math.pow(f(x[-1], y[-1]), 2) + math.pow(g(x[-1], y[-1]), 2)) > math.pow(10, -7)):
    previous_array = np.array([[x[-1]], [y[-1]]])
    function_array = np.array([[f(x[-1], y[-1])], [g(x[-1], y[-1])]])
    jacobian_array = np.asarray(jacobian(x[-1], y[-1]))
    new_array = previous_array - np.matmul(np.linalg.inv(jacobian_array), function_array)
    x = np.append(x, new_array[0])
    y = np.append(y, new_array[1])
xfinal = x[-1]
yfinal = y[-1]
solution = np.array([xfinal, yfinal])
print(f"The intersection is {solution}")




