# Demonstrasi ringkas seluruh operasi DLL.
# Menjalankan: python3 10_demo_semua_operasi.py

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
        if P:
            P.next = self.first
            P.prev = None
            if self.first:
                self.first.prev = P
            else:
                self.last = P
            self.first = P

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

    def printListReverse(self):
        if not self.last:
            print("List kosong")
        else:
            current = self.last
            while current:
                print(current.info, end=" ")
                current = current.prev
            print()

    def deleteFirst(self):
        if self.first:
            P = self.first
            self.first = P.next
            if self.first:
                self.first.prev = None
            else:
                self.last = None
            return P
        return None

    def deleteLast(self):
        if self.last:
            P = self.last
            self.last = P.prev
            if self.last:
                self.last.next = None
            else:
                self.first = None
            return P
        return None

    def searchInfo(self, x):
        current = self.first
        while current and current.info != x:
            current = current.next
        return current


if __name__ == "__main__":
    L = List()

    print("1. List baru:")
    L.printList()

    print("\n2. InsertLast 20 dan 30:")
    L.insertLast(L.createElement(20))
    L.insertLast(L.createElement(30))
    L.printList()

    print("\n3. InsertFirst 10:")
    L.insertFirst(L.createElement(10))
    L.printList()

    print("\n4. Traversal mundur:")
    L.printListReverse()

    print("\n5. Search 20:")
    found = L.searchInfo(20)
    print(f"Data {found.info} ditemukan" if found else "Data tidak ditemukan")

    print("\n6. DeleteFirst:")
    P = L.deleteFirst()
    print("Node dihapus:", P.info if P else None)
    L.printList()

    print("\n7. DeleteLast:")
    P = L.deleteLast()
    print("Node dihapus:", P.info if P else None)
    L.printList()
