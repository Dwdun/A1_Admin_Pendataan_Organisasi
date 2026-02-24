def sortByNimAsc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[0])

def sortByNimDesc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[0], reverse=True)

def sortByNamaAsc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[1].lower())

def sortByNamaDesc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[1].lower(), reverse=True)

data_mahasiswa = [
    ["251524023", "Muhammad Faqih Shiam", "Luar Himpunan"],
    ["251524004", "Bima Anugerah Prasetyo", "Teknologi"],
    ["251524010", "Irfan Ramadhan", "Seni dan Olahraga"]
]

print("=== Urut Berdasarkan NIM (Ascending) ===")
data_nim_asc = sortByNimDesc(data_mahasiswa)
for mhs in data_nim_asc:
    print(mhs)

print("\n=== Urut Berdasarkan Nama (Descending) ===")
data_nama_desc = sortByNamaAsc(data_mahasiswa)
for mhs in data_nama_desc:
    print(mhs)