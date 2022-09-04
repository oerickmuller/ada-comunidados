'''
Por 30 dias uma pessoa vai guardar 2 reais numa poupança, e a cada dia o valor guardado cresce 0.2%. Quanto dinheiro essa pessoa tem no final do período?
'''

saldo_atual = 0.0
for dia in range(30):
    saldo_atual += 2
    saldo_atual *= 1.002
    # print(dia+1, " = ", saldo_atual)

print(f"a pessoa tem {saldo_atual:.02f}")