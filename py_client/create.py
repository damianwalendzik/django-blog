import requests

endpoint = "http://localhost:8000/api/posts/create/" 

data = {
    "user": None,
    "title": "This field is done",
    "content": 'eloo test',
    "public": True
}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())
