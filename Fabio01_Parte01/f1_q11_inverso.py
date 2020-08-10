# ENTRADA
numero = int(input('Número de 3 dígitos: '))

# PROCESSAMENTO
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = unidade * 100 + dezena * 10 + centena * 1

# SAÍDA
print(f'O inverso de {numero} é {inverso}')