jarak1  = int(input("Jarak Kota A ke Kota B = "))
kec1    = int(input("Kecepatan = "))
jarak2  = int(input("Jarak Kota B ke Kota C = "))
kec2    = int(input("Kecepatan = "))

istirahatmenit = int(input("Waktu istirahat (menit) = "))
istirahatjam   = istirahatmenit

berangkatjam   = int(input("Jam berangkat = "))
berangkatmenit = int(input("Menit berangkat = "))

waktu      = (jarak1/kec1)*60+(jarak2/kec2)*60+(istirahatmenit)
waktujam   = waktu//60
waktumenit = 60*((waktu%60)//1)/100
#print(waktujam)
#print(waktumenit)

sampaijam   = berangkatjam+waktujam
sampaimenit = berangkatmenit+waktumenit

print("Pak Amir akan sampai tujuan pukul",sampaijam,"lebih",sampaimenit,"menit")
