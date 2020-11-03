
def faktorial(n):
    n2 = n-1 
    while (n2 > 1):
        n   = n*n2
        n2 -=1

    return n

a = 5
b = 3
C = faktorial(a) / faktorial(b) * faktorial(a-b)
print("a. C (",a,",",b,") =",C)

x = 10
y = 7
P = faktorial(x) / faktorial(x-y)
print("b. P (",x,",",x,") =",P)
