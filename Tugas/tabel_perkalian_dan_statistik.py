print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n
while n <= 0:
    print("n harus lebih dari 0.")
    n = int(input("Masukkan n lagi: "))

# Inisialisasi
total_keseluruhan = 0
count_genap = 0

# Nested loop
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end="\t")

        total_baris += hasil
        total_keseluruhan += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f"| Total baris {i} = {total_baris}")

print()
print(f"Total keseluruhan = {total_keseluruhan}")
print(f"Banyak bilangan genap = {count_genap}")