'''Leia 3 (três) números, verifique e escreva o maior entre os números lidos.'''

# ENTRADA
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

# PROCESSAMENTO
if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior.')

elif num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior.')

elif num3 > num1 and num3 > num2:
    print(f'O número {num3} é o maior.')

elif num1 == num2 == num3:
    print('Todos os números são iguais.')

elif num1 == num2 or num2 == num3 or num1 == num3:
    print('Não existe um único número maior.')
