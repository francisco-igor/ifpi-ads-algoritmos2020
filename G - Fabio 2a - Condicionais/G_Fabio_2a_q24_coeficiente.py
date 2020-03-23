'''Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
coeficiente A deve ser diferente de 0 (zero).'''

# ENTRADA
def main():
    a = int(input('Valor do coeficiente A: '))
    b = int(input('Valor do coeficiente B: '))
    c = int(input('Valor do coeficiente C: '))
    equação(a, b, c)

# PROCESSAMENTO
def equação(a, b, c):
    if a != 0:
        ra = a ** (1/2)
        print(f'A raiz de "a" é {ra}')
        rb = b ** (1/2)
        print(f'A raiz de "b" é {rb}')
        rc = c ** (1/2)
        print(f'A raiz de "c" é {rc}')
        
# SAÍDA
main()
