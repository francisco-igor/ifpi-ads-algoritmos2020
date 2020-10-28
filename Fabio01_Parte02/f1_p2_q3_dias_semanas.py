# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

# ENTRADA
total_dias = int(input('Leia o total de dias: '))

# PROCESSAMENTO
semanas = total_dias // 7
dias = total_dias % 7

# SAÍDA
print(f'{total_dias} dias correspondem a {semanas} semana(s) e {dias} dia(s).')
