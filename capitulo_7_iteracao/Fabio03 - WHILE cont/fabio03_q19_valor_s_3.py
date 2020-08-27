'''Leia N, calcule e escreva o valor de S.'''

# ENTRADA
def main():
    n = int(input('Digite um valor para N: '))

    valor(n)

# PROCESSADOR
def valor(n):
    numerador = 1
    denominador = n
    soma = 0
    while numerador <= n:
        soma = soma + (numerador / denominador)
        
        guardar_numerador = numerador
        numerador = denominador - 1
        denominador = guardar_numerador + 1

        soma = soma - (numerador / denominador)
        
        guardar_denominador = denominador
        denominador = numerador - 1
        numerador = guardar_denominador + 1

    print(f'O valor de S é {soma}')

# SAÍDA    
main()
