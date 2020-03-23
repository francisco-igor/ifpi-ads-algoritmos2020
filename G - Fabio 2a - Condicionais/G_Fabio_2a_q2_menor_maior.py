'''Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.'''

# ENTRADA
num1 = float(input('Digie um número: '))
num2 = float(input('Digite outro número: '))

# PROCESSAMENTO
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
else:
    print(f'O número {num2} é maior que o número {num1}')