#Ülesanne "Arved"

# Leia makstud ja tasumata arvete arv.	Leia kogusumma kõikidest makstud arvetest.
# Leia keskmine arvete summa.
# Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
# Loetle kõik tasumata arved, mille tĆ¤htaeg on juba möödunud.

import requests
import json
from datetime import datetime
from datetime import date


url = "https://metshein.com/kordamine/json/arved.json"
response = requests.get(url)
arved = response.json()["arved"]
if response.status_code==200:
   
    maksmata= 0
    makstud=0
    makstud_kokku=0
    kogu_summa=0
    kokku_arveid=0
    count=0

    start_date1 = datetime.strptime("2025-03-16", "%Y-%m-%d")
    end_date1= datetime.strptime(str(date.today()), "%Y-%m-%d")
    diff=abs(end_date1-start_date1)
    

    for arve in arved:

        if diff.days > 30:
            count+=1

        kogu_summa+= arve['summa']
        kokku_arveid+=1

        if arve['makstud']== True:
           makstud+=1 
           makstud_kokku+= arve['summa']
        else:
            maksmata+=1
       
        
    
    keskmine= kogu_summa/kokku_arveid
    print(f"Makstud arveid on: {makstud}")
    print(f"Maksmata arveid on: {maksmata}")
    print(f"Makstud arved kokku: {makstud_kokku}")
    print(f"Keskmine: {keskmine}")
    print(f"Mitu arvet on maksetähtajaga järgmise 30 päeva jooksul: {count}")

    


    
   






















