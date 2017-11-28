# Import some things like a basic file manipulation library
import os
import sys

# I need that sys library to do some magical shit here
source_path = str(sys.argv[1])

# Get the list of folders inside the source folder
def GetFolders (source):
	# This is the actual listing of everything
	contents = os.scandir(source)
	#Initialize a list. I probably don't have to do this
	#dirs = []
	# We're stripping out only the directories and appending them into that list we just made
	for entry in contents:
		if entry.is_dir():
			dirs.append(entry.path)
	# Send it all back somewheres
	return(dirs)

# Get that list we made in the function into this other stupid variable
folders = GetFolders(source_path)
# Now print it all just to prove to myself that I did a thing
for folder in folders:
	print(folder)
    
    
#Ex:
#PS C:\windows\ccmcache> python X:\Python\test.py c:\users\aogden
#c:\users\aogden\.android
#c:\users\aogden\AppData
#c:\users\aogden\Application Data
#c:\users\aogden\Contacts
#c:\users\aogden\Cookies
#c:\users\aogden\Desktop
#c:\users\aogden\Documents
#c:\users\aogden\Downloads
#c:\users\aogden\Favorites
#c:\users\aogden\Links
#c:\users\aogden\Local Settings
#c:\users\aogden\Music
#c:\users\aogden\My Documents
#c:\users\aogden\NetHood
#c:\users\aogden\OneDrive
#c:\users\aogden\Pictures
#c:\users\aogden\PrintHood
#c:\users\aogden\Recent
#c:\users\aogden\Saved Games
#c:\users\aogden\Searches
#c:\users\aogden\SendTo
#c:\users\aogden\Start Menu
#c:\users\aogden\Templates
#c:\users\aogden\Videos
#PS C:\windows\ccmcache>