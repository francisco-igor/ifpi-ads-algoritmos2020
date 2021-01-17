def main():
    cod, qtd = input().split(' ')
    cod = int(cod)
    qtd = int(qtd)
    preco(cod, qtd)

def preco(cod, qtd):
    if cod == 1:
        total = qtd * 4
    elif cod == 2:
        total = qtd * 4.5
    elif cod == 3:
        total = qtd * 5
    elif cod == 4:
        total = qtd * 2
    elif cod == 5:
        total = qtd * 1.5

    print('Total: R$ {:.2f}'.format(total))

main()
