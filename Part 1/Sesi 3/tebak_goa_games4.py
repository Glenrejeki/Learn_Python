import random
from libs import welcome_massage


welcome_massage()
glenpy_position = random.randint(1,4)

nama_user = input("Masukkan nama : ")

while nama_user == "":
  nama_user = input("Isi dulu nama anda: ")


bentuk_goa ="|_|" # ini kita pastikan bahwa string bukan array mapun list

goa_kosong = [bentuk_goa] * 4 # INI EMANG HARUS KOSONG
goa = goa_kosong.copy() # INI ADALAH GOA YANG BERISI GLENPY 
goa[glenpy_position] = "|0_0|"

goa_kosong = ' '.join(goa_kosong) # ini menggabungkan string bukan array / list
goa = ' '.join(goa) # ini juga menggabungkan string dan menghapus bentuk string supaya tidak ada kurung siku dan koma


print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini !
{goa_kosong}
      ''')

while True :
  try:
    #ini kita ubah input tapi tipe datanya int
    pilihan_user = int (input("Menurut anda di gua berapa GLENPY berada ? [1 / 2 / 3 / 4 ] : "))
    if pilihan_user in [1, 2, 3, 4] : 
      break
    else :
      print("Angka yang kamu pilih diluar rentang.\n Coba pilih lagi dari [1, 2, 3, 4]: ")
  except ValueError:
    print("Tolong masukkan angka yang valid  !")
  

print (f"Pilihan kamu adalah {pilihan_user}")

konfirmasi_pilihan = input(f"Apakah kamu yakin dengan {pilihan_user} sebegai pilihan mu ? [y/n] : ").lower() # ini memastikan bahwa huruf n atau N program akan dihentikan

while konfirmasi_pilihan == "":
  konfirmasi_pilihan = input(f"Apakah kamu yakin dengan {pilihan_user} \n sebagai pilihan mu ? [y/n]: ")

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
