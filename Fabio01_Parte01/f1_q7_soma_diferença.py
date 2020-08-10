# ENTRADA
numero = int(input('Número de 3 dígitos: '))

# PROCESSAMENTO
digito_1 = numero // 100
resto = numero % 100
digito_2 = resto // 10
digito_3 = resto % 10

soma = digito_1 + digito_2
subtração = digito_2 - digito_3

# SAÍDA
print(f'A soma dos dois primerios dígitos é {soma} e a diferença dos dois últimos é {subtração}')