# To read a file use
f = open('./Exercise Files/inputFile.txt', 'r')

# now print the file
## print(f.read())

# Show that you can iterate through each line
## count = 0
## for line in f:
   ## print(f"{count} {line}")
   ## count += 1

# Print everyone who passed the test, signified by P rather than F tag
## for line in f:
  ## line_split = line.split()
    ## if line_split[2] == "P":
       ## print(line)

# Now write a new file that contains all of the people who passed the test
passFile = open('PassFile.txt', 'w')
failFile = open('failFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
# Now create a new file that contains all of the people who failed the test
    else:
        failFile.write(line)

# After using a file always close it to prevent potential consequences
f.close()
passFile.close()
failFile.close()