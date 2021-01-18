#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # (firstargument is the file to act on, second is what it is used for. w means writing.
  # The + means that it should be added if it doesn't exist
  ## f = open("textfile.txt", "w+")
  
  # Open the file for appending text to the end
  # a means to append the data to the end of the file
  # r means to read the file
  ## f = open("textfile.txt", "a")
  f = open("textfile.txt", "r")

  # write some lines of data to the file
  ## for i in range(10):
    ## f.write(f"This is line {i} \r\n")
  
  # close the file when done
  ## f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    contents = f.read()
    print(contents)

  # To read line by line
  if f.mode == 'r':
    fl = f.readlines()
    for x in fl:
      print(x)
if __name__ == "__main__":
  main()
