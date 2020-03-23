'''Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
do algarismo da unidade.'''

# ENTRADA
numero = int(input('Digite um número de dois dígitos: '))

# PROCESSAMENTO
dezena = numero // 10
unidade = numero % 10

if dezena == unidade:
    print(f'O algarismo da dezena é igual ao algarismo da unidade.')
else:
    print(f'O algarismo da dezena é diferente do algarismo da unidade.')
