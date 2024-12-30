import main 
def start():
  while True :
    print("Ini WARUNGPY")
    play_again =  input("Kembali ke menu utama ? [y/n] : ").lower()
    if play_again == "y":
      main.menu()
    

if __name__ == "___main___":
  start()