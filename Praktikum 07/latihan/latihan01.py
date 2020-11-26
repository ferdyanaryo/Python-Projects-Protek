try:
    x = str(input("Masukkan nama file : "))

    file    = open(x,"r")
    print('')
    print(file.read())
    print('')


except FileNotFoundError:
    print("File yang anda cari tidak ditemukan, coba file lain")
    print('')