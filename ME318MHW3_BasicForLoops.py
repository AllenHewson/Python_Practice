# Problem 1
# Ask the user to enter two numbers, round them into integers, and then sum up all the integers between them
Num1 = round(int(input('Enter your first number here -> ')))
Num2 = round(int(input('Enter your second number here -> ')))
sum = 0
if Num1 < Num2:
    for i in range(Num1, Num2+1):
        sum = sum + i
else:
    for i in range (Num2, Num1+1):
        sum = sum + i
print(f'The sum between the two numbers is {sum}')

# Problem 2
# Ask how many strings the user wants to enter, then take that many strings from the user and display them
num_strings = round(int(input('How many strings would you like to enter? ')))
for i in range(0, num_strings):
    string_entered = input(f'Enter string number {i+1} here -> ')
    print(f"Your string number {i+1} is {string_entered}")

# Problem 3
# Ask the user how many integers they would like to enter and display a message with each integer
# If they enter a number that isn't an integer display an error message and round it to the nearest integer
num_integers = int(input('How many integers would you like to enter? '))
for i in range(1, num_integers + 1):
    integer_entered = input(f"This is loop number {i} and you should enter an integer here -> ")
    try:
        integer_entered = int(integer_entered)
    except:
        integer_entered = float(integer_entered)
    if integer_entered != int(integer_entered):
        integer_entered = round(integer_entered)
        print(f"Hey that is not an integer. I am rounding it to {integer_entered}")
    print(f"Your integer number {i} is {integer_entered}")





