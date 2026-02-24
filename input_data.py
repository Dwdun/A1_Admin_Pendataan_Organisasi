class InputData:
            
    def tambah(self):
        berapa = int(input("Masukkan Jumlah Mahasiswa Yang Ingin Diinputkan: "))
        
        data_baru = []
        
        for i in range(berapa):  
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            divisi = input("Masukkan Divisi: ")
        
            data ={"nim": nim, "nama": nama, "divisi": divisi}
            data_baru.append(data)
        return data_baru
    