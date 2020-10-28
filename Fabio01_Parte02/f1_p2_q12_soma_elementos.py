# Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

# ENTRADA
num = int(input('Leia um número inteiro de 4 dígitos: '))

# PROCESSAMENTO
digito1 = num // 1000
digito2 = (num % 1000) // 100
digito3 = ((num % 1000) % 100) // 10
digito4 = num % 10

numero = digito1 + digito2 + digito3 + digito4

# SAÍDA
print(f'O valor dos elementos de {num} corresponde a {numero}.')
