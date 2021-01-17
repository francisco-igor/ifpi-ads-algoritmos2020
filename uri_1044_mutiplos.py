def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    multiplos(a, b)

def multiplos(a, b):
    if a > b:
        if a % b == 0:
            print('Sao Multiplos')
        else:
            print('Nao sao Multiplos')

    elif b > a:
        if b % a == 0:
            print('Sao Multiplos')
        else:
            print('Nao sao Multiplos')

    else:
        print('Sao Multiplos')

main()
