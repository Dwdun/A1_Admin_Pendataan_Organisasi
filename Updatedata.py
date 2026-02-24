def UpdateNamabyNIM(data_mhs,target_NIM,nama_Baru):
    ditemukan = 0

    for i in range(len(data_mhs)):
        if data_mhs[i][0] == target_NIM:
            data_mhs[i][1] = nama_Baru
            ditemukan = 1
            break
    
    if ditemukan == 0:
        print("NIM tidak ditemukan")
    
    return data_mhs

def UpdateNIMbyNama(data_mhs,target_nama,NIM_baru):
    ditemukan = 0

    for i in range(len(data_mhs)):
        if data_mhs[i][1] == target_nama:
            data_mhs[i][0] = NIM_baru
            ditemukan = 1
            break

    if ditemukan == 0:
        print("Nama Tidak Ditemukan")

    return data_mhs

def UpdateDivisIByNIM(data_mhs,target_NIM, Divisi_baru):    
    ditemukan = 0

    for i in range(len(data_mhs)):
        if data_mhs[i][0] == target_NIM:
            data_mhs[i][2] = Divisi_baru
            ditemukan = 1
            break

    if ditemukan == 0:
        print("NIM tidak ditemukan")
    
    return data_mhs

def UpdateDivisibyNama(data_mhs,target_nama,Divisi_baru):
    ditemukan = 0

    for i in range(len(data_mhs)):
        if data_mhs[i][1] == target_nama:
            data_mhs[i][2] = Divisi_baru
            ditemukan = 1
            break

    if ditemukan == 0:
        print("Nama tidak ditemukan")

    return data_mhs

