negatif = 0
positif = 0

n = int(input("masukkan angka: "))

while n != 0:
    if n < 0:
        negatif += 1
    else:
        positif += 1
        
    n = int(input("Masukkan angka: "))

if negatif > positif:
    hasil = "negatif"
elif positif > negatif:
    hasil = "positif"
else:
    hasil = "imbang"

print(negatif, positif, hasil)