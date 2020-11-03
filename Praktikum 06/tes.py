def maks(*MyData):
    maks = 0
    for data in MyData:
        if data > maks:
            print(maks)
            maks = data
    
    print(maks)

maks(123,23,21,23,2,32)