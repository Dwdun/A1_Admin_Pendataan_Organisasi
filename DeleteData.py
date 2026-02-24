def DeleteData(data_mhs,target_nim):

    ditemukan=0
    for data in data_mhs:
        if data[0] == target_nim:
            ditemukan=1
            confirmasi = input("nim " + str(target_nim) + ' ditemukan. input "confirm" untuk lanjut: ')
            if confirmasi == 'confirm':
                data_mhs.remove(data)
    if ditemukan == 0:
        print("nim tidak ditemukan")
    return data_mhs