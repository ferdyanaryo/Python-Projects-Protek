import tkinter 
import math

window = tkinter.Tk()
window.geometry("500x600")
window.title("Menghitung Tabel Sinus Metode Loop")

label = tkinter.Label(window, text="Menghitung Tabel Sinus Metode Loop")
label1 = tkinter.Label(window, text="="*50).grid(row=1,column=0,columnspan=2)


def hitung():
    
    sdt_awal= int(entry1.get())
    sdt_akhir=int(entry2.get())
    interval_sdt=int(entry3.get())
    jml_looping = int((sdt_akhir - sdt_awal)/interval_sdt)+1
    
        
    
    for i in range(1,jml_looping):
        sdt = sdt_awal + (interval_sdt*i)
        s=float(math.sin(math.radians(sdt)))
        c=float(math.cos(math.radians(sdt)))
        t=float(math.tan(math.radians(sdt)))
        if sdt == 90:
            t = float("INF")
        elif sdt == 270:
            t = float("INF")

        print= tkinter.Label(window, text="| no | sdt | cos | sin | dsa |").grid(row=6,column=0)
        print= tkinter.Label(window, text="| %5d | %3d | %5.2f | %7.2f | %6.2f |" %(i,sdt,s,c,t)).grid(row=i+6,column=0)
        
label1 = tkinter.Label(window, text="Masukkan sudut awal \t:").grid(row=2,column=0)
label2 = tkinter.Label(window, text="Masukkan sudut akhir \t:").grid(row=3,column=0)
label3 = tkinter.Label(window, text="Masukkan interval sudut \t:").grid(row=4,column=0)

entry1 = tkinter.Entry(window)
entry1.grid(row=2,column=1)
entry2 = tkinter.Entry(window)
entry2.grid(row=3,column=1)
entry3 = tkinter.Entry(window)
entry3.grid(row=4,column=1)




button = tkinter.Button(window, text="Hitung!", command=hitung).grid(row=5,column=0,columnspan=2)


label.grid(row=0,column=0,columnspan=2,)
window.mainloop()