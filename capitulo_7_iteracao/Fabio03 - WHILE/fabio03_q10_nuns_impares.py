'''Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.'''

# ENTRADA
def main():
    li = int(input('Digite o Limite Inferior: '))
    ls = int(input('Digite o Limite Superior: '))
    contador(li, ls)

def contador(li, ls):
    while li <= ls:
        if li % 2 != 0:
            print(li, end=' ')
        li = li + 1

# SAÍDA
main()
