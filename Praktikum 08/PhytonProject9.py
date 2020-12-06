buah = {'apel' : 5000, 
        'jeruk' : 8500, 
        'mangga' : 7800,
        'duku' : 6500}

print('Daftar harga buah :')

for x,y in buah.items():
    print(x,': Rp',y)

while True:

    pilih = str(input("Nama buah yang dibeli = "))
    while True:
        try:
            jumlh = int(input("Berapa                = "))
            print('------------------------')
            print('Total harga           =',buah.get(pilih,0)*jumlh)
        except ValueError:
            print('tidak valid')
            continue
