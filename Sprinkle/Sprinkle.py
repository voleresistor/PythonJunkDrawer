import json

sourcefile = 'x:\\Git\\Python\\Sprinkle\\test.conf'

def get_json(f):
    with open(f) as json_file:
        d = json.load(json_file)
    json_file.close()
    return (d)

def save_json(f, d):
    with open(f, 'w') as json_file:
        json.dump(d, json_file)
    json_file.close()

d = get_json(sourcefile)
print (d["WaterDays"]["Thursday"]["Enabled"])

if d["WaterDays"]["Thursday"]["Enabled"] == "0":
    print("Enabling...")
    d["WaterDays"]["Thursday"]["Enabled"] = "1"
else:
    print("Disabling...")
    d["WaterDays"]["Thursday"]["Enabled"] = "0"

print (d["WaterDays"]["Thursday"]["Enabled"])

save_json(sourcefile, d)
