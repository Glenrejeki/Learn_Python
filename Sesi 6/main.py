from libs import welcome_message, exit_program
from games import games2
from tools import warung


def menu():
  user_option = int( input(f"menu programnya:\n\n 1. Games GLENPY\n 2. Warung Mini\n 3. Keluar program \n\n Silah pilih: "))
  
  if user_option == 1 :
    games2.start()    
  elif user_option == 2 :
    warung.start()
  elif user_option == 3 :
    exit_program()
  else :
    print("Hanya boleh pilih yang tersedia di menu !")

  
  

def main():
  welcome_message("SELAMAT DATANG DI GLENPY")
  menu()
  


if __name__ == "__main__": # ini mengambil fungsi main dan memanggil fungsi main agar bisa di eksekusi 
  main()