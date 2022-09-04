# Crie um algoritmo que aceite 10 numeros e, a cada numero entrado, coloque este numero numa lista de forma ordenada.

numeros_ordenados = []

for pos in range(10):
    numero = -1
    while True:
        numero = int(input(f"Digite o {pos+1}o numero: "))
        if numero in numeros_ordenados: 
            print("Número já existe, digite novamente. ")
        else:
            break
                
    if len(numeros_ordenados) == 0:
        numeros_ordenados.append(numero)
    elif len(numeros_ordenados) == 1:
        if numero > numeros_ordenados[0]:
            numeros_ordenados.append(numero)
        else:
            numeros_ordenados.insert(0, numero)
    else:        
        pos = 0
        while pos < len(numeros_ordenados): 
            if numero < numeros_ordenados[pos]:
                numeros_ordenados.insert(pos, numero)
                inserido = True
                break
            pos += 1
        if numero not in numeros_ordenados:
            numeros_ordenados.append(numero)


print(numeros_ordenados)