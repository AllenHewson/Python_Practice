import os
from pathlib import Path
# This file sorts the files in the example folder organizeme. It can be applied to other folders if it is saved in them.
# First create a dictionary that is going to sort the respective suffixes into their document types.
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# Next create a function to show that we can sort individual items using the dictionary
def PickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    # If the file type doesn't exist, MISC should be returned.
    return 'MISC'


# Now create a function to organize the directory
# Use the os function scandir to check through everything in our directory
# Use the Path function from pathlib to find the path of each item in the directory
def OrganizeDirectory():
    for item in os.scandir():
        # If the item is already a directory this should be skipped
        if item.is_dir():
            continue
        # Extract the file path for each item in the directory
        filePath = Path(item)
        # Now isolate the suffix of each item as the filetype
        filetype = filePath.suffix.lower()
        # Use the previously defined PickDirectory function to organize each filetype
        directory = PickDirectory(filetype)
        # Cast the directory to a path to help with file movement
        directoryPath = Path(directory)
        # Use a conditional, basically if the directory that our script paths to does not exist
        # Then a new directory with that name should be created
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # Add the file to that directory
        filePath.rename(directoryPath.joinpath(filePath))

# BEFORE RUNNING CODE, PROGRAM SHOULD BE SAVED WITHIN DIRECTORY THAT NEEDS ORGANIZING IN.
OrganizeDirectory()