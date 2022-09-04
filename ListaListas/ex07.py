'''
# O exercicio esta com um problema, porque saem mais onibus do que o tem intervalos de saida. 
# No exemplo eu mudei para 27 minutos.
Um ônibus parte a cada 40 minutos do ponto inicial. O primeiro ônibus sai às 06:00 e depois saem mais 40 viagens. Crie uma lista com os horários das viagens.
'''

horarios = []
intervalo = 27

for viagem in range(40):    
    if viagem == 0:
        hora = 6
        minuto = 0
    horarios.append(f"{hora:02d}:{minuto:02d}")    
    minuto += intervalo 
    if minuto >= 60: 
        hora += 1
        minuto = minuto - 60

print(horarios)