# Program demonstrasi DLL, menggunakan dll.py
# Menjalankan: python3 main.py

from dll import List


def main():
    L = List()

    nim = []
    print("Input NIM (Student ID) digit by digit:")

    for i in range(10):
        digit = int(input(f"Digit {i + 1}: "))
        nim.append(digit)
        L.insertLast(L.createElement(digit))

    print("\nIsi list (depan ke belakang): ", end="")
    L.printList()

    print("Isi list (belakang ke depan): ", end="")
    L.printListReverse()

    print("\nMenghapus elemen pertama...")
    P = L.deleteFirst()
    if P:
        print("Elemen yang dihapus:", P.info)
    else:
        print("List kosong, tidak ada elemen yang dihapus")
    print("Isi list: ", end="")
    L.printList()

    print("\nMenghapus elemen terakhir...")
    P = L.deleteLast()
    if P:
        print("Elemen yang dihapus:", P.info)
    else:
        print("List kosong, tidak ada elemen yang dihapus")
    print("Isi list: ", end="")
    L.printList()

    print("\nMencari digit 4...")
    found = L.searchInfo(4)
    if found:
        print(f"Data {found.info} ditemukan")
    else:
        print("Data tidak ditemukan")


if __name__ == "__main__":
    main()
