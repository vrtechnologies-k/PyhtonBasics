
import json

with open(r'D:\Projects\pythonBasics\readjson.json') as f:
    data = json.load(f)
    print(data)
    print(data['name'])
    print(data['Subjects'][0])
    print(data['Subjects'][1])