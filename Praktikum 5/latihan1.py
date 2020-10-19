nindo   = int(input("MasukKan nilai Bhs Indonesia   : "))
nmtk    = int(input("Masukkan nilai Matematika      : "))
nipa    = int(input("Masukkan nilai IPA             : "))

if (nmtk > 70):
    if (nindo >= 60) and (nipa >= 60):
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
else:
    status = "TIDAK LULUS"

print("Status Kelulusan               :",status)