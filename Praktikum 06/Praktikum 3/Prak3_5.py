from operation import *

a = 2
b = 4
c = 6
d = 4
print("a. ",a,"+",b,"x",c,"-",d,"= ",
    kurang(jumlah(a,kali(b,c)),d))

a2 = 4
b2 = 7
c2 = 6
d2 = 9
print("b.  (",a2,"+",b2,") x (",c2,"-",d2,") = ",
    kali(jumlah(a2,b2),(kurang(c2,d2))))

a3 = 10
b3 = 2
c3 = 7
d3 = 5
e3 = 12
f3 = 34
print("c.  (",a3,"+",b3,") / (",c3,"+",d3,") / (",e3,"-",f3,") = ",
    bagi(bagi(jumlah(a3,b3),jumlah(c3,d3)),kurang(e3,f3)))