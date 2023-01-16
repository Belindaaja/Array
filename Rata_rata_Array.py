# deklarasi array
array = []
# membuat variabel total
total = 0
# membuat variabel n untuk menampung jumlah array
# n = jumlah elemen
n = int(input("Masukan Jumlah Elemen Array :"))
for x in range(n):
    # menginputkan nilai yang akan bertambah 1
    nilai = float(input("Masukan Nilai ke - {} : ".format(x+1)))
    array.append(nilai)
    # menampilkan jumlah dari nilai
    print("\nHasil nilai total adalah : {}".format(sum(array)))
    # menampilkan rata rata
    print("Hasil Rata - Rata adalah : {}".format(sum(array)/n))
