'''
Faça um programa que registre um pedido de um cliente. O cliente pode escrever, de forma livre, mas um por vez, a entrada, o prato principal, a bebida e se quer sobremesa. Caso queira a sobremesa, pedir para que digite. 
No final, mostre o pedido completo em letras maiúsculas, um item por linha.
'''

entrada = input("Por favor, digite a entrada: ")
prato_principal = input("Por favor, digite o prato principal: ")
bebida = input("Por favor, digite a bebida: ")

if input('Quer sobremesa (s/n)? ').lower() == 's': 
    sobremesa = input("Por favor, digite a sobremesa: ")
else:
    sobremesa = ''

print("### Listagem do pedido: ###")
print(f"entrada: {entrada}".upper())
print(f"prato principal: {prato_principal}".upper())
print(f"bebida: {bebida}".upper())
if sobremesa != '':
    print(f"sobremesa: {sobremesa}".upper())

