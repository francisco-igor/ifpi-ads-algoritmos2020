'''Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
maior quadrado menor que 38 é 36 (quadrado de 6).'''

# ENTRADA
def main():
    n = int(input('Digite um número para saber qual o seu quadrado ou o menor mais próximo: '))

    quadrado(n)

# PROCESSAMENTO
def quadrado(n):
    q = 1
    while q ** 2 <= n:
        t = q ** 2
        q = q + 1
    
    print(f'O maior quadrado menor ou igual a {n} é {t}.')

# SAÍDA
main()
