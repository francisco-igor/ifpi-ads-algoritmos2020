# Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

# ENTRADA
num = int(input('Leia um número binário de 4 dígitos: '))

# PROCESSAMENTO
digito1 = num // 1000
digito2 = (num % 1000) // 100
digito3 = ((num % 1000) % 100) // 10
digito4 = num % 10

decimal1 = digito1 * 8
decimal2 = digito2 * 4
decimal3 = digito3 * 2
decimal4 = digito4 * 1

numero = decimal1 + decimal2 + decimal3 + decimal4

# SAÍDA
print(f'O valor binário {num} corresponde a {numero} em decimal.')
