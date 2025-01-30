#Ül. "Murelikud lapsevanemad"

# porgandid=0
# ringide_arv=10

# while ringide_arv > 0:
#        #print(ringide_arv)
#      if ringide_arv % 2 == 0:
#         porgandid += ringide_arv
#      ringide_arv -= 1
# print(porgandid)

#Ül. "Õunad"

# import random 


# ounad= 14
# pp = int(input("Mitu pp tahab õuna: "))

# for i in range(pp):
#     oun = random.randint(1,2)
#     print(oun)
#     ounad -= oun

# print(f"Lumivalgekesele jäi {ounad} õuna")


#Ül. "Ülikooli vastuvõetud"

# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     #print(rida, end="")
#     vastuvõetud.append(int(rida))

# #vastuvõetud.append(int(rida))


# fail.close()



# aasta = input("Lisa aasta 2011-2019: ")
# print(vastuvõetud[int(aasta[3])-1])

#Ül. "Sissetulekud"

# fail = open("konto.txt")

# for kirje in fail:
#     if float(kirje) > 0:
#         print(float(kirje), end= "\n")

# fail.close()

#Ül. "Jukebox"

# musa= "edm.txt"
# fail =open(musa)
# nr=1

# for pala in fail:
#     print(str(nr)+". "+pala, end="")
#     nr+=1

# print()
# valik = int(input("Vali lugu: "))
# fail = open(musa)
# mangin = 1
# for pala in fail:
#     if valik == mangin:
#         print(pala, end="")
#     mangin+=1

# fail.close()

#Ül. "Tahvli juurde"


