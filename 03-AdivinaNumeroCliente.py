import socket

def main():
    IP = '127.0.0.1'  
    PORT = 2000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        
        while True:
            data = s.recv(64).decode()
            print(data)
            
            if "HAS ACERTADO" in data:
                break
            
            numero = input("Introduce un número: ")
            s.send(numero.encode())

if __name__ == "__main__":
    main()
