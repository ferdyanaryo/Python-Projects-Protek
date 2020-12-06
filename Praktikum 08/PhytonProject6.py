def sortStringByChar(bil):
    
    bil.sort(key=len,reverse=True)

    print(bil)


bil = ["jeruk","rambutan","tomat","kangkung"]
sortStringByChar(bil)
