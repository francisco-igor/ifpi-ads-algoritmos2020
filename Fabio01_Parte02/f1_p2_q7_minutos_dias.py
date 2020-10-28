# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

# ENTRADA
total_minutos = int(input('Leia o total de minutos: '))

# PROCESSAMENTO
dias = total_minutos // 1440
resto = total_minutos % 1440
horas = resto // 60
minutos = resto % 60

# SAÍDA
print(f'{total_minutos}min correspondem a {dias} dias(s), {horas}h e {minutos}min.')
