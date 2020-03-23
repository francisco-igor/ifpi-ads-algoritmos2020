'''Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.'''

# ENTRADA
def main():
    letra = str(input('Digite uma letra em maiúsculo para determinar gênero: '))
    genero(letra)

# PROCESSAMENTO
def genero(letra):
    if letra == 'F':
        print('F - Feminino')
    elif letra == 'M':
        print('M - Masculino')
    else:
        print('Sexo Inválido')

# SAÍDA
main()
