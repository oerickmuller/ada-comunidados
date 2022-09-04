'''
Faça um programa que pede uma lista de palavras (pelo menos dez) para o usuário, que deve digitar uma por vez, e depois mostre 4 listas: palavras que começam com vogal, palavras que começam com consoantes, palavras que terminam com vogal, e palavras que terminam em consoantes
'''
from sqlite3 import paramstyle

lista_vogais = ['a', 'e', 'i', 'o', 'u']

lista_palavras = []

iniciando_vogais = []
iniciando_consoantes = []
terminando_vogais = []
terminando_consoantes = []


while True: 
    palavra = input("Digite uma palavra, ou - para encerrar: ")
    
    if palavra == '-' and len(lista_palavras) < 10:
        print(f"ERRO: Preciso de pelo menos 10 palavras, e tenho apenas {len(lista_palavras)}")
        continue
    elif palavra == '-':
        break
    
    lista_palavras.append(palavra)

    if palavra[0].lower() in lista_vogais:
        iniciando_vogais.append(palavra)
    else:
        iniciando_consoantes.append(palavra)

    if palavra[-1].lower() in lista_vogais:
        terminando_vogais.append(palavra)
    else:
        terminando_consoantes.append(palavra)
    
print(f"""
Palavras começando em vogal: {', '.join(iniciando_vogais)}
Palavras começando em consoante: {', '.join(iniciando_consoantes)}
Palavras terminando em vogal: {', '.join(terminando_vogais)}
Palavras terminando em consoante: {', '.join(terminando_consoantes)}
""")