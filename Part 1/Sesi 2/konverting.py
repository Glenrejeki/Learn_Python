#typecasting 1
tanggal_lahir = "23" #ini tipe data string
konversi_tanggal_lahir = int(tanggal_lahir) # mau diubah dari string menjadi int

print(konversi_tanggal_lahir) #berubah menjadi int dari variabel konversi

# typecasting 2 dengan re-assignment (menggunakan variabel sebelumya)
tanggal_lahir2 = "25"
tanggal_lahir2 =int(tanggal_lahir2)

print (tanggal_lahir2)

#Data list atau array
kardus = ["semangka", "nanas", "pisang"]
kardus.append("anggur") # jadi fungsi dari append untuk menambahkan data ke array list dan dimasukkan sesuai urutan indeksnya
kardus.append("jeruk")


buah_gabungan = kardus[1:3]
print(kardus[0])
print(kardus[1])
print(kardus[2])
print(buah_gabungan)
print(kardus[2], kardus[1])
print (kardus[4]) #menampilkan jeruk dari data yang kita tambahkan
print(f"Panjang dari array kardus :{len(kardus)}")

print(kardus[4-4])
# 4 - 4 = 0
# setara dengan  print(kardus[0])
# maka hasilnya akan semangka

# Library
from math import sqrt, sin
A = 9
B = 90
print(sqrt(A))
print(sin(B))