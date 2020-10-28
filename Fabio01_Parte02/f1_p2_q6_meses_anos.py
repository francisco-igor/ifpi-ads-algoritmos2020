# Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

# ENTRADA
total_meses = int(input('Leia o total de meses: '))

# PROCESSAMENTO
anos = total_meses // 12
meses = total_meses % 12

# SAÍDA
print(f'{total_meses} mês(meses) correspondem a {anos} ano(s) e {meses} mês(meses).')
