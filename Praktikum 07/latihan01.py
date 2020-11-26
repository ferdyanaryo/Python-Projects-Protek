try:
    file = open("c:/myfile.txt","r")
    print(file.read())

except FileNotFoundError:
    print("File anda tidak ditemukan")