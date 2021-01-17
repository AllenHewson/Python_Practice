# Problem 1
# Given the second order differential equation:
# d2y/dt2 = 1/m*(-b*dy/dt – ky)
# Solve as a system of first order differential equation using substitution
# Let z1 = y, z2 = dy/dt =dz1/dt, therefore dy2/dt = dz2/dt
# Using the original second order differential equaiton this makes the system of equations
# dz1/dt = z2
# dz2/dt = 1/m *(-b*z2 - k*z1)
# Solve this using the Runge-Kutta 4th method over the interval t = [0, 1] with step size of 0.01. Plot the solution.
import math
import numpy as np
import matplotlib.pyplot as plt
# dDefine the variables and system
m = 100
b = 100
k = 10000
def dzdt(z1, z2):
    value = np.matmul(np.array([[0, 1], [-k/m, -b/m]]), np.array([[z1], [z2]]))
    return value
# The initial condition of the matrix z = np.array([z1], [z2]]) is np.array([[z1], [z2]])
z = np.array([[0.1], [0]])
h = 0.01 # step size
for t in np.arange(h, 1, h):
    rows, cols = z.shape
    k1n = (dzdt(z[0,cols-1] + h/2, z[1, cols-1]))
    k2n = (dzdt((z[0, cols - 1] + (h/2) * k1n[0])[0], (z[1, cols - 1] + (h/2) * k1n[1])[0]))
    k3n = (dzdt((z[0, cols - 1] + (h / 2) * k2n[0])[0], (z[1, cols - 1] + (h / 2) * k2n[1])[0]))
    k4n = (dzdt((z[0, cols - 1] + h * k3n[0])[0], (z[1, cols - 1] + h * k3n[1])[0]))
    zcurrent = z[:, cols - 1][np.newaxis]
    znew = zcurrent.T + (h/6) * (k1n + 2*k2n + 2*k3n + k4n)
    z = z = np.hstack((z, znew))
# Now plot it
t = np.arange(0,1,h)
position = (z[0,:])
velocity = (z[1,:])
plt.plot(t,position, 'r', label='Position (m)')
plt.plot(t,velocity, 'b', label='Velocity(m/s)')
plt.legend()
plt.title('Position and Velocity over Time')
plt.xlabel('Time')
plt.show()