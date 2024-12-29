from libs import welcome_message
from games import games2

def main():
  welcome_message("SELAMAT DATANG DI GLENPY")
  games2.start()


if __name__ == "__main__": # ini mengambil fungsi main dan memanggil fungsi main agar bisa di eksekusi 
  main()
