print("----------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("----------------------------")

nlgi = 'y'
njml = 0
nsat = 0

while (nlgi == 'y'):
    try:
        n     = int(input('Masukkan bilangan bulat : '))
        njml  = njml + n
        nsat += 1
        nlgi = str(input('Lagi (y/n) : '))            
        
    except ValueError:
        print("Bukan bilangan bulat")
        nlgi = 'y'

nrat = njml / nsat
print('')
print("Rata-ratanya adalah: ",nrat)
print('')

