'''
Crie um programa que calcula e lista os primeiros 20 números primos.
'''

lista_primos = []
numero_a_testar = 2
while len(lista_primos) <= 20:
    tem_divisor = False
    for numero_dividir in range(numero_a_testar, 2, -1):
        if numero_a_testar == numero_dividir: 
            continue
        if numero_a_testar % numero_dividir == 0: 
            tem_divisor = True
            break
    if not tem_divisor:
        lista_primos.append(numero_a_testar)
    numero_a_testar += 1

print(lista_primos)