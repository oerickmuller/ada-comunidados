'''
01
Crie uma função que receba uma lista de nomes e MOSTRE qual o que tem mais caracteres e qual tem menos caracteres.
'''

def mostrar_maior_menor(lista_nomes): 
    mais_caracteres = ''
    menos_caracteres = ''
    pos = 0
    while pos < len(lista_nomes):
        if pos == 0: 
            mais_caracteres = lista_nomes[pos]
            menos_caracteres = lista_nomes[pos]
        else:
            if len(lista_nomes[pos]) > len(mais_caracteres):
                mais_caracteres = lista_nomes[pos]
            elif len(lista_nomes[pos]) < len(menos_caracteres):
                menos_caracteres = lista_nomes[pos]
        pos = pos + 1
    print(f"Nome com mais caracteres: {mais_caracteres}")
    print(f"Nome com menos caracteres: {menos_caracteres}")


lista_de_nomes = ['Bianca', 'Maria', 'Ana', 'Mario', 'Hermenegildo']
mostrar_maior_menor(lista_de_nomes)
