nkod = input("Masukkan kode karyawan   : ")
nnam = input("Masukkan nama karyawan   : ")
ngol = input("Masukkan golongan        : ")

print()
print("================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("--------------------------------")
print("Nama Karyawan            :",nnam,"(Kode:",nkod,")")
print("Golongan                 :",ngol)
print("--------------------------------")

if (ngol == "A"):
    ngaji = 10000000
    npers = 0.025
    npoto = ngaji * npers
    nbers = ngaji - npoto
if (ngol == "B"):
    ngaji = 8500000
    npers = 0.02
    npoto = ngaji * npers
    nbers = ngaji - npoto
if (ngol == "C"):
    ngaji = 7000000
    npers = 0.015
    npoto = ngaji * npers
    nbers = ngaji - npoto
if (ngol == "D"):
    ngaji = 5500000
    npers = 0.01
    npoto = ngaji * npers
    nbers = ngaji - npoto

        
print("Gaji Pokok               : Rp",ngaji)
print("Potongan (",npers*100,"% )       : Rp",npoto)
print("--------------------------------")
print("Gaji Bersih              : Rp",nbers)

