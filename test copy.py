print('============================')
print('Kode Waktu')
print('1. Jam')
print('2. Menit')
print('3. Detik')

a = int(input('Pilih kode waktu yang dikonversi : '))
b = int(input('Pilih kode waktu hasil konversi  : '))
c = int(input('Masukan jam = '))
x = 60

if a == 1:
    if b == 1:
        hasil = c
    if b == 2:
        hasil = c*x
    if b == 3:
        hasil = c*x*x

if a == 2:
    if b == 1:
        hasil = c/x
    if b == 2:
        hasil = c
    if b == 3:
        hasil = c*x

if a == 3:
    if b == 1:
        hasil = c/x/x
    if b == 2:
        hasil = c/x
    if b == 3:
        hasil = c

print('Hasil konversi',int(hasil))
    