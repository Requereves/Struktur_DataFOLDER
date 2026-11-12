# Materi: deleteLast()
# Menjalankan: python3 08_delete_last.py

class Node:
    def __init__(self, data):
        self.info = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.createList()

    def createList(self):
        self.first = None
        self.last = None

    def createElement(self, x):
        return Node(x)

    def insertLast(self, P):
        if P:
            P.prev = self.last
            P.next = None
            if self.last:
                self.last.next = P
            else:
                self.first = P
            self.last = P

    def printList(self):
        if not self.first:
            print("List kosong")
        else:
            current = self.first
            while current:
                print(current.info, end=" ")
                current = current.next
            print()

    def deleteLast(self):
        """Menghapus node terakhir dari list."""
        if self.last:
            P = self.last
            self.last = P.prev
            if self.last:
                self.last.next = None
            else:
                self.first = None
            return P
        return None


if __name__ == "__main__":
    L = List()
    for angka in [10, 20, 30]:
        L.insertLast(L.createElement(angka))

    print("Sebelum deleteLast:")
    L.printList()

    P = L.deleteLast()
    if P:
        print("Node yang dihapus:", P.info)
    else:
        print("List kosong, tidak ada node yang dihapus")

    print("Sesudah deleteLast:")
    L.printList()

    # Uji kondisi list satu node:
    satu = List()
    satu.insertLast(satu.createElement(99))
    print("\\nList satu node sebelum deleteLast:")
    satu.printList()
    dihapus = satu.deleteLast()
    print("Node yang dihapus:", dihapus.info if dihapus else None)
    print("first setelah deleteLast:", satu.first)
    print("last setelah deleteLast:", satu.last)
