# Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

# ENTRADA
total_segundos = int(input('Leia o total de segundos: '))

# PROCESSAMENTO
horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

# SAÍDA
print(f'{total_segundos}s correspondem a {horas}h, {minutos}min e {segundos}s.')
