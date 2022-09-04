"""
Crie um conjunto de funções que calculem

- a área de um retângulo
- a área de um triangulo
- a área de circulo
- o comprimento de um retângulo
- o comprimento de um triangulo
- o comprimento de circulo

Crie depois dois exemplos de uso de cada função
"""

pi = 3.1415


def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return base * altura / 2

def area_circulo(raio):
    return pi * (raio ** 2)

def comprimento_retangulo(base, altura):
    return base * 2 + altura * 2

def comprimento_triangulo(compr_lado_1, compr_lado_2, compr_lado_3):
    return compr_lado_1 + compr_lado_2 + compr_lado_3

def comprimento_circulo(raio):
    return 2 * pi * raio 

print(area_retangulo(2, 4))
print(area_retangulo(13, 21))
print(comprimento_retangulo(2, 4))
print(comprimento_retangulo(13, 21))

print(area_triangulo(2, 4))
print(area_triangulo(13, 21))
print(comprimento_triangulo(13, 14, 15))
print(comprimento_triangulo(21, 21, 21))

print(area_circulo(2))
print(area_circulo(13))
print(comprimento_circulo(2))
print(comprimento_circulo(13))

