'''Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.'''

# ENTRADA

def main():
    n = int(input('Digite a quantidade de termos requeridos da sequência de Fibonacci: '))

    sequencia(n)

# PROCESSAMENTO
def sequencia(n):
    primeiro = 0   # termo anterior
    segundo = 1    # termo posterior
    contador = 1
    while contador <= n:
        print(primeiro, end=' ')
        soma = primeiro + segundo
        primeiro = segundo
        segundo = soma
        contador = contador + 1

# SAÍDA
main()
