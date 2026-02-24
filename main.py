import DeleteData
import input_data
import Outputdata
import search
import Updatedata
import sort

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
        print("4. Delete Data")
        print("5. Update Data")
        print("6. Sort Data")
        print("0. Keluar Program")
        token = int(input("Masukkan menu : "))
        match token:
            case 1:
                 while is_input:
                    input_mhs = InputData()
                    hasil_input_dict = input_mhs.tambah()
                    
                    for mhs in hasil_input_dict:
                        data_format_list = [mhs["nim"], mhs["nama"], mhs["divisi"]]
                        data_mahasiswa.append(data_format_list)
                        
                    lanjut = input("Lanjut Isi? (Y/N): ")
                    if lanjut == "Y" or lanjut == "y":
                        is_input = True
                    else:
                        is_input = False
            case 2:
                print("\n=== OUTPUT DATA ===")
                Outputdata.tampil_data(data_mahasiswa)
            case 3:
                print("\nMenu Pencarian Data")
                print("1. Cari berdasarkan NIM")
                print("2. Cari berdasarkan Nama")
                print("3. Keluar")
                
                pilihan_search = input("Pilih menu pencarian (1-3): ")
                
                match pilihan_search:
                    case "1":
                        target_nim = input("Masukkan NIM yang dicari: ")
                        hasil = search.searchByNim(target_nim, data_mahasiswa)
                        
                        if type(hasil) == list:
                            print("\n--- Data Ditemukan ---")
                            print(f"NIM    : {hasil[0]}")
                            print(f"Nama   : {hasil[1]}")
                            print(f"Divisi : {hasil[2]}")
                            print("----------------------")
                        else:
                            print(f"\n{hasil}") 
                            
                    case "2":
                        target_nama = input("Masukkan potongan Nama yang dicari: ")
                        hasil = search.searchByNama(target_nama, data_mahasiswa)
                
                        if type(hasil) == list:
                            print("\n--- Data Ditemukan ---")
                            print(f"NIM    : {hasil[0]}")
                            print(f"Nama   : {hasil[1]}")
                            print(f"Divisi : {hasil[2]}")
                            print("----------------------")
                        else:
                            print(f"\n{hasil}") 
                    case "3":
                        print("Batal pencarian dan keluar.")
                    case _:
                        print("Pilihan tidak valid, silahkan coba lagi.")
            case 4:
                target_nim = input("Masukkan NIM data yang akan dihapus: ")
                data_mahasiswa = DeleteData.DeleteData(data_mahasiswa, target_nim)
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
            case 6:
                print("\nMenu Sort Data")
                print("1. Sort Data berdasarkan NIM (Ascending)")
                print("2. Sort Data berdasarkan NIM (Descending)")
                print("3. Sort Data berdasarkan Nama (Ascending)")
                print("4. Sort Data berdasarkan Nama (Descending)")
                print("5. Keluar")
                
                pilihan_sort = input("Pilih menu sort (1-5): ")
                
                match pilihan_sort:
                    case "1":
                        temp = sort.sortByNimAsc(data_mahasiswa)
                        for mhs in temp:
                            print(mhs)
                    case "2":
                        temp = sort.sortByNimDesc(data_mahasiswa)
                        for mhs in temp:
                            print(mhs)
                    case "3":
                        temp = sort.sortByNamaAsc(data_mahasiswa)
                        for mhs in temp:
                            print(mhs)
                    case "4":
                        temp = sort.sortByNamaDesc(data_mahasiswa)
                        for mhs in temp:
                            print(mhs)
                    case "5":
                        print("Batal sort dan keluar")
                    case _:
                        print("Silahkan input kembali di menu")
            case 0:
                break