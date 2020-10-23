i = 0
n = 0

while (i <= 100):
    g = i % 2
    if (g == 1):
        print(i) 
        i += 1       
        n += 1  
    else:
        i += 1

print("Banyaknya bilangan ganjil :",n)