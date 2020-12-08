import math
#Judul program
print("Menghitung Tabel Sinus Metode Loop")
print("==========================================")

# tabel_sudut()
sdt_awal = int(input("Masukkan data sudut awal ="))
sdt_akhir = int(input("Masukkan data sudut akhir ="))
interval_sdt = int(input("Masukkan data interval sudut ="))
jml_looping = int((sdt_akhir - sdt_awal)/interval_sdt)+1

print("==========================================")
print("| Nomor | sdt | sinus | cosinus | tangen |")
print("==========================================")

#proses
for i in range(1,jml_looping):
    sdt = sdt_awal + (interval_sdt*i)
    s=float(math.sin(math.radians(sdt)))
    c=float(math.cos(math.radians(sdt)))
    t=float(math.tan(math.radians(sdt)))
    if sdt == 90:
        t = float('inf')

    print("| %5d | %3d | %5.2f | %7.2f | %6.2f |" %(i,sdt,s,c,t))

print("==========================================")