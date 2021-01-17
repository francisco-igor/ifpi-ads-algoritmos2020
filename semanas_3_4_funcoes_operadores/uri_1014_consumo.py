def main():
    x = int(input())
    y = float(input())
    consumo(x, y)

def consumo(x, y):
    consumo = x / y

    print('{:.3f} km/l'.format(consumo))

main()
