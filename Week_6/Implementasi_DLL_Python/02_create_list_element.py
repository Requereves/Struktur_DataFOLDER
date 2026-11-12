# Materi: createList() dan createElement()
# Menjalankan: python3 02_create_list_element.py

class Node:
    def __init__(self, data):
        self.info = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.createList()

    def createList(self):
        """Menginisialisasi list kosong."""
        self.first = None
        self.last = None

    def createElement(self, x):
        """Membuat node baru dengan data x."""
        return Node(x)


if __name__ == "__main__":
    L = List()
    print("List baru dibuat:")
    print("L.first =", L.first)
    print("L.last  =", L.last)

    P = L.createElement(5)
    print("\nNode P berhasil dibuat:")
    print("P.info  =", P.info)
    print("P.prev  =", P.prev)
    print("P.next  =", P.next)

    print("\nNode P belum dimasukkan ke list:")
    print("L.first =", L.first)
    print("L.last  =", L.last)
