# Problem 1 set variables then perform calculations
import math
var1 = 1.234
var2 = 7.789
var3 = 1.457
# Plug variables into equations and find solutions
problem1_1 = (var2/var1) + (math.pi*var3) - math.sin(math.pi/4)
print(f"Problem 1.1: {problem1_1}")
problem1_2 = var3 + (var2*math.exp(-var1)) + math.acos(0.2)
print(f"Problem 1.2: {problem1_2}")
problem1_3 = var1 + var2 - math.pow(var2, var1-var3)
print(f"Problem 1.3: {problem1_3}")
problem1_4 = problem1_1 + problem1_2 + problem1_3
print(f"Problem 1.4: {problem1_4} \n")

# Problem 2 set up logic variables than evaluate logical expressions
L1 = True
L2 = False
L3 = False
L4 = True
problem2_a = (L1 and L2) or (not L3 and L4)
print(f"Problem 2.a: {problem2_a}")
problem2_b = (not L1 or not L2) and (L3 or not L4)
print(f"Problem 2.b: {problem2_b}")
problem2_c = problem2_a ^ problem2_b
print(f"Problem 2.c: {problem2_c} \n")

# Problem 3 set up name variables and then concatenate name
firstname = 'Allen'
lastname = 'Hewson'
firstandlastname = f"{firstname} {lastname}"
print('Problem 3:' + ' ' + firstandlastname)


