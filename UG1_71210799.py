try:
    Bil1 = int(input("Masukkan bilangan bulat pertama: "))
    Bil2 = int(input("Masukkan bilangan bulat kedua: "))
    Perkalian = Bil1 * Bil2

    if Perkalian < 1000:
        print("Nilai Perkalian:", Perkalian)
    else:
        penambahan = Bil1 + Bil2
        print("Hasil Penambahan:", penambahan)

except ValueError:
    print("Masukan harus berupa bilangan bulat.")
