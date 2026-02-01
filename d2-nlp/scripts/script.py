import json

import requests

rows = 1000
url = "https://api.archives-ouvertes.fr/search/"

params = {"q": "collCode_s:CREST", "fl": "*", "rows": rows, "wt": "json"}

all_docs = []
start = 0

while True:
    params["start"] = start
    params["rows"] = rows

    r = requests.get(url, params=params)
    r.raise_for_status()

    resp = r.json()
    docs = resp["response"]["docs"]

    if not docs:
        break

    all_docs.extend(docs)
    start += rows
    print(f"Fetched {len(docs)} documents, total so far: {len(all_docs)}")

with open("hal_crest_data.json", "w", encoding="utf-8") as f:
    json.dump(all_docs, f, ensure_ascii=False, indent=4)

print(f"Total documents fetched: {len(all_docs)}")
