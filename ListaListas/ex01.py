'''
Faça um programa que mostre o fatorial de 1 a 20. Lembrando que fatorial é a multiplicação de todos os números até o indicado no fatorial. Por exemplo, 5! = 5 * 4 * 3 * 2 * 1
'''

for numero_final in range(1, 21):
    resultado = 1
    for numero_inicial in range(1, numero_final+1):
        resultado *= numero_inicial
    print(f"{numero_final}! = {resultado}")