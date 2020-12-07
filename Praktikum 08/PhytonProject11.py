buah = {'apel' : 5000, 
        'jeruk' : 8500, 
        'mangga' : 7800,
        'duku' : 6500}

def show():
    print("Data buah:")
    print('')
    for x,y in buah.items():
        print('- {0} (Harga Rp {1}/kg)'.format(x,y))
    print('')

def beli():
    x= []

    while True:
        #try:
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
                print('Total harga           = Rp',sum(x))
                print('')
                break

        else:
            print("Nama buah tidak ditemukan")
            print('')
        #except     

def tambah():
    nma = str(input('Masukkan nama buah         : '))
    if nma in buah.keys():
        print('buah sudah ada dalam daftar')
        print('')
    else:
        try:
            hrg = int(input('Masukkan harga satuan      : '))
        except ValueError:
            print('harga harus angka')
            print('')
            return
        buah.update({nma: hrg})
        show()

        
    
while True:
    print("Menu :")
    print("A. Tambah data buah")
    print("B. Beli buah")
    print('')

    pilih = str(input('Pilihan menu : '))
    print('')
    if (pilih == 'A') or (pilih == 'a'):
        tambah()
    elif (pilih == 'B') or (pilih == 'b'):
        beli()
    else:
        break
         
