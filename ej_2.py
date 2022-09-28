from operator import ne
import requests
from pprint import pprint
import json
mylist = []
c=0

url = 'https://api.covidtracking.com/v1/us/daily.json'
response=requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)

    for i in data:
        c += 1
        positive = i['positiveIncrease']
        negative = i['negativeIncrease'] 
        negative30 = negative*.3

        if positive > negative30:
            mylist.append(str(i['date']))
            
print(mylist)
print(len(mylist), c)

