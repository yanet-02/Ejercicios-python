import math

radio = float(input("Introduce el radio del círculo en metros:\n"))

area = math.pi * (radio ** 2)

print(f"\nEl área del círculo con radio {radio} metros es: {area: 2f} metros cuadrados.")