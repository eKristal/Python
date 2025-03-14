#PIL stands for Python Image Library



#Ülesanne "Arved"

# Leia makstud ja tasumata arvete arv.  Leia kogusumma kõikidest makstud arvetest.
# Leia keskmine arvete summa.
# Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
# Loetle kõik tasumata arved, mille tĆ¤htaeg on juba möödunud.

import requests

url = "https://metshein.com/kordamine/json/arved.json"

response = requests.get(url)


import requests
import json
from datetime import datetime, timedelta

# Laadige JSON-andmed
url = "https://metshein.com/kordamine/json/arved.json"
response = requests.get(url)
data = response.json()  # Eeldame, et vastus on JSON

# Hetke kuupäev
current_date = datetime.now()

# Muutujad kogumise jaoks
paid_count = 0
unpaid_count = 0
paid_total = 0
in_30_days_count = 0
overdue_unpaid_invoices = []

# Läbime iga arve ja töötleme andmeid
for invoice in data:
    due_date = datetime.strptime(invoice['tähtaeg'], "%Y-%m-%d")  # Eeldame, et kuupäev on formaat 'YYYY-MM-DD'
    paid = invoice['makstud']  # Eeldame, et "makstud" väärtus on bool

    # Arvutame makstud ja tasumata arvete arvu
    if paid:
        paid_count += 1
        paid_total += invoice['summa']
    else:
        unpaid_count += 1

    # Arvutame, kui arve on järgmise 30 päeva jooksul tasumisel
    if not paid and due_date > current_date and due_date <= current_date + timedelta(days=30):
        in_30_days_count += 1

    # Loetleme kõik tasumata arved, mille tähtaeg on möödas
    if not paid and due_date < current_date:
        overdue_unpaid_invoices.append(invoice)

# Arvutame keskmise arve summa
if paid_count > 0:
    average_invoice = paid_total / paid_count
else:
    average_invoice = 0

# Prindi tulemused
print(f"Makstud arvete arv: {paid_count}")
print(f"Tasumata arvete arv: {unpaid_count}")
print(f"Makstud arvete kogusumma: {paid_total} EUR")
print(f"Keskmine arve summa: {average_invoice:.2f} EUR")
print(f"Arveid, mille tähtaeg on järgmise 30 päeva jooksul: {in_30_days_count}")
print("Tasumata arved, mille tähtaeg on möödunud:")
for invoice in overdue_unpaid_invoices:
    print(f"- Arve ID: {invoice['id']}, Tähtaeg: {invoice['tähtaeg']}, Summa: {invoice['summa']} EUR")


Parimate soovidega,

Eliise Lisete Kristal 
ITS24
Koostamine:
Uus sõnum
MinimeeriEraldi aknasseSule
