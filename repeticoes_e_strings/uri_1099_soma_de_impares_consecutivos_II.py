def main():
    n = int(input())
    cont = 0
    while cont < n:
        x, y = input().split()
        x = int(x)
        y = int(y)
        soma = 0

        if x < y:
            for x in range(x + 1, y):
                if eh_impar(x):
                    soma = soma + x
        if x > y:
            for y in range(y + 1, x):
                if eh_impar(y):
                    soma = soma + y
        
        print(soma)
        cont += 1

def eh_impar(x):
    return x % 2 != 0
main()
