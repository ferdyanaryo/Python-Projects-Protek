try:
    file    = open("D:/UNS/Github/data.txt","r")
    sum     = 0

    for data in file:
        try:
            sum = sum + int(data)
            
        except ValueError:
            continue

    print(sum)

except FileNotFoundError:
    print("File anda tidak ditemukan")