# Homework 8 Problem 3
# Linear and Quadratic curve fitting
import pandas as pd
import math
import numpy as np
df = pd.read_csv('speed_data.csv')
print(df)

# Develop a linear fit for reaction component, usin y = mx + b
# Let y = reaction distance, x = speed
# System of equations for linear fit
sumx = 0
sumxsqared = 0
n = len(df.index)
sumxy = 0
sumy = 0
for index, row in df.iterrows():
    sumx = sumx + row['Speed']
    sumy = sumy + row['Reaction Distance']
    sumxsqared = sumxsqared + math.pow(row['Speed'], 2)
    sumxy = sumxy + row['Reaction Distance']*row['Speed']
A = np.array([[sumxsqared, sumx], [sumx, n]])
b = np.array([[sumxy], [sumy]])
m, c = np.matmul(np.linalg.inv(A), b)
print('Linear fit y=mc+c where y is reaction distance, and x is speed')
print(f"m is equal to {m}")
print(f"c is equal to {c}\n")

# Now find a quadratic fit for breaking component, let y = breaking component and x = speed
# y = ax^2 + bx + c
sumx4th = sumx3rd = sumxsquared = sumx = sumxsquaredy = sumxy = sumy = 0
n = len(df.index)

for index, row in df.iterrows():
    sumx = sumx + row['Speed']
    sumy = sumy + row['Breaking Distance']
    sumxsquared = sumxsquared + math.pow(row['Speed'], 2)
    sumx3rd = sumx3rd + math.pow(row['Speed'], 3)
    sumx4th = sumx4th + math.pow(row['Speed'], 4)
    sumxy = sumxy + row['Breaking Distance']*row['Speed']
    sumxsquaredy = sumxsquaredy + row['Breaking Distance']*math.pow(row['Speed'], 2)
A = np.array([[sumx4th, sumx3rd, sumxsquared], [sumx3rd, sumxsquared, sumx], [sumxsquared, sumx, n]])
b = np.array([[sumxsquaredy], [sumxy], [sumy]])
a, b, c = np.matmul(np.linalg.inv(A), b)
print('Quadratic fit y = ax^2 + bx + c where y is breaking distance, and x is speed')
print(f"a is equal to {a}")
print(f"b is equal to {b}")
print(f"c is equal to {c}\n")

# Exponential Curve fitting
expfit = pd.read_csv('exponential_curve_fitting_data.csv')
print(expfit)
# Find an exponential curve fit of y(t)=Ke^(-at).
# Use y = c + bx where c = ln(k) and b = - a
sumtsquared = sumt = sumtlny = sumlny = 0
n = len(expfit.index)
for index, row in expfit.iterrows():
    sumtsquared = sumtsquared + math.pow(row['t'], 2)
    sumt = sumt + row['t']
    sumtlny = sumtlny + row['t']*math.log(row['y'])
    sumlny = sumlny + math.log(row['y'])
A = np.array([[sumtsquared, sumt], [sumt, n]])
B = np.array([[sumtlny], [sumlny]])
b, c = np.matmul(np.linalg.inv(A), B)
k = math.exp(c)
a = -b
print('\nExponential Curve Fitting y(t)=Ke^(-at)')
print(f"a is equal to {a}")
print(f"k is equal to {k}\n")

# Power Law Curve Fitting y = a*x^(b)
# Did not have data but...
# The equation is
# A = np.array([[sumln(x)squared, sumln(x)], [sumln(x), n]])
# B = np.array([[sumln(x)ln(y)], [sumlny]])
# b, c = np.matmul(np.linalg.inv(A), B)
# Where b = b and c = ln(a)
