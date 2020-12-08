nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]


def tertinggi():
    nakhrMhs = []
    nama      = {}
    nim      = {}
    for i in range(len(nilaiMhs)):
        nmid = nilaiMhs[i]['mid']
        nuas = nilaiMhs[i]['uas']
        akhr = (nmid + 2*nuas) / 3
        nama[nilaiMhs[i]['nama']] = akhr
        nim[nilaiMhs[i]['nim']] = akhr
    x   = max(nama, key=nama.get)
    y   = max(nim, key=nim.get)
    print('Mahasiswa nilai tertinggi adalah',x,'dengan nim',y)

tertinggi()


