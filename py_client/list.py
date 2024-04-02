import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/posts/" 

get_response = requests.get(endpoint) 
    
data = get_response.json()
print(data)
