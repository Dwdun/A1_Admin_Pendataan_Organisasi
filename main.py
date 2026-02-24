class Main:
    from input_data import InputData
    data_mahasiswa = []
    is_input = True
    
    while is_input:
        input_mhs = InputData()
        data_mahasiswa.append(input_mhs.tambah())
        lanjut = input("Lanjut Isi? (Y/N): ")
        if lanjut == "Y" or lanjut == "y":
            is_input = True
        else:
            is_input = False

    print(data_mahasiswa)