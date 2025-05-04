import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# print(response)
# print(response.json())

for data in response.json()['items']:
    if data['is_answered'] != 0:
        print(f"Answer count: {data['answer_count']}")
        print(data['title'])
        print(data['link'])
    else:
        print("no answers here!")
    print()