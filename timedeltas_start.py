#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
# time deltas are spans of time, can be used to perform time based mathematics

# construct a basic timedelta and print it. (Create the class and then pass in the amount of time it should represent)
print(timedelta(days=365, hours=5, minutes=1))

# print today's date (as reference point)
now = datetime.now()
print(f"Today is : {now}")

# print today's date one year from now
print(f"One year from now it will be: {str(now + timedelta(days=365))}")

# create a timedelta that uses more than one argument
print(f"In two days and three weeks it will be: {now + timedelta(days=2, weeks=3)}")

# calculate the date 1 week ago, formatted as a string
print(f"The date one week ago was: {now - timedelta(weeks=1)}")

### How many days until April Fools' Day?
today = date.today()
april_fools_date = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if april_fools_date < today:
    print("April Fool's day already went by %d days ago" % ((today - april_fools_date).days))
    april_fools_date = afd.replace(year = today.year + 1)
# Now calculate the amount of time until April Fool's Day  
time_to_afd = april_fools_date - today
print(f"It's just {time_to_afd.days} days until April Fool's day")

