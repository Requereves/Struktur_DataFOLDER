# Materi: insertLast(P)
# Menjalankan: python3 04_insert_last.py

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
        """Menyisipkan node P di akhir list."""
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


if __name__ == "__main__":
    L = List()

    # Kasus 1: menyisipkan ke list kosong
    L.insertLast(L.createElement(10))
    print("Setelah insertLast(10):")
    L.printList()

    # Kasus 2: menyisipkan node baru di akhir
    L.insertLast(L.createElement(20))
    L.insertLast(L.createElement(30))
    print("Setelah insertLast(20) dan insertLast(30):")
    L.printList()

    print("first =", L.first.info)
    print("last  =", L.last.info)
    print("20.next =", L.first.next.info)
    print("30.prev =", L.last.prev.info)
