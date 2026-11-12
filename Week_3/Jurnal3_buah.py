# ── DATA TOKO ─────────────────────────────────────────

nama_buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]
harga = [15000, 12000, 10000, 8000, 35000]
N_BUAH = 5


# ── FUNGSI ────────────────────────────────────────────

def hitung_subtotal(harga_satuan, berat):
    return harga_satuan * berat


def hitung_total(subtotal, n):
    total = 0

    for i in range(n):
        total = total + subtotal[i]

    return total


def hitung_kembalian(bayar, total):
    return bayar - total


# ── PROSEDUR ──────────────────────────────────────────

def tampilkan_menu(nama_buah, harga, n):
    print("===========================")
    print("     TOKO BUAH SEGAR")
    print("===========================")

    for i in range(n):
        print(f"  {i + 1}. {nama_buah[i]:<10} Rp {harga[i]:,}/kg".replace(",", "."))

    print("===========================")


def tampilkan_struk(nama_buah, harga, berat_beli, subtotal_beli,
                    n_beli, total, bayar):

    print("\n============================================================")
    print("                       STRUK BELANJA")
    print("============================================================")
    print("  No   Buah        Berat     Harga/kg    Subtotal")
    print("  --------------------------------------------------")

    for i in range(n_beli):
        indeks = nama_buah.index(nama_buah[i])

        print(f"  {i + 1:<4} {nama_buah[i]:<10} "
              f"{berat_beli[i]:<9} kg  "
              f"Rp {harga[indeks]:>8,}   "
              f"Rp {subtotal_beli[i]:>8,.0f}".replace(",", "."))

    print("  --------------------------------------------------")
    print(f"  Total Belanja   : Rp {total:,.0f}".replace(",", "."))
    print(f"  Uang Bayar      : Rp {bayar:,.0f}".replace(",", "."))

    kembalian = hitung_kembalian(bayar, total)

    print(f"  Kembalian       : Rp {kembalian:,.0f}".replace(",", "."))
    print("============================================================")
    print("  Terima kasih sudah berbelanja!")


# ── PROGRAM UTAMA ─────────────────────────────────────

buah_dibeli = []
berat_dibeli = []
subtotal_dibeli = []
n_transaksi = 0

tampilkan_menu(nama_buah, harga, N_BUAH)


# LOOP PEMBELIAN
while True:

    # Input dan validasi pilihan buah
    while True:
        try:
            pilihan = int(input("\nPilih buah (1-5): "))

            if pilihan >= 1 and pilihan <= 5:
                break
            else:
                print("  [!] Pilihan harus 1-5.")
        except:
            print("  [!] Masukkan angka.")


    # Input dan validasi berat
    while True:
        try:
            berat = float(input("Berat (kg)      : "))

            if berat > 0:
                break
            else:
                print("  [!] Berat harus lebih dari 0. Coba lagi.")
        except:
            print("  [!] Masukkan angka.")


    # Ubah pilihan menjadi indeks array
    indeks = pilihan - 1

    # Hitung subtotal
    subtotal = hitung_subtotal(harga[indeks], berat)

    # Simpan ke array menggunakan +
    buah_dibeli = buah_dibeli + [indeks]
    berat_dibeli = berat_dibeli + [berat]
    subtotal_dibeli = subtotal_dibeli + [subtotal]

    n_transaksi = n_transaksi + 1

    print(f"  >> {nama_buah[indeks]} {berat:g} kg = "
          f"Rp {subtotal:,.0f}".replace(",", "."))


    # Tanya beli lagi
    while True:
        lagi = input("\nBeli buah lagi? (y/t): ").lower()

        if lagi == "y" or lagi == "t":
            break
        else:
            print("  [!] Masukkan y atau t.")

    if lagi == "t":
        break

total = hitung_total(subtotal_dibeli, n_transaksi)


while True:
    try:
        bayar = float(input("\nUang bayar      : Rp "))

        if bayar >= total:
            break
        else:
            print("Uang bayar kurang dari total. Coba lagi: ")
    except:
        print("Masukkan angka: ")


#
tampilkan_struk(
    [nama_buah[i] for i in buah_dibeli],
    harga,
    berat_dibeli,
    subtotal_dibeli,
    n_transaksi,
    total,
    bayar
)