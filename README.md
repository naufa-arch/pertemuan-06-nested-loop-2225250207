# Pertemuan 06 Nested Loop Python

**Algoritma dan Pemrograman | Pertemuan 06 | 12**

**Nama: Hashifah Naufa Setiawan**   
**NIM: 2225250207**  
**Kelas: 3E** 

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam program Python.

## Cara Menjalankan

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

1. Meminta pengguna memasukkan nilai `n`.
2. Melakukan validasi menggunakan `while` agar `n` harus lebih dari 0.
3. Menginisialisasi `total_keseluruhan` untuk menyimpan jumlah seluruh hasil perkalian.
4. Menginisialisasi `count_genap` sebagai counter untuk menghitung banyaknya hasil perkalian yang genap.
5. Menggunakan **loop luar** untuk menentukan nomor baris dari 1 sampai `n`.
6. Menginisialisasi `total_baris` pada setiap awal baris.
7. Menggunakan **loop dalam** untuk menentukan nomor kolom dari 1 sampai `n`.
8. Menghitung hasil perkalian `i * j`.
9. Menambahkan hasil perkalian ke `total_baris` dan `total_keseluruhan`.
10. Memeriksa apakah hasil perkalian merupakan bilangan genap menggunakan `hasil % 2 == 0`.
11. Jika genap, `count_genap` ditambah 1.
12. Setelah loop dalam selesai, menampilkan total setiap baris.
13. Setelah seluruh nested loop selesai, menampilkan total keseluruhan dan jumlah bilangan genap.

### Peran Setiap Bagian

- **Loop luar (`for i`)**: menentukan baris pada tabel perkalian.
- **Loop dalam (`for j`)**: menentukan kolom dan menghitung hasil perkalian pada setiap baris.
- **Akumulator (`total_baris` dan `total_keseluruhan`)**: menyimpan dan menjumlahkan hasil perkalian.
- **Counter (`count_genap`)**: menghitung jumlah hasil perkalian yang merupakan bilangan genap.

## Hasil Pengujian

| Input `n` | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| `3` | Tabel perkalian 1–3, total keseluruhan 36, bilangan genap 5 | Tabel perkalian 1–3, total keseluruhan 36, bilangan genap 5 | Lulus |
| `1` | Tabel hanya berisi `1`, total keseluruhan 1, bilangan genap 0 | Tabel hanya berisi `1`, total keseluruhan 1, bilangan genap 0 | Lulus |
| `0` | Program meminta input kembali karena `n` harus lebih dari 0 | Program meminta input kembali | Lulus |

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali.

Pada setiap satu kali loop luar, loop dalam juga berjalan sebanyak `n` kali. Oleh karena itu, badan loop dalam dijalankan sebanyak:

**n × n = n² kali**

Contoh:
- Jika `n = 3`, badan loop dalam berjalan `3 × 3 = 9` kali.
- Jika `n = 5`, badan loop dalam berjalan `5 × 5 = 25` kali.
- Jika `n = 10`, badan loop dalam berjalan `10 × 10 = 100` kali.

Dengan demikian, kompleksitas waktu utama program adalah **O(n²)**.

## Refleksi

Kesalahan nested loop yang saya temukan adalah **indentasi yang tidak tepat**. Awalnya, loop dalam dan perintah `if` tidak ditempatkan di dalam blok loop yang sesuai sehingga program tidak berjalan sesuai tujuan.

Saya memperbaikinya dengan memberikan indentasi yang benar. Loop `for j` ditempatkan di dalam `for i`, sedangkan perhitungan dan pengecekan bilangan genap ditempatkan di dalam loop `for j`. Dengan begitu, setiap kombinasi baris dan kolom dapat diproses dengan benar.