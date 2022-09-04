'''
Obtenha, para dez aluno/as, o nome e as 4 notas deles, 
e exiba a média de cada aluna/o e a média de cada prova e a média geral da turma.
'''

total_de_alunos = 4
total_de_notas = 4
lista_media_dos_alunos = []

alunos_e_notas = []
for nro_aluno in range(1, (total_de_alunos+1)):
    nome_aluno = input(f'Digite o nome da pessoa {nro_aluno}: ')
    lista_notas = []
    for i in range(1, (total_de_notas + 1)):
        nota = float(input(f"Digite a {i}a nota: "))
        lista_notas.append(nota)
    alunos_e_notas.append([nome_aluno, lista_notas])
    print("")   # Para dar uma linha em branco... :)

print("### Media por aluno: ")

for aluno_e_notas in alunos_e_notas:
    nome_aluno = aluno_e_notas[0]
    notas_aluno = aluno_e_notas[1]
    media = sum(notas_aluno) / len(notas_aluno)
    lista_media_dos_alunos.append(media)
    print(f"{nome_aluno:>15s}: {media:.02f}")
print("")   # Para dar uma linha em branco... :)

print("### Media de cada prova")
todas_notas = []
for numero_prova in range(total_de_notas):
    notas = []
    for aluno_e_notas in alunos_e_notas:
        notas.append(aluno_e_notas[1][numero_prova])
    todas_notas.append(notas)
numero_prova = 1
for lista_notas in todas_notas:
    print(f"Media da prova {numero_prova}: {sum(lista_notas)/len(lista_notas):.02f}")
    numero_prova += 1
print("")   # Para dar uma linha em branco... :)

print("### Media geral da turma")
print(f"Media geral da turma: {sum(lista_media_dos_alunos) / len(lista_media_dos_alunos):.04f} ")