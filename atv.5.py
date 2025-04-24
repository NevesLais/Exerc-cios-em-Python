altura_trapezio = 145
base_maior = 120
base_menor = 75


largura_palco = 15
altura_palco = 8.5


area_trapezio = ((base_maior + base_menor) / 2) * altura_trapezio

area_palco = largura_palco * altura_palco

area_publico = area_trapezio - area_palco

capacidade_maxima = area_publico * 4

print(f"Junior poderá vender {int(capacidade_maxima)} ingressos.")
