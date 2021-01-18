#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    source = path.realpath('textfile.txt')

    # let's make a backup copy by appending "bak" to the name
    destination = source + ".bak"

    # copy over the permissions, modification times, and other info
    ## shutil.copy(source, destination)
    # To copy over other information like modification times
    ## shutil.copystat(source, destination)
    
    # rename the original file
    ## os.rename('textfile.txt', 'newfile.txt')
    
    # now put things into a ZIP archive
    ## root_dir, tail = path.split(source)
    ## shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile('testzip.zip', 'w') as newzip:
      newzip.write("texfile.txt")
      newzip.write("texfile.txt.bak")
if __name__ == "__main__":
  main()
