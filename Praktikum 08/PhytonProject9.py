buah = {'apel' : 5000, 
        'jeruk' : 8500, 
        'mangga' : 7800,
        'duku' : 6500}

print('Daftar harga buah :')

for x,y in buah.items():
    print(x,': Rp',y)

while True:
    #try:
    pilih = str(input("Nama buah yang dibeli = "))
    if pilih in buah.keys():
        while True:
            try:
                jumlh = int(input("Berapa                = "))
                print('------------------------')
                print('Total harga           =',buah.get(pilih,0)*jumlh)
                break
            except ValueError:
                print("input harus angka")
        break
    else:
        print("Nama buah tidak ditemukan")
    #except         
        
