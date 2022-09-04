'''
07
Receba uma data de nascimento (com dia, mês e ano) e retorne a idade em dias, meses e anos, relativo a 01/02/2022
'''

dia_nascimento = int(input("Digite o dia de nascimento: "))
mes_nascimento = int(input("Digite o mes de nascimento: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_referencia = 2022
mes_referencia = 2
dia_referencia = 1

idade_em_anos = ano_referencia - ano_nascimento
idade_em_meses = 0 
idade_em_dias = 0

if mes_nascimento == mes_referencia:
    idade_em_dias = dia_nascimento - 1
    idade_em_meses = 0
elif mes_nascimento < mes_referencia: 
    if dia_nascimento == dia_referencia:
        idade_em_meses = 1
        idade_em_dias = 0
    else:
        idade_em_dias = 31 - dia_nascimento + 1
elif mes_nascimento > mes_referencia: 
    idade_em_anos -= 1
    idade_em_meses = 12 - mes_nascimento + 1
    if mes_nascimento in (3, 5, 7, 8, 10, 12):
        idade_em_dias = 31 - dia_nascimento
    elif mes_nascimento in (4, 6, 9, 11):
        idade_em_dias = 30 - dia_nascimento
    idade_em_dias += 1
    if dia_nascimento == dia_referencia:
        idade_em_meses += 1
        idade_em_dias = 0
    

print(f"Idade: {idade_em_anos} anos, {idade_em_meses} meses e {idade_em_dias} dias.")


