nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('')
print('='*65)

print('NIM'.ljust(8),'NAMA'.ljust(12),'N.MID'.ljust(10),'N.UAS'.ljust(10),
      'N.AKHIR'.ljust(12),'STATUS'.ljust(10))
      
print('-'*65)

for i in nilai:
    nak = (i['mid'] + 2*i['uas']) / 3
    sts = 'LULUS'
    if nak < 60:
        sts = 'TIDAK LULUS'
    print(i['nim'].ljust(8),i['nama'].ljust(12),
          str(i['mid']).rjust(5),str(i['uas']).rjust(10),
          str(round(nak, 1)).rjust(12),' ',sts.center(11))

print('-'*65)
print('')