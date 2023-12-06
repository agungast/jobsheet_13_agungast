print("Program Penghitung Kecepatan Mobil: ")

meter=int(input("Masukkan jarak tempuh(meter): "))
jam= int(input("Masukkan jam: "))
menit= int(input("Masukkan menit: "))
detik= int(input("Masukkan detik: "))

print(f"Diketahui jarak tempuh {meter} meter, {jam} jam, {menit} menit, {detik} detik ")

a= jam*3600
b= menit*60
c= a+b+detik

e= meter/c
print(f"Jadi kecepatannya = {round(e,3)} m/s ")