# ENTRADA
numero = int(input("Número de 3 dígitos: "))

# PROCESSAMENTO
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

somatório = centena + dezena + unidade

# SAÍDA
print(f'A soma dos dígitos é {somatório}')