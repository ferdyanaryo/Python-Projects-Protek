def ubahHuruf(teks, a, b):
    lst = list(teks)
    hsl = '' 
    
    for i in lst:
        if i == a:
            i = b
        hsl = ''.join([hsl,i])
    return hsl

n = ubahHuruf('MATEMATIKA','T','S')
print(n)