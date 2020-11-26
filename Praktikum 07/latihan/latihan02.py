try:
    x = str(input("Masukkan nama file : "))

    file   = open(x,"r")
    #print(file.read())
    
    nlgi = True

    while (nlgi == True):
        file   = open(x,"a")
        ninput = str(input("Data yang mau ditambahkan : "))
        file.write(ninput)

        ninp = str(input("Mau lagi (y/n) : "))
        if ninp == "y":
            nlgi = True

        elif ninp == "n":
            nlgi = False

        else:
            print("input tidak valid")
            nlgi = False

        file.close()
        
            
except FileNotFoundError:
    print("File yang anda cari tidak ditemukan, coba file lain")

except OSError:
    print("File yang anda cari tidak ditemukan, coba file lain")