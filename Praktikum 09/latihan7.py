mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('')
print('='*65)

print('NIM'.ljust(10),'NAMA MAHASISWA'.ljust(25),
      'TGL LAHIR'.ljust(14),'TEMPAT LAHIR'.ljust(15))

print('-'*65)

for i in mhs:
    lst = i.split(':')
    tgl = lst[2].split('-')
    tg2 = '/'.join([tgl[2],tgl[1],tgl[0]])
    
    print(lst[0].ljust(10),lst[1].ljust(25),
          tg2.ljust(14),lst[3].ljust(15))

print('-'*65)
print('')

