n = int(input("Masukkan angka: "))

jumlah = 0
if n > 1:
    jumlah = 1          
    i = 2
    while i * i <= n:
        if n % i == 0:
            jumlah += i
            if i != n // i:      
                jumlah += n // i
        i += 1

if n > 1 and jumlah == n:
    print("sempurna")
else:
    print("tidak sempurna")