#Ülesanne "Arved"

# Leia makstud ja tasumata arvete arv.	Leia kogusumma kõikidest makstud arvetest.
# Leia keskmine arvete summa.
# Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
# Loetle kõik tasumata arved, mille tĆ¤htaeg on juba möödunud.

import requests
import json



url = "https://metshein.com/kordamine/json/arved.json"
response = requests.get(url)
arved = response.json()["arved"]
if response.status_code==200:
   
    maksmata= 0
    makstud=0

    for arve in arved:
       if arve['makstud']:
           makstud+=1
    else:
        maksmata+=1

    print(f"Makstud arveid on: {makstud}")
    print(f"Maksmata arveid on: {maksmata}")




















