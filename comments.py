import requests
url = "https://dummyjson.com/comments"
params = {"limit" : 0}
response = requests.get(url=url, params=params)
response_json = response.json()
comments = response_json["comments"]
print(comments)
for comment in comments :
    print (comments) 