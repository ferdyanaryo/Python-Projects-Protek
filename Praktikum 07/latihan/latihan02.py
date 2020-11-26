try:
    x = str(input("Masukkan nama file : "))

    
    nlgi = 'y'
    if (nlgi == 'y'):
        ninput = str(input("Data yang mau ditambahkan : "))
        file   = open(x,"r")
        file.write(ninput)
        nlgi = str(input("Mau lagi (y/n) : "))
    else:
        print('')
        print(file.read())
        print('')


except FileNotFoundError:
    print("File yang anda cari tidak ditemukan, coba file lain")
    print('')