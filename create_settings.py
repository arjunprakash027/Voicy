import json
 
# Data to be written
dictionary = {
    "name":'en-US-Wavenet-D',
    "lang_code":'en-in',
    "speaking_rate": 1.0
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("settings.json", "w") as outfile:
    outfile.write(json_object)