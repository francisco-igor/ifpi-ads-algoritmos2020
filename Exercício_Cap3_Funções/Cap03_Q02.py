def do_twice(o, v):
    o(v)
    o(v)

def print_twice(v):
    print(v)
    print(v)

def do_four(o, v):
    do_twice(o, v)
    do_twice(o,v)

do_twice(print_twice, 'spam')
do_four(print_twice, 'Eae')