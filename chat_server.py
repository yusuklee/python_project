import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = []

def broadcast(message, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                pass  # 에러 무시하고 다음으로

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    server.settimeout(1.0)  # Ctrl+C 먹히게 하기

    print(f"[서버 시작] {HOST}:{PORT} 에서 대기 중...")

    try:
        while True:
            try:
                client_socket, addr = server.accept()
                print(f"[접속] {addr} 연결됨")
                clients.append(client_socket)

                thread = threading.Thread(target=handle_client, args=(client_socket,))
                thread.start()
            except socket.timeout:
                continue
    except KeyboardInterrupt:
        print("\n[서버 종료됨]")
        server.close()

if __name__ == "__main__":
    main()
    
    