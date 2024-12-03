import socket
import threading
import random

adivinar = random.randrange(1,9)

def ManejaCliente(c,a):
    c.send(b"Intenta adivianr mi numero! ")
    while True:
        dato = c.recv(64).decode() #bloqueante
        print (dato)
        if int(dato) == adivinar:
            c.send(b"HAS ACERTADO")
            break
        elif int(dato) > adivinar:
            c.send(b"Mi numero es menor")
        else:
            c.send(b"Mi numero es mayor")            
    c.close()

if __name__ == '__main__':
    IP = ''
    PORT = 2000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP,PORT))
        s.listen()
        
        print ("Servidor escuchando")
        print ("Número a adivinar: " +str(adivinar))
        while True:
            (cli,addr) = s.accept() #bloqueante
            print ("Cliente conectado en: ", addr)
        
            t= threading.Thread(target=ManejaCliente, args=(cli,addr))
            t.start()
        
        