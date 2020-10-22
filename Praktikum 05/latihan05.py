nkod = input("Masukkan kode karyawan             : ")
nnam = input("Masukkan nama karyawan             : ")
ngol = input("Masukkan golongan                  : ")
nmen = input("Masukkan status (1:menikah,2:belum): ")

if (nmen == "1"):
    nank = int(input("Masukkan jumlah anak               : "))
    nme2 = "Menikah"
    tmen = 0.1
    tank = nank * 0.05
    
if (nmen == "2"):
    nme2 = "Belum Menikah"
    nank = 0
    tmen = 0
    tank = 0

print()
print("================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("--------------------------------")
print("Nama Karyawan            :",nnam,"(Kode:",nkod,")")
print("Golongan                 :",ngol)
print("Status Menikah           :",nme2)
print("Jumlah Anak              :",nank)
print("--------------------------------")

if (ngol == "A"):
    ngaji = 10000000
    npers = 0.025

if (ngol == "B"):
    ngaji = 8500000
    npers = 0.02
    
if (ngol == "C"):
    ngaji = 7000000
    npers = 0.015
    
if (ngol == "D"):
    ngaji = 5500000
    npers = 0.01
   
ntmen   = ngaji * tmen
ntank   = ngaji * tank
nkot    = ngaji + ntmen + ntank
npoto   = nkot * npers
nbers   = nkot - npoto

     
print("Gaji Pokok               : Rp",ngaji)
print("Tunjangan Istri/Suami    : Rp",ntmen)
print("Tunjangan Anak           : Rp",ntank)
print("________________________________ +")
print("Gaji Kotor               : Rp",nkot)
print("Potongan (",npers*100,"% )       : Rp",npoto)
print("________________________________ -")
print("Gaji Bersih              : Rp",nbers)