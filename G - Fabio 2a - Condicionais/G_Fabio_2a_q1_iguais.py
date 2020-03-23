'''Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.'''

# ENTRADA
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# PROCESSAMENTO
if num1 == num2 == num3:
    print('Existem 3 números iguais.')

elif num1 == num2:
    print('Existem 2 números iguais.')

elif num2 == num3:
    print('Existem 2 números iguais.')

elif num1 == num3:
    print('Existem 2 números iguais.')
