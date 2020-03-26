'''Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
sempre pelo mais barato.'''

# ENTRADA
def main():
    preço1 = float(input('Quanto custa o produto 1? R$ '))
    preço2 = float(input('Quanto custa o produto 2? R$ '))
    preço3 = float(input('Quanto custa o produto 3? R$ '))
    comprar(preço1, preço2, preço3)

# PROCESSAMENTO
def comprar(preço1, preço2, preço3):
    if preço1 != preço2 != preço3:
        if preço1 < preço2 and preço1 < preço3:
            print('O produto 1 deve ser comprado.')
        elif preço2 < preço1 and preço2 < preço3:
            print('O produto 2 deve ser comprado.')
        elif preço3 < preço2 and preço3 < preço1:
            print('O produto 3 deve ser comprado.')
    else:
        print('Produtos com preços iguais.')
    
# SAÍDA
main()
