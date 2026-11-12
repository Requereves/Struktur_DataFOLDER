n = int(input("Masukkan angka: "))

prima = n >= 2
i = 2
while i * i <= n and prima:
    if n % i == 0:
        prima = False
    i += 1

if prima:
    print("prima")
else:
    print("bukan prima")