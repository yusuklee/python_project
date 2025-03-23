import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print("\r" + message + "\n> ", end="")
        except:
                print("\n[연결 종료됨]")
                break
        
def main():
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.connect((HOST,PORT))

     nickname = input("닉네임을 입력하세요:")
     print("채팅을 시작하세요! 종료하려면 Ctrl+C")

     thread = threading.Thread(target=receive_messages, args=(client,))
     thread.daemon = True
     thread.start()

     while True:
          try:
               message = input("> ")
               if message:
                    full_message = f"{nickname} : {message}"
                    client.send(full_message.encode())

          except KeyboardInterrupt:
               print("\[종료]")
               client.close()
               break
          
          
          
if __name__ == "__main__":
    main()