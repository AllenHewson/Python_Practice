# Skip Problem 1
# Problem 2
print("Problem 2")
# Use numerical procedures to find all real roots of the polynomial function f(x) = x^(3) - 4.9x^(2) + 6.73x - 2.011
# The accuracy should be less than 10^(-5)

# In order to do this plot the function to get a rough estimate of where the roots are, then use the bisection method
# to narrow down the root to 0.01 accuracy, finally use the newton raphsons method to narrow the accuracy down further.
import math
import numpy as np
import matplotlib.pyplot as plt
from Bisection_Method_Function import bisection_method
# Define the function
def func(x):
    return math.pow(x, 3) - 4.9*math.pow(x, 2) + 6.73*x - 2.011
# Have to  use np.vectorize to let the function accept an array like x
func2 = np.vectorize(func)
# Plot the function
x = np.linspace(0,5,100)
y = (func2(x))
plt.plot(x, y)
plt.grid()
plt.title('Plot of the function')
plt.xticks(np.linspace(0,5,11))
plt.show()

# From this it seems that there are roots between 0 and 0.5, 1.5 and 2.0, and 2.5 and 3
# Now run the bisection method for each of these bounds with accuracy 0.05 to narrow it down for the Newton Raphson
root1 = bisection_method(func, 0, 0.5, 0.001)
root2 = bisection_method(func, 1.5, 2, 0.001)
root3 = bisection_method(func, 2.5, 3, 0.001)

# The Newton Raphson's function is defined in another file, it will be used to finalize the roots.
from NewtonRaphsons_Method_Function import newton_raphsons_method


def dfunc(x):
    return 3*math.pow(x, 2) - 9.8*x + 6.73


root1 = newton_raphsons_method(func, dfunc, root1, math.pow(10, -5))
root2 = newton_raphsons_method(func, dfunc, root2, math.pow(10, -5))
root3 = newton_raphsons_method(func, dfunc, root3, math.pow(10, -5))
print(f"Root 1 is {root1}")
print(f"Root 2 is {root2}")
print(f"Root 3 is {root3}")