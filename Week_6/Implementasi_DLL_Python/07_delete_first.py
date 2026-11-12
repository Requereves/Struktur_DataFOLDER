# Materi: deleteFirst()
# Menjalankan: python3 07_delete_first.py

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

    def deleteFirst(self):
        """Menghapus node pertama dari list."""
        if self.first:
            P = self.first
            self.first = P.next
            if self.first:
                self.first.prev = None
            else:
                self.last = None
            return P
        return None


if __name__ == "__main__":
    L = List()
    for angka in [10, 20, 30]:
        L.insertLast(L.createElement(angka))

    print("Sebelum deleteFirst:")
    L.printList()

    P = L.deleteFirst()
    if P:
        print("Node yang dihapus:", P.info)
    else:
        print("List kosong, tidak ada node yang dihapus")

    print("Sesudah deleteFirst:")
    L.printList()

    # Uji kondisi list kosong:
    kosong = List()
    print("deleteFirst pada list kosong:", kosong.deleteFirst())
