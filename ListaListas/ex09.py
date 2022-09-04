'''
Receba uma lista de produtos, um por vez, com a quantidade o nome do produto e o preço unitário.

No final, mostre um modelo de nota fiscal, com quantidade, nome do produto, preço total do produto e preço total da compra.
'''

lista_de_produtos = []

continuar = 's'
while continuar == 's': 
    nome_produto = input("Nome do produto: ")
    qtd_produto = float(input("Quantidade do produto: "))
    preco_produto = float(input("Preço unitário do produto: "))
    lista_de_produtos .append((nome_produto, qtd_produto, preco_produto))
    print("")
    
    continuar = ''
    while continuar.lower() not in ('s', 'n'):
        continuar = input("Deseja adicionar novo produto? (s/n) ")

print("\n\nNOTA FISCAL\n")
print("Quantidade | Produto " + (" " * 33)  + "| Valor Total |")
preco_da_nota = 0
for produto in lista_de_produtos:
    preco_total_produto = produto[1] * produto[2]
    print(f"{produto[1]:>10.02f} | {produto[0]:>40s} | {preco_total_produto:>11.02f} |")
    preco_da_nota += preco_total_produto

print("-" * 69)
print(f"Preco total: {preco_da_nota:>54.02f} |\n")
