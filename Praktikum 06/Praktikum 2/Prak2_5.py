def luasSegitiga(a,t):
    luas = a * t / 2
    return luas

alas    = 10
tinggi  = 20
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(alas,tinggi))

alas1   = 15
tinggi1 = 45
print('Luas segitiga dg alas ', alas1,
      ' dan tinggi ', tinggi1,
      ' adalah ', luasSegitiga(alas1,tinggi1))

total = luasSegitiga(alas,tinggi) + luasSegitiga(alas1,tinggi1)
print("Total luas kedua segitiga tersebut adalah ",total)