import random
import sys

welcome_massege = "WELCOME TO GLENPY GAMES"
glenpy_position = random.randint(1,4)

print("***************************")
print(f"*{welcome_massege}*")
print("***************************")


nama_user = input("Masukkan nama :")
print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini 
|_| |_| |_| |_|
      ''')


#ini kita ubah input tapi tipe datanya int
pilihan_user = int (input("Menurut anda di gua berapa GLENPY berada ? [1 / 2 / 3 / 4 ] : "))
print (f"Pilihan kamu adalah {pilihan_user}")

konfirmasi_pilihan = input("Apakah kamu yakin dengan pilihan mu ? [y/n] : ").lower()

if konfirmasi_pilihan == 'y':
  print ("y")
else :
   print("Anda tidak berani menentukan pilihan")
   exit()

if pilihan_user == glenpy_position :
  print(f"Selamat {nama_user} kamu menang! posisi GLENPY  ada di goa nomor {glenpy_position} dan pilihan kamu adalah goa nomor {pilihan_user}")
else :
  print (f"KAMU KALAH !!glenpy bukan disitu, tapi ada di goa nomor {glenpy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}")


# ini kalau mau mengubah tipe data di if else varialbel pilihan user
# if int (pilihan_user) == glenpy_position :
#   print("Kamu menang")
# else :
#   print ("Kamu kalah")
