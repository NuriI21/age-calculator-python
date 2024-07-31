## project menghitung umur ##

import datetime as dt

print("\nSilahkan masukan tanggal lahir kamu !!\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

# memprint tanggal lahir
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"\ntanggal lahir kamu adalah {tanggal_lahir}")

# mengetahui umur dalam hari
sekarang = dt.date.today() 
umur_dalam_hari = (sekarang - tanggal_lahir)
print(f"kamu sudah hidup selama {umur_dalam_hari.days:,} hari") 

# mengetahui umur dalam tahun
umur_dalam_tahun = umur_dalam_hari.days // 365
print(f"1. umur kamu sekarang {umur_dalam_tahun} tahun ")

# mengetahui umur dalam tahun + bulan
umur_dalam_bulan = (umur_dalam_hari.days % 365) // 30
print(f"2. umur kamu sekarang {umur_dalam_tahun} tahun, {umur_dalam_bulan} bulan ")

# mengetahui umur dalam tahun + bulan + hari
umur_dalam_hari = (umur_dalam_hari.days % 365) % 30
print(f"3. umur kamu sekarang {umur_dalam_tahun} tahun, {umur_dalam_bulan} bulan, {umur_dalam_hari} hari ")
