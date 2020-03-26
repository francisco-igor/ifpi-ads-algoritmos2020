'''Leia um número e escreva se o número é inteiro ou decimal.'''

# ENTRADA
def main():
    num = float(input('Número a ser verificado: '))
    itdc(num)

# PROCESSAMENTO
def itdc(num):
    if num % 1 == 0:
        print('O número é inteiro.')
    else:
        print('O número é decimal.')

# SAÍDA
main()
