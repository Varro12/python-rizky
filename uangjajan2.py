anggaran_bulanan= int(input("Anggaran Bulanan: "))
jajan_perhari= int(input("Uang JaJan Perhari: "))
jumlah_hari_jajan= int(input("Jumlah Hari Jajan: "))
pengeluaran_takterduga= int(input("Pengeluaran Tak Terduga: "))

total_pengeluaran_bulanan= (jajan_perhari * jumlah_hari_jajan) + pengeluaran_takterduga
selisih= (anggaran_bulanan - total_pengeluaran_bulanan)
sisa_uang= (anggaran_bulanan - total_pengeluaran_bulanan)

print("=== LAPORAN KEUANGAN ===")
print("Total Pengeluaran    :   Rp.",total_pengeluaran_bulanan )
print("Anggaran Bulanan     :   Rp.", anggaran_bulanan)
print("Sisa Uang Anda       :   Rp.", sisa_uang)
print("------------------------")

if total_pengeluaran_bulanan > anggaran_bulanan:
    print("nombok")
elif total_pengeluaran_bulanan == anggaran_bulanan:
    print("keuangan pas")
elif total_pengeluaran_bulanan < anggaran_bulanan:
    print("keuangan aman, Anda bisa menabung")

if sisa_uang >= 200000:
    print("kategori: tabungan super")
elif 50000 <= sisa_uang < 200000:
    print("kategori: tabungan wajar")
else:
    print("kategori: tabungan tipis")
print("------------------------")