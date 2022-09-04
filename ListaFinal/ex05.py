'''
05
Crie um programa que simule um caixa eletrônico. O que precisa implementar:
- Depósito
- Saque
- Pagamento de conta
- Listagem de movimentações (extrato)
'''




def mostrar_menu_e_obter_selecao():
    opcoes = '''
    Menu de operacoes: 
    (d) Deposito
    (s) Saque
    (p) Pagamento de conta
    (l) Lista de movimentacoes / extrato
    (x) Terminar o programa
    '''
    print(opcoes)

    opcao = '-'
    while opcao.lower() not in ['d', 's', 'p', 'l', 'x']:
        opcao = input('Digite a opcao desejada: ')
        if opcao.lower() not in ['d', 's', 'p', 'l', 'x']:
            print('Opcao invalida, tente novamente')            
    return opcao



### Inicio do programa

# aqui registramos todas as operacoes
operacoes = []

while True:
    opcao = mostrar_menu_e_obter_selecao() 
    if opcao == 's': 
        valor = float(input('Qual o valor do saque? ')) * -1
        descricao = "Saque"
        operacoes.append([valor, descricao])
    elif opcao == 'd':
        valor = float(input('Qual o valor do depósito? '))
        descricao = input('Qual a origem do deposito? ')
        operacoes.append([valor, descricao])
    elif opcao == 'p': 
        valor = float(input('Qual o valor do pagamento de conta? '))
        descricao = input('Qual a conta em pagamento? ')    
        descricao = f'Conta paga: {descricao}'
        operacoes.append([valor, descricao])
    elif opcao == 'l':
        print("\n>> Lista de operacoes: ")
        print(('-' * 30) + "|" + ('-' * 15))
        for operacao in operacoes:
            print(f"{operacao[1]:>30s}| R$ {operacao[0]:>10.02f}")
    elif opcao == 'x':
        print('Encerrando o programa. ')
        break