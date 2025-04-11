#   JSON

# PYTHONDAN JSONGA

# json.dumps()

import json

x = 10
x_json = json.dumps(x)

ism = "anvar"
ism_json = json.dumps(ism)

sonlar = [12, 45, 23, 67]
sonlar_json = json.dumps(sonlar)

print(type(sonlar_json))


bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)

with open('json_bemor', 'w') as f:
    json.dump(bemor,f)
    
    
# JSONDAN PYTHONGA

# json.loads

sonlar = json.loads(sonlar_json)
bemor = json.loads(bemor_json)
print(type(bemor))

# json.load()
filename = 'bemor.dict'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))
    
    
    
    