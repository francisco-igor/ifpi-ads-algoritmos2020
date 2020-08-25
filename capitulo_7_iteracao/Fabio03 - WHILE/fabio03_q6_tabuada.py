'''Escreva a tabuada dos números de 1 a 10.'''

# ENTRADA
def main():
    m = int(input('Digite um número: '))
    li = 1
    ls = 10
    adicao(li, ls, m)
    subtracao(li, ls, m)
    multiplicacao(li, ls, m)
    divisao(li, ls, m)
    
# PROCESSAMENTO    
def adicao(li, ls, m):
    print('Adição:')
    while li <= ls:
        print(f'{li} + {m} = {li+m}')
        li = li + 1

def subtracao(li, ls, m):
    print('Subtração:')
    while li <= ls:
        print(f'{li} - {m} = {li-m}')
        li = li + 1

def multiplicacao(li, ls, m):
    print('Multiplicação:')
    while li <= ls:
        print(f'{li} x {m} = {li*m}')
        li = li + 1

def divisao(li, ls, m):
    print('Divisão:')
    while li <= ls:
        print(f'{li} / {m} = {li/m:.0f}')
        li = li + 1

# SAÍDA
main()
