
import random

def shuffleString(x,n):
    hsl = []
    i   = 0
    while i < n:
        print(i+1)
        ack = ''.join(random.sample(x,len(x)))
        if (ack not in hsl):
            hsl.append(ack)
            i   += 1
    print(hsl)

shuffleString('abc',6)