import requests
url = "https://dummyjson.com/comments"
params = {"limit" : 0}
response = requests.get(url, params=params)


