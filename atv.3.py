import math


a = 1
b = 20
c = -525


delta = b**2 - 4*a*c


raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)


print(f"As soluções são: {raiz1} e {raiz2}")


idade = max(raiz1, raiz2)
print(f"Sua idade é: {idade}")
