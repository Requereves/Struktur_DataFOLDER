# Materi: printListReverse() — traversal mundur
# Menjalankan: python3 06_print_list_reverse.py

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

    def printListReverse(self):
        """Menampilkan semua elemen dari belakang ke depan."""
        if not self.last:
            print("List kosong")
        else:
            current = self.last
            while current:
                print(current.info, end=" ")
                current = current.prev
            print()


if __name__ == "__main__":
    L = List()
    for angka in [10, 20, 30]:
        L.insertLast(L.createElement(angka))

    print("Traversal mundur:")
    L.printListReverse()
