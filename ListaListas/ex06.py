'''
Peça 10 nomes e dez idades e retorne:

quem é a pessoa mais velha
quem é a pessoa mais nova
que pessoas nasceram antes do ano 2000
quais as idades ímpares
'''

idade_mais_velha = 0
idade_mais_nova = 0 
pessoa_mais_velha = ''
pessoa_mais_nova = ''
idades_impares = []
pessoas_antes_2000 = []

for n in range(10):
    nome = input(f"Digite o {n+1}o nome: ")
    idade = int(input(f"Digite a {n+1}a idade: "))
    if n == 0:
        idade_mais_nova = idade
        idade_mais_velha = idade
        pessoa_mais_velha = nome
        pessoa_mais_nova = nome
    else:
        if idade < idade_mais_nova:
            idade_mais_nova = idade
            pessoa_mais_nova = nome
        elif idade > idade_mais_velha:
            idade_mais_velha = idade
            pessoa_mais_velha = nome
    if idade % 2 == 1:
        idades_impares.append(idade)
    if 2022 - idade < 2000:
        pessoas_antes_2000.append(nome)

print(f"Pessoa mais velha: {pessoa_mais_velha}")
print(f"Pessoa mais nova: {pessoa_mais_nova}")
print("Pessoas nascidas antes do ano 2000: ", pessoas_antes_2000)
print("Idades ímpares: ", idades_impares)
