# Ülesanne 7.2 

jtemp= ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav kuu: {jtemp[0]}")
print(f"Viimase mõõtmise tulemus: {jtemp[-1]} kraadi")

maks= -100
mini= 100
summa = 0
kokku = 0
kordused= 0 

for t in range(1,len(jtemp)):
    print(jtemp[t], end=" ")                    #prindib kõik tempid
    if jtemp[t]>maks:                           #max temp kontroll
        maks = jtemp[t]
    if  jtemp[t]<mini:
        mini = jtemp[t]                         #min temp kontroll
    summa+=jtemp[t]                             #keskmise arvutamine
    kokku+=1
    if jtemp[t]== -20:                          #== - täpselt võrdne
        kordused+=1

jtemp.pop(5)                                    #kustutab
jtemp.insert(5,21)                              #asendab/lisab
#temp.sort() - sorteerib

print()
print (f"Maksimum temp on: {maks}")
print (f"Miinimum temp on: {mini}")
print (f"Keskmine temperatuur on: {summa/kokku:0.0f}") #0.0f - ümardame täisarvuks
print (f"Temperatuur -20 esineb: {kordused} korda") 
print(jtemp)




