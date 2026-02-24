import DeleteData
import input_data
import Outputdata
import search
import Updatedata

class Main:
    from input_data import InputData
    data_mahasiswa = []
    is_input = True
    token = 0

    while True:
        print("Menu Admin Pendataan Organisasi")
        print("1. Input Data")
        print("2. Output Data")
        print("3. Searching Data")
        print("4.Delete Data")
        print("5.Update Data")
        print("0. Keluar Program")
        token = int(input("Masukkan token menu"))
        match token:
            case 1:
                 while is_input:
                    input_mhs = InputData()
                    data_mahasiswa.append(input_mhs.tambah())
                    lanjut = input("Lanjut Isi? (Y/N): ")
                    if lanjut == "Y" or lanjut == "y":
                        is_input = True
                    else:
                        is_input = False
            case 2:
            case 3:
            case 4:
            case 5:
                print("\nMenu Update Data")
                print("1. Update Nama berdasarkan NIM")
                print("2. Update NIM berdasarkan Nama")
                print("3. Update Divisi berdasarkan NIM")
                print("4. Update Divisi berdasarkan Nama")
                print("5. Keluar")
                
                pilihan_update = input("Pilih menu update (1-5): ")
                
                match pilihan_update:
                    case "1":
                        target_nim = input("Masukkan NIM target yang akan diupdate: ")
                        nama_baru = input("Masukkan Nama baru: ")
                        data_mahasiswa = Updatedata.UpdateNamabyNIM(data_mahasiswa, target_nim, nama_baru)
                        print("Update selesai silahkan cek di menu no.2")
                    case "2":
                        target_nama = input("Masukkan Nama target yang akan diupdate: ")
                        nim_baru = input("Masukkan NIM baru: ")
                        data_mahasiswa = Updatedata.UpdateNIMbyNama(data_mahasiswa, target_nama, nim_baru)
                        print("Update selesai silahkan cek di menu no.2")
                    case "3":
                        target_nim = input("Masukkan NIM target yang akan diupdate:")
                        divisi_baru = input("Masukkan Divisi baru: ")
                        data_mahasiswa = Updatedata.UpdateDivisIByNIM(data_mahasiswa, target_nim, divisi_baru)
                        print("Update selesai silahkan cek di menu no.2")
                    case "4":
                        target_nama = input("Masukkan Nama target yang akan diupdate: ")
                        divisi_baru = input("Masukkan Divisi baru: ")
                        data_mahasiswa = Updatedata.UpdateDivisibyNama(data_mahasiswa, target_nama, divisi_baru)
                        print("Update selesai silahkan cek di menu no.2") 
                    case "5":
                        print("Batal update dan keluar")
                    case _:
                        print("Silahkan input kembali di menu")
                