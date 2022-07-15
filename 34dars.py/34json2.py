#34-DARS. JSON

import json

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))