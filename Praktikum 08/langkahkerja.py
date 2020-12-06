print("1.Buatlah list a = [1, 5, 6, 3, 6, 9, 11, 20, 12] dan b = [7, 4, 5, 6, 7, 1, 12, 5, 9")
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
print(a)
print(b)
print('')

print("2.Sisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b")
#insert(indeks ke-9, nilai)
a.insert(3,10)
b.insert(2,15)
print(a)
print(b)
print('')

print("3.Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b")
#insert ke indeks terakhir
a.append(4)
b.append(8,4,2)
print(a)
print(b)
print('')

print("4.Kemudian lakukan sorting secara ascending pada list a dan b")
a.sort()
b.sort()
print(a)
print(b)
print('')

print("5.Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)")
c = a[0:8]
d = b[2:10]
print(c)
print(d)
print('')

print("6.Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.")
e = []
for i in range(len(c)):
    n = c[i] + d[i]
    e.append(n)
print(e)
print('')

print("7.Ubahlah list e ke dalam tuple")
eTup = tuple(e)
print(eTup)
print('')

print('8.Carilah nilai min, maks, dan jumlahan seluruh elemen dari e')
print('min    = ',min(eTup))
print('maks   = ',max(eTup))
print('jumlah = ',sum(eTup))
print('')

print('9.Buatlah sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”')
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)
print('')

print('10.Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut')
nmyS = set(myString)
print(nmyS)
print('')

print('11.Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list. ')
lstm = list(nmyS)
lstm.sort()
print(lstm) 

