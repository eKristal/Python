#2. Ülesanne

"""Loo aken, mille nimi on “Olümpiarõngad ja sinu nimi”
Akna suurus 500×400
Loo värvilised 50px olümpiarõngad (sinine, must, punane, kollane, roheline)
Joone paksus 6
Kiirus 0"""


import turtle

aken= turtle.Screen()
aken.setup(width=600, height=400)
aken.title("Olümpiamängud Eliise Lisete Kristal")

#sinine

turtle.speed(0)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.color("blue")
turtle.pensize(6)
turtle.circle(50,360)

#must
turtle.speed(0)
turtle.penup()
turtle.goto(-90,100)
turtle.pendown()
turtle.color("black")
turtle.pensize(6)
turtle.circle(50,360)

#punane

turtle.speed(0)
turtle.penup()
turtle.goto(20,100)
turtle.pendown()
turtle.color("red")
turtle.pensize(6)
turtle.circle(50,360)

#kollane

turtle.speed(0)
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.color("yellow")
turtle.pensize(6)
turtle.circle(50,360)

#roheline

turtle.speed(0)
turtle.penup()
turtle.goto(-35,50)
turtle.pendown()
turtle.color("green")
turtle.pensize(6)
turtle.circle(50,360)

turtle.done()


