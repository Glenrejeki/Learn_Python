import socket
from time import sleep 

PC_NAME = socket.gethostname()

def welcome_message(title):
    style = "*" * (len(PC_NAME) + 6)
    
    print(style)
    print(f"** {PC_NAME} **")
    print(style)

def exit_program():
    print("Program akan dihentikan")
    sleep(1)
    print("3 . . . ")
    sleep(1)
    print("2 . . . ")
    sleep (1)
    print("1 . . .")
    sleep (1)
    print("Program berhasil dihentikan")
    exit() # ini perlu supaya program sepenuhnya berhenti ketika dipilih menu ini 
    
if __name__ == "__main__":
    welcome_message("")
    exit_program()