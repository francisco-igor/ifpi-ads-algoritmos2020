# Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

# ENTRADA
total_horas = int(input('Leia um valor em h: '))

# PROCESSAMENTO
semanas = total_horas // 168
resto = total_horas % 168
dias = resto // 24
horas = resto % 24

# SAÍDA
print(f'{total_horas}h correspondem a {semanas} semana(s), {dias} dia(s) e {horas}h.')
