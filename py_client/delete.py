import requests

endpoint = "http://127.0.0.1:8000/api/posts/1/delete/" 


get_response = requests.delete(endpoint) 
print(get_response.content)
print(get_response.json)
