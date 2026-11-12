# Materi: searchInfo(x)
# Menjalankan: python3 09_search_info.py

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

    def searchInfo(self, x):
        """Mencari node dengan data x."""
        current = self.first
        while current and current.info != x:
            current = current.next
        return current


if __name__ == "__main__":
    L = List()
    for angka in [10, 20, 30]:
        L.insertLast(L.createElement(angka))

    target = 20
    found = L.searchInfo(target)
    if found:
        print(f"Data {found.info} ditemukan")
    else:
        print("Data tidak ditemukan")

    target = 40
    found = L.searchInfo(target)
    if found:
        print(f"Data {found.info} ditemukan")
    else:
        print("Data tidak ditemukan")
