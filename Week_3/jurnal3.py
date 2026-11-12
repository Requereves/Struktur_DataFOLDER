def hitung_rata(nilai, n):
    total = 0
    for i in range(n):
        total += nilai[i]
    return total / n 

def cari_nilai_tertinggi(nilai, n):
    tertinggi = nilai[0]
    i = 1
    while i < n:
        if nilai[i] > tertinggi:
            tertinggi = nilai[i]
        i += 1
    return tertinggi

def cari_nilai_terendah(nilai, n):
    terendah = nilai[0]
    i = 1
    while i < n:
        if nilai[i] < terendah:
            terendah = nilai[i]
        i += 1
    return terendah

def cari_indeks_tertinggi(nilai, n):
    index = 0
    i = 1
    while i < n:
        if nilai[i] > nilai[index]:
            index = i
        i += 1
    return index

def cari_indeks_terendah(nilai, n):
    index = 0
    i = 1
    while i < n:
        if nilai[i] < nilai[index]:
            index = i
        i += 1
    return index

def tampilkan_laporan(nama, nilai, n):
    nilai_tertinggi = cari_nilai_tertinggi(nilai, n)
    nilai_terendah = cari_nilai_terendah(nilai, n)
    index_tertinggi = cari_indeks_tertinggi(nilai, n)
    index_terendah = cari_indeks_terendah(nilai, n)
    rata_rata = hitung_rata(nilai, n)
    
    print("====================================")
    print("        LAPORAN NILAI               ")
    print("====================================")
    
    for i in range(n):
        if nilai[i] >= 60:
            status = "lulus"
        else:
            status = "tidak lulus"
        print(i + 1, nama[i], nilai[i], status)
        
    print(f"Nilai Tertinggi: {nilai_tertinggi}", nama[index_tertinggi])
    print(f"Nilai Tertinggi: {nilai_terendah}", nama[index_terendah])
    print(f"rata - rata: ", rata_rata)

nama = []
nilai = []

n = int(input("Masukkan jumlah siswa (2-10): "))

while n < 2 or n > 10:
    print("input harus dari 2 - 10")
    n = int(input("Masukkan jumlah siswa (2-10): "))
    
for i in range(n):
    print("siswa ke ", i + 1)
    nama.append((input("masukin nama: ")))
    nilai_siswa = int(input("masukin nilai: "))
    
    while nilai_siswa < 0 or nilai_siswa > 100:
        print("nilai cuma 0 - 100")
        nilai_siswa = int(input("nilai: "))
        
    nilai.append(nilai_siswa)
        
tampilkan_laporan(nama, nilai, n)