def searchByNim(nim, data_mhs):
    for x in range(len(data_mhs)):
        if data_mhs[x][0]==nim:
            return data_mhs[x]
    return "Mahasiswa dengan nim " + nim + " tidak ditemukan"  

def searchByNama(nama, data_mhs):
    for x in range(len(data_mhs)):
        if nama.lower() in data_mhs[x][1].lower():
            return data_mhs[x]
    return "Mahasiswa dengan nama " + nama + " tidak ditemukan"