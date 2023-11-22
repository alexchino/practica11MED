#Crea un módulo llamado "geometría" que contenga funciones para calcular el área y el
#perímetro de formas geométricas comunes, como círculos, rectángulos y triángulos. Luego,
#en un programa principal, importa el módulo y utiliza estas funciones para calcular el área
#y el perímetro de diferentes formas.

import math

def calcula_forma(a, b, c):
    if a == b == c:
        print("Es un triángulo equilátero")
        s = (a + b + c) / 3
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = 2 * (a + b + c) / 3
    elif a != b and a != c and b != c:
        print("Es un triángulo escaleno")
        area = math.sqrt(a * b * c) / 4
        perimeter = a + b + c
    else:
        print("Es un triángulo isósceles")
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = 2 * (a + b + c) / 3
    return area, perimeter

# Prueba con diferentes valores de a, b y c
a = 5
b = 5
c = 5

area, perimeter = calcula_forma(a, b, c)
print("Área:", area)
print("Perímetro:", perimeter)