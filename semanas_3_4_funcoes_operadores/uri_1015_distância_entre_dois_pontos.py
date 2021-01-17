def main():
    x1, y1 = input().split(' ')
    x2, y2 = input().split(' ')
    distancia(x1, x2, y1, y2)

def distancia(x1, x2, y1, y2):
    Distancia = (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** 0.5

    print('{:.4f}'.format(Distancia))

main()
