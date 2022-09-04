'''
06
Defina uma função que recebe 5 palavras e retorne uma lista com as palavras em ordem de tamanho da palavra.
'''

def ordenar_por_tamanho(lista_palavras):
    if len(lista_palavras) != 5:
        print('Retornando vazio, lista de palavras está inválida')
        return None
    
    lista_ordenada = lista_palavras[:]
    
    # Implementando algoritmo de ordenacao! 
    pos_ext = 0 
    while pos_ext < len(lista_ordenada):
        pos_int = pos_ext + 1        
        while pos_int < len(lista_ordenada):
            if len(lista_ordenada[pos_ext]) > len(lista_ordenada[pos_int]):
                lista_ordenada[pos_ext], lista_ordenada[pos_int] = lista_ordenada[pos_int], lista_ordenada[pos_ext]
            pos_int = pos_int + 1
        pos_ext = pos_ext + 1

    return lista_ordenada


lista_palavras_1 = ['banana', 'uva', 'abacate', 'pera', 'mamao']
print(ordenar_por_tamanho(lista_palavras_1))

lista_palavras_2 = ['banana', 'uva', 'abacate', 'pera', 'maca']
print(ordenar_por_tamanho(lista_palavras_2))

lista_palavras_3 = ['banana', 'uva', 'abacate', 'pera']
print(ordenar_por_tamanho(lista_palavras_3))