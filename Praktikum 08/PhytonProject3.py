while True :
    try:
        n = int(input("Tentukan banyak mahasiswa = "))
    except ValueError:
        print("Input tidak valid")
        continue

    nlist = []
    for i in range(n):
        print('')
        x = str(input("Masukkan nama mahasiswa = "))
        nlist.append(x)

    print('')
    nlist.sort()
    for i in range(n):
        print(nlist[i],'(',len(nlist[i]),'karakter )')
    
    break

