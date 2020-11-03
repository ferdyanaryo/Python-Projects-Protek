
def starFormation1(n):
    i = 0
    while (i < n):
        j = i + 1
        while (j > 0):
            print('* ', end='')
            j -= 1
        print()
        i += 1

#starFormation1(5)