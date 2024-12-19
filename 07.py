#Ülesanne 7

nimi= ["Jyri", "Mari", "Maali", "Bob"]

# print(nimi[0])
# for i in nimi:
#     print(i)
    
for i in range(4):
    print(f"{i+1}. {nimi[i]}")

valik= int(input("Vali lugu (1-4): "))-1
print(f"Mängin: {nimi[valik-1]}")
