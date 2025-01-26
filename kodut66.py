import turtle

size = 100

for _ in range(6):
    turtle.forward(size)
    turtle.left(60)

for _ in range(1):
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(60)
    turtle.backward(size)

for _ in range(1):
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)
    turtle.backward(size)

for _ in range(1):
    turtle.backward(size)
    turtle.right(120)

for _ in range(1):
    turtle.left(120)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.left(60)
    turtle.backward(size)
    turtle.left(60)
    turtle.forward(size)
    
    





turtle.done()
