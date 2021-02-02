def main():
    x = int(input())
    
    while x != 0:
        s = 0
        cont = 0
        while cont < 5:
            if x % 2 == 0:
                s = s + x
                cont = cont + 1
            x = x + 1
        
        print(s)
        x = int(input())

main()
