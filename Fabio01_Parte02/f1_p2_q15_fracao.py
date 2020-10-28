# Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

# ENTRADA
num1 = int(input('Leia o numerador 1: '))
den1 = int(input('Leia o denominador 1: '))
num2 = int(input('Leia o numerador 2: '))
den2 = int(input('Leia o denominador 2: '))

# PROCESSAMENTO
mmc = den1 * den2
soma = (mmc / den1) * num1 + (mmc / den2) * num2

# SAÍDA
print(f'A soma das frações é {soma:.0f}/{mmc:.0f}')
