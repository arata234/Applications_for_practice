import requests

TOKYO_LATITUDE = 35.4122
TOKYO_LONGITUDE = 139.4130


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
# print(data["iss_position"])

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(longitude, latitude)

if abs(float(longitude) - TOKYO_LONGITUDE) < 10 and abs(float(latitude) - TOKYO_LATITUDE) < 10:
    print("You can see the iss.")