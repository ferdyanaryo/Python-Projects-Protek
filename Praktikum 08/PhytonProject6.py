def sortStringByChar(bil):
    #key=len berdasarkan panjang char
    bil.sort(key=len,reverse=True)

    print(bil)


bil = ["jeruk","rambutan","tomat","kangkung"]
sortStringByChar(bil)
