# nimed= ["Marilis", "Paula", "Elise", "Valter", "Sannu"]
# print(nimed[3])
# print(nimed[-1])
# print(nimed[1:3])
# print(nimed[2:])
# nimed.append("Kass")
# nimed.insert(0,"Grisha")
# print(nimed)

# uued_nimed=["Kaka","Junn"]
# nimed.extend(uued_nimed)
# print(nimed)

# nimed.remove("Sannu")
# print(nimed)

# len() – Tagastab loendi elementide koguarvu
# max() – Leiab ja tagastab loendis suurima elemendi
# min() – Leiab ja tagastab loendis väikseima elemendi
# sum() – Arvutab ja tagastab numbriliste väärtustega loendi elementide summa
# index() – Tagastab esimese leitud elemendi indeksi loendis, mille väärtus vastab määratud argumendile
# count() – Loendab, mitu korda määratud väärtus loendis esineb
# sort() – Sorteerib loendi elemendid kasvavas järjekorras
# reverse() – Sorteerib loendi elemendid kahanevas järjekorras

numbrid= [1,2,3,4,5,6,3,4,5,2,2,]

#Loendi pikkus:
# print(len(numbrid))

#Suurim element loendis: 
# print(max(numbrid))

#Väikseim element loendis:
# print(min(numbrid))

#Elementide summa
# print(sum(numbrid))

#Elemendi indeks
# print(numbrid.index(3))

#Elemendi esinemiste arv
# print(numbrid.count(3))

#Sorteerib kasvavas järjekorras:
# numbrid.sort()
# print(numbrid)

#Sorteerib kahanevas järjekorras:
# numbrid.sort()
# numbrid.reverse()
# print(numbrid)

#Ennik-tuple. Muutumatud.

# opilase_info=("Eliise Lisete Kristal, 5816-3819")

#Hulk set()-konstruktor või {} -süntaks

# hulk1={1,2,3,4}
# hulk2=set([1,2,3,4,])

# hulk1.add(5)
# hulk1.remove(1) - viskab vea kui elementi eemaldamisel ei leidu
# hulk1.discard(2) - ei viska viga

#Ülesanne 07 

# lood = [
#     "1. ALIKA – Bridges",
#     "2. Anett x Fredi – Read Between The Lines",
#     "3. villemdrillem – leekiv armastus",
#     "4. Clicherik & Mäx – PAKSUD",
#     "5. nublu – ära ärata",
#     "6. NOËP – Move Your Feet",
#     "7. Trad.Attack! – Bring It On",
#     "8. Bedwetters – It Is What It Is",
#     "9. Reket – Panama paberid",
#     "10. Grete Paia – Võluväel"
# ]

# for lugu in lood:
#     print(lugu)  # Prindib iga loo eraldi reale



# soovilugu=int(input("Vali loo number: "))-1 #lisame -1, sest listis on indeksiga 0 

# print(f"Siin on sinu lugu: {lood[soovilugu]}")


#Ülesanne 7.2

jantemp=["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3                                      
]

for temp in jantemp:
    print(temp)


print(f"Mõõdetav kuu on: {jantemp[0]}")
print(f"Viimase mõõtmise tulemus on: {jantemp[-1]}")