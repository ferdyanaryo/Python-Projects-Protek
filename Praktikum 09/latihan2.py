def bintang(n):    
    for i in range(0,n):
        x = (i*2+1) * '*'
        y = n * 2 - 1
        print(x.center(y))
  
bintang(11)