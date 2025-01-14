import mysql.connector

db = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = '',
  database = 'mini_market'
)

def insert_item(kode_barang, nama_barang, harga_barang , stok_barang): 
  cursor = db.cursor() #ekseksusi query 
  cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang,harga_barang ,stok_barang ) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang , stok_barang))
  # Menyimpan data ke database 
  db.commit()
  
  if cursor.rowcount > 0:
    print("Data berhasil dimasukkan ")
  else :
    print("Data gagal di insert")
  
def fetch_item(): # menampilkan semua daftar barang dari database
  cursor = db.cursor()
  cursor.execute("SELECT * FROM tbl_barang") # jangan sampai lupa membuat SELECT ke tabel mana, jika tidak di buat maka program akan bingung akan mengambil data dari tabel yang mana 
  return cursor.fetchall() 

  