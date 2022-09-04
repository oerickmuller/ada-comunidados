"""
Crie uma lista com 5 nomes de pessoas, 5 sobrenomes, e exiba os 25 nomes completos que podem surgir dos cruzamentos entre nomes e sobrenomes.
"""

nomes = ['maria', 'pedro', 'mario', 'joana', 'joao']
sobrenomes = ['silva', 'oliveira', 'pereira', 'soares', 'tavares']

for nome in nomes: 
    for sobrenome in sobrenomes:
        print(f"{nome} {sobrenome}")