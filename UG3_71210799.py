baris = input("Masukkan angka: ")

angka = input("Masukkan angka yang dihitung: ")

hitung = 0

for karakter in baris:
    if karakter == angka:
        hitung += 1

print("angka", angka, "muncul sebanyak", hitung, "kali")
