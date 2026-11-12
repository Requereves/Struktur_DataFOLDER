"""
LATIHAN SOAL UTS STRUKTUR DATA - 1 soal per pekan (Pekan 1 - 6)
Tiap soal berisi: teks SOAL, JAWABAN (kode), dan OUTPUT yang diharapkan.
Tips belajar: tutup bagian jawaban, kerjakan sendiri dulu, baru cocokkan.
Jalankan di VSCode: klik kanan > Run Python File in Terminal
"""
from math import gcd


# =====================================================================
# PEKAN 1 - POINTER DAN ADT
# =====================================================================
# SOAL:
# Buat ADT Pecahan dengan atribut pembilang dan penyebut.
# Operasi: sederhanakan(), tambah(lain) -> Pecahan baru (sudah sederhana), tampil().
# (a) Hitung 1/2 + 1/3.
# (b) Sederhanakan 6/8.
# (c) Buat fungsi ubah_penyebut(p, nilai) yang mengubah penyebut objek ASLI
#     (membuktikan bahwa parameter objek adalah referensi/pointer).

class Pecahan:
    def __init__(self, pembilang, penyebut):
        if penyebut == 0:
            raise ValueError("Penyebut tidak boleh 0")
        self.pembilang = pembilang
        self.penyebut = penyebut

    def sederhanakan(self):
        f = gcd(self.pembilang, self.penyebut)   # FPB
        self.pembilang //= f
        self.penyebut //= f

    def tambah(self, lain):
        pembilang = self.pembilang * lain.penyebut + lain.pembilang * self.penyebut
        penyebut = self.penyebut * lain.penyebut
        hasil = Pecahan(pembilang, penyebut)
        hasil.sederhanakan()
        return hasil

    def tampil(self):
        print(f"{self.pembilang}/{self.penyebut}")


def ubah_penyebut(p, nilai):
    p.penyebut = nilai        # p menunjuk objek yang sama dengan milik pemanggil


def soal1():
    a = Pecahan(1, 2)
    b = Pecahan(1, 3)
    print("(a) 1/2 + 1/3 =", end=" ")
    a.tambah(b).tampil()
    c = Pecahan(6, 8)
    c.sederhanakan()
    print("(b) 6/8 disederhanakan =", end=" ")
    c.tampil()
    ubah_penyebut(a, 10)
    print("(c) a setelah ubah_penyebut(a, 10) =", end=" ")
    a.tampil()

# OUTPUT:
# (a) 1/2 + 1/3 = 5/6
# (b) 6/8 disederhanakan = 3/4
# (c) a setelah ubah_penyebut(a, 10) = 1/10


# =====================================================================
# PEKAN 2 - SINGLY LINKED LIST (dasar)
# =====================================================================
# SOAL:
# Buat Singly Linked List dengan operasi insert_front, insert_last, display.
# Masukkan 10, 20, 30 di belakang, lalu 5 di depan.
# Tampilkan: isi list, banyak node, total nilai semua node, dan nilai terbesar.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_front(self, data):
        baru = Node(data)
        baru.next = self.head
        self.head = baru

    def insert_last(self, data):
        baru = Node(data)
        if self.is_empty():
            self.head = baru
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = baru

    def display(self):
        cur, hasil = self.head, []
        while cur is not None:
            hasil.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(hasil) + " -> None")

    def hitung_node(self):
        n, cur = 0, self.head
        while cur is not None:
            n += 1
            cur = cur.next
        return n

    def jumlah(self):
        total, cur = 0, self.head
        while cur is not None:
            total += cur.data
            cur = cur.next
        return total

    def terbesar(self):
        if self.is_empty():
            return None
        maks, cur = self.head.data, self.head.next
        while cur is not None:
            if cur.data > maks:
                maks = cur.data
            cur = cur.next
        return maks


