'''Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades'''

# ENTRADA
def main():
    num = int(input('Digite um número inteiro: '))
    imprimir(num)

# PROCESSAMENTO
def plural_c(c):
    if c > 1:
        return 'centenas'
    elif c == 1:
        return 'centena'

def plural_d(d):
    if d > 1:
        return 'dezenas'
    elif d == 1:
        return 'dezena'

def plural_u(u):
    if u > 1:
        return 'unidades'
    elif u == 1:
        return 'unidade'

def imprimir(n):
    c = n // 100
    d = (n % 100) // 10
    u =  (n % 100) % 10
    if 0 < n < 1000:
        if c != 0 and d != 0 and u != 0:
            print(f'{n} = {c} {plural_c(c)}, {d} {plural_d(d)} e {u} {plural_u(u)}.')
        elif c == 0 and d == 0:
            print(f'{n} = {u} {plural_u(u)}.')
        elif c == 0 and u == 0:
            print(f'{n} = {d} {plural_d(d)}.')
        elif d == 0 and u == 0:
            print(f'{n} = {c} {plural_c(c)}.')
        elif c == 0:
            print(f'{n} = {d} {plural_d(d)} e {u} {plural_u(u)}.')
        elif d == 0:
            print(f'{n} = {c} {plural_c(c)} e {u} {plural_u(u)}.')
        elif u == 0:
            print(f'{n} = {c} {plural_c(c)} e {d} {plural_d(d)}.')
        else:
            print('Valor deve ser menor que 1000.')

# SAÍDA
main()
