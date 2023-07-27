def hitung_volume_tabung(diameter, tinggi):
    jari_jari = diameter / 2
    volume = 3.14 * jari_jari**2 * tinggi
    return volume

def hitung_volume_kubus(sisi):
    volume = sisi**3
    return volume

def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

print("="*20, " KALKULATOR CERDAS ","="*20)
print("Pilihlah bangun yang ingin anda hitung (inputan angka saja) :")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")

pilihan = int(input(">> "))

if pilihan == 1:
    diameter = float(input("Masukkan diameter(cm) : "))
    tinggi = float(input("Masukkan tinggi(cm) : "))
    volume_tabung = hitung_volume_tabung(diameter, tinggi)
    print(f"Volume tabung adalah {volume_tabung:.15f} cm\u00b3")
elif pilihan == 2:
    sisi = float(input("Masukkan sisi(cm) : "))
    volume_kubus = hitung_volume_kubus(sisi)
    print(f"Volume kubus adalah {int(volume_kubus)} cm\u00b3")
elif pilihan == 3:
    panjang = float(input("Masukkan panjang(cm) : "))
    lebar = float(input("Masukkan lebar(cm) : "))
    tinggi = float(input("Masukkan tinggi(cm) : "))
    volume_balok = hitung_volume_balok(panjang, lebar, tinggi)
    print(f"Volume balok adalah {int(volume_balok)} cm\u00b3")
else:
    print("Inputan yang anda masukkan salah !!")
