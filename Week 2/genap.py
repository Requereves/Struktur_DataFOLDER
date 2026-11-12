banyak = 0
terbesar = 0

n = int(input("masukkan angka: "))
while n != 0:
    if n % 2 == 0:
        banyak += 1
        if n > terbesar:
            terbesar = n
    n = int(input("masukkan angka: "))

print(banyak, terbesar)