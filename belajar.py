"""
MATERI UTS STRUKTUR DATA (Pekan 1 - 6)  |  Python
Jalankan di VSCode: klik kanan > Run Python File in Terminal
Tiap bagian punya kelas + demo di bagian MAIN paling bawah.
"""

# =====================================================================
# PEKAN 1 - POINTER DAN ABSTRACT DATA TYPE (ADT)
# =====================================================================
# Python tidak punya pointer eksplisit seperti C. Tapi SEMUA variabel
# objek adalah REFERENSI (mirip pointer): variabel menyimpan alamat objek.
# None = null pointer (tidak menunjuk ke apa-apa).

def demo_pointer():
    a = [1, 2, 3]
    b = a                      # b menunjuk ke objek yang SAMA dengan a
    b.append(4)
    print("a =", a, "| b =", b)                 # keduanya berubah
    print("alamat sama?", id(a) == id(b))       # True
    print("a is b?", a is b)                    # True (identitas objek)

    c = a.copy()               # salinan baru, alamat berbeda
    c.append(5)
    print("a =", a, "| c =", c)
    print("a is c?", a is c)                    # False

    p = None                   # null pointer
    print("p kosong?", p is None)


# ADT = tipe data yang didefinisikan lewat DATA + OPERASI-nya.
# Pengguna hanya tahu operasinya, bukan implementasi di dalamnya.
class Mahasiswa:
    """ADT Mahasiswa: data (nim, nama, nilai) + operasi."""

    def __init__(self, nim, nama, nilai=0):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.nilai = nilai
        else:
            print("Nilai harus 0-100")

    def get_grade(self):
        if self.nilai >= 85: return "A"
        if self.nilai >= 70: return "B"
        if self.nilai >= 55: return "C"
        return "D"

    def tampil(self):
        print(f"{self.nim} | {self.nama} | {self.nilai} | {self.get_grade()}")


# =====================================================================
# PEKAN 2 & 3 - SINGLY LINKED LIST
# =====================================================================
# Node: data + next (pointer ke node berikutnya).
# head menunjuk node pertama; node terakhir next-nya None.
#   head -> [10|*] -> [20|*] -> [30|None]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # ---- INSERT ----
    def insert_front(self, data):          # O(1)
        baru = Node(data)
        baru.next = self.head             # node baru menunjuk head lama
        self.head = baru                  # head pindah ke node baru

    def insert_last(self, data):           # O(n)
        baru = Node(data)
        if self.is_empty():
            self.head = baru
            return
        cur = self.head
        while cur.next is not None:       # jalan sampai node terakhir
            cur = cur.next
        cur.next = baru

    def insert_after(self, target, data):  # sisip setelah node bernilai target
        cur = self.head
        while cur is not None and cur.data != target:
            cur = cur.next
        if cur is None:
            print(f"{target} tidak ditemukan")
            return
        baru = Node(data)
        baru.next = cur.next              # urutan penting: sambung dulu ke depan
        cur.next = baru

    # ---- DELETE ----
    def delete_front(self):                # O(1)
        if self.is_empty():
            print("List kosong")
            return
        self.head = self.head.next

    def delete_last(self):                 # O(n)
        if self.is_empty():
            print("List kosong")
            return
        if self.head.next is None:        # hanya 1 node
            self.head = None
            return
        cur = self.head
        while cur.next.next is not None:  # berhenti di node sebelum terakhir
            cur = cur.next
        cur.next = None

    def delete_value(self, data):          # hapus node pertama bernilai data
        if self.is_empty():
            print("List kosong")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next is not None and cur.next.data != data:
            cur = cur.next
        if cur.next is None:
            print(f"{data} tidak ditemukan")
        else:
            cur.next = cur.next.next      # lompati node yang dihapus

    # ---- LAINNYA ----
    def search(self, data):
        cur, idx = self.head, 0
        while cur is not None:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1                         # tidak ditemukan

    def length(self):
        n, cur = 0, self.head
        while cur is not None:
            n += 1
            cur = cur.next
        return n

    def reverse(self):                     # balik arah semua pointer
        prev, cur = None, self.head
        while cur is not None:
            nxt = cur.next                # simpan node berikutnya
            cur.next = prev               # balik arah
            prev = cur
            cur = nxt
        self.head = prev

    def display(self):
        if self.is_empty():
            print("(kosong)")
            return
        cur, hasil = self.head, []
        while cur is not None:
            hasil.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(hasil) + " -> None")


