def reratasatuan(bil):
    totl = 0
    jmlh = 0

    for x,y in buah.items():
        totl += y
        jmlh += 1

    rta2 = totl/jmlh
    print(rta2)

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

reratasatuan(buah)