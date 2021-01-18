#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  print(now.strftime("%a, %d, %B, %y"))
  # Reference date formatting below. (Lower case is abreviated, uppercase is full)
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month


  # %c - locale's date and time, %x - locale's date, %X - locale's time
  # These will display correct date time and format for the location it is called
  print(now.strftime("Local date and time: %c"))
  print(now.strftime("Local date: %x"))
  print(now.strftime("Local time: %X"))

  #### Time Formatting ####
  print(now.strftime("Current Time %I:%M:%S:%p"))
  print(now.strftime("24-Hour time: %H:%M"))
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  

if __name__ == "__main__":
  main();
