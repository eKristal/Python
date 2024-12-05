# 4. Ülesanne

a=int(input("Sisesta külg 1: "))
b=int(input("Sisesta külg 2: "))

ymbermoot= 2*(a+b)
print(f"Aia kogupikkus on {ymbermoot} meetrit.")

# 4.4 Ülesanne
try:
    karbi_suurus= 5
    kingitused = int(input("Lisa kingituste arv: "))
    kastid= kingitused // karbi_suurus
    jaak= kingitused % karbi_suurus

    print(f" Saad teha {kastid} täis kinkekasti. Üle jääb {jaak} kingitust")

except:
    print("Jälle tekitad probleeme")
    

