def tampil_data(data_mhs):
    if not data_mhs:
        print("Data mahasiswa masih kosong.")
        return
    
    print("\n=== DATA MAHASISWA ===")
    print("{:<10} {:<20} {:<15}".format("NIM", "Nama", "Divisi")) #jarak supaya format rapi
    print("-" * 45) #print - 45 kali

    for i in range(len(data_mhs)):
        print("{:<10} {:<20} {:<15}".format(
            data_mhs[i][0],
            data_mhs[i][1],
            data_mhs[i][2]
        ))