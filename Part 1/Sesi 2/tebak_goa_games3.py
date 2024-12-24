import random
import sys

welcome_massege = "WELCOME TO GLENPY GAMES"
glenpy_position = random.randint(1,4)

print("***************************")
print(f"*{welcome_massege}*")
print("***************************")


nama_user = input("Masukkan nama : ")

bentuk_goa =["|_|"]
goa_kosong = [bentuk_goa] * 4 # INI EMANG HARUS KOSONG
goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI GLENPY
goa[glenpy_position] = "|0_0|"


print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini !
{goa_kosong}
      ''')


#ini kita ubah input tapi tipe datanya int
pilihan_user = int (input("Menurut anda di gua berapa GLENPY berada ? [1 / 2 / 3 / 4 ] : "))
print (f"Pilihan kamu adalah {pilihan_user}")

konfirmasi_pilihan = input(f"Apakah kamu yakin dengan {pilihan_user} sebegai pilihan mu ? [y/n] : ").lower() # ini memastikan bahwa huruf n atau N program akan dihentikan

if konfirmasi_pilihan == 'n':
  print ("Program dihentikan !")
  exit()
else:
  if pilihan_user == glenpy_position :
    print(f"{goa}\n Selamat kamu menang !\n Poisi GLENPY ada di {glenpy_position}")
  else :
    print (f"{goa}\n Maaf kamu kalah !\n Poisi GLENPY ada di {glenpy_position}")


# ini kalau mau mengubah tipe data di if else varialbel pilihan user
# if int (pilihan_user) == glenpy_position :
#   print("Kamu menang")
# else :
#   print ("Kamu kalah")
