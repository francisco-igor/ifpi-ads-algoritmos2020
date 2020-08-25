'''Leia N e escreva todos os números inteiros pares de 1 a N.'''

# ENTRADA
def main():
    n = int(input('Digite um número: '))
    
    inteiros(n)

# PROCESSAMENTO
def inteiros(n):
    contador = 1
    while contador <= n:
        if contador % 2 == 0:
            print(contador, end=' ')
        contador = contador + 1

# SAÍDA
main()
