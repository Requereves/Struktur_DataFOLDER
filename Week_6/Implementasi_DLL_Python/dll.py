# Implementasi lengkap Doubly Linked List (DLL)
# Nama class, atribut, dan method mengikuti materi PPT.

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
        """Menampilkan semua elemen dalam list dari depan ke belakang."""
        if not self.first:
            print("List kosong")
        else:
            current = self.first
            while current:
                print(current.info, end=" ")
                current = current.next
            print()

    def printListReverse(self):
        """Menampilkan semua elemen dalam list dari belakang ke depan."""
        if not self.last:
            print("List kosong")
        else:
            current = self.last
            while current:
                print(current.info, end=" ")
                current = current.prev
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

    def searchInfo(self, x):
        """Mencari node dengan data x."""
        current = self.first
        while current and current.info != x:
            current = current.next
        return current
