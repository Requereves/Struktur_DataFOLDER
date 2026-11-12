# Materi: printList() — traversal maju
# Menjalankan: python3 05_print_list.py

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
        """Menampilkan semua elemen dari depan ke belakang."""
        if not self.first:
            print("List kosong")
        else:
            current = self.first
            while current:
                print(current.info, end=" ")
                current = current.next
            print()


if __name__ == "__main__":
    L = List()
    for angka in [10, 20, 30]:
        L.insertLast(L.createElement(angka))

    print("Traversal maju:")
    L.printList()
