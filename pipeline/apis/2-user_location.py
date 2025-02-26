#!/usr/bin/env python3

""" Return list of ships"""

import requests
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <URL>")
        sys.exit(1)

    try:
        res = requests.get(sys.argv[1], timeout=10)

        if res.status_code == 403:
            rate_limit = res.headers.get('X-Ratelimit-Reset')
            if rate_limit:
                rate_limit = int(rate_limit)
                current_time = int(time.time())
                diff = (rate_limit - current_time) // 60
                print(f"Reset in {diff} min")
            else:
                print("Rate limit information unavailable.")

        elif res.status_code == 404:
            print("Not found")

        elif res.status_code == 200:
            try:
                res_json = res.json()
                print(res_json.get('location', 'Location not found'))
            except ValueError:
                print("Invalid JSON response received.")

        else:
            print(f"Unexpected response code: {res.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