def soal2():
    sll = SinglyLinkedList()
    for x in [10, 20, 30]:
        sll.insert_last(x)
    sll.insert_front(5)
    sll.display()
    print("Banyak node:", sll.hitung_node())
    print("Total nilai:", sll.jumlah())
    print("Terbesar   :", sll.terbesar())

# OUTPUT:
# 5 -> 10 -> 20 -> 30 -> None
# Banyak node: 4
# Total nilai: 65
# Terbesar   : 30


# =====================================================================
# PEKAN 3 - SINGLY LINKED LIST (hapus, cari, balik)
# =====================================================================
# SOAL:
# Gunakan Singly Linked List berisi 3, 1, 3, 2, 3, 4.
# (a) Buat method hapus_semua(x) yang menghapus SEMUA node bernilai x. Hapus 3.
# (b) Buat method cari(x) yang mengembalikan index node (atau -1). Cari 2 dan 9.
# (c) Buat method balik() untuk membalik urutan list.

class SLLLanjut(SinglyLinkedList):
    def hapus_semua(self, x):
        # 1) buang node di depan yang bernilai x
        while self.head is not None and self.head.data == x:
            self.head = self.head.next
        # 2) buang node di tengah/belakang
        cur = self.head
        while cur is not None and cur.next is not None:
            if cur.next.data == x:
                cur.next = cur.next.next      # lompati node bernilai x
            else:
                cur = cur.next                # maju hanya jika tidak menghapus

    def cari(self, x):
        cur, idx = self.head, 0
        while cur is not None:
            if cur.data == x:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def balik(self):
        prev, cur = None, self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


def soal3():
    sll = SLLLanjut()
    for x in [3, 1, 3, 2, 3, 4]:
        sll.insert_last(x)
    print("Awal      :", end=" ")
    sll.display()
    sll.hapus_semua(3)
    print("Hapus 3   :", end=" ")
    sll.display()
    print("Cari 2    :", sll.cari(2))
    print("Cari 9    :", sll.cari(9))
    sll.balik()
    print("Dibalik   :", end=" ")
    sll.display()

# OUTPUT:
# Awal      : 3 -> 1 -> 3 -> 2 -> 3 -> 4 -> None
# Hapus 3   : 1 -> 2 -> 4 -> None
# Cari 2    : 1
# Cari 9    : -1
# Dibalik   : 4 -> 2 -> 1 -> None


# =====================================================================
# PEKAN 4 - DOUBLY LINKED LIST
# =====================================================================
# SOAL:
# Buat Doubly Linked List yang menyimpan huruf dari sebuah kata.
# Tampilkan isi dari depan (maju) dan dari belakang (mundur).
# Lalu buat method is_palindrom() yang memeriksa apakah kata palindrom
# dengan dua pointer: satu dari head, satu dari tail.
# Uji dengan "KATAK" dan "BUKU".

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_last(self, data):
        baru = DNode(data)
        if self.head is None:
            self.head = self.tail = baru
        else:
            baru.prev = self.tail
            self.tail.next = baru
            self.tail = baru

    def tampil_maju(self):
        cur, hasil = self.head, []
        while cur is not None:
            hasil.append(cur.data)
            cur = cur.next
        print("Maju  : " + " <-> ".join(hasil))

    def tampil_mundur(self):
        cur, hasil = self.tail, []
        while cur is not None:
            hasil.append(cur.data)
            cur = cur.prev
        print("Mundur: " + " <-> ".join(hasil))

    def is_palindrom(self):
        kiri, kanan = self.head, self.tail
        # berhenti kalau pointer bertemu (ganjil) atau saling melewati (genap)
        while kiri is not kanan and kiri.prev is not kanan:
            if kiri.data != kanan.data:
                return False
            kiri = kiri.next
            kanan = kanan.prev
        return True


def buat_dll(kata):
    dll = DoublyLinkedList()
    for huruf in kata:
        dll.insert_last(huruf)
    return dll


def soal4():
    for kata in ["KATAK", "BUKU"]:
        print(f"--- {kata} ---")
        dll = buat_dll(kata)
        dll.tampil_maju()
        dll.tampil_mundur()
        print("Palindrom?", dll.is_palindrom())

