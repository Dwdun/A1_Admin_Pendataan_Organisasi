def sortByNimAsc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[0])

def sortByNimDesc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[0], reverse=True)

def sortByNamaAsc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[1].lower())

def sortByNamaDesc(data_mhs):
    return sorted(data_mhs, key=lambda x: x[1].lower(), reverse=True)