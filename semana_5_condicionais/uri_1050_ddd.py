def main():
    ddd = int(input())
    cidade = buscar(ddd)
    print(cidade)

def buscar(x):
    if x == 61:
        return 'Brasilia'
    elif x == 71:
        return 'Salvador'
    elif x == 11:
        return 'Sao Paulo'
    elif x == 21:
        return 'Rio de Janeiro'
    elif x == 32:
        return 'Juiz de Fora'
    elif x == 19:
        return 'Campinas'
    elif x == 27:
        return 'Vitoria'
    elif x == 31:
        return 'Belo Horizonte'
    else:
        return 'DDD nao cadastrado'

main()
