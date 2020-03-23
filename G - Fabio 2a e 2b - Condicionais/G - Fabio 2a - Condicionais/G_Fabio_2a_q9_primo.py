'''Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.'''

# ENTRADA
def main():
    numero = int(input('Digite um número: '))
    primo(numero)

# PROCESSAMENTO
def primo(numero):
    if numero == 2 or numero == 3:
        print(f'O número é primo.')
    elif numero == 1:
        print(f'O número não é primo.')
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 9 == 0:
        print(f'O número não é primo.')
    else:
        print('O número é primo.')
   
# SAÍDA
main()
