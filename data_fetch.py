import requests
import json
#import boto3

#response = requests.get("https://api.covid19api.com/country/germany/status/confirmed/live?from=2022-06-01")
response = requests.get("https://api.covid19api.com/total/dayone/country/germany")
data = response.json()


for item in data:
    print(item["Date"] +": "+ str(item["Active"]))
    #print(item["Cases"] + ": " str(item["Cases"]))


# {
#     "cases":12345,
#     "active": 234,
#     "trend": "UP",
#     "lockdown": true
# }