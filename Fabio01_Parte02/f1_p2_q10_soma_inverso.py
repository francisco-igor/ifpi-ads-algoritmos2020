# Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso. (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

# ENTRADA
num = int(input('Leia um número inteiro de 3 dígitos: '))

# PROCESSAMENTO
digito1 = num // 100
digito2 = (num % 100) // 10
digito3 = num % 10

inverso1 = digito3 * 100
inverso2 = digito2 * 10
inverso3 = digito1 * 1

numero = inverso1 + inverso2 + inverso3

diferenca = num + numero

# SAÍDA
print(f'A diferença de {num} com o seu inverso de {numero} é igual a {diferenca}.')
