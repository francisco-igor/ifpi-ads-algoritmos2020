def main():
    a, b, c = input().split(' ')
    maior(a, b, c)

def maior(a, b, c):
    MaiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2

    MaiorABC = (int(MaiorAB) + int(c) + abs(int(MaiorAB) - int(c))) / 2

    print('{:.0f} eh o maior'.format(MaiorABC))

main()
