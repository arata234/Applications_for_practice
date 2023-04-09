import requests
import time

TOKYO_LATITUDE = 35.4122
TOKYO_LONGITUDE = 139.4130

def iss_is_near():
    if is_night():
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()

        data = response.json()
        # print(data["iss_position"])

        longitude = data["iss_position"]["longitude"]
        latitude = data["iss_position"]["latitude"]

        if abs(float(longitude) - TOKYO_LONGITUDE) < 5 and abs(float(latitude) - TOKYO_LATITUDE) < 5:
            print("You can see the iss.")
        else:
            print("You cannot see the iss")

    else:
        print("You cannot see the iss")


def is_night():
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={TOKYO_LATITUDE}&lng={TOKYO_LONGITUDE}&date=today&formatted=0")
    # print(response)

    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise = sunrise.split("T")[1]
    sunrise = sunrise.split(":")
    sunrise_h = sunrise[0]

    sunset = sunset.split("T")[1]
    sunset = sunset.split(":")
    sunset_h = sunset[0]

    sunrise_h = (int(sunrise_h)+9) % 24
    sunrise[0] = str(sunrise_h)
    sunset_h = (int(sunset_h)+9) % 24
    sunset[0] = str(sunset_h)

    sunrise = ":".join(sunrise).split("+")[0]
    sunset = ":".join(sunset).split("+")[0]

    sunrise = sunrise.split(":")
    sunset = sunset.split(":")
    sunrise = 3600 * int(sunrise[0]) + 60 * int(sunrise[1]) + int(sunrise[2])
    sunset = 3600 * int(sunset[0]) + 60 * int(sunset[1]) + int(sunset[2])

    now = time.strftime("%H:%M:%S").split(":")
    now = 3600 * int(now[0]) + 60 * int(now[1]) + int(now[2])

    if now < sunrise or sunset < now:
        return True

if __name__ == "__main__":
    iss_is_near()