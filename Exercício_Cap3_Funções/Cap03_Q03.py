def linha():
    print('+ - - - - - + - - - - - +')

def coluna():
    print('|           ', end='')

def coluna2():
    coluna()
    coluna()
    print('|')

def coluna4():
    coluna2()
    coluna2()

def coluna8():
    coluna4()
    coluna4()

def montagem():
    linha()
    coluna8()
    linha()
    coluna8()
    linha()

montagem()