Import math
a = 1
b = 20
c = -525

baoQuadrado = b * b
delta = a * c
delta = -4 * delta
delta = baoQuadrado +  delta
print(delta)

raizDelta = math.sqrt(delta)
print(raizDelta)
numerador = -b + raizDelta
denominador = 2*a

x= numerador/ denominador
print ("A minha idade é:", str(x))
