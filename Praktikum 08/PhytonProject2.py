def dataStat(x):
    xlis = []
    a = sum(x) / len(x)
    b = max(x)
    c = min(x)
    xlis.append(a)
    xlis.append(b)
    xlis.append(c)

    print(xlis)

while True :
    try:
        n = int(input("Tentukan banyak bilangan n = "))

        nlist = []
        for i in range(n):
            print('')
            print('n ke',i+1)
            z = int(input("Masukkan nilai n = "))
            nlist.append(z)

        print('')
        print('n =',nlist)
        print('')
        x = nlist
        dataStat(x)
        break 

    except ValueError:
        print("Input harus integer")
        continue