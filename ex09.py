'''
Crie um programa que espera que o usuário digite 2 números entre 0 e 100, e depois retorne o mínimo múltiplo comum dos dois números.
'''


def obter_numero():    
    numero = -1
    while numero < 0 or numero > 100:        
        numero = int(input("Entre com um numero entre 0 e 100: "))
        if numero > 0 and numero < 101: 
            return numero
        print("Numero inválido")


def calcular_mmc(primeiro_numero, segundo_numero):
    if primeiro_numero == 0 or segundo_numero == 0:
        return 0

    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    pn = primeiro_numero
    sn = segundo_numero
    pos_primos = 0
    fatores = []
    while True: 
        if pn == 1 and sn == 1:
            mmc = 1
            for f in fatores:
                mmc *= f
            return mmc
        primo_atual = numeros_primos[pos_primos]
        fator_append = -1
        if pn % primo_atual == 0:
            pn = pn // primo_atual
            fator_append = primo_atual
        if sn % primo_atual == 0:
            sn = sn // primo_atual
            fator_append = primo_atual
        if fator_append != -1:
            fatores.append(fator_append)
        else: 
            pos_primos += 1
        

primeiro_numero = obter_numero()
segundo_numero = obter_numero()

minimo_multiplo_comum = calcular_mmc(primeiro_numero, segundo_numero)
print('mmc: ' + str(minimo_multiplo_comum))
