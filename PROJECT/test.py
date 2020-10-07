import requests
import json
import pandas as pd

url = 'http://127.0.0.1:5000/'
response1 = requests.get(url)
print(response1, response1.text)

data = ["5ec3ba5374f7660d73aa1201"]
# data = ["123"]

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
url = 'http://127.0.0.1:5000/predict'
response3 = requests.post(url, data=j_data, headers=headers)
# print(response3, response3.text)

response3 = pd.read_json(response3.text)
response3 = response3.merge(pd.read_csv("../Post dataset/posts.csv"), on='itemID')
response3 = response3.merge(pd.read_csv("../Post dataset/users.csv"), on='userID')

print(response3.head(10))