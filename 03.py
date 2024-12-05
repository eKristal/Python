# 3. Ülesanne
#Eliise Lisete Kristal

nimi = "Eliise" #sõne, string, str
vanus = 21 #int, integer, täisarv
Keskmine_hinne = 5.9 #komarv, float

print(nimi+", " +str(vanus)+" aastat vana ja keskmine hinne on "+str(Keskmine_hinne))
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",Keskmine_hinne)
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {Keskmine_hinne}")
print(f"{vanus} aastat vana on {nimi} ja tema keskmine hinne on {Keskmine_hinne}")

#kolmnurk

import turtle

kylje_pikkus = 100
nurk = 120
varv = "pink"

turtle.color(varv)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)


turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

turtle.color(varv)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

turtle.color(varv)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)





