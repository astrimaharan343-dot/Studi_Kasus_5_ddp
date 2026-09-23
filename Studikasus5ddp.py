def menghitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan == "mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan == "motor":
        tarif_per_jam = 3000
    else:
        print("jenis kendaraan tidak valid")
        return 0

    total_biaya = tarif_per_jam * durasi_parkir
    return total_biaya

def jenis_kendaraan():
    print("=== jenis_kendaraan(mobil/motor) ===")
    jenis = input("Masukkan jenis kendaraan: ")
    print("jenis kendaraan berhasil di tambahkan")
    return jenis

def jam_masuk():
    print("=== jam_masuk ===")
    masuk = int(input("Masukkan jam masuk (0-24): "))
    print("jam masuk berhasil di tambahkan")
    return masuk

def jam_keluar():
    print("=== jam_keluar ===")
    keluar = int(input("Masukkan jam keluar (0-24): "))
    print("jam keluar berhasil di tambahkan")
    return keluar

def lama_parkir(var_masuk, var_keluar):
    print("=== lama_parkir ===")
    if var_keluar >= var_masuk:
        lama = var_keluar - var_masuk
    else:
        lama = (24 - var_masuk) + var_keluar
    if lama == 0:
        lama = 1

    print(f"lama parkir: {lama} jam")
    print("lama parkir berhasil di hitung")
    return lama

def total_biaya_parkir(var_kendaraan, var_lama):
    print("=== total_biaya_parkir ===")
    
    if var_kendaraan == "mobil":
        tarif_per_jam = 5000
    elif var_kendaraan == "motor":
        tarif_per_jam = 3000
    else:
        print("jenis kendaraan belum di pilih")
        return 0

    total = var_lama * tarif_per_jam
    print(f"total biaya yang harus di bayar Rp{total}")
    print("total biaya berhasil di tambahkan")
    return total

var_kendaraan = ""
var_masuk = 0
var_keluar = 0
var_lama = 0
var_total = 0

while True:
    print("===== Tampilkan =====")
    print("1. Jenis kendaraan")
    print("2. Jam masuk")
    print("3. Jam keluar")
    print("4. Lama parkir")
    print("5. Total biaya parkir")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        var_kendaraan = jenis_kendaraan()
    elif pilihan == "2":
        var_masuk = jam_masuk()
    elif pilihan == "3":
        var_keluar = jam_keluar()
    elif pilihan == "4":
        var_lama = lama_parkir(var_masuk, var_keluar)
    elif pilihan == "5":
        var_total = total_biaya_parkir(var_kendaraan, var_lama)
    elif pilihan == "6":
        print("selesai")
        break
    else:
        print("pilihan tidak valid!")





