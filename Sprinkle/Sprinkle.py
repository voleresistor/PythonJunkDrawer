import json
import datetime

def get_json(file):
    """
    Load JSON data into memory
    file: the path to the data file
    """
    with open(file) as json_file:
        json_data = json.load(json_file)
    json_file.close()
    return json_data

def save_json(file, data):
    """
    Save and close data file
    file: path to the data file
    data: data object to save
    """
    with open(file, 'w') as json_file:
        json.dump(data, json_file)
    json_file.close()

# Gather current date and time
#day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3:'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
day = datetime.datetime.now().weekday()
time = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute)

# int(time) >= int(sched) - 1 & int(time) <= int(sched) + 1

# Get source file from arguments
sourcefile = 'x:\\Git\\Python\\Sprinkle\\test.conf'

# Load the config file
d = get_json(sourcefile)

# Determine schedule type
if d["ScheduleType"]["Type"] == 'Static':
    print("Running static schedule.")
elif d["ScheduleType"]["Type"] == 'Interval':
    print("Running interval schedule every %s day(s)." % d["ScheduleType"]["Interval"])

if d["WaterDays"][str(day)]["Enabled"] == '0':
    water_schedule = d["WaterDays"][str(day)]["Schedule"]
    for e in water_schedule:
        if e["Time"] == time:
            i = 1
            for station in e["Duration"]:
                print("Running Station %d for %s minutes." % (i, str(e["Duration"][i-1])))
                i += 1
        else:
            #A timespan here to log time until water event?
            print("Waiting.")

save_json(sourcefile, d)
