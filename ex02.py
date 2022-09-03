'''
02
Crie uma função que recebe um número de CPF sem pontos e traço e RETORNE o número formatado
'''

def formata_cpf(numero):
    # o formato é 000.000.000-00

    numero_em_str = int(numero)
    numero_em_str = f'{numero_em_str:011d}'
    numero_formatado = f'{numero_em_str[0:3]}.{numero_em_str[3:6]}.{numero_em_str[6:9]}.{numero_em_str[-2:]}'
    return numero_formatado

print(formata_cpf(1212312312))
print(formata_cpf(212312311))
print(formata_cpf(121454787861))