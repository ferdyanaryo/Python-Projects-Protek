buah = {'apel' : 5000, 
        'jeruk' : 8500, 
        'mangga' : 7800,
        'duku' : 6500}

#print('Daftar harga buah :')

#for x,y in buah.items():
#    print(x,': Rp',y)

x= []

while True:
    #try:
    print('')
    pilih = str(input("Nama buah yang dibeli = "))
    if pilih in buah.keys():
        
        try:
            jumlh = int(input("Berapa  Kg            = "))
            z = buah.get(pilih,0)*jumlh
            x.append(z)
        except ValueError:
            print("input harus angka")
            print('')
            continue
        
        print('')
        lagii = str(input('Beli buah yang lain (y/n) ? '))
        if lagii == 'n':
            print('------------------------')
            print('Total harga           =',sum(x))
            break

    else:
        print("Nama buah tidak ditemukan")
        print('')
    #except         
        
