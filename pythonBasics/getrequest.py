
import requests

# Get Response
# Get Resource from the server
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
getjsonfile = response.json()
status = response.status_code
print(status)
print(response)

# Create new resource

api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
todo = getjsonfile
response = requests.post(api_url, json=todo)
postjson = response.json()
print(postjson)
print(response.status_code)

# Put/Patch Update a request on the server

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()
{'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json())
{'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
print(response.status_code)

