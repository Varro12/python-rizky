print("PROGRAM KASIR MINI")
nama_barang = input("Masukkan Nama Barang: ")
harga = int(input("Masukkan Harga Satuan (Rp): "))
jumlah = int(input("Masukkan Jumlah Beli: "))

total_asli = harga * jumlah

if total_asli >= 100000:
    diskon = total_asli * 0.12
    total_bayar = total_asli - diskon
    print("\nSelamat kamu mendapatkan diskon 10%")
else:
    diskon = 0
    total_bayar = total_asli

print("\n--- STRUK BELANJA ---")
print(f"Nama Barang     : {nama_barang}")
print(f"Harga Satuan    : Rp {harga:,}")
print(f"Jumlah Beli     : {jumlah}")
print("---------------------------------------")
print(f"Total Asli      : Rp {total_asli:,}")
print(f"Diskon (10%)    : Rp {int(diskon):,}")
print("---------------------------------------")
print(f"Total Bayar     : Rp {int(total_bayar):,}")
