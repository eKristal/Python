# Ülesanne 6

import math
import turtle

nurk= 53
korgus= 4.4

rad = math.radians(nurk)
kaugus = korgus / math.tan(rad)
c = math.sqrt(math.pow(kaugus,2)+math.pow(korgus,2))

print(c)
kordaja = 10
turtle.fd(kaugus*kordaja)
turtle.lt(90)
turtle.fd(korgus*kordaja)
turtle.rt(360-53-90)
turtle.fd(c*kordaja)


turtle.done()


