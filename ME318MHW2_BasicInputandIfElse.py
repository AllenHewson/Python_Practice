# Skip Problem 1

# Problem 2. Ask how many siblings the user has, then thank them for telling the program
num_of_siblings = input('How many siblings do you have? ')
print(f"Thank you for letti"
      f""
      f"ng me know that you have {num_of_siblings} siblings!")

# Problem 3. Ask for the users age, then respond based on their age
age = int(input('How old are you? '))
if (age>0) and (age<5):
    print('Oh that''s so cute cute!')
elif (age>=5) and (age<14):
    print('Oh, how is school going?')
elif (age>=14) and (age<19):
    print('So, how do you like high school?')
elif (age>=19) and (age<25):
    print('Are you in college?')
elif (age>=25) and (age<55):
    print('Oh, what do you do for a living?')
elif (age>=55) and (age<70):
    print('Do you have any grand children?')
elif (age>=70):
    print('Stay healthy and beware the corona virus!')





