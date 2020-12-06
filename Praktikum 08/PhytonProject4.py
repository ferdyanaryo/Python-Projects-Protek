sayur = ["bayam", "kangkung", "wortel", "selada"]
print(sayur)

while True:
    print('')
    print('Menu:')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    print('')

    menu = str(input("Pilihan anda: "))
    if (menu == 'A') or (menu == 'a'):
        tmbh = str(input('Sayur yang akan anda tambahkan : '))
        sayur.append(tmbh)
        print(tmbh,'ditambahkan\n')

    elif (menu == 'B') or (menu == 'b'):
        try:
            haps = str(input('Sayur yang akan anda hapus : '))
            sayur.remove(haps)
            print(haps,'dihapus\n')
        except ValueError:
            print('Data tidak ditemukan')

    elif (menu == 'C') or (menu == 'c'):
        print('')
        print(sayur)
        print('')
        break

    else:
        print("Menu anda tidak valid")
        break