nindo   = int(input("MasukKan nilai Bhs Indonesia   : "))
nipa    = int(input("Masukkan nilai IPA             : "))
nmtk    = int(input("Masukkan nilai Matematika      : "))

if (0 <= nmtk <= 100) and (0 <= nindo <= 100) and (0 <= nipa <= 100):
    if (nmtk > 70):
        if (nindo >= 60) and (nipa >= 60):
            status = "LULUS"
        else:
            status = "TIDAK LULUS"
    else:
        status = "TIDAK LULUS"
    
    print("Status Kelulusan               :",status)
    if (nindo < 60) or (nipa < 60) or (nmtk <= 70):
        print("Sebab                          :")
        if (nindo < 60):
            print("- Nilai bahasa Indonesia kurang dari 60")
        if (nmtk <= 70):
            print("- Nilai matematika tidak lebih dari 70")
        if (nipa < 60):
            print("- Nilai IPA kurang dari 60")
 

else:
    print("")
    print("Maaf input ada yang tidak valid")
    print("")
