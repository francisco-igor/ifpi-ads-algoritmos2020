'''Leia um número e mostre na tela se o número é positivo ou negativo.'''

# ENTRADA
def main():
    num = int(input('Digite um número: '))
    sinal(num)

# PROCESSAMENTO
def sinal(num):
    if num > 0:
        print('O número é positivo.')
    elif num == 0:
        print('O número é zero, portanto neutro.')
    else:
        print('O número é negativo.')

# SAÍDA
main()
