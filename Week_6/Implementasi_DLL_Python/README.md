# Implementasi Doubly Linked List (DLL) dengan Python

Kumpulan file latihan berdasarkan materi PPT DLL_Python.pptx. Setiap materi operasi dipisah ke file tersendiri agar bisa dipelajari dan dijalankan satu per satu.

## Daftar file

1. `01_node.py` — class Node dan pembuatan satu node.
2. `02_create_list_element.py` — class List, `createList()`, dan `createElement()`.
3. `03_insert_first.py` — operasi `insertFirst(P)`.
4. `04_insert_last.py` — operasi `insertLast(P)`.
5. `05_print_list.py` — traversal maju dengan `printList()`.
6. `06_print_list_reverse.py` — traversal mundur dengan `printListReverse()`.
7. `07_delete_first.py` — operasi `deleteFirst()`.
8. `08_delete_last.py` — operasi `deleteLast()`.
9. `09_search_info.py` — operasi `searchInfo(x)`.
10. `10_demo_semua_operasi.py` — demonstrasi seluruh operasi.
11. `dll.py` — implementasi lengkap class `Node` dan `List` dalam satu modul.
12. `main.py` — program demonstrasi terpisah yang mengimpor `List` dari `dll.py`.

## Cara menjalankan

Pastikan Python 3 sudah terpasang. Buka terminal di folder ini, lalu jalankan file yang ingin dipelajari, misalnya:

```bash
python3 03_insert_first.py
```

Setiap file latihan `01` sampai `09` dibuat mandiri (self-contained), sehingga dapat dijalankan tanpa harus menjalankan file latihan lainnya.

Untuk versi yang menggunakan file terpisah seperti program modular, jalankan:

```bash
python3 main.py
```

Program `main.py` meminta 10 digit satu per satu. Masukkan digit angka sesuai instruksi. Untuk demonstrasi cepat, bisa juga menjalankan `10_demo_semua_operasi.py`.

## Catatan

- Nama atribut dan method mengikuti materi: `info`, `next`, `prev`, `first`, `last`, `createList`, `createElement`, `insertFirst`, `insertLast`, `printList`, `printListReverse`, `deleteFirst`, `deleteLast`, dan `searchInfo`.
- File latihan mandiri mengulang class yang diperlukan supaya setiap topik bisa dijalankan sendiri.
- `dll.py` menjadi versi gabungan yang digunakan oleh `main.py`.
- Operasi delete mengembalikan objek node yang dihapus, atau `None` jika list kosong.
