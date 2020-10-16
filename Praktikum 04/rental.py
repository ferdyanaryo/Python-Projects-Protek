#input waktu awal dan akhir penyewaan
ja = int(input("Input Jam Ambil ..."))
ma = int(input("Input Menit Ambil ..."))
jk = int(input("Input Jam Kembali ..."))
mk = int(input("Input Menit Kembali ..."))

lamasewa    = ( jk - ja ) + ((mk-ma)/60)
lamajam     = jk-ja
lamamenit   = mk-ma

print("Disewa selama",lamajam,"jam",lamamenit,"menit")

if (lamasewa < 12):
    harga = 200000
    print("Tarif penyewaan sebanyak Rp",harga)
else:
    harga = (lamasewa-12)*10000+200000
    print("Tarif penyewaan sebanyak Rp",harga)
    
