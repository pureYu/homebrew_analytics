# $ pip install requests

""" Parse json from Homebrew with all packages and numbers of their installations """

import json
import time
import requests
from datetime import datetime


r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

results = []
t1 = time.perf_counter()

for package in packages_json:

    package_name = package["name"]
    package_desc = package["desc"]
    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    r = requests.get(package_url)
    package_json = r.json()

    installs_30d = package_json["analytics"]["install_on_request"]["30d"][package_name]
    installs_90d = package_json["analytics"]["install_on_request"]["90d"][package_name]
    installs_365d = package_json["analytics"]["install_on_request"]["365d"][package_name]

    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            'analytics': installs_30d,
            '90d': installs_90d,
            '365d': installs_365d
        }
    }

    results.append(data)
    time.sleep(r.elapsed.total_seconds())
    # The Response object as returned by requests.post() has a property called elapsed, which give the time delta
    # between the Request was sent and the Response was received.
    # To get the delta in seconds, use the total_seconds() method
    print(f"Got {package_name} in {r.elapsed.total_seconds()} seconds")
    # break

t2 = time.perf_counter()
print(f"Finished in {t2 - t1} seconds")

now = datetime.now()
file_name = f"package_info_{now:%Y%m%d_%H%M%S}.json"
with open(file_name, "w") as f:
    json.dump(results, f, indent=2)

# print(len(packages_json))   # 4820