'''Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.'''

# ENTRADA
def main():
    li = int(input('Digite o Limite Inferior: '))
    ls = int(input('Digite o Limite Superior: '))
    primos(li, ls)

# PROCESSAMENTO
def primos(i, f):
    print('O(s) número(s)', end=' ')
    while i <= f:
        if i == 1:
            i = i + 1
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i, end=' ')
            i = i + 1
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i, end=' ')
            i = i + 1
        else:
            i = i + 1
    print('é(são) primo(s).')

# SAÍDA
main()
