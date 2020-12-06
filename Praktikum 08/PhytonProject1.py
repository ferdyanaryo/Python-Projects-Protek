while True :
    try:
        n = int(input("Tentukan banyak bilangan n = "))

        nlist = []
        for i in range(n):
            print('')
            print('n ke',i+1)
            x = int(input("Masukkan nilai n = "))
            nlist.append(x)

        print('')
        nlist.sort(reverse=True)
        print('n =',nlist)
        break 

    except ValueError:
        print("Input harus integer")
        continue