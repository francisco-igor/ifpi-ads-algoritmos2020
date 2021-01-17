def main():
    tg = int(input())
    vm = int(input())
    gasto(tg, vm)

def gasto(x, y):
    distancia = x * y

    gasolina = distancia / 12

    print('{:.3f}'.format(gasolina))

main()
