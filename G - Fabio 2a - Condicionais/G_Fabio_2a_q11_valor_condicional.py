'''Leia quatro números (opção, num1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
possíveis para a variável opção são 1, 2 e 3.'''

# ENTRADA
def main():
    opção = float(input('Digite o valor da variável "opção": '))
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    num3 = float(input('Digite o terceiro número: '))
    print('-' * 25)
    condicional(opção, num1, num2, num3)

# PROCESSAMENTO
def condicional(o, n1, n2, n3):
    if o == 1:
        print(n1)
    elif o == 2:
        print(n2)
    elif o == 3:
        print(n3)
    else:
        print('Os únicos valores possíveis para a variável "opção" são 1, 2 e 3.')

# SAÍDA
main()