# =====================================================================
# PEKAN 4 - DOUBLY LINKED LIST
# =====================================================================
# Tiap node punya prev DAN next, jadi bisa maju dan mundur.
#   None <- [10] <-> [20] <-> [30] -> None
# Menyimpan head dan tail supaya insert_last jadi O(1).

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_front(self, data):          # O(1)
        baru = DNode(data)
        if self.is_empty():
            self.head = self.tail = baru
        else:
            baru.next = self.head
            self.head.prev = baru
            self.head = baru

    def insert_last(self, data):           # O(1) karena ada tail
        baru = DNode(data)
        if self.is_empty():
            self.head = self.tail = baru
        else:
            baru.prev = self.tail
            self.tail.next = baru
            self.tail = baru

    def insert_after(self, target, data):
        cur = self.head
        while cur is not None and cur.data != target:
            cur = cur.next
        if cur is None:
            print(f"{target} tidak ditemukan")
            return
        if cur is self.tail:
            self.insert_last(data)
            return
        baru = DNode(data)
        baru.prev = cur
        baru.next = cur.next
        cur.next.prev = baru
        cur.next = baru

    def delete_front(self):
        if self.is_empty():
            print("List kosong")
            return
        if self.head is self.tail:        # hanya 1 node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self):
        if self.is_empty():
            print("List kosong")
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_value(self, data):
        cur = self.head
        while cur is not None and cur.data != data:
            cur = cur.next
        if cur is None:
            print(f"{data} tidak ditemukan")
            return
        if cur is self.head:
            self.delete_front()
        elif cur is self.tail:
            self.delete_last()
        else:
            cur.prev.next = cur.next      # sambungkan tetangga kiri-kanan
            cur.next.prev = cur.prev

    def display_forward(self):
        cur, hasil = self.head, []
        while cur is not None:
            hasil.append(str(cur.data))
            cur = cur.next
        print("Maju  : " + " <-> ".join(hasil) if hasil else "(kosong)")

    def display_backward(self):
        cur, hasil = self.tail, []
        while cur is not None:
            hasil.append(str(cur.data))
            cur = cur.prev
        print("Mundur: " + " <-> ".join(hasil) if hasil else "(kosong)")


# =====================================================================
# PEKAN 5 - STACK (LIFO: Last In First Out)
# =====================================================================
# Operasi hanya di satu ujung (top). Seperti tumpukan piring.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):                  # taruh di atas
        self.items.append(data)

    def pop(self):                         # ambil dari atas
        if self.is_empty():
            print("Stack kosong")
            return None
        return self.items.pop()

    def peek(self):                        # lihat atas tanpa mengambil
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (bawah -> atas):", self.items)


# Aplikasi stack 1: membalik string
def balik_string(teks):
    s = Stack()
    for ch in teks:
        s.push(ch)
    hasil = ""
    while not s.is_empty():
        hasil += s.pop()
    return hasil


# Aplikasi stack 2: cek kurung seimbang
def kurung_seimbang(ekspresi):
    pasangan = {")": "(", "]": "[", "}": "{"}
    s = Stack()
    for ch in ekspresi:
        if ch in "([{":
            s.push(ch)
        elif ch in ")]}":
            if s.is_empty() or s.pop() != pasangan[ch]:
                return False
    return s.is_empty()


