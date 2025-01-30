import turtle

suurus = 100  

for _ in range(6):
    turtle.forward(suurus)
    turtle.left(60)
    
    for _ in range(3):
        turtle.forward(suurus)
        turtle.left(120)
    
    turtle.backward(suurus)


turtle.done()
