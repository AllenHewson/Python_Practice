import numpy as np
# Problem 1
print('Problem 1')
# Take two number inputs and a limit input from the user. Then perform the Fibonacci sequence with two initial inputs
# until the limit and display the numbers in a sequence.
Fib1 = float(input('Enter the first initial input: '))
Fib2 = float(input('Enter the second initial input: '))
limit = float(input('Enter a limit for the sequence: '))
Fib = np.array([Fib1, Fib2])
new_value = 0
while Fib[-2] + Fib[-1] <= limit:
    new_value = Fib[-1] + Fib[-2]
    Fib = np.append(Fib, new_value)
print(f"The Fibonacci Sequence with these inputs is {Fib}")

# Problem 2
print('Problem 2')
# Ask a user how many integers they want to enter into an array, if they don't enter an integer then they will be warned
# and the program will continue to ask for an 1integer until they provide one.
# It will then display an array with all the integers, an array with all even numbers and an array with all odd.
num_integers = int(input('How many integers would you like to enter? '))
array = np.array([])
for i in range(0, num_integers):
    is_not_integer = True
    integer = input('Enter an integer that you would like to add to your array -> ')
    while is_not_integer:
        try:
            integer = int(integer)
            is_not_integer = False
        except ValueError:
            print('Hey that is not an integer try again!')
            integer = input('Enter an integer that you would like to add to your array -> ')
    array = np.append(array, integer)
even_array = np.array([])
odd_array = np.array([])
for i in array:
    if i % 2==0:
        even_array = np.append(even_array, i)
    else:
        odd_array =np.append(odd_array, i)
print(f"The overall array is {array}")
print(f"The even array is {even_array}")
print(f"The odd array is {odd_array}\n")

# Problem 3
print('Problem 3')
M1 = np.array([[2, 1, 7], [5, 4, 1], [3, 1, 5]])
M2 = np.array([[2, 7], [4, 9], [5, 2]])
M3 = M1 + np.matmul(M2, M2.T)
print(f"The solution matrix is \n {M3}")
detM3 = np.linalg.det(M3)
print(f"The determinant is {detM3}")






