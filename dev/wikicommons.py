# Objective slide image - https://www.mediawiki.org/wiki/API:Images
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": config['objective_short'],
    "prop": "images"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA['query']['pages']

for k, v in PAGES.items():
    for img in v['images']:
        print(img["title"])