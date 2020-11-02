
def starFormation(n):
    i = 0
    while (i < n):
        j = i + 1
        while (j > 0):
            print('* ', end='')
            j -= 1
        print()
        i += 1

starFormation(5)