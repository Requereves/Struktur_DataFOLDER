# Materi: insertFirst(P)
# Menjalankan: python3 03_insert_first.py

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

    def insertFirst(self, P):
        """Menyisipkan node P di awal list."""
        if P:
            P.next = self.first
            P.prev = None
            if self.first:
                self.first.prev = P
            else:
                self.last = P
            self.first = P

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
    L.insertFirst(L.createElement(20))
    print("Setelah insertFirst(20):")
    L.printList()

    # Kasus 2: menyisipkan node baru di depan
    L.insertFirst(L.createElement(10))
    print("Setelah insertFirst(10):")
    L.printList()

    print("first =", L.first.info)
    print("last  =", L.last.info)
    print("10.next =", L.first.next.info)
    print("20.prev =", L.last.prev.info)
