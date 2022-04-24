import json

turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

with open('output.json', 'w') as json_file: #opens file in write mode
    json.dump(turn_to_json, json_file) #uses json.dump() to write to the file json_file.

#json.dump() takes two arguments: first the data object, then the file object you want to save.
