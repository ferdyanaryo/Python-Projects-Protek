def kuadrat(bil):
    n = []
    for i in range(len(bil)):
        x = bil[i] * bil[i]
        n.append(x)
    
    return n

bil   = [4,2,42,2,1,4,3]
hasil = kuadrat(bil)
print(hasil)