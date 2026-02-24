def UpdateNamabyNIM(data_mhs,target_NIM,nama_Baru):
    ditemukan = 0

    for i in data_mhs:
        if data_mhs[i][0] == target_NIM:
            data_mhs[i][1] = nama_Baru
            ditemukan = 1
            break
    
    if ditemukan == 0:
        print("NIM tidak ditemukan")
    
    return data_mhs




