'''
04
Crie duas listas com 20 números não iguais, e depois crie uma função que recebe as duas listas e retorna uma lista com os 25 maior números, em ordem inversa
'''

import random

lista_01 = random.choices(range(1, 10000), k=20)
lista_02 = random.choices(range(1, 10000), k=20)

lista_final  = lista_01[:]
lista_final.extend(lista_02)
lista_final.sort(reverse=True)
print(f'Tamanho da lista final: {len(lista_final)}')
print(lista_final[:25])