# OUTPUT:
# --- KATAK ---
# Maju  : K <-> A <-> T <-> A <-> K
# Mundur: K <-> A <-> T <-> A <-> K
# Palindrom? True
# --- BUKU ---
# Maju  : B <-> U <-> K <-> U
# Mundur: U <-> K <-> U <-> B
# Palindrom? False


# =====================================================================
# PEKAN 5 - STACK
# =====================================================================
# SOAL:
# Buat kelas Stack (push, pop, peek, is_empty). Lalu buat fungsi
# evaluasi_postfix(ekspresi) untuk menghitung ekspresi postfix.
# Aturan: angka -> push. Operator -> pop dua angka (b dulu, lalu a),
# hitung a (op) b, push hasilnya.
# Hitung: "5 6 2 + * 12 4 / -"  dan  "3 4 + 2 *"

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack kosong")
            return None
        return self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]


def evaluasi_postfix(ekspresi):
    s = Stack()
    for token in ekspresi.split():
        if token in "+-*/":
            b = s.pop()                # operand kanan diambil lebih dulu
            a = s.pop()
            if token == "+":
                s.push(a + b)
            elif token == "-":
                s.push(a - b)
            elif token == "*":
                s.push(a * b)
            else:
                s.push(a // b)
        else:
            s.push(int(token))
    return s.pop()


def soal5():
    for ekspresi in ["5 6 2 + * 12 4 / -", "3 4 + 2 *"]:
        print(f"{ekspresi}  =  {evaluasi_postfix(ekspresi)}")

# Penjelasan "5 6 2 + * 12 4 / -":
#   6 2 +  -> 8      | 5 8 *  -> 40
#   12 4 / -> 3      | 40 3 - -> 37
# OUTPUT:
# 5 6 2 + * 12 4 / -  =  37
# 3 4 + 2 *  =  14


# =====================================================================
# PEKAN 6 - QUEUE
# =====================================================================
# SOAL:
# Buat kelas Queue (enqueue, dequeue, is_empty). Lalu simulasikan antrian
# printer: tiap job berupa (nama_file, jumlah_halaman), 1 halaman = 2 detik.
# Cetak tiap job sesuai urutan masuk (FIFO) beserta detik selesainya,
# lalu total waktu.
# Data: laporan.pdf (5 hal), foto.jpg (2 hal), tugas.docx (3 hal)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong")
            return None
        return self.items.pop(0)


def simulasi_printer(jobs, detik_per_halaman=2):
    q = Queue()
    for job in jobs:
        q.enqueue(job)
    waktu = 0
    while not q.is_empty():
        nama, halaman = q.dequeue()
        waktu += halaman * detik_per_halaman
        print(f"{nama} selesai pada detik ke-{waktu}")
    print("Total waktu:", waktu, "detik")


def soal6():
    jobs = [("laporan.pdf", 5), ("foto.jpg", 2), ("tugas.docx", 3)]
    simulasi_printer(jobs)

# OUTPUT:
# laporan.pdf selesai pada detik ke-10
# foto.jpg selesai pada detik ke-14
# tugas.docx selesai pada detik ke-20
# Total waktu: 20 detik


# =====================================================================
# MAIN
# =====================================================================
if __name__ == "__main__":
    daftar_soal = [
        ("PEKAN 1 - POINTER & ADT", soal1),
        ("PEKAN 2 - SINGLY LINKED LIST (dasar)", soal2),
        ("PEKAN 3 - SINGLY LINKED LIST (hapus, cari, balik)", soal3),
        ("PEKAN 4 - DOUBLY LINKED LIST", soal4),
        ("PEKAN 5 - STACK", soal5),
        ("PEKAN 6 - QUEUE", soal6),
    ]
    for judul, fungsi in daftar_soal:
        print("\n" + "=" * 55)
        print(judul)
        print("=" * 55)
        fungsi()
