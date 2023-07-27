import math


def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari**2 * tinggi


def volume_kubus(sisi):
    return sisi**3


def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


def main():
    print("==================== KALKULATOR CERDAS ====================")
    print("Pilihlah bangun yang ingin anda hitung(inputan angka saja) :")
    print("1. Tabung")
    print("2. Kubus")
    print("3. Balok")

    pilihan = int(input(">> "))

    if pilihan == 1:
        jari_jari_tabung = float(input("Masukkan jari-jari tabung (cm): "))
        tinggi_tabung = float(input("Masukkan tinggi tabung (cm): "))
        hasil_tabung = volume_tabung(jari_jari_tabung, tinggi_tabung)
        print(f"Volume tabung adalah {round(hasil_tabung, 2)} cm³")

    elif pilihan == 2:
        sisi_kubus = float(input("Masukkan panjang sisi kubus (cm): "))
        hasil_kubus = volume_kubus(sisi_kubus)
        print(f"Volume kubus adalah {round(hasil_kubus, 2)} cm³")

    elif pilihan == 3:
        panjang_balok = float(input("Masukkan panjang balok (cm): "))
        lebar_balok = float(input("Masukkan lebar balok (cm): "))
        tinggi_balok = float(input("Masukkan tinggi balok (cm): "))
        hasil_balok = volume_balok(panjang_balok, lebar_balok, tinggi_balok)
        print(f"Volume balok adalah {round(hasil_balok, 2)} cm³")

    else:
        print("inputan yang anda masukan salah!!")


if __name__ == "__main__":
    main()
