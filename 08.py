

#Ülesanne 8.2

tooted = {
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}

try:
    toode = input("Vali toode: ")
    if toode in tooted:
        kogus = int(input("Lisa kogus:"))
        if kogus<=tooted[toode]["kogus"]:
            hind =tooted[toode]["hind"]
            summa = round(hind*kogus,2)
            print(summa)
            tooted[toode]["hind"]-=kogus
            print(f"Laoseis: {tooted[toode]["kogus"]} tk")
        else:
            print("Kahjuks sellist kogust ei ole!")
    else: 
        print("Kahjuks seda toodet ei ole")
except:
    print("Midagi on jama!")