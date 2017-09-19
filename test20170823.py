import json

# with open('./json.json', 'r') as jsonFile:
#     data = json.load(jsonFile)
#     print(data)
#

jsonData = [
  {
    "uuid": "8EDBCD47-2F39-4618-BAE1-F1A3910F533A",
    "password": "abc123"
  },
  {
    "uuid": "8EDBCD47-2F39-4618-BAE1-F1A3910F533A",
    "password": "abc123"
  },
  {
    "uuid": "中文",
    "password": "abc123"
  }
]
# json.dump(json_dict, f, indent=4)，
with open('./json2.json', 'w') as jsonFile2:
    # jsonFile2.write(json.dumps(jsonData, ensure_ascii=False, indent=4))
    print(json.dumps(jsonData, ensure_ascii=False, indent=4))