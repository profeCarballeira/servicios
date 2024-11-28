import socket
import random

IP = ''
PORT = 2000
adivinar = random.randrange(1,9)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP,PORT))
    s.listen()
    
    print ("Servidor escuchando")
    print ("Número a adivinar: " +str(adivinar))
    
    (cli,addr) = s.accept() #bloqueante
    print ("Cliente conectado en: ", addr)
    
    cli.send(b"Intenta adivianr mi numero! ")
    while True:
        dato = cli.recv(64).decode() #bloqueante
        print (dato)
        if int(dato) == adivinar:
            cli.send(b"HAS ACERTADO")
            break
        elif int(dato) > adivinar:
            cli.send(b"Mi numero es menor")
        else:
            cli.send(b"Mi numero es mayor")            
    cli.close()
        