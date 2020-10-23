from random import randint

print('')
print('"Hai.. Nama saya Mr.Lepi, saya telah memiliki sebuah bilangan bulat acak antara 1 sampai 100. Silahkan tebak ya !!!"')
print('')

bil = randint(0, 100)
nil = 100

while True:
    #print(bil,nil)
    tbk = int(input("Tebakan Anda : "))
    if (tbk == bil):
        print("Yap... Bilangan tebakan anda benar...")
        print('')
        print("Skor Anda : ",nil)
        print('')
        break
    else:
        if (tbk < bil):
            print("Yah... Bilangan tebakan anda terlalu kecil...")
        else:
            print("Yah... Bilangan tebakan anda terlalu besar...")
        nil -= 2
        if (nil < 0):
            print('')
            print("Skor anda habis")
            print('')
            break
         
            
            