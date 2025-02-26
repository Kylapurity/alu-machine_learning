#!/usr/bin/env python3
"""Pipeline Api"""
import requests
from datetime import datetime


if __name__ == '__main__':
    """pipeline api"""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(url)
    recent = 0

    for dic in r.json():
        new = int(dic["date_unix"])
        if recent == 0 or new < recent:
            recent = new
            launch_name = dic["name"]
            date = dic["date_local"]
            rocket_number = dic["rocket"]
            launch_number = dic["launchpad"]

    rurl = "https://api.spacexdata.com/v4/rockets/" + rocket_number
    rocket_name = requests.get(rurl).json()["name"]
    lurl = "https://api.spacexdata.com/v4/launchpads/" + launch_number
    launchpad = requests.get(lurl)
    launchpad_name = launchpad.json()["name"]
    launchpad_local = launchpad.json()["locality"]

    # Format the date to match the expected output
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%dT%H:%M:%S%z")

    string = "{} ({}) {} - {} ({})".format(launch_name, date, rocket_name,
                                           launchpad_name, launchpad_local)

    print(string)
