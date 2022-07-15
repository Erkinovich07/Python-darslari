#34-DARS. JSON

import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

# ism = "samandar"
# ism_json = json.dumps(ism)
# familiya_json = json.dumps('erkinovich')

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)


bemor = {
    "ism": "samanda erkinovich",
    "yosh": 18,
    "oila": False,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}
