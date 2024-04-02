import requests

endpoint = "http://127.0.0.1:8000/api/posts/1/patch/" 

data = {
    "title": "This field is doneeee",
    "content": 'eloo patch',
}
get_response = requests.patch(endpoint, json=data) 
print(get_response.content)
print(get_response.json)
