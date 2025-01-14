import main 
from Services import db

def add():
  kode_barang = input("kode_barang: ")
  nama_barang = input("nama_barang: ")
  harga_barang = int (input("harga_barang: ")) 
  stok_barang = int (input ("stok_barang: "))
  
  db.insert_item(kode_barang, nama_barang,harga_barang,stok_barang)
  
def check():
  items = db.fetch_item()  # Pastikan ada tanda kurung untuk memanggil metode
  for item in items:
    kode_barang = item[1]
    nama_barang = item[2]
    harga_barang = item[3]
    stok_barang = item[4]
    print(f'''
KODE {kode_barang}
{nama_barang} | RP {harga_barang}
stok : {stok_barang}
    ''')



def start():
  while True :
    menu = input ('menu:\n\n 1. Tambah Barang\n 2. Cek Barang \n 3. Kembali\n\n Silahkan pilih: ')
    
    if menu == '1' :
      add()
    elif menu == '2' :
      check()
    elif menu == '3' :
      main.menu()
    else :
      break

    

if __name__ == "__main__":
  start()