# Aplikasi stack 3: konversi desimal ke biner
def desimal_ke_biner(n):
    if n == 0:
        return "0"
    s = Stack()
    while n > 0:
        s.push(n % 2)
        n //= 2
    return "".join(str(s.pop()) for _ in range(s.size()))


# =====================================================================
# PEKAN 6 - QUEUE (FIFO: First In First Out)
# =====================================================================
# Masuk di belakang (rear), keluar dari depan (front). Seperti antrian loket.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):               # masuk di belakang
        self.items.append(data)

    def dequeue(self):                     # keluar dari depan
        if self.is_empty():
            print("Queue kosong")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Sisa antrian:", self.items)


def simulasi_antrian(daftar_orang, jumlah_dilayani):
    q = Queue()
    for orang in daftar_orang:
        q.enqueue(orang)
    for _ in range(jumlah_dilayani):
        if not q.is_empty():
            dilayani = q.dequeue()
            print(f"Melayani: {dilayani}")
    q.display()


# Versi Queue berbasis linked list (enqueue & dequeue sama-sama O(1))
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        baru = Node(data)
        if self.is_empty():
            self.front = self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:             # antrian jadi kosong
            self.rear = None
        return data

    def display(self):
        cur, hasil = self.front, []
        while cur is not None:
            hasil.append(cur.data)
            cur = cur.next
        print("Sisa antrian:", hasil)


# =====================================================================
# MAIN - demo semua materi
# =====================================================================
def judul(teks):
    print("\n" + "=" * 55)
    print(teks)
    print("=" * 55)


if __name__ == "__main__":
    judul("PEKAN 1 - POINTER & ADT")
    demo_pointer()
    m = Mahasiswa("2301001", "Andi", 80)
    m.tampil()
    m.set_nilai(90)
    m.tampil()

    judul("PEKAN 2-3 - SINGLY LINKED LIST")
    sll = SinglyLinkedList()
    sll.insert_front(20)
    sll.insert_front(10)
    sll.insert_last(30)
    sll.insert_last(40)
    sll.insert_after(20, 25)
    sll.display()                          # 10 -> 20 -> 25 -> 30 -> 40
    print("Panjang:", sll.length())
    print("Cari 30 di index:", sll.search(30))
    sll.delete_front()
    sll.delete_last()
    sll.delete_value(25)
    sll.display()                          # 20 -> 30
    sll.reverse()
    sll.display()                          # 30 -> 20

    judul("PEKAN 4 - DOUBLY LINKED LIST")
    dll = DoublyLinkedList()
    dll.insert_front(20)
    dll.insert_front(10)
    dll.insert_last(30)
    dll.insert_after(20, 25)
    dll.display_forward()                  # 10 <-> 20 <-> 25 <-> 30
    dll.display_backward()                 # 30 <-> 25 <-> 20 <-> 10
    dll.delete_value(25)
    dll.delete_front()
    dll.delete_last()
    dll.display_forward()                  # 20

    judul("PEKAN 5 - STACK")
    st = Stack()
    for x in [1, 2, 3]:
        st.push(x)
    st.display()
    print("Peek:", st.peek())
    print("Pop :", st.pop())
    st.display()
    print("Balik 'STRUKTUR':", balik_string("STRUKTUR"))
    print("Kurung '{[()]}' seimbang?", kurung_seimbang("{[()]}"))
    print("Kurung '([)]' seimbang?", kurung_seimbang("([)]"))
    print("13 desimal ke biner:", desimal_ke_biner(13))

    judul("PEKAN 6 - QUEUE")
    daftar = ["Andi", "Budi", "Cici", "Dedi"]
    simulasi_antrian(daftar, jumlah_dilayani=2)
    lq = LinkedQueue()
    for nama in daftar:
        lq.enqueue(nama)
    print("Dequeue (LinkedQueue):", lq.dequeue())
    lq.display()
