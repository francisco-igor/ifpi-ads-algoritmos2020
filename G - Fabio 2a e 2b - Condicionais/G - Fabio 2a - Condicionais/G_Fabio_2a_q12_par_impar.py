'''Leia 1 (um) número inteiro e escreva se este número é par ou impar.'''

# ENTRADA
def main():
    numero = int(input('Digite um número: '))
    par_ou_impar(numero)

# PROCESSAMENTO
def par_ou_impar(num):
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')

# SAÍDA
main()
