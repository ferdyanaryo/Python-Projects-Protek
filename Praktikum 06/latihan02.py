
def starFormation1(n):
    i = 0
    while (i < n):
        j = i + 1
        while (j > 0):
            print('* ', end='')
            j -= 1
        print()
        i += 1

def starFormation2(n):
    i = 0
    while (i < n):
        j = i
        while (j < n):
            print('* ', end='')
            j += 1
        print()
        i += 1

def starFormation(n):
    n = n/2
    starFormation1(n)

    if (n % 2 == 0):
        starFormation2(n)
    else:
        n = n-1
        starFormation2(n)
    
starFormation(9)