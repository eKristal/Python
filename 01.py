# 01. ülesanne
# Eliise Lisete Kristal ITS-24

import turtle

#kolmnurk
turtle.speed(0) #reguleeri 1-9
turtle.penup()
turtle.goto(-500,200)
turtle.pendown()

turtle.forward(200)#fd,  pikslites
turtle.left(120)
turtle.forward(200)#fd,  pikslites
turtle.left(120)
turtle.forward(200)#fd,  pikslites
turtle.left(120)

#süda
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.fd(100)
turtle.circle(50,180)
turtle.right (90)
turtle.circle(50,180)
turtle.fd(100)


#lõpetab kilpkonna
turtle.done()
