# Simple program to generate a new ThinkPy notes file with boilerplate
# Switch syntax for this script is <switch>:<value>
import sys
from os import startfile
from datetime import date

# Rudimentary switch handler
def get_switches():
    temp_dict = dict()
    # Split arguments on the ':' to derive key:value pairs
    for i in range(1, len(sys.argv)):
        switch = sys.argv[i]
        swindex = switch.index(':')
        temp_dict.update({switch[:swindex]: switch[swindex+1:]})
    return temp_dict

def add_boilerplate(file):
    now = date.today()
    file.write('# Think Python chapter %s examples and exercises\n' % (switch_dict['chapter']))
    file.write(f'# {now.month:02d}/{now.day:02d}/%s\n\n' % (now.year))
    file.write('import math\n\n')
    file.write('# Section %s.1\n' % (switch_dict['chapter']))
    file.write('# ' + '*' * 85 + '\n# ')


switch_dict = get_switches()

# Since most work is done from my desk at work, 'path' can just default to
# my home drive dev path
if 'path' not in switch_dict:
    switch_dict.update({'path':'x:\\development\\python'})

try:
    notes_file = open('%s\\ThinkPy%s.py' % (switch_dict['path'], switch_dict['chapter']), 'w')
    add_boilerplate(notes_file)
finally:
    notes_file.close()

startfile('%s\\ThinkPy%s.py' % (switch_dict['path'], switch_dict['chapter']))