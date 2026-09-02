# Εργαστηριακός Οδηγός 2: Προγραμματισμός Sockets σε Python (TCP & UDP)

## 1. Σκοπός Εργαστηρίου
Εκμάθηση των θεμελιωδών κλήσεων του Berkeley Sockets API μέσω της γλώσσας Python για την ανάπτυξη δικτυακών εφαρμογών πελάτη-εξυπηρετητή (Client-Server) με χρήση πρωτοκόλλων TCP και UDP.

---

## 2. Υλοποίηση TCP Echo Server και Client

### Κώδικας Εξυπηρετητή (`tcp_server.py`)
```python
import socket

def run_tcp_server(host='127.0.0.1', port=9000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[TCP Server] Akroash sth dieuthinsi {host}:{port}...")

    try:
        while True:
            client_conn, client_addr = server_socket.accept()
            print(f"[TCP Server] Nea syndesh apo: {client_addr}")
            
            while True:
                data = client_conn.recv(1024)
                if not data:
                    break
                print(f"[TCP Server] Elhfthisan dedomena: {data.decode('utf-8')}")
                client_conn.sendall(data)
            
            client_conn.close()
            print(f"[TCP Server] H syndesh me {client_addr} termatistike.")
    except KeyboardInterrupt:
        print("\n[TCP Server] Diakoph leitourgias.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    run_tcp_server()
```

### Κώδικας Πελάτη (`tcp_client.py`)
```python
import socket

def run_tcp_client(host='127.0.0.1', port=9000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"[TCP Client] Syndedemenos ston {host}:{port}")

    message = "Geia sou kosme apo ton Python TCP Client!"
    client_socket.sendall(message.encode('utf-8'))

    response = client_socket.recv(1024)
    print(f"[TCP Client] Apantisi server: {response.decode('utf-8')}")

    client_socket.close()

if __name__ == '__main__':
    run_tcp_client()
```

---

## 3. Υλοποίηση UDP Server και Client

### Κώδικας Εξυπηρετητή UDP (`udp_server.py`)
```python
import socket

def run_udp_server(host='127.0.0.1', port=9001):
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind((host, port))
    print(f"[UDP Server] Anamonh datagrams sth thyra {port}...")

    while True:
        data, addr = udp_sock.recvfrom(2048)
        print(f"[UDP Server] Minyma apo {addr}: {data.decode('utf-8')}")
        reply = f"ACK: {data.decode('utf-8')}".encode('utf-8')
        udp_sock.sendto(reply, addr)

if __name__ == '__main__':
    run_udp_server()
```

