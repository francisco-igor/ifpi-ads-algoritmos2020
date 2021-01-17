def main():
    x = float(input())

    if 0 <= x <= 400:
        percentual = 15
        salario = novo_salario(x, percentual)
    
    elif 400.01 <= x <= 800:
        percentual = 12
        salario = novo_salario(x, percentual)
    
    elif 800.01 <= x <= 1200:
        percentual = 10
        salario = novo_salario(x, percentual)

    elif 1200.01 <= x <= 2000:
        percentual = 7
        salario = novo_salario(x, percentual)

    elif 2000 < x:
        percentual = 4
        salario = novo_salario(x, percentual)

    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste(x, percentual):.2f}')
    print(f'Em percentual: {percentual} %')

def reajuste(x, y):
    reajuste = (x * y) / 100
    return reajuste

def novo_salario(x, y):
    novo = reajuste(x, y) + x
    return novo

main()
