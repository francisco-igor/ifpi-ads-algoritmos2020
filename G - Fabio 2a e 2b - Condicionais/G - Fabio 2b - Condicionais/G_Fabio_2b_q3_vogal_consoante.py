'''Leia uma letra e verifique se a letra digitada é vogal ou consoante.'''

# ENTRADA
def main():
    letra = str(input('Determinar se é vogal ou consoante: '))
    verif(letra)

# PROCESSAMENTO
def verif(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A letra é uma vogal.')
    else:
        print('A letra é uma consoante.')

# SAÍDA
main()
