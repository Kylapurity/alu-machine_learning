#!/usr/bin/env python3
"""Pipeline API - Count SpaceX launches per rocket"""

import requests

if __name__ == "__main__":
    # Fetch launch data
    url = "https://api.spacexdata.com/v4/launches"
    r = requests.get(url)

    if r.status_code != 200:
        print("Error: Unable to fetch launch data")
        exit()

    rocket_dict = {}

    # Count launches per rocket
    for launch in r.json():
        rocket_id = launch["rocket"]
        rocket_dict[rocket_id] = rocket_dict.get(rocket_id, 0) + 1

    # Fetch rocket names
    for key, value in sorted(rocket_dict.items(), key=lambda kv: kv[1], reverse=True):
        rurl = f"https://api.spacexdata.com/v4/rockets/{key}"
        req = requests.get(rurl)

        if req.status_code == 200:
            print(req.json()["name"] + ": " + str(value))
        else:
            print(f"Error fetching rocket name for ID: {key}")
