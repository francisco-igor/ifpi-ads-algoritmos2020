def main():
    x = int(input())
    z = 0
    while z <= x:
        z = int(input())
    
    cont = 1
    soma = x
    while x <= z:
        x = x + soma + 1
        soma = soma + 1
        cont = cont + 1
    print(cont)

main()
