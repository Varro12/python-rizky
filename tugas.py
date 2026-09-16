nilai1= float(input("masukan nilai MTK: "))
nilai2= float(input("masukan nilai B.Inggris: "))
nilai3= float(input("masukan nilai B.Indonesia: "))
nilai4= float(input("masukan nilai PPKN: "))
jumlah_nilai= (nilai1 + nilai2 + nilai3 + nilai4)

if jumlah_nilai > 300:
    print("anda lulus, nilai anda:", jumlah_nilai)
elif 250 <= jumlah_nilai <= 300:
    print("remedial, nilai anda:", jumlah_nilai)
elif 0 <= jumlah_nilai < 250:
    print("tidak lulus, nilai anda:", jumlah_nilai)