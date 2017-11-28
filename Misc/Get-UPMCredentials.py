# Intended to search a specified profile folder to gather a list
# of profiles in the folder. Then searches for a folder named
# "credentials" inside each individual profile and lists any files
# inside that folder.
# Import some things like a basic file manipulation library
import os
import sys
from os.path import exists

# Get the list of folders inside the source folder
def GetChildren (source, type):
	# This is the actual listing of everything in our folder
	contents = os.scandir(source)
	#Declare a list. <s>I probably don't need to do this</s>
	#Edit: It turns out that Python gets pissed if I don't declare this now
	children = []
	# We're stripping out only the child items of the type requested and 
	# appending them into that empty list we just made
	for entry in contents:
		if entry.is_dir() and type == 'dir':
			children.append(entry.path)
		elif entry.is_file() and type == 'file':
			children.append(entry.path)
	# Send it all back somewheres
	return(children)

# Use this function for all output. It just prints to the console and writes to a log file
# at the same time.	
def WriteLog (path, value):
	print(value)
	with open(path, "a") as log_file:
		log_file.write(value + "\n")

# I need that sys library to turn that command line argument into a string so I can
# get that list we made in the function into this other stupid variable. If the argument
# isn't included we can still prompt the user for it
if len(sys.argv) == 1:
	folders = GetChildren(input('Source folder: '), 'dir')
else:
	folders = GetChildren(str(sys.argv[1]), 'dir')

log_path = "C:\\temp\\logthis.log"

for folder in folders:
	if os.path.exists(folder + "\\credentials"):
		subcontents = []
		subcontents = GetChildren(folder + "\\credentials", 'file')
		if len(subcontents) >= 1:
			WriteLog(log_path,folder)
			for folder in subcontents:
				WriteLog(log_path,"\t" + folder)
	else:
		WriteLog(log_path,folder)
