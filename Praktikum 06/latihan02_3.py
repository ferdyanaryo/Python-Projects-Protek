
def starFormation(n):
    i   = 0
    x   = 0
    n2  = n / 2
    n3  = n / 2 - 1 

    while (i < n2):
        j = i + 1
        while (j > 0):
            print('* ', end='')
            j -= 1
        print()
        i += 1
        
    while (x < n3):
        j = x
        while (j < n3):
            print('* ', end='')
            j += 1
        print()
        x += 1

starFormation(10)