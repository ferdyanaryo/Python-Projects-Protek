def bintang(n):
    if (n % 2 == 1): #n harus bilangan ganjil
        n2 = int((n-1)/2)
        n3 = n2+1

        for i in range(0,n2):
            x = (i*2+1) * '*'
            print(x.center(n))
        
        for i in reversed(range(0,n3)):
            x = (i*2+1) * '*'
            print(x.center(n))
    
    else:
        print('n bukan ganjil')
            

bintang(7)