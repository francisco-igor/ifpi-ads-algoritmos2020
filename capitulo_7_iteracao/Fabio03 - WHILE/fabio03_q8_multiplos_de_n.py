'''Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.'''

# ENTRADA
def main():
    n = int(input('Digite um Número: '))
    li = int(input('Digite o Limite Inferior: '))
    ls = int(input('Digite o Limite Superior: '))

    multiplo(n, li, ls)

# PROCESSAMENTO
def multiplo(n, li, ls):
    while li <= ls:
        if li % n == 0:
            print(li)
        li = li + 1

# SAÍDA
main()
