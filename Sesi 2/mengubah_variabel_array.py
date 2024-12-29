hobi = "Main bola, berenang, ngoding"
print(hobi)

hobbies = ["Main bola", "Berenang", "Ngoding", "x", "Main bola", "Berenang", "Ngoding", "x", "Main bola", "Berenang", "Ngoding", "Judi"]
print(len(hobbies))    
print(hobbies[len(hobbies)-1]) # untuk menampilkan data terkahir tanpa memberitahukan urutan array, tapi kita pakai formula length - 1 atau penjang data kurang satu
print (f"hobbies -> {hobbies}")
print(hobbies[0])

tmp_hobbies  = hobbies 
tmp_hobbies[1] = "Golf"

print(f"tmp_hobbies -> {tmp_hobbies}")