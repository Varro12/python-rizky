matpel= ["Matematika", "B.Inggris", "B.Indonesia"]
total_nilai= 0

for semester in range(1, 5):
    print(f" SEMESTER {semester} ".center (30, "="))
    for mp in matpel:
        nilai= float(input(f"Nilai {mp} : "))
        total_nilai += nilai
        print()

jumlah_nilai= 4 * len(matpel)
rata_rata= total_nilai / jumlah_nilai

if rata_rata >= 85:
    status= "Lolos Jalur Prestasi (Beasiswa)"
elif rata_rata >= 70:
    status= "Lolos Jalur Reguler"
else:
    status= "Tidak Lolos"

print("=" * 30)
print(f"Total Nilai Keseluruhan     : {total_nilai:.0f}")
print(f"Rata-Rata Nilai             : {rata_rata:.1f}")
print(f"Status Kualifikasi          : {status}")
